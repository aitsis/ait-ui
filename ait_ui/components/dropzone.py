from .element import Element
from .text import Text
from . import scripts
from .. import socket_handler

scripts.header_items.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.js"></script>')
scripts.header_items.append('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.css" />')

scripts.add_script("dropzone", """
    event_handlers["init-dropzone"] = function(id, value, event_name){
        elements[id] = new Dropzone("#"+id, { url: "/file/post" });
        console.log("init-dropzone");
    }
    event_handlers["dropzone"] = function(id, value, event_name){
    console.log("dropzone",id,value);
        elements[id][value.action](value.value);}
    """)


class Dropzone(Element):
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
        socket_handler.send(self.id, self.value_to_command("open"), "dropzone")

    def render(self):
        if self.id is not None:            
            socket_handler.queue_for_send(self.id, self.value, "init-dropzone")
        if self.value is not None:
            socket_handler.queue_for_send(self.id, self.value_to_command("open"), "dropzone")
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