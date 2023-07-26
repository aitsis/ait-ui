from .element import Element
class Option(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "option"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["value"] = value