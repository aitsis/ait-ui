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
        self.events["change"] = lambda id, value: print("change", id, value)
        self.on_upload_done = on_upload_done

    def get_client_handler_str(self, event_name):
        if event_name in ["input","change"]:
            return f" on{event_name}='clientEmit(this.id,this.files[0],\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

    def upload_done(self, uploaded_file_path, uploaded_file_name):
        try:
            if self.save_path:
                save_file_path = os.path.join(self.save_path, uploaded_file_name)
                shutil.move(uploaded_file_path, save_file_path)
                self.on_upload_done(save_file_path)
        except Exception as e:
            print(e)

    def upload_started(self, id, file):
        print("upload_started", id, file["file_name"])
        uploaded_file_path = os.path.join(tempfile.gettempdir(), file["uid"])
        uploaded_file_name = file["file_name"]

        if os.path.exists(uploaded_file_path):
            # check if the file is used by another process
            try:
                with open(uploaded_file_path, "rb") as f:
                    f.close()
                self.upload_done(uploaded_file_path, uploaded_file_name)
                return
            except Exception as e:
                print(e)
                pass
        else:
            print("File not found:", uploaded_file_path)
            return -1