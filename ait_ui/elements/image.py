from .element import Element
class Image(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False
        self.attrs["src"] = value