from ..core import Element

class TextArea(Element):
    def __init__(self,id = None, value = None , placeholder = None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "textarea"
        self.attrs["placeholder"] = placeholder
        self.classes.append("textarea")

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self