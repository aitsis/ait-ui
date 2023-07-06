from .element import Element
class ListItem(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "li"
        self.value_name = "innerHTML"
        self.attrs["class"] = "list-item"