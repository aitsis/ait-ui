from ..core import Element

class Input(Element):
    def __init__(self, id=None, value=None, name=None, type="text", placeholder="", step=None, required=False, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = type
        self.attrs["placeholder"] = placeholder
        self.attrs["name"] = name

        if step is not None:
            self.attrs["step"] = step

        if required:
            self.attrs["required"] = "required"

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self