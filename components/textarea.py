from components.element import Element
class TextArea(Element):
    def __init__(self,id = None, value = None , placeholder = None):
        super().__init__(id, value)
        self.tag = "textarea"
        self.value_name = "innerHTML"
        self.has_content = True
        self.attrs["placeholder"] = placeholder
        