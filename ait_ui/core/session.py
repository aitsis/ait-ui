import os
import requests
import httpx

from .index_gen import get_index

class Session:
    #Static Variables
    socket = None
    current_session: 'Session' = None
    BASE_URL = "http://192.168.99.78:3000"
    
    def __init__(self, ui, base_url=None):                
        self.elements = {}
        self.sid = None
        self.message_queue = []
        self.root = None
        self.parent_stack = []
        self.cookies = None

        Session.current_session = self
        self.ui_temp = ui
        self.ui = None

        # Set the base URL for API calls
        if base_url:
            Session.BASE_URL = base_url

    def push_parent(self, parent):
        self.parent_stack.append(parent)

    def pop_parent(self):
        return self.parent_stack.pop() if self.parent_stack else None

    @property
    def current_parent(self):
        return self.parent_stack[-1] if self.parent_stack else None

    def init(self,sid):
        self.sid = sid
        self.ui = self.ui_temp()              
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
        return get_index()
    
    def navigate(self, path):
        self.send("myapp", path, "navigate")
    
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

    # Cookie handling
    def cookies_to_dict(self):
        return self.cookies if self.cookies else {}

    def api_call(self, method='GET', endpoint='', data=None, headers=None, json=None, cookies=None, isSecure=True):
        try:
            endpoint = endpoint.lstrip('/')
            base_url = self.BASE_URL if self.BASE_URL.endswith('/') else self.BASE_URL + '/'
            full_url = base_url + endpoint
            
            cookies_to_use = cookies if cookies else self.cookies_to_dict()
            which_cookies = "cookies" if cookies else "self.cookies"
            print(f"API Call: {method} {full_url} with {which_cookies}\nself.cookies: {self.cookies}\ncookies: {cookies}")

            print("Cookies before request: ", cookies_to_use) # Ensure this prints the correct cookies
            response = requests.request(method, full_url, data=data, cookies=cookies_to_use, headers=headers, json=json)
            return response
        except Exception as e:
            print("API Call Error: ", e)
            return None