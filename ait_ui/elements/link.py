from .element import Element
class Link(Element):
    def __init__(self,id = None,value = None,href = None):
        super().__init__(id = id, value = value)
        self.tag = "a"
        self.value_name = "innerHTML"
        self.attrs["href"] = href