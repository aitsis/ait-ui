from .element import Element
class Label(Element):
    def __init__(self, id = None , usefor = None,value = None):
        super().__init__(id= id , value = value)
        self.classes.append("label")
        self.usefor = usefor
        self.tag = "label"
        self.attrs["for"] = usefor
        self.has_content = True