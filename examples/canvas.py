
#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app, UI
from ait_ui.elements import Element, Elm, Canvas, Row, Button, Slider
from ait_ui.component import Component

class MyApp(Component):
    colors = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.mouse_down = False
        self.selected_color = MyApp.colors[0]
        self.radius = 10

        with self:
            with Row() as row:
                row.style("align-items", "center")
                for index, value in enumerate(MyApp.colors):
                    button = Button(value=value)
                    button.color = MyApp.colors[index]
                    button.style("background-color", value).style("width", "50px").style("height", "50px")
                    button.on("click", self.on_click)
                Slider(value=self.radius, min=1, max=100, step=1).on("change", self.on_change_slider)
                self.colorBox = Element().style("width", "100px").style("height", "50px").style("background-color", self.selected_color)
            
            self.canvas = Canvas().width(800).height(600).cls("border")
            self.canvas.on("mousedown", self.on_mouse_down)
            self.canvas.on("mouseup", self.on_mouse_up)
            self.canvas.on("mousemove", self.on_mouse_move)

    def on_mouse_down(self, id, value):
        self.mouse_down = True
        print("on_mouse_down", id, value)
        self.canvas.fill_rect(value["x"], value["y"], 10, 10,self.selected_color)

    def on_mouse_up(self, id, value):
        self.mouse_down = False
        print("on_mouse_up", id, value)

    def on_mouse_move(self, id, value):
        if self.mouse_down:
            print("on_mouse_move", id, value)
            self.canvas.fill_circle(value["x"], value["y"], self.radius, self.selected_color)
        
    def on_click(self, id, value):
        self.selected_color = Elm(id).color
        self.colorBox.set_style("background-color", self.selected_color)
    
    def on_change_slider(self,id, value):
        self.radius = value
        print("on_change_slider", id, value)
    
if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)
