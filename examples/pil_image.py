#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
print(sys.path)
#----------------------------------------
import time

from ait_ui import app
from ait_ui.elements import Element, Elm
from ait_ui.elements import Text
from ait_ui.elements import Image
from ait_ui.elements import Button
from PIL import Image as PILImage
from PIL import ImageDraw, ImageFont

import threading as th

timer = None
img = PILImage.new('RGB', (160, 160), color = 'white')
font = ImageFont.truetype("arial.ttf", 24)

def draw_image():    
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0,0),(160,160)], fill=(255,255,255,255))
    draw.text((20, 20), "Hello World", font=font, fill=(0, 0, 0, 128))

def rotate_image(id, value):
    global img
    angle = int(value.split(" ")[1])
    if angle is None:
        angle = 0
    img = img.rotate(angle,resample=PILImage.BICUBIC)
    img.save("assets/rotated.png")
    timestamp = str(time.time())
    Elm("image1").value = "assets/rotated.png" + "?t=" + timestamp  # add timestamp to force reload
    

def animate_image(id, value):    
    global img
    global timer
    angle = int(value.split(" ")[1])
    if angle is None:
        angle = 0
    img = img.rotate(angle,resample=PILImage.BICUBIC)
    img.save("assets/rotated.png")
    timestamp = str(time.time())
    Elm("image1").value = "assets/rotated.png" + "?t=" + timestamp  # add timestamp to force reload
    timer = th.Timer(0.1, animate_image, args=[id, value])
    timer.start()
    

def stop_animation(id, value):
    global timer
    timer.cancel()
    

def reset(id, value):
    global img    
    draw_image()
    img.save("assets/rotated.png")
    timestamp = str(time.time())
    Elm("image1").value = "assets/rotated.png" + "?t=" + timestamp  # add timestamp to force reload
    print("reset")


with Element() as main:    
    Image(id="image1")
    reset("","")
    Button(id="button1", value="Rotate 30").on("click", rotate_image)
    Button(id="button2", value="Animate 5").on("click", animate_image)
    Button(id="button3", value="Stop").on("click", stop_animation)
    Button(id="button4", value="Reset").on("click", reset)
    
if __name__ == "__main__":
    custom_path = os.path.join(os.getcwd(), "assets")
    app.add_custom_file_route(osDirPath=custom_path,route="assets")
    app.run(ui = main)