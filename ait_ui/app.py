from flask import Flask, request, jsonify, send_from_directory, send_file, abort
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import os

from . import socket_handler
from . import index_gen
from . import Session

flask_app = Flask(__name__)
socketio = SocketIO(flask_app)

socket_handler.socket = socketio
socket_handler.web_server = flask_app
socket_handler.web_request = request

CORS(flask_app)

ui_root = None
ui_root2 = None

dir_routes = {}
sessions = {}
un_init_sessions = []

@socketio.on('connect')
def handle_from_client(json):
    print('Socket connected')
    Session.socket = socketio
    sessions[request.sid] = un_init_sessions.pop()
    sessions[request.sid].init(request.sid)

@socketio.on('from_client')
def handle_from_client(json):
    print('Received json: ' + str(json))
    Session.current_session = sessions[request.sid]
    Session.current_session.clientHandler(json['id'], json['value'], json['event_name'])

@flask_app.route('/')
def home():
    session = Session(ui_root2)
    un_init_sessions.append(session)
    return session.get_index()

@flask_app.route('/<path:path>')
def files(path):
    return send_from_directory("static", path)

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
    global ui_root2
    assert ui is not None, "ui is None"
    ui_root2 = ui
    flask_app.run(host="0.0.0.0",port=port, debug=debug)

if __name__ == '__main__':
    run()