#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------
from ait_ui import app, UI
from ait_ui.elements import Element, Elm, Text, Button, Row
from ait_ui.component import Component

class myApp(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.click_count = 0

        with self:
            with Row() as row:
                row.cls("container")
                self.text = Text(value="Clicked for -> ").style("color", "red")
                self.btn1 = Button(value="BTN 1").on("click", self.on_click)
                Button(value="BTN 2").on("click", self.on_click)
                Button(value="BTN 3").on("click", self.on_click)
            with Row() as row:
                row.cls("container")
                Button(value="BTN 4").on("click", self.on_click)
                Button(value="BTN 5").on("click", self.on_click)
                Button(value="BTN 6").on("click", self.on_click)
            self.create_button_group()

    def create_button_group(self):
        with Row(id="btnGrp"):
            for i in range(self.click_count):
                Button(value="Clicked")

    def on_click(self, id, value):
        self.click_count += 1
        self.text.value = "Clicked for -> " + str(self.click_count) + " times"
        self.btn1.value = "Clicked for -> " + str(self.click_count) + " times"
        self.create_button_group()
        Elm("btnGrp").update()

if __name__ == '__main__':
    app.run(ui = myApp, debug=True)