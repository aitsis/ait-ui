#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.elements import Element, Elm
from ait_ui.elements import Text
from ait_ui.elements import Image
from ait_ui.elements import Button
from PIL import Image as PILImage

# create a new image
img = PILImage.new('RGB', (60, 30), color = 'red')


def rotate_image(id, value):
    global img
    img = img.rotate(90)
    img.save("rotated.png")
    Elm("image1").value = img

with Element() as main:
    Image(id="image1")
    Button(id="button1", value="Rotate").on_click(lambda id, value: Image().rotate(30))
    