#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.elements import Element, Elm, File, Label, Image,Button
from ait_ui.component import Component
import random

class MyApp(Component):
    def __init__(self, id=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.style("display", "flex").style("flex-direction", "column").style("align-items", "center").style("justify-content", "center").style("height", "100vh")

        with self:
            Label(value = "Upload File", usefor="file").style("width", "100px").style("height", "100px").style("border", "1px solid black").style("background-color", "red")
            save_path = os.path.join(os.path.dirname(__file__), 'assets')
            self.file = File(save_path=save_path, on_upload_done=self.on_upload_done)
            Button(value="Test Color").on("click", self.on_click)
            self.image = Image(value="/assets/ait.png")

    def on_upload_done(self, file):
        if isinstance(file, str):
            print("File uploaded to:", file)
            file_name = os.path.basename(file)
            self.image.value = "/assets/" + file_name
        else:
            print("File uploaded:", file.filename)
            print("File content_type:", file.content_type)
    
    def on_click(self, id, value):
        colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        Elm(id).set_style("background-color", random.choice(colors))

if __name__ == '__main__':
    images_path = os.path.join(os.path.dirname(__file__), 'assets')
    app.add_static_route('assets', images_path)
    app.run(ui = MyApp, debug=True)