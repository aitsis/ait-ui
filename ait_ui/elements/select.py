from ..core import Element

class Select(Element):
    def __init__(self,id = None, value = None, autoBind=True):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "select"
        self.value_name = "value"
        self.has_content = True