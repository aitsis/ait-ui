#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Header , Text

def ImaginerHeader():
    with Header() as content:
        content.cls("imaginer-header")
        with Element() as content:
            content.cls("imaginer-header-left")
            Text(value = "Imaginer").style("margin", "0")
        with Element() as content:
            content.cls("imaginer-header-right")
            Text(value = "Imaginer").style("margin", "0")
    return content
