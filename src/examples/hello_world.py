#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#-------------------------------------------------------------

from ait_ui import  app

from ait_ui.components.element import Element, Elm
from ait_ui.components.text import Text
from ait_ui.components.button import Button

def on_click(id, value):
    print("clicked", id, value)
    Elm(id).toggle_class("selected")

with Element() as main:
    for i in range(15):
        Button(id = f"btn{i}", value="Hello World").on("click", on_click)


if __name__ == '__main__':
    app.run(ui = main, debug=True)

