from ..core import Element

class Button(Element):
    def __init__(self,id = None, value = None, type='button', formID=None, autoBind=True, disabled=False):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "button"
        self.attrs["type"] = type
        self.value_name = "innerHTML"
        self.classes.append("btn")
        self.disabled = disabled

        if formID is not None:
            self.attrs["form"] = formID

        if self.disabled:
            self.attrs["disabled"] = "disabled"