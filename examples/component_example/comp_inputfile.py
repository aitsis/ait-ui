#----------------------------------------------#
#  AIT UI Component                             #
#----------------------------------------------#
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ait_ui.elements import Text, File, Label, Col, Image
from ait_ui.core import Component

class Comp_InputFile(Component):
    def __init__(self, id=None , save_path=None, autoBind=True, **kwargs):
        super().__init__(id=id, autoBind=autoBind, **kwargs)
        self.save_path = save_path
        self.add_css("inputfile-css", """                                 
                            .dropzone-label{
                                width: 100%;
                                height: 100%;
                                border: 1px dashed gray;
                                border-radius: 3px;
                                display: flex;
                                flex-direction: column;
                                justify-content: center;
                                align-items: center;
                                color: gray;
                                font-size: 20px;
                                font-weight: 600;
                                cursor: pointer;
                            }""")
        
        self.style("height","100%").style("width","100%")
        with self:
            self.file = File(save_path=self.save_path, on_upload_done=self.on_upload_done)
            with Label(usefor=self.file.id).cls("dropzone-label"):
                with Col().style("gap", "10px").style("height", "100%").style("width", "100%").style("justify-content", "center").style("align-items", "center") as dropzone_inside:
                    self.dropzone_inside = dropzone_inside
                    Text(value="Drag and Drop")
                    Text(value="- or -")
                    Text(value="Click to Upload")
                with Image().style("display", "none").style("max-width", "80%").style("max-height", "90%") as dropzone_image:
                    self.dropzone_image = dropzone_image
    
    def on_upload_done(self,file):
        if isinstance(file, str):
            print("File uploaded to:", file)
            file_name = os.path.basename(file)
            self.dropzone_inside.set_style("display", "none")
            self.dropzone_image.set_style("display", "flex")
            self.dropzone_image.value = file
            self.value = file
        else:
            print("File uploaded:", file.filename)
            print("File content_type:", file.content_type)