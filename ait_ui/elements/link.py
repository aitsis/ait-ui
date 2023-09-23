from ..core import Element

class Link(Element):
    def __init__(self,id = None, value = None, href = None, tooltip="",autoBind=True, target = ""):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "a"
        self.value_name = "innerHTML"
        self.attrs["href"] = href
        self.attrs["target"] = target
        self.attrs["title"] = tooltip