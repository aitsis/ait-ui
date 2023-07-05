from .element import Element
class Select(Element):
    def __init__(self,id = None, value = None):
        super().__init__(id, value)
        self.tag = "select"
        self.value_name = "value"
        self.has_content = True