#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui import socket_handler
from ait_ui.elements import Element, Elm

from examples.component_example.Imaginer_Bottom_Side import Imaginer_Bottom_Side
from examples.component_example.Imaginer_Center_Side import Imaginer_Center_Side
from examples.component_example.Imaginer_Top_Side import Imaginer_Top_Side
from examples.component_example.Imaginer_Header import ImaginerHeader

with Element(id = "imaginer-wrapper") as main:
        main.cls("imaginer-wrapper")
        #Header Row
        ImaginerHeader()
        #Top_Side
        Imaginer_Top_Side()
        #Center_Side
        Imaginer_Center_Side()
        #Bottom_Side
        Imaginer_Bottom_Side()

        
if __name__ == '__main__':
    app.run(ui = main, debug=True)  