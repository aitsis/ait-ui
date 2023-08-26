from ..core import Element

class Option(Element):
    def __init__(self, id=None, value=None, autoBind=True, text=""):
        super().__init__(id=id, value=text, autoBind=autoBind)
        self.tag = "option"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["value"] = value

    def selected(self):
        self.attrs["selected"] = "true"
        return self
    
    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self