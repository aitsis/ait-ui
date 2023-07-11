from .element import Element
class OrderedList(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True