from .element import Element
class Option(Element):
    def __init__(self, id=None, value=None, auto_bind=True):
        super().__init__(id, value, auto_bind)
        self.tag = "option"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["value"] = value