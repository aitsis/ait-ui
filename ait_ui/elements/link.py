from ..core import Element

class Link(Element):
    def __init__(self,id = None, value = None, href = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "a"
        self.value_name = "innerHTML"
        self.attrs["href"] = href