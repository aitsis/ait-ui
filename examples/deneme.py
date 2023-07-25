#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

import random

from ait_ui import app
from ait_ui import socket_handler
from ait_ui.elements import Element, Elm, Text, ImageViewer, Button, Col

class Deneme():
    def __init__(self):
        self.main = Element()
        with self.main:
            self.main.cls("border").cls("p4")
            with Col(id="col1") as col:
                col.style("width", "50%")
                self.Comp(id = "comp1", value = "Hello World")
            with Col() as col:
                col.style("width", "50%")
                # https://www.ait.com.tr/wp-content/themes/aittema/images/logo.svg
                ImageViewer(id="seadragon", value = "https://www.ait.com.tr/wp-content/themes/aittema/images/logo.svg").style("width", "100%").style("height", "500px")

    def on_click(self, id, value):
        print("clicked", id, value)
        with Element(id="col1") as elem:
            Text(id = "counter", value = "0")
            Text(id="counter2" ,value = "0")
            Text(id="sum", value = "0")
            for i in range(4):
                    with Element() as content:
                        content.cls("border").style("background-color", "red").style("margin", "10px")
                        Text(value = f"SELAM {i}", id = "text"+str(i))
            Button(id = "btn2", value = "Click Me").on("click", self.on_click2)
        socket_handler.send("col1", elem.render(), "init-content")

    def on_click2(self, id, value):
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

    def Comp(self, id, value):
        with Element(id = "muge") as content:
            content.cls("semih")
            Text(value = "Hello World")
            Button(id = "btn1", value = "Click Me").on("click", self.on_click)
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

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run(ui = Deneme, debug=True)