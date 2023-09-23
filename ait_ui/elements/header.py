from ..core import Element

class Header(Element):
    def __init__(self,id = None,value = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "header"
        self.classes.append("header")