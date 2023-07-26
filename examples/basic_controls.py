#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.elements import Element, Elm, Row, Col, Label, Radio, Slider, Input, Check, Text

class BasicControls():
    def __init__(self):
        self.main = Element()
        with self.main:
            self.main.cls("p3")
            with Col() as col:
                col.style("border", "2px solid black")
                col.cls("p3").style("width", "auto")
                self.radio_set("radio1", "Radio 1","radios1").checked(True).on("change", self.on_change_radio)
                self.radio_set("radio2", "Radio 2","radios1").on("change", self.on_change_radio)
                self.radio_set("radio3", "Radio 3","radios1").on("change", self.on_change_radio)
                Text(id = "Radio").style("margin-left", "3px")
            with Col() as space:
                space.style("height", "10px")
            with Col() as col:
                col.style("border", "1px solid black")
                col.cls("p3").style("width", "auto")
                self.slider_set("slider1", "Slider 1",10)
                self.slider_set("slider2", "Slider 2",50)
                self.slider_set("slider3", "Slider 3",90)
            with Col() as space:
                space.style("height", "10px")
            with Col() as col:
                col.style("border", "1px solid black").style("width","120px").style("height", "200px")
                col.cls("p3").style("overflow-y", "scroll").style("overflow-x", "hidden")
                self.check_set("check1", "Check 1").checked(True)
                self.check_set("check2", "Check 2")
                self.check_set("check3", "Check 3")
                self.check_set("check4", "Check 4")
                self.check_set("check5", "Check 5")
                self.check_set("check6", "Check 6")
                self.check_set("check7", "Check 7")
                self.check_set("check8", "Check 8")
                self.check_set("check9", "Check 9")
                self.check_set("check10", "Check 10")

    def on_click(self, id, value):
        print("clicked", id, value)
        Elm(id).toggle_class("selected")

    def radio_set(self, id, value, name):
        with Row() as row:
            Label(value=value,usefor=id).style("margin-right", "10px")
            radio = Radio(id = id, name=name)
        return radio

    def slider_set(self, id, label, value):
        with Row() as row:
            Label(value=label,usefor=id).style("margin-right", "10px")
            slider = Slider(id = id,value=value, min=1, max=100, step=1).on("change", lambda id, value: Elm(id+"-input").set_value(value))
            input = Input(id = f"{id}-input",value=value, type="number").on("change", lambda id, value: Elm(id.replace("-input","")).set_value(value))
            input.cls("w2")
        return input

    def check_set(self, id, value):
        with Row() as row:
            Label(value=value,usefor=id).style("width", "80px").style("margin-right", "10px")
            check = Check(id = id).on("click", self.on_click).style("margin-right", "10px")
        return check

    def on_change_radio(self, id, value):
        print("on_change_radio", id, value)
        Elm("Radio").set_value(id + " selected.")

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run(ui = BasicControls, debug=True)