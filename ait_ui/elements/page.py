from ..core import Element

class Page(Element):
    def __init__(self,id = None, value = None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.classes.append("main")