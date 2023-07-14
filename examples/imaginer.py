#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui import socket_handler
from ait_ui.elements import Element , Header , Text , Image , File , Label , Select , Option , TextArea , Button , Elm

from examples.component_example.comp_select import Comp_Select
from examples.component_example.comp_inputfile import Comp_InputFile
from examples.component_example.comp_slider import Comp_Slider
from examples.component_example.comp_header import Comp_Imaginer_Header

def on_change(id, value):
    Elm("input1").value = value

def on_click(id, value):
    Elm("input1").value = value

#await function
def setImage(id, value):
        image = Elm(id="image1")
        image.value = value
        print(value)
    
def change_slider_value(id, value):
        print(id, value)

isAccordionOpen = True

def change_accordion(id, value):
    global isAccordionOpen
    print(isAccordionOpen)
    if isAccordionOpen:
        print("if")
        Elm("accordion-wrapper").set_style("height", "100%")
        Elm("imaginer-body-left-bottom").set_style("height", "50%")
    else:
        print("else")
        Elm("accordion-wrapper").set_style("height", "0px")
        Elm("imaginer-body-left-bottom").set_style("height", "9%")
    isAccordionOpen = not isAccordionOpen
   


with Element(id = "imaginer-wrapper").cls("imaginer-wrapper") as main:
        with Element().cls("imaginer-top-side"):
                Comp_Imaginer_Header()
                with Element().cls("imaginer-body-top"):
                        with Element().cls("imaginer-body-right-top"):
                                with Element().cls("imaginer-body-right-input-wrapper"):
                                        TextArea(id = "input1", placeholder="Write Your Prompt Here").on("change", print("changed"))
                        with Element().cls("imaginer-body-buttonwrapper"):
                                Button(value = "Generate" , id="imaginer-button").on("click", on_click).style("background-color", "green")
                                Button(value = "Clear" , id="imaginer-button").on("click", on_click)
                with Element().cls("imaginer-body-center"):
                        with Element().cls("imaginer-body-left-center").style("display", "flex").style("flex-direction", "column") as content:
                                with Element().style("height","100%"):
                                     Comp_InputFile(id="file1").on("input", setImage)
                                with Element(id="imaginer-body-left-bottom").cls("imaginer-body-left-bottom"):
                                        with Button(id="accordion-opener").on("click", change_accordion):
                                                Text(value = "Advanced Options")
                                        with Element(id="accordion-wrapper"):
                                                with Element().cls("imaginer-body-left-bottom-top-div"):
                                                        with Element().cls("slider-wrapper"):
                                                                Comp_Slider(label="Slider 1", id="slider1", min=0, step=1 , max=100, value=50).on("change_slider", change_slider_value)
                                                        with Element().cls("slider-wrapper"):
                                                                Comp_Slider(label="Slider 2", id="slider2", min=0,step=1 , max=100, value=50).on("change_slider", change_slider_value)
                                                with Element().cls("imaginer-body-left-bottom-top-div"):
                                                        with Element().cls("slider-wrapper"):
                                                                Comp_Slider(label="Slider 3", id="slider3", step=1 , min=0, max=100, value=50).on("change_slider", change_slider_value)
                                                        with Element().cls("slider-wrapper"):
                                                                pass
                                                Comp_Select(id="select1").on("change", on_change)
                        with Element().cls("imaginer-body-right-center"):
                                with Element().cls("imaginer-body-right-input-wrapper"):
                                        with Image(id="image1", value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png").style("max-width","70%").style("max-height","70%") as image:
                                                pass

        with Element().cls("imaginer-bottom-side"):
                with Header().cls("imaginer-header"):
                        with Element().cls("imaginer-header-left").style("font-size", "20px"):
                                Text(value = "My Assets")
                        with Element().cls("imaginer-header-right"):
                                pass
                with Element().cls("imaginer-asset-body"):
                        with Element().cls("imaginer-asset-body-left"):
                                pass
                        with Element().cls("imaginer-asset-body-right"):
                                pass 
if __name__ == '__main__':
    app.run(ui = main, debug=True)  