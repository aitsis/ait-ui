#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Text, Slider
from ait_ui.core import Component, Element

class Comp_Slider(Component):
    def __init__(self, label=None, id=None, min=0, max=100, value=50, step=1, autoBind=True, callback=None, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.label = label
        self.id = id
        self.min = min
        self.max = max
        self.step = step
        self.value = value
        self.callback = callback
        self.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
        
        with self:
            with Element():
                Text(value=self.label)
                self.slider_text = Text(value=str(value)).style("color", "black")
            Slider(step=self.step, min=self.min, max=self.max, value=self.value).style("width", "100%").on("input", self.on_change_slider)

    def on_change_slider(self, id, value):
        print("on_change_slider", id, value)
        self.slider_text.value = value
        self.value = value
        if self.callback:
            self.callback(id, value)