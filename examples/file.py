#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import  app
from ait_ui.elements import Element, Elm
from ait_ui.elements import Text
from ait_ui.elements import Button
from ait_ui.elements import File
from ait_ui.elements import Form
from ait_ui.elements import Submit
from ait_ui.elements import Label
with Element() as main:
    Label(id="dropzone1" , usefor="file").style("width", "100px").style("height", "100px")
    file = File(id="file").on("input", lambda id, value: print("Input Happened", id, value))
    file.on("change", lambda id, value: print("Change Happened", id, value))



if __name__ == '__main__':
    app.run(ui = main, debug=True)