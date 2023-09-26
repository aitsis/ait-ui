from ..core import Element, index_gen

index_gen.add_script_source('fabric-js-lib', '<script src="fabric.min.js"></script>')
index_gen.add_script_source('image-cropper', '<script src="js/image_cropper.js"></script>')

class ImageCropper(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "canvas"
        self.value_name = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        if self._value is not None:
            self.send(self.id, self.value_to_command("loadImage", self._value), "image-cropper")

    def render(self):
        if self.id is not None:
            self.queue_for_send(self.id, "", "init-image-cropper")
        if self.value is not None:
            self.queue_for_send(self.id, self.value_to_command("loadImage", self._value), "image-cropper")
        return super().render()

    def closeImage(self):
        self.send(self.id, self.value_to_command("close", None), "image-cropper")

    def crop_and_move(self, axis, scale):
        self.send(self.id, self.value_to_command("cropAndMove", {"axis": axis, "scale": scale}), "image-cropper")

    def repeatImage(self, value):
        self.send(self.id, self.value_to_command("repeatImage", value), "image-cropper")

    def resetImage(self):
        self.send(self.id, self.value_to_command("resetImage", ""), "image-cropper")

    def value_to_command(self, command, value):
        command = {
            "action": command,
            "value": value
        }
        return command