#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui import  app
from ait_ui.elements import Element, Elm
from ait_ui.elements import Text
from ait_ui.elements import Button
from ait_ui.elements import File
from ait_ui.elements import Form
from ait_ui.elements import Label,Image

def on_upload_done(file):
    if isinstance(file, str):
        print("File uploaded to:", file)
        file_name = os.path.basename(file)
        Elm("image1").value = "/assets/" + file_name
    else:
        print("File uploaded:", file.filename)
        print("File content_type:", file.content_type)
        
    
def on_file_input(id, value):
    print("on_file_input", id, value)
    
with Element() as main:
    Label(id="dropzone1" , usefor="file").style("width", "100px").style("height", "100px")
    save_path = os.getcwd() + "/examples/assets"
    Image(id = "image1")
    file = File(id="file", save_path=save_path,on_upload_done=on_upload_done)
    file.on("change",on_file_input)


if __name__ == '__main__':
    images_path = os.path.join(os.path.dirname(__file__), 'assets')
    app.add_static_route('assets', images_path)
    app.run(ui = main, debug=True)