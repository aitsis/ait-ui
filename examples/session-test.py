#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app, UI
from ait_ui.elements import Element, Elm
from ait_ui.elements import Text
from ait_ui.elements import Button

class myApp():
    def __init__(self):
        self.click_count = 0
        self.main = Element()
        with self.main:
            Button(id = "btn1", value="Hello World").on("click", self.on_click)


    def on_click(self, id, value):
        print("clicked", id, value)
        self.click_count += 1
        Elm("btn1").value = "Clicked " + str(self.click_count) + " times"
    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run2(ui = myApp, debug=True)