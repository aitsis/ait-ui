from .element import Element
class File(Element):
    def __init__(self,id = None,value = None):
        super().__init__(id = id, value = value)                
        self.tag = "input"
        self.value_name = "value"
        self.attrs["type"] = "file"
        self.attrs["name"] = "file"
        self.cls("file")
        self.style("display", "none")

    def get_client_handler_str(self, event_name):
        if event_name in ["input", "change"]:
            return f" on{event_name}='clientEmit(this.id,this.files,\"{event_name}\")'"
        else:
            return super().get_client_handler_str(event_name)

