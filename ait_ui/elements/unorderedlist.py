from .element import Element
class UnorderedList(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "ul"
        self.value_name = "innerHTML"
        self.has_content = True