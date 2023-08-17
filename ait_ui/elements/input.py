from ..core import Element

class Input(Element):
    def __init__(self, id=None, value=None, type="text", placeholder="", step=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = type
        self.attrs["placeholder"] = placeholder

        if step is not None:
            self.attrs["step"] = step