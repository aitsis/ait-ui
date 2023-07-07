from .element import Element
from . import scripts
from .. import socket_handler


scripts.header_items.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>')

scripts.add_script("seadragon", """
    event_handlers["init-seadragon"] = function(id, value, event_name){
        elements[id] = {
            mouse_mode: "pan",
            viewer: OpenSeadragon({
                    id: id,
                    prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
                    animationTime: 0,
                    maxZoomPixelRatio: 4,
                })
            }
            elements[id].viewer.addHandler('canvas-drag', function(event) {
                console.log('mouse-mode: ' + elements[id].mouse_mode)
                if(elements[id].mouse_mode == "draw-mode") {
                    event.preventDefaultAction = true;
                    var viewportPoint = elements[id].viewer.viewport.pointFromPixel(event.position);
                    console.log("Dragging at viewport coordinates", viewportPoint.x, viewportPoint.y);
                }
            });
        }
    event_handlers["seadragon"] = function(id, command, event_name){
        switch(command.action){
            case "open":
                elements[id].viewer.open(command.value);
                break;
            case "mouse-mode":
                elements[id].mouse_mode = command.value;
                console.log("mouse-mode: " + elements[id].mouse_mode)
                break;
            default:
                console.log("Unknown command: " + command.action);
            }
        } 
    """)
class ImageViewer(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "div"
        self.id = id
        self.value_name = None
        
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value                
        socket_handler.send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")

    def render(self):
        if self.id is not None:            
            socket_handler.queue_for_send(self.id, self.value, "init-seadragon")
        if self.value is not None:
            socket_handler.queue_for_send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")
        return super().render()
    
    def mouse_mode(self, value):
        print("(python)mouse_mode: " + value)
        socket_handler.send(self.id, self.value_to_command("mouse-mode", value), "seadragon")

    def value_to_command(self,command,value):        
        command = {
            "action": command,
            "value": value
        }
        return command
        