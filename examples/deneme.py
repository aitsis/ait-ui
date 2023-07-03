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
from components.col import Col
from components.row import Row
import connection
def on_click(id, value):
    print("clicked", id, value)
    with Element(id="col1") as elem:
        Text(id = "counter", value = "0")
        Text(id="counter2" ,value = "0")
        Text(id="sum", value = "0")
        for i in range(4):
                with Element() as content:
                    content.cls("border").style("background-color", "red").style("margin", "10px")
                    Text(value = f"SELAM {i}", id = "text"+str(i))
        Button(id = "btn2", value = "Click Me").on("click", on_click2)
    connection.send("col1", elem.render(), "init-content")

import random

def on_click2(id, value):
    print("clicked", id, value)
    # increase counter
    counter = int(Elm("counter").value)
    # random number
    counter += random.randint(1, 10)
    Elm("counter").value = str(counter)
    # increase counter2
    counter2 = int(Elm("counter2").value)
    counter2 += 1
    Elm("counter2").value = str(counter2)
    # multiply
    sum = counter * counter2
    Elm("sum").value = str(sum)

def Comp(id, value):
    with Element(id = "muge") as content:
        content.cls("semih")
        Text(value = "Hello World")
        Button(id = "btn1", value = "Click Me").on("click", on_click)
        with Element() as content:
            content.cls("border").style("background-color", "blue")
            Text(value = "Hello World")
            for i in range(4):
                with Element() as content:
                    content.cls("border").style("background-color", "red").style("margin", "10px")
                    Text(value = f"Hello World {i}", id = "text"+str(i))
        with Element() as content:
            content.cls("border")
            Text(value = "Hello afsgvhdjaskjfhgjk")
    with Element() as content:
        content.cls("border")
        Text(value = "Hello World")
        with Element() as content:
            content.cls("border")
            Text(value = "Hello World")

with Row() as main:
    main.cls("border").cls("p4")
    with Col(id="col1") as col:
        col.style("width", "50%")
        Comp(id = "comp1", value = "Hello World")
    with Col() as col:
        col.style("width", "50%")
        # https://www.ait.com.tr/wp-content/themes/aittema/images/logo.svg
        ImageViewer(id="seadragon", value = "https://www.ait.com.tr/wp-content/themes/aittema/images/logo.svg").style("width", "100%").style("height", "500px")

if __name__ == '__main__':
    app.run(ui = main, debug=True)
