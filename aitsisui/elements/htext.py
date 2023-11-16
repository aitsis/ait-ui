from ..core import Element

class Htext(Element):
    def __init__(self,id = None,value = None, tag="1", autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "h"+ tag
        self.value_name = "innerHTML"  