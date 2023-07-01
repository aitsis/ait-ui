
#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))
#---------------------------------------------------------------#

import app

from components.element import Element, Elm
from components.text import Text
from components.image import Image
from components.imageviewer import ImageViewer
def on_click(id, value):
    print("clicked", id, value)
    Elm(id).toggle_class("selected")
    Elm("imageviewer1").value = value

with Element() as main:
    ImageViewer(id = "imageviewer1", value="http://127.0.0.1:5001/image/0").style("width", "100%").style("height", "500px")
    for i in range(15):
        Image(id = f"btn{i}", value=f"http://127.0.0.1:5001/image/{i}").on("click", on_click)


if __name__ == '__main__':
    app.run(ui = main, debug=True)

