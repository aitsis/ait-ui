from .element import Element
class TextArea(Element):
    def __init__(self,id = None, value = None , placeholder = None):
        super().__init__(id, value)
        self.tag = "textarea"
        self.attrs["placeholder"] = placeholder
        self.classes.append("textarea")