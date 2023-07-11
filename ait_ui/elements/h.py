from .element import Element
class H(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)
        self.tag = "h"+ str(self.value)
