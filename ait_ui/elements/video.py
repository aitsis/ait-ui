from ..core import Element

class Video(Element):
    def __init__(self, id=None, value=None, src=None, loop="true", autoplay="true", autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "video"
        self.has_content = True
        self.attrs["value"] = value
        self.attrs["loop"] = "true"
        self.attrs["autoplay"] = "true"
        self.attrs["playsinline"] = "true"
        self.attrs["muted"] = "true"