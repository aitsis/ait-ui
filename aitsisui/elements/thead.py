from ..core import Element

class Thead(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id, value, autoBind)
        self.tag = "thead"