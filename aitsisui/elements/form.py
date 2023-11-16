from ..core import Element

enctypes = [
    "application/x-www-form-urlencoded",
    "multipart/form-data",
    "text/plain"
]

class Form(Element):
    def __init__(
            self,
            id=None,
            value=None,
            action=None,
            method=None,
            enctype=enctypes[0],
            autoBind=True
        ):
        super().__init__(id=id, value=value, autoBind=autoBind)
        self.tag = "form"
        if method is not None:
            self.attrs["method"] = method

        if enctype is not None:
            self.attrs["enctype"] = enctype

        if action is not None:
            self.attrs["action"] = action