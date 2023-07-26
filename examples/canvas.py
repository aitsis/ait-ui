
#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app, UI
from ait_ui.elements import Element, Elm, Canvas, Row, Button, Slider

class MyApp():
    colors = ["red", "green", "blue", "yellow", "black", "white"]
    def __init__(self):
        self.mouse_down = False
        self.selected_color = "red"
        self.radius = 10
        self.main = Element()
        with self.main:
            with Row() as row:
                row.style("align-items", "center")
                for i in range(len(MyApp.colors)):
                    Button(id = f"btn{i+1}", value=MyApp.colors[i]).on("click", self.on_click).style("background-color", MyApp.colors[i]).style("width", "50px").style("height", "50px")
                Slider(id = "slider1", value=self.radius, min=1, max=100, step=1).on("change", self.on_change_slider)
                Element(id="selected-color").style("width", "100px").style("height", "50px").style("background-color", self.selected_color)
            
            canvas = Canvas(id = "canvas1").width(800).height(600).cls("border")
            canvas.on("mousedown", self.on_mouse_down)
            canvas.on("mouseup", self.on_mouse_up)
            canvas.on("mousemove", self.on_mouse_move)
    def on_mouse_down(self, id, value):
        self.mouse_down = True
        print("on_mouse_down", id, value)
        Elm(id).fill_rect(value["x"], value["y"], 10, 10,self.selected_color)

    def on_mouse_up(self, id, value):
        self.mouse_down = False
        print("on_mouse_up", id, value)

    def on_mouse_move(self, id, value):
        if self.mouse_down:
            print("on_mouse_move", id, value)
            Elm(id).fill_circle(value["x"], value["y"], self.radius,self.selected_color)
        
    def on_click(self, id, value):
        print("clicked", id, value)
        self.selected_color = MyApp.colors[int(id[-1])-1]
        Elm("selected-color").set_style("background-color", self.selected_color)
    
    def on_change_slider(self,id, value):
        self.radius = value
        print("on_change_slider", id, value)
    
    def render(self):        
        return self.main.render()
    
if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)
