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
from components.button import Button
from components.link import Link
from components.file import File
def on_click(id, value):
    Elm(id).set_attr("location", "https://ait.com.tr")


def Component(id):
    with Element(id = "muge") as content:
        content.cls("semih")
        Text(value = "Hello World")
        Button(value = "Click Me").on("click", on_click)
    with Element() as content:
        content.cls("border")
        Text(value = "Hello World")
    with Element() as content:
        content.cls("border")
        Text(value = "Hello World")

with Element() as main:
    main.cls("border").cls("p4")
    with Element() as header:
        header.cls("border").cls("p4")
        Component("muge")
        Component("muge")
        Component("muge")


if __name__ == '__main__':
    app.run(ui = main, debug=True)
