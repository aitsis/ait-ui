from ..core import Element

class UnorderedList(Element):
    def __init__(self,id = None,value = None,role = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "ul"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["role"] = role