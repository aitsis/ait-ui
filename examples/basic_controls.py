#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------


from ait_ui import app
from ait_ui.components import Element, Elm
from ait_ui.components import Row
from ait_ui.components import Col
from ait_ui.components import Label
from ait_ui.components import Radio
from ait_ui.components import Slider
from ait_ui.components import Input
from ait_ui.components import Check
from ait_ui.components import Button
from ait_ui.components import Text

def on_click(id, value):
    print("clicked", id, value)
    Elm(id).toggle_class("selected")

def radio_set(id, value,name):
    with Row() as row:
        Label(value=value,usefor=id).style("margin-right", "10px")
        radio = Radio(id = id, name=name)
    return radio

def slider_set(id, label,value):
    with Row() as row:
        Label(value=label,usefor=id).style("margin-right", "10px")
        slider = Slider(id = id,value=value, min=1, max=100, step=1).on("change", lambda id, value: Elm(id+"-input").set_value(value))
        input = Input(id = f"{id}-input",value=value, type="number").on("change", lambda id, value: Elm(id.replace("-input","")).set_value(value))
        input.cls("w2")
    return input

def check_set(id, value):
    with Row() as row:
        Label(value=value,usefor=id).style("width", "80px").style("margin-right", "10px")
        check = Check(id = id).on("click", on_click).style("margin-right", "10px")
    return check

def on_change_radio(id, value):
    print("on_change_radio", id, value)
    Elm("Radio").set_value(id + " selected.")


with Element() as main:
    main.cls("p3")
    with Col() as col:
        col.style("border", "2px solid black")
        col.cls("p3").style("width", "auto")
        radio_set("radio1", "Radio 1","radios1").checked(True).on("change", on_change_radio)
        radio_set("radio2", "Radio 2","radios1").on("change", on_change_radio)
        radio_set("radio3", "Radio 3","radios1").on("change", on_change_radio)
        Text(id = "Radio").style("margin-left", "3px")
    with Col() as space:
        space.style("height", "10px")
    with Col() as col:
        col.style("border", "1px solid black")
        col.cls("p3").style("width", "auto")
        slider_set("slider1", "Slider 1",10)
        slider_set("slider2", "Slider 2",50)
        slider_set("slider3", "Slider 3",90)
    with Col() as space:
        space.style("height", "10px")
    with Col() as col:
        col.style("border", "1px solid black").style("width","120px").style("height", "200px")
        col.cls("p3").style("overflow-y", "scroll").style("overflow-x", "hidden")
        check_set("check1", "Check 1").checked(True)
        check_set("check2", "Check 2")
        check_set("check3", "Check 3")
        check_set("check4", "Check 4")
        check_set("check5", "Check 5")
        check_set("check6", "Check 6")
        check_set("check7", "Check 7")
        check_set("check8", "Check 8")
        check_set("check9", "Check 9")
        check_set("check10", "Check 10")
    
    

if __name__ == '__main__':
    app.run(ui = main, debug=True)

