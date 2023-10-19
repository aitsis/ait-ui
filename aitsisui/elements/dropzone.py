from ..core import Element, index_gen

index_gen.add_header_item('dropzone-css','<link rel="stylesheet" href="dropzone.min.css" />')
index_gen.add_script_source('dropzone-js-lib', '<script src="dropzone.min.js"></script>')
index_gen.add_script_source('dropzone', '<script src="js/dropzone.js"></script>')

class Dropzone(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "div"
        self.value_name = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.send(self.id, self.value_to_command("open"), "dropzone")

    def render(self):
        if self.id is not None:
            self.queue_for_send(self.id, self.value, "init-dropzone")
        if self.value is not None:
            self.queue_for_send(self.id, self.value_to_command("open"), "dropzone")
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