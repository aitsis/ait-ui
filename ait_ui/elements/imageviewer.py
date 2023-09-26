from ..core import Element, index_gen

index_gen.add_script_source('seadragon-js-lib', '<script src="openseadragon.min.js"></script>')
index_gen.add_script_source('seadragon', '<script src="js/seadragon.js"></script>')

class ImageViewer(Element):
    def __init__(self, id=None, value=None, hasButtons=True, ableToZoom=False, autoBind=True, tool=None):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "div"
        self.value_name = None
        self.hasButtons = hasButtons
        self.ableToZoom = ableToZoom
        self.tool = tool       
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        if self._value is not None:
            self.send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")

    def render(self):
        if self.id is not None:
            self.queue_for_send(self.id, {"hasButtons": str(self.hasButtons).lower(), "tool":self.tool}, "init-seadragon")
        if self.value is not None:
            self.queue_for_send(self.id, self.value_to_command("open",{"type": "image","url": self._value}), "seadragon")
        if self.ableToZoom is not None:
            self.queue_for_send(self.id, self.value_to_command("set-scroll-zoom", str(self.ableToZoom).lower()), "seadragon")
        return super().render()

    def closeImage(self):
        self.send(self.id, self.value_to_command("close", None), "seadragon")

    def mouse_mode(self, value):
        #print("(python)mouse_mode: " + value)
        self.send(self.id, self.value_to_command("mouse-mode", value), "seadragon")

    def setScrollZoom(self, value):
        self.send(self.id, self.value_to_command("set-scroll-zoom", str(value).lower()), "seadragon")

    def brush_size(self, value):
        self.send(self.id, self.value_to_command("brush-size", value), "seadragon")
    def value_to_command(self,command,value):
        command = {
            "action": command,
            "value": value
        }
        return command