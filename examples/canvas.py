
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



mouse_down = False
def on_mouse_down(id, value):
    global mouse_down
    mouse_down = True
    print("on_mouse_down", id, value)
    Elm(id).fill_rect(value["x"], value["y"], 10, 10)

def on_mouse_up(id, value):
    global mouse_down
    mouse_down = False
    print("on_mouse_up", id, value)

def on_mouse_move(id, value):
    global mouse_down
    if mouse_down:
        print("on_mouse_move", id, value)
        Elm(id).fill_rect(value["x"], value["y"], 10, 10)
        

with Element() as main:
    canvas = Canvas(id = "canvas1").width(800).height(600)
    canvas.on("mousedown", on_mouse_down)
    canvas.on("mouseup", on_mouse_up)
    canvas.on("mousemove", on_mouse_move)
    


if __name__ == '__main__':
    app.run(ui = main, debug=True)

