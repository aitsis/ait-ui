from .element import Element

class ImageViewer(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "div"
        self.id = id
        self.value_name = None
        self.add_script_source('seadragon-js-lib', '<script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/openseadragon.min.js"></script>')
        self.add_script_source('seadragon', '<script src="js/seadragon.js"></script>')
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value                
        self.send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")

    def render(self):
        if self.id is not None:            
            self.queue_for_send(self.id, self.value, "init-seadragon")
        if self.value is not None:
            self.queue_for_send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")
        return super().render()
    
    def mouse_mode(self, value):
        print("(python)mouse_mode: " + value)
        self.send(self.id, self.value_to_command("mouse-mode", value), "seadragon")

    def brush_size(self, value):
        self.send(self.id, self.value_to_command("brush-size", value), "seadragon")
    def value_to_command(self,command,value):        
        command = {
            "action": command,
            "value": value
        }
        return command