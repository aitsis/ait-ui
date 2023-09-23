#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Text, Button, Image
from ait_ui.core import Component, Element

class Comp_Dropdown(Component):    
    def __init__(self, id=None, autoBind=True, image=None, data=None, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.data = data
        self.image = image

        self.cls("dropdown-menu")
        with self:
            Image(value=self.image).cls("logo").style("width","30px").style("height","30px")
            with Element().cls("dropdown-content"):
                for title in self.data:
                    with Element().cls("dropdown-item-wrapper"):
                        Text(value=title["name"]).cls("dropdown-item")
                        with Element().cls("dropdown-item-wrapper-inside"):
                            for content in title["content"]:
                                Button(value=content).cls("dropdown-item-inside").on("click",self.on_click)
    
    def on_click(self, id, value):
        print("Clicked:", id, value)