#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Text , Slider , Elm
from ait_ui.component import Component


class Comp_Slider(Component):  # Component sınıfının alt sınıfı olarak tanımlayın
    def __init__(self, label=None, id=None, min=0, max=100, value=50, step=1):
        super().__init__()  # Component sınıfının __init__ yöntemini çağırın
        self.label = label
        self.id = id
        self.min = min
        self.max = max
        self.value = value
        self.step = step

    def render(self):  # render yöntemini ekleyin
        with Element() as content:
            content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
            Text(value=self.label)
            Text(value=str(self.value), id=self.id + "-text")
        Slider(id=self.id + "-slider", step=self.step, min=self.min, max=self.max, value=self.value).style("width", "100%").on("input", self.on_change_slider)

    def on_change_slider(self, id, value):
        Elm(id.split("-")[0] + "-text").value = value
        if self.events["change_slider"]:
            self.events["change_slider"](id, value)
    