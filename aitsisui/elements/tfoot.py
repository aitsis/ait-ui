from ..core import Element

class Tfoot(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id, value, autoBind)
        self.tag = "tfoot"