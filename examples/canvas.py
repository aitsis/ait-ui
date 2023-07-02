
#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
#---------------------------------------------------------------#

import app

from components.element import Element, Elm
from components.text import Text
from components.image import Image
from components.imageviewer import ImageViewer
from components.canvas import Canvas
from components.row import Row
from components.button import Button
from components.slider import Slider

mouse_down = False
selected_color = "red"
colors = ["red", "green", "blue", "yellow", "black", "white"]
radius = 10
def on_mouse_down(id, value):
    global mouse_down
    mouse_down = True
    print("on_mouse_down", id, value)
    Elm(id).fill_rect(value["x"], value["y"], 10, 10,selected_color)

def on_mouse_up(id, value):
    global mouse_down
    mouse_down = False
    print("on_mouse_up", id, value)

def on_mouse_move(id, value):
    global mouse_down
    if mouse_down:
        print("on_mouse_move", id, value)
        Elm(id).fill_circle(value["x"], value["y"], radius,selected_color)
        

def on_click(id, value):
    global selected_color
    print("clicked", id, value)
    selected_color = colors[int(id[-1])-1]
    Elm("selected-color").set_style("background-color", selected_color)
    
def on_change_slider(id, value):
    global radius
    radius = value
    print("on_change_slider", id, value)
    
with Element() as main:
    with Row() as row:
        row.style("align-items", "center")
        for i in range(len(colors)):
            Button(id = f"btn{i+1}", value=colors[i]).on("click", on_click).style("background-color", colors[i]).style("width", "50px").style("height", "50px")
        Slider(id = "slider1", value=radius, min=1, max=100, step=1).on("change", on_change_slider)
        Element(id="selected-color").style("width", "100px").style("height", "50px").style("background-color", selected_color)
        
    canvas = Canvas(id = "canvas1").width(800).height(600).cls("border")
    canvas.on("mousedown", on_mouse_down)
    canvas.on("mouseup", on_mouse_up)
    canvas.on("mousemove", on_mouse_move)
    


if __name__ == '__main__':
    app.run(ui = main, debug=True)

