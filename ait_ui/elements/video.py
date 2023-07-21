from .element import Element
class Video(Element):
    def __init__(self, id=None, value=None, auto_bind=True , src = None , controls = False , autoplay = None):
        super().__init__(id, value, auto_bind)
        self.tag = "video"
        self.value_name = "src"
        self.has_content = True
        self.attrs["value"] = value
        self.attrs["src"] = src
        self.attrs["controls"] = controls

