
from components.element import Element
class Row(Element):
    def __init__(self,id = None, value = None):
        super().__init__(id, value)
        self.classes.append("row")
        
    
