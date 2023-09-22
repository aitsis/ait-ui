#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Select, Option
from ait_ui.core import Component

class Comp_Select(Component):
    def __init__(self, id=None , options=None, autoBind=True, callback=None, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.options = options
        self.callback = callback
        self.value = self.options[0]
        self.add_css("select-css", """                                  
                        .select-wrapper{
                            border: 1px solid gray;
                            border-radius: 3px;
                            background-color: #333333;
                            box-sizing: border-box;
                            padding: 7px;
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                            box-shadow: 1px 1px 1px 1px gray;
                        }

                        .select{
                            border: 1px solid gray;
                            border-radius: 3px;
                            background-color: black;
                            color: white;
                            box-sizing: border-box;
                            padding: 7px;
                            display: flex;
                            flex-direction: column;
                            justify-content: space-between;
                        }

                        .option{
                            width: 100%;
                            height: 100%;
                            color: white;
                            border: 1px solid gray;
                            border-radius: 3px;
                            background-color: black;
                            padding: 20px;
                            box-sizing: border-box;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            cursor: pointer;
                            transition: all 300ms ease-out;
                        }""")

        with self:
            with Select().cls("select").on("change", self.on_change):
                for option in self.options:
                    Option(value=option).cls("option")

    def on_change(self, id, value):
        if self.callback:
            #self.value = value
            self.callback(self.id, value)