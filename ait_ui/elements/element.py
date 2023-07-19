from .. import socket_handler
from .. import Session
root = None
cur_parent = None

def Elm(id):
    if id in Session.current_session.elements:
        return Session.current_session.elements[id]
    else:
        return None

class Element:
    _current = None

    def __init__(self, id = None,value = None,auto_bind = True):        
        self.tag = "div"
        self.id = id
        self._value = value
        self.children = []
        self.events = {}
        self.styles = {}
        self.classes = []
        self.attrs = {}
        self.parent = None
        self.value_name = "value"
        self.has_content = True

        # FOR HTML HEAD -> Both Scripts and Styles
        self.header_items = {}

        # FOR HTML BODY -> Scripts Only
        self.script_sources = {}
        self.scripts = {}
        self.custom_styles = {}
        
        if id is not None:
            Session.current_session.elements[id] = self
        
        if auto_bind:
            if Element._current is not None:
                self.parent = Element._current
                Element._current.add_child(self)

    def append_header_item(self, id, item, type="script"):
        self.header_items[id] = item
        
    def append_script_source(self, id:str, script:str):
        self.script_sources[id] = script

    def append_script(self, id:str, script:str):
        self.scripts[id] = script

    def append_custom_style(self, id:str, style:str):
        self.custom_styles[id] = style

    def get_header_items(self):
        return self.header_items

    def get_scripts(self):
        return self.scripts
    
    def get_script_sources(self):
        return self.script_sources
    
    def get_custom_styles(self):
        return self.custom_styles
    
    def get_all_scripts(self):
        scripts = self.get_scripts()
        for child in self.children:
            child_scripts = child.get_all_scripts()
            scripts.update(child_scripts)
        return scripts

    def get_all_script_sources(self):
        scripts = self.get_script_sources()
        for child in self.children:
            child_scripts = child.get_all_script_sources()
            scripts.update(child_scripts)
        return scripts

    def get_all_custom_styles(self):
        custom_styles = self.get_custom_styles()
        for child in self.children:
            custom_styles.update(child.get_all_custom_styles())
        return custom_styles
    
    def get_all_header_items(self):
        header_items = self.get_header_items()
        for child in self.children:
            child_header_items = child.get_all_header_items()
            header_items.update(child_header_items)
        return header_items

    def update(self):
        Session.current_session.send(self.id, self.render(), "init-content")

    def set_value(self, value):
        self.value = value

    @property
    def root(self):
        return Session.current_session.root

    @root.setter
    def root(self, value):
        Session.current_session.root = value

    @property
    def cur_parent(self):
        return Session.current_session.cur_parent
    
    @cur_parent.setter
    def cur_parent(self, value):
        Session.current_session.cur_parent = value

    @property
    def value(self):
        return self._value
    
    @property
    def webserver(self):
        return socket_handler.web_server

    @property
    def web_request(self):
        return socket_handler.web_request

    @value.setter
    def value(self, value):
        self._value = value
        Session.current_session.send(self.id, value, "change-"+self.value_name)

    def toggle_class(self, class_name):
        Session.current_session.send(self.id, class_name, "toggle-class")
    
    def set_attr(self, attr_name, attr_value):
        Session.current_session.send(self.id, attr_value, "change-"+attr_name)
    
    def set_style(self, attr_name, attr_value):
        Session.current_session.send(self.id, attr_value, "set-"+attr_name)

    def add_child(self, child):        
        self.children.append(child)

    def __enter__(self):
        # Store the previous current parent, and set the current parent to this instance
        self._prev = Element._current
        Element._current = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the previous current parent when exiting this context
        Element._current = self._prev
        
    def __str__(self):
        return self.render()
    
    def cls(self,class_name):
        self.classes.append(class_name)
        return self

    def style(self,style,value):
        self.styles[style] = value
        return self
    
    def on(self,event_name,action):
        self.events[event_name] = action
        return self
    
    def get_client_handler_str(self, event_name):
        return f" on{event_name}='clientEmit(this.id,this.{self.value_name},\"{event_name}\")'"

    def render(self):
        str = f"<{self.tag}"
        if self.id is not None:
            str += f" id='{self.id}'"
        class_str = " ".join(self.classes)
        if(len(class_str) > 0):
            str += f" class='{class_str}'"
        if(len(self.styles) > 0):
            style_str = " style='"
            for style_name, style_value in self.styles.items():
                style_str += f" {style_name}:{style_value};"
            str += style_str + "'"
        for attr_name, attr_value in self.attrs.items():
            str += f" {attr_name}='{attr_value}'"
        for event_name, action in self.events.items():
            str += self.get_client_handler_str(event_name)
        if self.has_content:
            str +=">"
            str +=f"{self.value if self.value is not None and self.value_name is not None else ''}"
            for child in self.children:
                str += child.render()
            str += f"</{self.tag}>"
        else:
            if self.value is not None:
                if(self.value_name is not None):
                    str +=f' {self.value_name} ="{self.value}"'
            str += "/>"
        return str

