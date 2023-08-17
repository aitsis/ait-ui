from ..core import Element

class Button(Element):
    def __init__(self,id = None, value = None, type='button', formID=None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.classes.append("btn")
        
        if formID is not None:
            self.attrs["form"] = formID