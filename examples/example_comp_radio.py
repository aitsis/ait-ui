#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element,Elm
from ait_ui import app
from examples.component_example.comp_radio import Comp_Radio


def on_change(id, value):
    radio = Elm(id=id)
    checked_value = radio.attrs.get("checked")
    print(checked_value)

with Element().style("width","20%") as test:
    values=["a","b","c","d"]
    Comp_Radio(value_list=values).on("change", on_change)
  

if __name__ == "__main__":
    app.run(ui = test, debug=True, port=5001)
