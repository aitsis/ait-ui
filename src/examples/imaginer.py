#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#-------------------------------------------------------------

from ait_ui import app

from ait_ui import connection
from ait_ui.components.element import Element, Elm
from ait_ui.components.text import Text
from ait_ui.components.image import Image
from ait_ui.components.row import Row
from ait_ui.components.col import Col
from ait_ui.components.button import Button
from ait_ui.components.input import Input
from ait_ui.components.textarea import TextArea
from ait_ui.components.dropzone import Dropzone
from ait_ui.components.select import Select
from ait_ui.components.option import Option

def on_change(id, value):
    print("changed", id, value)
    Elm("input1").value = value

global isLoading
isLoading = False

def loading():
    print("loading")
    isLoading = True

with Element(id = "imaginer-wrapper") as main:
        main.cls("imaginer-wrapper")
        #Header Row
        with Element() as content:
            content.cls("imaginer-header")
            with Col() as content:
                content.cls("imaginer-header-left")
                Text(value = "Imaginer").style("margin", "0")
            with Col() as content:
                content.cls("imaginer-header-right")
                Text(value = "Imaginer").style("margin", "0")
        #Body Row
        with Element() as content:
            content.cls("imaginer-body-top")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-top")
                if isLoading:
                    Text(value = "Loading")
                else:
                    Text(value = "Model")
                with Select(id="imaginer-dropdown" ) as select:
                    select.on("change", print("changed"))
                    Option(value = "Model 1" , id="imaginer-option")
                    Option(value = "Model 2" , id="imaginer-option")
                    Option(value = "Model 3" , id="imaginer-option")
                    Option(value = "Model 4" , id="imaginer-option")
                    Option(value = "Model 5" , id="imaginer-option")
            #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-top")
                Text(value = "Prompt")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")
                    TextArea(id = "input1", placeholder="Type Here ...").on("change", print("changed"))
            with Element() as content:
                content.cls("imaginer-body-buttonwrapper")
                Button(value = "Generate" , id="imaginer-button").on("click", loading()).style("background-color", "green")
                Button(value = "Clear" , id="imaginer-button").on("click", print("clicked"))
        with Element() as content:
            content.cls("imaginer-body-center")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-center")
                Text(value = "Input")
                Dropzone(id = "dropzone1", value = "https://i.imgur.com/4ZgXQ2g.jpg")
            #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-center")
                Text(value = "Output")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")
        with Element() as content:
            content.cls("imaginer-body-bottom")
            #Left Col
            with Element() as content:
                content.cls("imaginer-body-left-bottom")
                Text(value = "Advanced Options")
            #Right Col
            with Element() as content:
                content.cls("imaginer-body-right-center")
                Text(value = "Output")
                with Element() as content:
                    content.cls("imaginer-body-right-input-wrapper")

if __name__ == '__main__':
    app.run(ui = main, debug=True)
