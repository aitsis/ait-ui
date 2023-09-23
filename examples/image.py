#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------
from PIL import Image as PILImage

from ait_ui import app
from ait_ui.elements import Image, Button
from ait_ui.core import Component

# create a new image
img = PILImage.new('RGB', (60, 30), color = 'red')

class MyApp(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        with self:
            self.img = Image()
            Button(value="Rotate").on("click", self.rotate_image)

    def rotate_image(self, id, value):
        global img
        img = img.rotate(90)
        img.save("rotated.png")
        self.img.__setattr__("value", "/rotated.png")

if __name__ == '__main__':
    app.run(ui = MyApp, debug=True)