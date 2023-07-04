from components.element import Element
from components.text import Text
import connection

import components.scripts as scripts

scripts.header_items.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.js"></script>')

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
        self.add_child(Text(value = "Drop Image Here"))
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value                
        connection.send(self.id, self.value_to_command("open"), "dropzone")

    def render(self):
        if self.id is not None:            
            connection.queue_for_send(self.id, self.value, "init-dropzone")
        if self.value is not None:
            connection.queue_for_send(self.id, self.value_to_command("open"), "dropzone")
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