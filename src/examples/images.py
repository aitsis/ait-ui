#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#-------------------------------------------------------------

from ait_ui import app

from ait_ui.components.element import Element, Elm
from ait_ui.components.text import Text
from ait_ui.components.image import Image
from ait_ui.components.imageviewer import ImageViewer
from ait_ui.components.button import Button
def on_click(id, value):
    print("clicked", id, value)
    Elm("text1").value = "Button clicked"
    with Element(id = "image1") as content:
        content.cls("border").style("background-color", "blue")
        Image(src = "https://www.w3schools.com/html/pic_trulli.jpg")

with Element() as main:
    Text(id = "text1", value = "Image Viewer Example")
    Button(id = "button1", value = "image1").on("click", on_click)

    
    

if __name__ == '__main__':
    app.run(ui = main, debug=True)

