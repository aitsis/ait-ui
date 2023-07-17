import os
from .element import Element
class File(Element):
    def __init__(self,id = None,value = None,multiple = False, save_path = None,on_upload_done = None):
        super().__init__(id = id, value = value)                
        self.tag = "input"
        self.value_name = "value"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.attrs["multiple"] = multiple
        self.cls("file")
        self.style("display", "none")
        self.webserver.add_url_rule('/file-upload', 'upload', self.upload, methods=['POST'])
        self.save_path = save_path
        self.events["input"] = self.on_input
        self.on_upload_done = on_upload_done

    def on_input(self, id, value):
        print("on_input", id, value)

    def get_client_handler_str(self, event_name):
        if event_name in ["input"]:
            return f" on{event_name}='clientEmit(this.id,this.files[0],\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)
        
    def upload(self):
        request = self.web_request        
        file = request.files['file']        
        if file:
            if self.save_path is not None:
                filepath = os.path.join(self.save_path, file.filename)
                file.save(filepath)
                if self.on_upload_done is not None:
                    self.on_upload_done(filepath)
            else:
                if self.on_upload_done is not None:
                    self.on_upload_done(file)
            return 'File uploaded successfully.'
        else:
            return 'No file uploaded.'

