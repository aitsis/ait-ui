from ..core import Element

class OrderedList(Element):
    def __init__(self,id = None,value = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "ol"
        self.value_name = "innerHTML"
        self.has_content = True