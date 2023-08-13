from ..core import Element

class Video(Element):
    def __init__(self, id=None, value=None, src=None, controls=False, autoplay=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "video"
        self.value_name = "src"
        self.has_content = True
        self.attrs["value"] = value
        self.attrs["src"] = src
        self.attrs["controls"] = controls