from ..core import Element

class Tbody(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id, value, autoBind)
        self.tag = "tbody"