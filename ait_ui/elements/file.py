import os
import tempfile
import threading
import shutil

from ..core import Element

class File(Element):
    def __init__(self,id = None,value = None,multiple = False, save_path = None,on_upload_done = None, autoBind=True):
        super().__init__(id = id, value = value, autoBind=autoBind)
        self.tag = "input"
        self.value_name = "value"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.attrs["multiple"] = multiple
        self.cls("file")
        self.style("display", "none")
        self.save_path = save_path
        self.events["file-upload-started"] = self.upload_started
        self.events["change"] = self.on_change
        self.on_upload_done = on_upload_done
        self.uploaded_file_path = None
        self.uploaded_file_name = None
        self.timeout = 10
        self.counter = 0

    def get_client_handler_str(self, event_name):
        if event_name in ["input","change"]:
            return f" on{event_name}='clientEmit(this.id,this.files[0],\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def on_change(self,id,file):
        pass

    def upload_done(self):
        if self.save_path is not None:
            save_file_path = os.path.join(self.save_path, self.uploaded_file_name)
            shutil.copyfile(self.uploaded_file_path, save_file_path)
            print("File saved to", save_file_path)
            os.remove(self.uploaded_file_path)
            self.on_upload_done(save_file_path)
            #TODO: add error handling here

    def upload_started(self,id,file):
        #timer = threading.Timer(1, self.upload_started, [id,file])
        #print(f"{self.counter} {self.timeout}")
        if self.counter == 0:
            print("upload_started", id, file["file_name"])
            self.uploaded_file_path = os.path.join(tempfile.gettempdir(), file["uid"])
            self.uploaded_file_name = file["file_name"]

        # self.counter += 1
        # if self.counter > self.timeout:
        #     self.counter = 0
        #     self.uploaded_file_name = None
        #     self.uploaded_file_path = None
        #     print("upload timeout")
        #     #TODO: add error handling here
        #     return

        if os.path.exists(self.uploaded_file_path):
            # check if the file is used by another process
            try:
                with open(self.uploaded_file_path, "rb") as f:
                    f.close()
                self.upload_done()
                self.counter = 0
                return
            except:
                pass

        # timer.start()