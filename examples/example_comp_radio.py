#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element,Elm
from ait_ui.component import Component
from ait_ui import app
from examples.component_example.comp_radio import Comp_Radio

class CompRadio(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)

        self.style("width", "20%")
        with self:
            values=["a","b","c","d"]
            Comp_Radio(value_list=values, callback=self.getCheckedValue)

    def getCheckedValue(self, id, value):
        checked_value = Elm(id=id).attrs.get("checked")
        print(checked_value, value)

if __name__ == "__main__":
    app.run(ui = CompRadio, debug=True)
