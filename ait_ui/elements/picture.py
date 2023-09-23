from ..core import Element

class Picture(Element):
    def __init__(self,id = None,value = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "picture"
        self.value_name = "innerHTML"
        self.has_content = True