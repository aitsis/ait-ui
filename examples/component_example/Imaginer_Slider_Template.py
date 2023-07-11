#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Text , Slider , Elm

def change_slider_value(id, value):
    print("changed", id, value)
    Elm("slider-value-"+id).value = value

def Imaginer_Slider_Template(text=None, id=None, min=None, max=None, value=None):
    with Element() as content:
        content.style("display", "flex").style("justify-content", "space-between").style("align-items", "center").style("width", "100%")
        Text(value = text)
        Text(value = value, id="slider-value-"+id)
    Slider(id = id, min = min, max = max, value=value).style("width", "100%").on("input", change_slider_value)
    
    return content