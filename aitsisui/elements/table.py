from ..core import Element

class Table(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id, value, autoBind)
        self.tag = "table"