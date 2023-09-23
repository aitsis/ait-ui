from ..core import Element

class Slider(Element):
    def __init__(self,id = None,value = None, min = 0, max = 100, step = 1, autoBind = True):
        super().__init__(id = id, value = value, autoBind = autoBind)
        self.min = min
        self.max = max
        self.step = step
        self.tag = "input"
        self.value_name = "value"
        self.has_content = False
        self.attrs["type"] = "range"
        self.attrs["min"] = self.min
        self.attrs["max"] = self.max
        self.attrs["step"] = self.step

    def disabled(self):
        self.attrs["disabled"] = "disabled"
        return self