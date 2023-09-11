from ..core import Element

class Modal(Element):
    def __init__(self, id = None, value = None, autoBind=True ):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "div"
        self.classes.append("modal")