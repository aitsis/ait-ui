import os
import requests
import httpx

from .index_gen import get_index

class Session:
    #Static Variables
    socket = None
    current_session: 'Session' = None
    BASE_URL = "domain"
    
    def __init__(self, ui, base_url=None):                
        self.elements = {}
        self.sid = None
        self.message_queue = []
        self.root = None
        self.parent_stack = []
        self.cookies = None

        Session.current_session = self
        self.ui = ui()

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
        return {c.key: c.value for c in self.cookies.values()} if self.cookies else {}

    def construct_url_and_cookies(self, endpoint):
        full_url = os.path.join(Session.BASE_URL, endpoint.lstrip('/'))
        cookies_dict = self.cookies_to_dict()
        return full_url, cookies_dict

    def api_call(self, endpoint, method='GET', data=None, headers=None, json=None):
        full_url, cookies_dict = self.construct_url_and_cookies(endpoint)
        response = requests.request(method, full_url, data=data, cookies=cookies_dict, headers=headers, json=json)
        return response

    async def async_api_call(self, endpoint, method='GET', data=None, headers=None, json=None):
        full_url, cookies_dict = self.construct_url_and_cookies(endpoint)
        async with httpx.AsyncClient() as client:
            response = await client.request(method, full_url, data=data, cookies=cookies_dict, headers=headers, json=json)
        return response