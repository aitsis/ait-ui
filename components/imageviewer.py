from components.element import Element
import connection

import components.scripts as scripts

scripts.header_items.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>')

scripts.add_script("seadragon", """
    event_handlers["init-seadragon"] = function(id, value, event_name){
        elements[id] = OpenSeadragon({
                id: id,
                prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
                animationTime: 0,
                maxZoomPixelRatio: 2,
            });
            console.log("init-seadragon");
        }
    event_handlers["seadragon"] = function(id, value, event_name){
    console.log("seadragon",id,value);
        elements[id][value.action](value.value);}
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
        connection.send(self.id, self.value_to_command("open"), "seadragon")

    def render(self):
        if self.id is not None:            
            connection.queue_for_send(self.id, self.value, "init-seadragon")
        if self.value is not None:
            connection.queue_for_send(self.id, self.value_to_command("open"), "seadragon")
        return super().render()
    
    def value_to_command(self,command):
        src = {
            "type": "image",
            "url": self._value
        }
        command = {
            "action": command,
            "value": src
        }
        return command
        