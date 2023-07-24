#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Select , Option , Text , Element
from ait_ui.component import Component


class Comp_Select(Component):
    def __init__(self, id=None , options=None):
        super().__init__()
        self.options = options

    def render(self):
        Text(value = "Models")  
        with Select(id=id).cls("select") as select:
            select.on("change", self.on_change)
            for option in self.options:
                    Option(value=option).cls("option")
    
    def on_change(self, id, value):
        if self.events["change"]:
            self.events["change"](id, value)