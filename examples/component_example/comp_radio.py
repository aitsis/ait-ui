#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Radio,Element, Label
from ait_ui.component import Component

class Comp_Radio(Component):
    def __init__(self, id=None, value_list=None):
        super().__init__()
        value_list=value_list
        with Element().cls("container").style("flex-direction","row").style("height","100%").style("justify-content","space-around"):
            for index, value in enumerate(value_list):
                radio_id = "radio{}".format(index)
                with Element().cls("btn").style("position","relative").style("margin-right","5px").style("padding","0").style("display","grid").style("grid-template-columns","repeat(auto-fit, minmax(40px, 1fr))").style("border","5px solid black").style("max-height","100%"):      
                    Radio(name="check-substitution-2", id=radio_id).checked(value=value).on("change", self.on_change)
                    with Element().cls("container").style("height","100%").style("justify-content","center").style("align-items","center"):
                        Label(value=value)
    
    def on_change(self, id, value):
        if self.events["change"]:
            self.events["change"](id, value)

