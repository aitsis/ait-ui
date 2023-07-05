from .element import Element
from . import scripts
from .. import socket_handler


scripts.add_script("canvas", """
    event_handlers["init-canvas"] = function(id, value, event_name){            
            canvas = document.getElementById(id);
            elements[id] = {canvas: canvas, ctx: canvas.getContext('2d')};            
        }
    event_handlers["canvas"] = function(id, value, event_name){        
        if (value.action == "fillRect"){
            elements[id].ctx.fillStyle = value.params.color;
            elements[id].ctx.fillRect(value.params.x, value.params.y, value.params.width, value.params.height);
        }
        if (value.action == "fillCircle"){
            elements[id].ctx.beginPath();
            elements[id].ctx.arc(value.params.x, value.params.y, value.params.radius, 0, 2 * Math.PI);
            elements[id].ctx.fillStyle = value.params.color;
            elements[id].ctx.fill();
        }

    }
    """)
class Canvas(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "canvas"
        self.id = id
        self.value_name = None
        
    
    def render(self):
        if id is not None:            
            socket_handler.queue_for_send(self.id, self.value, "init-canvas")
        return super().render()

    def width(self, value):
        self.attrs["width"] = value
        return self
    def height(self, value):
        self.attrs["height"] = value
        return self

    def get_client_handler_str(self, event_name):
        if event_name in ["mousedown", "mouseup", "mousemove"]:
            return f" on{event_name}='clientEmit(this.id,{{x: event.offsetX, y: event.offsetY}},\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def fill_rect(self, x, y, width, height,color):
        socket_handler.send(self.id, {"action": "fillRect", "params": {"x": x, "y": y, "width": width, "height": height, "color": color}}, "canvas")
        return self
    
    def fill_circle(self, x, y, radius,color):
        socket_handler.send(self.id, {"action": "fillCircle", "params": {"x": x, "y": y, "radius": radius, "color":color}}, "canvas")
        return self
