#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Text , Slider , Option , TextArea , Button , Elm
from .Imaginer_Slider_Template import Imaginer_Slider_Template

def change_slider_value(id, value):
    print("changed", id, value)
    Elm("slider-value-"+id).value = value

def Imaginer_Bottom_Side():
        with Element().cls("imaginer-body-bottom"):
            #Left Col
            with Element().cls("imaginer-body-left-bottom"):
                with Element(id="accordion-wrapper"):
                    with Element(id="accordion-opener").on("click", lambda : print("clicked")):
                     Text(value = "Advanced Options" , id="accordion-text")
                    with Element().cls("imaginer-body-left-bottom-top-div"):
                        with Element().cls("imaginer-body-left-bottom-top-div-left"):
                            Imaginer_Slider_Template(text="Temperature",id="1",min="0",max="100",value="50")
                        with Element().cls("imaginer-body-left-bottom-top-div-left"):
                            Imaginer_Slider_Template(text="Temperature",id="2",min="0",max="100",value="50")
                    with Element().cls("imaginer-body-left-bottom-top-div"):
                        with Element().cls("imaginer-body-left-bottom-top-div-left"):
                            Imaginer_Slider_Template(text="Temperature",id="3",min="0",max="100",value="50")
                    with Element().cls("imaginer-body-left-bottom-top-div"):
                        with Element().cls("imaginer-body-left-bottom-top-div-left"):
                            Imaginer_Slider_Template(text="Temperature",id="4",min="0",max="100",value="50")
                        with Element().cls("imaginer-body-left-bottom-top-div-left") :
                            Imaginer_Slider_Template(text="Temperature",id="5",min="0",max="100",value="50")
                #Right Col
            with Element().cls("imaginer-body-right-bottom"):
                Text(value = "Output")
                with Element().cls("imaginer-body-right-input-wrapper"):
                    pass