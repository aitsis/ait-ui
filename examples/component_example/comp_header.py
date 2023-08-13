#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Header, Text, Image
from ait_ui.core import Component, Element

class Comp_Imaginer_Header(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)

        with self:
            with Header().cls("imaginer-header"):
                with Element().cls("imaginer-header-left") :
                    Image(value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png").style("width", "100px")            
                with Element().cls("imaginer-header-right"):
                    Text(value = "Imaginer").style("margin", "0")