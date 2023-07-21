#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Text , File , Elm , Label
from ait_ui.component import Component


class Comp_InputFile(Component):
    def __init__(self, id=None):
        super().__init__()
        with Element().style("height","100%").style("width","100%"):
            pass
            File(id = id,on_upload_done=self.on_input)
            with Label(id="dropzone1" , usefor="file1"):
                    Text(value = "Drag and Drop")
                    Text(value = "- or -")
                    Text(value = "Click to Upload")
    
    def on_input(self, value):
        print("Input File: ", value)
    