from .. import socket_handler
from .. import Session

def Elm(id):
    if id in Session.current_session.elements:
        return Session.current_session.elements[id]
    else:
        return None

class Element:
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
        if id is not None:
            Session.current_session.elements[id] = self
        
        if auto_bind:
            if self.root is None:
                self.root = self
                self.cur_parent = self
                self.parent = None
            else:
                if self.cur_parent is not None:
                    self.parent = self.cur_parent
                    self.cur_parent.add_child(self)
                else:
                    self.parent = None
                    self.cur_parent = self

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
        return Session.current_session.current_parent
    
    @cur_parent.setter
    def cur_parent(self, value):
        Session.current_session.current_parent = value

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
        self.cur_parent = self
        self.children = []
        return self
    
    def __exit__(self, type, value, traceback):                
        self.cur_parent = self.parent
        
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
        # <div
        if self.id is not None:
            str += f" id='{self.id}'"
        # <div id='myid'   
        class_str = " ".join(self.classes)
        # <div id='myid' class='myclass1 myclass2'
        if(len(class_str) > 0):
            str += f" class='{class_str}'"
        # <div id='myid' class='myclass1 myclass2'
        if(len(self.styles) > 0):
            style_str = " style='"
            # <div id='myid' class='myclass1 myclass2' style='
            for style_name, style_value in self.styles.items():
                style_str += f" {style_name}:{style_value};"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;'
            str += style_str + "'"
        for attr_name, attr_value in self.attrs.items():
            str += f" {attr_name}='{attr_value}'"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value'
        for event_name, action in self.events.items():
            str += self.get_client_handler_str(event_name)
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")'
        if self.has_content:
            str +=">"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")'>
            str +=f"{self.value if self.value is not None and self.value_name is not None else ''}"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")'>value
            for child in self.children:
                str += child.render()
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")'>value<child1><child2>
            str += f"</{self.tag}>"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")'>value<child1><child2></div>
        else:
            if self.value is not None:
                if(self.value_name is not None):
                    str +=f' {self.value_name} ="{self.value}"'
            str += "/>"
            # <div id='myid' class='myclass1 myclass2' style='width:100px;height:100px;' attr_name='attr_value' onevent_name='clientEmit(this.id,this.value,"event_name")' value='value'/>
        return str

