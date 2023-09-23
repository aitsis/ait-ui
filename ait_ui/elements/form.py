from ..core import Element

class Form(Element):
    def __init__(self,id = None, value = None, action = None, method = "POST", autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "form"
        self.attrs["method"] = method
        self.attrs["enctype"] = "multipart/form-data"
        if action is not None:
            self.attrs["action"] = action