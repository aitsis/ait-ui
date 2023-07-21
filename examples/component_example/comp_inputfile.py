#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Element , Text , File , Elm , Label , Col , Image
from ait_ui.component import Component


class Comp_InputFile(Component):

    save_path = os.getcwd() + "/assets"
    
    def __init__(self, id=None):
        super().__init__()
        with Element().style("height","100%").style("width","100%"):
            File(id = "file1", save_path=self.save_path,on_upload_done=self.on_upload_done)
            with Label(id="dropzone-label" , usefor="file1"):
                with Col(id="dropzone-inside").style("height","100%").style("width","100%").style("justify-content","center").style("align-items","center"):    
                    Text(value = "Drag and Drop").style("height","0")
                    Text(value = "- or -").style("height","0")
                    Text(value = "Click to Upload").style("height","0")
                with Image(id="dropzone-image").style("display","none").style("max-width","80%").style("max-height","90%"):
                    pass
    
    def on_upload_done(self,file):
        if isinstance(file, str):
            print("File uploaded to:", file)
            file_name = os.path.basename(file)
            Elm("dropzone-inside").set_style("display","none")
            Elm("dropzone-image").set_style("display","flex")
            Elm("dropzone-image").value = "/assets/" + file_name 
        else:
            print("File uploaded:", file.filename)
            print("File content_type:", file.content_type)
        if self.events["change"]:
            self.events["change"](id, file)
        

    def on_input(self, value):
        print("Input File: ", value)
    