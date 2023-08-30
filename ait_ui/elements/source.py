from ..core import Element

class Source(Element):
    def __init__(self,id = None, value = None, media = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "source"
        self.value_name = "src"
        self.has_content = False
        self.attrs["media"] = media