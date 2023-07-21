#app.py
from flask import Flask, send_from_directory, abort, request, g
from flask_cors import CORS
from flask_socketio import SocketIO
from . import index_gen
from .elements import Element

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(flask_app)
socket_handler.socket = socketio
socket_handler.web_server = flask_app
socket_handler.web_request = request
CORS(flask_app)

client_sessions = {}
dir_routes = {}

ui_generator = None

class Session:
    def __init__(self, ui, sid):
        global current_session
        current_session = self
        self.ui = ui
        self.sid = sid
        self.elements = {}

    def Elm(self, id):
        return self.elements.get(id)
    
    def send_event(self, id, value, event_name):
        socketio.emit("from_server", {'id': id, 'value': value, 'event_name': event_name}, room=self.sid)

    def create_element(session, element_class, *args, **kwargs):
        element = element_class(*args, **kwargs)
        session.add_element(element)
        return element

    def handle_event(self, json):
        global current_session
        current_session = self
        client_id = json.get('client_id')
        print(f"Client id: {client_id}")
        if client_id is not None and client_id in self.elements:
            elm = self.Elm(client_id)
            if json['event_name'] in elm.events:
                elm.events[json['event_name']](client_id, json['value'])
        print(f'Received json: {str(json)} from client {self.sid}\nCurrent sids -> {client_sessions}\n')
        if json['id'] == "myapp":
            if json['value'] == "init":
                socketio.emit("from_server", {'id': "myapp", 'value': self.ui.render(), 'event_name': "init-content"}, room=self.sid)
        else:
            print(f"Handling event {json['event_name']} for {json['id']}")
            print(f"Current elements: {self.elements}")
            elm = self.Elm(json['id'])
            if elm is not None:
                if json['event_name'] in elm.events:
                    elm.events[json['event_name']](json['id'], json['value'])

@socketio.on('from_client')
def handle_from_client(json):
    sid = request.sid
    if sid not in client_sessions:
        client_sessions[sid] = Session(ui_generator(sid), sid)
    client_sessions[sid].handle_event(json)

@socketio.on('connect')
def handle_connect():
    sid = request.sid
    client_sessions[sid] = Session(ui_generator(sid), sid)

@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    del client_sessions[sid]

@flask_app.route('/')
def home():
    return index_gen.generate_index()

@flask_app.route('/<path:path>')
def files(path):
    print("Path:",path)  # Ensure the path is correct
    return send_from_directory("static", path)

def add_static_route(route, osDirPath):
    print("Route Path:",osDirPath)  # Ensure the path is correct
    dir_routes[route] = osDirPath

@flask_app.route('/<route>/<path:file_path>')
def custom_files(route, file_path):
    if route not in dir_routes:
        abort(404)    
    return send_from_directory(dir_routes[route], file_path)

def run(_ui_generator=None, port=5000, debug=True):
    global ui_root, ui_generator
    if _ui_generator is not None:
        ui_generator = _ui_generator
    flask_app.run(host="0.0.0.0", port=port, debug=debug)

if __name__ == '__main__':
    run()