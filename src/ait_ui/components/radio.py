from .element import Element
class Radio(Element):
    def __init__(self,id = None,value = None,name = None):
        super().__init__(id = id, value = value)
        self.tag = "input"
        self.value_name = "checked"
        self.has_content = False
        self.attrs["type"] = "radio"
        self.attrs["name"] = name

    def checked(self, value):
        self.attrs["checked"] = value
        return self