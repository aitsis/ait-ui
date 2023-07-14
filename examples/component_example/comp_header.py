#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Header , Text , Image
from ait_ui.component import Component

class Comp_Imaginer_Header(Component):
    def __init__(self, id=None):
        super().__init__()
        with Header().cls("imaginer-header") as content:
            with Element().cls("imaginer-header-left") :
                Image(value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png").style("width", "100px")            
            with Element().cls("imaginer-header-right"):
                Text(value = "Imaginer").style("margin", "0")
