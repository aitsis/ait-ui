from ..core import Element

class Radio(Element):
    def __init__(self,id = None,value = None,name = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "input"
        self.value_name = "checked"
        self.has_content = False
        self.attrs["type"] = "radio"
        self.attrs["name"] = name

    def checked(self):
        self.attrs["checked"] = "true"
        return self
    
    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self