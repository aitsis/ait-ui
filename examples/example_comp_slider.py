#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------


from ait_ui import app
from ait_ui.elements import Element
from examples.component_example.comp_slider import Comp_Slider

class MyApp():
    def __init__(self):
        self.main = Element()
        with self.main:
            Comp_Slider(label="Slider 1", id="slider1", min=0, max=100, value=50).on("change_slider", self.on_change_slider)
            Comp_Slider(label="Slider 2", id="slider2", min=0, max=100, value=50).on("change_slider", self.on_change_slider)

    def on_change_slider(id, value):
        print("Slider Changed", id, value)

    def render(self):
        return self.main.render()

if __name__ == "__main__":
    app.run(ui = MyApp, debug=True)