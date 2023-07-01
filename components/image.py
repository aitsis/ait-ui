from components.element import Element
class Image(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "img"
        self.value_name = "src"
        self.style("width","100px")
        self.has_content = False
        