#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------
from PIL import Image as PILImage

from ait_ui import app
from ait_ui.elements import Element, Elm, Image, Button

# create a new image
img = PILImage.new('RGB', (60, 30), color = 'red')

class MyApp():
    def __init__(self):
        self.main = Element()
        with self.main:
            Image(id="image1")
            Button(id="button1", value="Rotate").on("click", self.rotate_image)

    def rotate_image(self, id, value):
        global img
        img = img.rotate(90)
        img.save("rotated.png")
        Elm("image1").__setattr__("value", "/rotated.png")

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)