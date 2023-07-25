from .element import Element
from .text import Text

global isAccordionOpen

class Accordion(Element):
    def __init__(self, id=None, value=None):
        super().__init__(id, value)
        self.tag = "div"
        self.value_name = "innerHTML"
        self.cls("accordion")

    isAccordionOpen = True

    def open_accordion(self):
        print("clicked")
        isAccordionOpen = True
        if isAccordionOpen == False:
         self.set_style("display", "none")
         isAccordionOpen = True
        else:
           self.set_style("display", "none")
           isAccordionOpen = False

      
