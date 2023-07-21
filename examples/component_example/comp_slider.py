#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Text , Slider , Elm
from ait_ui.component import Component


class Comp_Slider(Component):
    def __init__(self, label=None, id=None, min=0, max=100, value=50 , step=1):
        super().__init__()  
        with Element() as content:
            content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
            Text(value = label)
            Text(value = str(value), id = id + "-text")
        Slider(id = id + "-slider" , step=step, min = min, max = max, value=value).style("width", "100%").on("input", self.on_change_slider)

    def on_change_slider(self, id, value):
        Elm(id.split("-")[0] + "-text").value = value
        if self.events["change_slider"]:
            self.events["change_slider"](id, value)
    