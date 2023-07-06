#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.components import Element, Elm
from ait_ui.components import Text
from ait_ui.components import Image
from ait_ui.components import ImageViewer
from ait_ui.components import Button
import urllib.parse

# def on_click(id, value):
#     print("clicked", id, value)
#     Elm("text1").value = "Button clicked"
#     with Element(id="image1") as content:
#         content.cls("border").style("background-color", "blue")
#         images_dir = os.path.join(os.getcwd(), "myImages")
#         image_files = os.listdir(images_dir)
#         for file_name in image_files:
#             image_url = "/myImages/" + urllib.parse.quote(file_name)
#             print(f'Image URL: {image_url}')
#             Image(value=image_url)

with Element() as main:
    images_dir = os.path.join(os.getcwd(), "myImages")
    image_files = os.listdir(images_dir)
    for file_name in image_files:
        image_url = "/myImages/" + urllib.parse.quote(file_name)
        print(f'Image URL: {image_url}')
        Image(value=image_url)
    
    images_dir2 = os.path.join(os.getcwd(), "myImages2")
    image_files2 = os.listdir(images_dir)
    for file_name in image_files:
        image_url = "/myImages2/" + urllib.parse.quote(file_name)
        print(f'Image URL: {image_url}')
        Image(value=image_url)

if __name__ == '__main__':
    custom_files_dir = os.path.join(os.getcwd(), "myImages")
    custom_files_dir = os.path.join(os.getcwd(), "myImages2")
    app.add_custom_file_route("myImages", osDirPath=custom_files_dir)
    app.add_custom_file_route("myImages2", osDirPath=custom_files_dir)
    app.run(ui=main, debug=True, port=5002)

