from . import index_gen

class Session:
    #Static Variables
    socket = None
    current_session = None
    
    def __init__(self,ui):                
        self.elements = {}
        self.sid = None
        self.message_queue = []
        self.root = None
        self.parent_stack = []

        Session.current_session = self
        self.ui = ui()

    def push_parent(self, parent):
        self.parent_stack.append(parent)

    def pop_parent(self):
        return self.parent_stack.pop() if self.parent_stack else None

    @property
    def current_parent(self):
        return self.parent_stack[-1] if self.parent_stack else None

    def init(self,sid):
        self.sid = sid                    
        self.flush_message_queue()
    
    def send(self,id, value, event_name):    
        Session.socket.emit("from_server", {'id': id, 'value': value, 'event_name': event_name}, room=self.sid)

    def queue_for_send(self, id, value, event_name):
        print("queueing for send", id, value, event_name)
        self.message_queue.append({'id': id, 'value': value, 'event_name': event_name})

    def flush_message_queue(self):
        for item in self.message_queue:            
            self.send(item['id'], item['value'], item['event_name'])
        self.message_queue = []

    def get_index(self):
        return index_gen.get_index()
    
    def clientHandler(self, id, value,event_name):
        if id == "myapp":
            if value == "init":                
                print("Client Initialized")
                self.send("myapp", self.ui.render(), "init-content")
                self.flush_message_queue()
        else:
            if id in self.elements:
                elm = self.elements[id]
                if elm is not None:            
                    if event_name in elm.events:
                        elm.events[event_name](id, value)