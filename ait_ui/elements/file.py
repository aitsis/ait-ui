from .element import Element
class File(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)                
        self.tag = "input"
        self.value_name = "value"
        self.attrs["type"] = "file"
        self.cls("file")
        self.style("display", "none")
