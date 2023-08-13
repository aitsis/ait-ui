#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.core import Component
from examples.component_example.comp_slider import Comp_Slider

class MyApp(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        with self:
            Comp_Slider(label="Slider 1", min=0, max=100, value=50, callback=self.on_change_slider)
            Comp_Slider(label="Slider 2", min=0, max=100, value=50, callback=self.on_change_slider)

    def on_change_slider(self, id, value):
        print("Slider Changed", id, value)

if __name__ == "__main__":
    app.run(ui = MyApp, debug=True)