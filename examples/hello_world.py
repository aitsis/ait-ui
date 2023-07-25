#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import  app
from ait_ui.elements import Element, Elm, Button
    
class MyApp():
    def __init__(self):
        self.main = Element()
        with self.main:
            for i in range(15):
                Button(id = f"btn{i}", value="Hello World").on("click", self.on_click)

    def on_click(id, value):
        print("clicked", id, value)
        Elm(id).toggle_class("selected")

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)