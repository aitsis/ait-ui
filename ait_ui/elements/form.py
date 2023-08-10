from .element import Element
class Form(Element):
    def __init__(self,id = None,value = None,action = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "form"
        self.attrs["method"] = "post"
        self.attrs["enctype"] = "multipart/form-data"
        if action is not None:
            self.attrs["action"] = action