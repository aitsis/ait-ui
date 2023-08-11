from .element import Element
class Button(Element):
    def __init__(self,id = None,value = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "button"
        self.value_name = "innerHTML"
        self.classes.append("btn")