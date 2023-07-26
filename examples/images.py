#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------
import urllib.parse

from ait_ui import app
from ait_ui.elements import Element, Image, Row

custom_route = "assets"

class MyApp():
    def __init__(self):
        self.main = Element()
        with self.main:
            with Row():
                images_dir = os.path.join(os.getcwd(), custom_route)
                image_files = os.listdir(images_dir)
                for file_name in image_files:
                    image_url = "/assets/" + urllib.parse.quote(file_name)
                    print(f'Image URL: {image_url}')
                    Image(value=image_url)

    def render(self):
        return self.main.render()

if __name__ == '__main__':
    custom_path = os.path.join(os.getcwd(), "assets")
    app.add_static_route(custom_route, osDirPath=custom_path)    
    app.run(ui=MyApp, debug=True)