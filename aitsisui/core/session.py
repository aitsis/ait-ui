import requests

from urllib.parse import urljoin
from requests.exceptions import MissingSchema, InvalidURL

class Session:
    #Static Variables
    socket = None
    current_session: 'Session' = None
    BASE_URL = "http://0.0.0.0"
    PORT = 3000
    
    def __init__(self, ui, base_url=None, port=None, cookies=None, user=None, locale='en-US'):                
        self.elements = {}
        self.sid = None
        self.message_queue = []
        self.root = None
        self.parent_stack = []
        self.user = user if user else {}
        self.clientPublicData = {}
        self.cookies = cookies
        self.locale = locale

        Session.current_session = self
        self.ui = ui(locale=locale)

        if base_url:
            Session.BASE_URL = base_url
        if port:
            Session.PORT = port

    def push_parent(self, parent):
        self.parent_stack.append(parent)

    def pop_parent(self):
        return self.parent_stack.pop() if self.parent_stack else None

    @property
    def current_parent(self):
        return self.parent_stack[-1] if self.parent_stack else None

    def init(self,sid):
        self.sid = sid
    
    def send(self,id, value, event_name):    
        Session.socket.emit("from_server", {'id': id, 'value': value, 'event_name': event_name}, room=self.sid)

    def queue_for_send(self, id, value, event_name):
        #print("queueing for send", id, value, event_name)
        self.message_queue.append({'id': id, 'value': value, 'event_name': event_name})

    def flush_message_queue(self):
        for item in self.message_queue:            
            self.send(item['id'], item['value'], item['event_name'])
        self.message_queue = []

    def navigate(self, path):
        self.send("myapp", path, "navigate")
    
    def clientHandler(self, id, value,event_name):
        if id == "myapp":
            if value == "init":                
                #print("Client Initialized")
                self.send("myapp", self.ui.render(), "init-content")
                self.flush_message_queue()
        else:
            if id in self.elements:
                elm = self.elements[id]
                if elm is not None:            
                    if event_name in elm.events:
                        elm.events[event_name](id, value)
        self.flush_message_queue()

    # Cookie handling
    def cookies_to_dict(self):
        return self.cookies if self.cookies else {}

    def api_call(self, method='GET', endpoint='', data=None, headers=None, json=None, cookies=None, usePORT=None):
        try:
            base_url_with_port = f"{self.BASE_URL}:{self.PORT}" if usePORT else self.BASE_URL

            full_url = urljoin(base_url_with_port, endpoint)

            cookies_to_use = cookies if cookies else self.cookies_to_dict()
            
            response = requests.request(method, full_url, data=data, cookies=cookies_to_use, headers=headers, json=json)
            return response
        except MissingSchema as e:
            #print("API Call Error: Missing or incorrect URL schema", e)
            return None
        except InvalidURL as e:
            #print("API Call Error: Invalid URL", e)
            return None
        except Exception as e:
            #print("API Call Error: ", e)
            return None
