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
from ait_ui.elements import Label

def on_upload_done(file):
    if isinstance(file, str):
        print("File uploaded to:", file)
    else:
        print("File uploaded:", file.filename)
        print("File content_type:", file.content_type)
        #get first 20 bytes of file
        print("File content:", file.read(20))
        file.seek(0)



with Element() as main:
    Label(id="dropzone1" , usefor="file").style("width", "100px").style("height", "100px")
    file = File(id="file",on_upload_done=on_upload_done)


if __name__ == '__main__':
    app.run(ui = main, debug=True)