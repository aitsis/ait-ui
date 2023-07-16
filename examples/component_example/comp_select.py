#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Select , Option , Text , Element
from ait_ui.component import Component


class Comp_Select(Component):
    def __init__(self, id=None):
        super().__init__()
        with Element().cls("imaginer-body-left-top"):
                Text(value = "Models")
                with Select(id=id) as select:
                        select.on("change", self.on_change)
                        Option(value="1")
                        Option(value="2")
                        Option(value="3")
                        Option(value="4")
    
    def on_change(self, id, value):
        if self.events["change"]:
            self.events["change"](id, value)
    