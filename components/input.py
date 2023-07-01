from components.element import Element
class Input(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)                
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = "text"
        