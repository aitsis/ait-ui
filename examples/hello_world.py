#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import  app
from ait_ui.elements import Button
from ait_ui.core import Component, Elm
    
class MyApp(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        with self:
            for i in range(15):
                Button(value="Hello World").on("click", self.on_click)

    def on_click(self, id, value):
        Elm(id).toggle_class("selected")

if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)