from .element import Element
class Text(Element):
    def __init__(self,id = None, value = None, autoBind = True):
        super().__init__(id, value, autoBind)
        self.tag = "p"
        self.value_name = "innerHTML"
        self.classes.append("text")