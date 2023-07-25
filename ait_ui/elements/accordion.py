from .element import Element

global isAccordionOpen

class Accordion(Element):
    def __init__(self, id=None, value=None, auto_bind=True):
        super().__init__(id, value, auto_bind)
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