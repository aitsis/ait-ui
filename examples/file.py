#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import app
from ait_ui.elements import Element, Elm, File, Label, Image

class MyApp():
    def __init__(self):
        self.main = Element()
        self.main.style("display", "flex").style("flex-direction", "column").style("align-items", "center").style("justify-content", "center").style("height", "100vh")
        with self.main:
            Label(id="dropzone1", usefor="file").style("width", "100px").style("height", "100px").style("border", "1px solid black").style("background-color", "red")
            save_path = os.path.join(os.path.dirname(__file__), 'assets')
            #Image(id = "image1", value="/assets/blue.png").style("width", "100px").style("height", "100px")
            file = File(id="file", save_path=save_path, on_upload_done=self.on_upload_done)
            file.on("change", self.on_file_input)

    def on_upload_done(file):
        if isinstance(file, str):
            print("File uploaded to:", file)
            file_name = os.path.basename(file)
            Elm("image1").value = "/assets/" + file_name
        else:
            print("File uploaded:", file.filename)
            print("File content_type:", file.content_type)

    def on_file_input(self, id, value):
        print("on_file_input", id, value)
    
    def render(self):
        return self.main.render()

if __name__ == '__main__':
    images_path = os.path.join(os.path.dirname(__file__), 'assets')
    app.add_static_route('assets', images_path)
    app.run(ui = MyApp, debug=True)