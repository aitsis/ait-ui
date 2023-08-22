from ..core import Element

class Image(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False
        self.attrs["src"] = value if value else ""