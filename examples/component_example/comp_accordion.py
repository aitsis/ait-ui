#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ait_ui.elements import Select , Option , Text , Element , Button , Elm
from ait_ui.component import Component

class Comp_Accordion(Component):
    def __init__(self, id=None, elements=None):
        super().__init__()
        with Element(id="accordion").cls("accordion"):
            with Button(id="accordion-button").on("click", change_accordion):
                Text(value="Advanced Options")
            with Element(id="accordion-wrapper"):
                    for element in elements:
                        with Element().cls("accordion-element-wrapper"):
                            with Element().cls("slider-wrapper"):
                                element.render()  # Comp_Slider nesnesini burada render edin

isAccordionOpen = True

def change_accordion(id, value):
    global isAccordionOpen
    print(isAccordionOpen)
    if isAccordionOpen:
        print("if")
        Elm("accordion-wrapper").set_style("height", "100%")
        Elm("accordion").set_style("height", "100%")
    else:
        print("else")
        Elm("accordion-wrapper").set_style("height", "0px")
        Elm("accordion").set_style("height", "9%")
    isAccordionOpen = not isAccordionOpen



    def on_change(self, id, value):
        if self.events["change"]:
            self.events["change"](id, value)
    