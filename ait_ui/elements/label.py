from ..core import Element

class Label(Element):
    def __init__(self, id = None, tabindex = -1, usefor = None,value = None, autoBind = True):
        super().__init__(id= id , value = value, autoBind= autoBind)
        self.classes.append("label")
        self.usefor = usefor
        self.tag = "label"
        self.attrs["for"] = usefor
        self.attrs["tabindex"] = tabindex
        self.has_content = True