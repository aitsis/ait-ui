import os
import tempfile
from functools import wraps
from uuid import uuid4
from threading import Lock

from flask import Flask, request, send_from_directory, abort, jsonify, make_response
from flask_cors import CORS
from flask_socketio import SocketIO

from .core import Session, index_gen

# DISABLE LOGGING
import logging
logging.getLogger('werkzeug').disabled = True

flask_app = Flask(__name__)
socketio = SocketIO(flask_app, cors_allowed_origins="*", transports=["websocket"])
#socketio = SocketIO(flask_app, cors_allowed_origins="*")

# Global definitions for convenience
server = flask_app
web_socket = socketio
web_request = request
Session.socket = socketio

CORS(flask_app)

ui_root = None

dir_routes = {}
sessions = {}
un_init_sessions = {}

# Thread Locks
route_lock = Lock()
socket_lock = Lock()

@socketio.on('connect')
def handle_client_connect():
    #print('Socket connected')
    session_id = request.args.get('session_id')
    clientPublicData = request.args.get('clientPublicData')

    if session_id and session_id in un_init_sessions:
        session_instance = un_init_sessions.pop(session_id)
        session_instance.clientPublicData = clientPublicData
        sessions[request.sid] = session_instance
        session_instance.init(request.sid)
    else:
        pass

@socketio.on('disconnect')
def handle_client_disconnect():
    del sessions[request.sid]

@socketio.on('from_client')
def handle_from_client(msg):
    with socket_lock:
        Session.current_session = sessions[request.sid]
        Session.current_session.clientHandler(msg['id'], msg.get('value', ""), msg['event_name'])

@flask_app.route('/<path:path>')
def files(path):
    response = send_from_directory("static", path)
    response.headers['Cache-Control'] = 'max-age=31536000'
    return response

@flask_app.route('/file-upload', methods=['POST'])
def upload():
    try:
        id = request.form.get('id')
        uid = request.form.get('uid')
        file = request.files.get('file')

        if not id or not uid or not file:
            return jsonify({'error': 'Missing parameters', 'status': 400}), 400

        if file.filename == '':
            return jsonify({'error': 'No selected file', 'status': 400}), 400

        allowed_extensions = {'png', 'jpg', 'jpeg', 'tif', 'tiff'}
        if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            return jsonify({'error': 'Invalid file extension', 'status': 400}), 400

        max_file_size = 100 * 1024 * 1024
        if len(file.read()) > max_file_size:
            return jsonify({'error': 'File size exceeds the limit', 'status': 400}), 400
        file.seek(0)

        file_path = os.path.join(tempfile.gettempdir(), uid)
        file.save(file_path)

        return jsonify({'message': 'File uploaded successfully', 'status': 200}), 200

    except Exception as e:
        return jsonify({'error': str(e), 'status': 500}), 500

@flask_app.route('/js/<path:path>')
def js_files(path):
    response = send_from_directory("js", path)
    response.headers['Cache-Control'] = 'max-age=31536000'
    return response

def add_static_route(route, osDirPath):
    #print("Route Path:",osDirPath)  # Ensure the path is correct
    dir_routes[route] = osDirPath

@flask_app.route('/<route>/<path:file_path>')
def custom_files(route, file_path):
    if route not in dir_routes:
        abort(404)
    response = send_from_directory(dir_routes[route], file_path)
    response.headers['Cache-Control'] = 'max-age=31536000'
    return response

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return no_cache

@DeprecationWarning
def add_custom_route(route, ui_class, middlewares=[]):
    @flask_app.route(route, endpoint=f"{ui_class.__name__}")
    def custom_route_func():
        with route_lock:
            session_id = str(uuid4())
            session = Session(ui_class, cookies=request.cookies)
            un_init_sessions.append(session)

            wrapped_func = session.get_index
            for middleware in reversed(middlewares):
                wrapped_func = middleware(wrapped_func)

            response_data = wrapped_func()
            response = make_response(response_data)

            response.set_cookie('session_id', session_id)

            return response
    
    return custom_route_func

def run(ui = None,host = "0.0.0.0", port=5000, debug='production'):
    global ui_root
    if ui is not None:
        ui_root = ui

        @flask_app.route('/')
        def home():
            session_id = str(uuid4())
            session = Session(ui = ui_root, base_url = f"http://{host}", cookies=request.cookies)
            un_init_sessions[session_id] = session
            response = make_response(index_gen.get_index())
            response.set_cookie('session_id', session_id)
            return response

    flask_app.run(host="0.0.0.0",port=port, debug=debug)

if __name__ == '__main__':
    run()
