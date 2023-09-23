from ..core import Element

class ListItem(Element):
    def __init__(self,id = None,value = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "li"
        self.value_name = "innerHTML"
        self.attrs["class"] = "list-item"