#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Text , Select , Option , TextArea , Button , Elm


def on_change(id, value):
    print("changed", id, value)
    Elm("input1").value = value

def on_click(id, value):
    print("clicked", id, value)
    Elm("input1").value = value


def Imaginer_Top_Side(): 
    with Element() as content:
        content.cls("imaginer-body-top")
        #Left Col
        with Element() as content:
            content.cls("imaginer-body-left-top")
            Text(value = "Models")
            with Select(id="select1") as select:
                select.on("change", on_change)
                Option(value="1")
                Option(value="2")
                Option(value="3")
        #Right Col
        with Element() as content:
            content.cls("imaginer-body-right-top")
            Text(value = "Prompt")
            with Element() as content:
                content.cls("imaginer-body-right-input-wrapper")
                TextArea(id = "input1", placeholder="Type Here ...").on("change", print("changed"))
        with Element() as content:
            content.cls("imaginer-body-buttonwrapper")
            Button(value = "Generate" , id="imaginer-button").on("click", on_click).style("background-color", "green")
            Button(value = "Clear" , id="imaginer-button").on("click", on_click)
