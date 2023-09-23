from ..core import Element

global isAccordionOpen

class Accordion(Element):
    def __init__(self, id=None, value=None, autoBind=True):
        super().__init__(id=id, value=value, autoBind = autoBind)
        self.tag = "div"
        self.value_name = "innerHTML"
        self.cls("accordion")

    isAccordionOpen = True

    def open_accordion(self):
        isAccordionOpen = True
        if isAccordionOpen == False:
         self.set_style("display", "none")
         isAccordionOpen = True
        else:
           self.set_style("display", "none")
           isAccordionOpen = False