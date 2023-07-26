#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from ait_ui.elements import Element , Text , Input , Button , Elm , Label , Col , Image
from ait_ui.component import Component


class Comp_Dropdown(Component):    
    def __init__(self, id=None , image = None , data=None):
        super().__init__()
        self.data = data

        with Element().cls("dropdown-menu"):
            Image(value=image).cls("logo").style("width","30px").style("height","30px")
            with Element().cls("dropdown-content"):
                for title in self.data:
                    with Element().cls("dropdown-item-wrapper"):
                        Text(value=title["name"]).cls("dropdown-item")
                        with Element().cls("dropdown-item-wrapper-inside"):
                            for content in title["content"]:
                                Button(id="button" + content,value=content).cls("dropdown-item-inside").on("click",self.on_click)
    
    def on_click(self,id,value):
        if self.events["click"]:
            self.events["click"](id, value)