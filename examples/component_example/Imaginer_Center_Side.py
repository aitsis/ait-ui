#---------------------------------------------------------------#
# This code added to run app.py from the examples directory
# on production does not need to be added
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
#----------------------------------------

from ait_ui.elements import Element , Text , File , Label , Elm , Image

def setImage(id, value):
    print("changed", id, value)
    image = Elm(id="image1")
    print(value)
    image.value = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"

def Imaginer_Center_Side():
    with Element() as content:
        content.cls("imaginer-body-center")
        #Left Col
        with Element() as content:
            content.cls("imaginer-body-left-center")
            Text(value = "Input")
            File(id = "file1").on("input", setImage)
            with Label(id="dropzone1" , usefor="file1") as label:
                Text(value = "Drag and Drop")
                Text(value = "- or -")
                Text(value = "Click to Upload")
        #Right Col
        with Element() as content:
            content.cls("imaginer-body-right-center")
            Text(value = "Output")
            with Element() as content:
                content.cls("imaginer-body-right-input-wrapper")
                with Image(id="image1", value="").style("max-width","90%").style("max-height","90%") as image:
                    pass
