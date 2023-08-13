from ..core import Element

class Dropzone(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "div"
        self.value_name = None
        self.add_header_item('dropzone-css','<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.css" />')
        self.add_script_source('dropzone-js-lib', '<script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/dropzone.min.js"></script>')
        self.add_script_source('dropzone', '<script src="js/dropzone.js"></script>')

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