from ..core import Element

class Image(Element):
    def __init__(self, id=None, value=None, autoBind=True, lazy=False):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "img"
        self.value_name = "src"
        self.has_content = False
        if lazy:
            self.attrs["data-src"] = value if value else ""
            self.attrs["data-srcset"] = value if value else ""
            self.attrs["data-sizes"] = "auto"
            self.cls("lazyload")
        else:
            self.attrs["src"] = value if value else ""
        self.attrs["alt"] = "image"
        self.attrs["loading"] = "lazy"