from flask import Flask, request, jsonify, send_from_directory, send_file, abort
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from . import Session
import os
import tempfile
flask_app = Flask(__name__)
socketio = SocketIO(flask_app)

# Global definitions for convenience
server = flask_app
web_socket = socketio
web_request = request
Session.socket = socketio

CORS(flask_app)

ui_root = None

dir_routes = {}
sessions = {}
un_init_sessions = []

@socketio.on('connect')
def handle_from_client(json):
    print('Socket connected')
    sessions[request.sid] = un_init_sessions.pop()
    sessions[request.sid].init(request.sid)

@socketio.on('from_client')
def handle_from_client(msg):    
    Session.current_session = sessions[request.sid]
    Session.current_session.clientHandler(msg['id'], msg['value'], msg['event_name'])        

@flask_app.route('/')
def home():
    session = Session(ui_root)
    un_init_sessions.append(session)
    return session.get_index()

@flask_app.route('/<path:path>')
def files(path):
    return send_from_directory("static", path)

@flask_app.route('/file-upload', methods=['POST'])
def upload():
    id = request.form['id']
    file = request.files['file']
    uid = request.form['uid']
    if file:
        file.save(os.path.join(tempfile.gettempdir(), uid))        
    return 'File uploaded successfully.'    #TODO: add error handling here


@flask_app.route('/js/<path:path>')
def js_files(path):
    return send_from_directory("js", path)

def add_static_route(route, osDirPath):
    print("Route Path:",osDirPath)  # Ensure the path is correct
    dir_routes[route] = osDirPath

@flask_app.route('/<route>/<path:file_path>')
def custom_files(route, file_path):
    if route not in dir_routes:
        abort(404)
    return send_from_directory(dir_routes[route], file_path)

def run(ui = None, port=5000, debug=True):
    global ui_root
    assert ui is not None, "ui is None"
    ui_root = ui
    flask_app.run(host="0.0.0.0",port=port, debug=debug,ssl_context='adhoc')

if __name__ == '__main__':
    run()
