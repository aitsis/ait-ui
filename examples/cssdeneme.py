#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Header , Text , Image , File , Label , Select , Option , TextArea , Button , Elm
from ait_ui import app 

from examples.component_example.comp_select import Comp_Select
from examples.component_example.comp_inputfile import Comp_InputFile
from examples.component_example.comp_slider import Comp_Slider
from examples.component_example.comp_header import Comp_Imaginer_Header


def on_change(id, value):
    Elm("input1").value = value

file = None

def on_click(id, value):
    prompt = Elm("input1").value
    slider1 = Elm("slider1-slider").value
    slider2 = Elm("slider2-slider").value
    slider3 = Elm("slider3-slider").value
    global file
    print(prompt, slider1, slider2, slider3)
    Elm("input1").value = str(slider1) + " " + str(slider2) + " " + str(slider3) + " " + str(prompt) 

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
        Elm("accordion").set_style("height", "90%")
    else:
        print("else")
        Elm("accordion-wrapper").set_style("height", "0px")
        Elm("accordion").set_style("height", "9%")
    isAccordionOpen = not isAccordionOpen
   



with Element().cls("main").style("gap","10px") as main:
    with Element().cls("header"):
        with Element().cls("container").style("width", "1400px").style("gap", "10px").style("justify-content", "space-between").style("align-items", "center"):
            with Element().cls("wrapper").style("width", "1400px").style("gap", "10px").style("flex-direction", "row").style("border","none"):
                with Image(value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png").cls("logo"):
                    pass
                with Text(value = "Imaginer").cls("title"):
                    pass
    with Element().cls("container"):
        with Element().cls("wrapper").style("width", "1410px").style("gap", "10px"):
            with TextArea(id="input1" , placeholder="Write Your Prompt Here ...").cls("textarea").style("width", "100%").style("height", "100%"):
                pass
            with Element().cls("wrapper").style("flex-direction", "column").style("gap", "10px"):
                with Button(value="Button 1").cls("btn btn-green"):
                    pass
                with Button(value="Button 1").cls("btn"):
                    pass
    with Element().cls("container").style("flex-direction", "row").style("gap", "10px").style("height", "100%"):
        with Element().cls("wrapper").style("width", "700px").style("gap", "10px").style("height", "100%").style("flex-direction", "column"):
            Comp_InputFile(id="dropzone")
            with Element(id="accordion").cls("accordion"):
                with Button(id="accordion-button").on("click", change_accordion):
                        Text(value = "Advanced Options")
                with Element(id="accordion-wrapper"):
                        with Element().cls("accordion-element-wrapper"):
                                with Element().cls("slider-wrapper"):
                                        Comp_Slider(label="Slider 1", id="slider1", min=0, step=1 , max=100, value=50).on("change_slider", change_slider_value)
                                with Element().cls("slider-wrapper"):
                                        Comp_Slider(label="Slider 2", id="slider2", min=0,step=1 , max=100, value=50).on("change_slider", change_slider_value)
                        with Element().cls("accordion-element-wrapper"):
                                with Element().cls("slider-wrapper"):
                                        Comp_Slider(label="Slider 3", id="slider3", step=5 , min=0, max=100, value=50).on("change_slider", change_slider_value)
                                with Element().cls("slider-wrapper"):
                                                pass
                        Comp_Select(id="select1").on("change", on_change)
        with Element().cls("wrapper").style("width", "700px").style("gap", "10px").style("height", "100%"):
            pass

        



if __name__ == "__main__":
    app.run(ui = main, debug=True)