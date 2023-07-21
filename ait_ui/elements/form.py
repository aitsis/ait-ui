from .element import Element
class Form(Element):
    def __init__(self,id = None,value = None,action = None):
        super().__init__(id = id, value = value)
        self.tag = "form"
        self.attrs["method"] = "post"
        self.attrs["enctype"] = "multipart/form-data"
        if action is not None:
            self.attrs["action"] = action
        