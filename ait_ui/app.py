import os
import tempfile
from http.cookies import SimpleCookie

from flask import Flask, request, send_from_directory, abort, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

from .core import Session, clear_index

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
def handle_client_connect():
    print('Socket connected')
    cookie_str = request.args.get('cookie')

    cookies_dict = {}
    if cookie_str and cookie_str.strip():
        parsed_cookie = SimpleCookie()
        try:
            parsed_cookie.load(cookie_str)
            cookies_dict = {key: morsel.value for key, morsel in parsed_cookie.items()}
        except Exception as e:
            print(f"Error parsing cookie: {e}")

    session_instance = un_init_sessions.pop()
    session_instance.cookies = cookies_dict

    sessions[request.sid] = session_instance
    session_instance.init(request.sid)
    session_instance.socket.emit('afterconnect', {'message': 'Connection initialized'}, room=request.sid)

@socketio.on('disconnect')
def handle_client_disconnect():
    print('Socket disconnected')
    if request.sid in sessions:
        del sessions[request.sid]
        print("Session deleted")

@socketio.on('from_client')
def handle_from_client(msg):
    Session.current_session = sessions[request.sid]
    if msg.get('value') is None:
        msg['value'] = ''
    Session.current_session.clientHandler(msg['id'], msg['value'], msg['event_name'])

@flask_app.route('/')
def home():
    session = Session(ui_root)
    un_init_sessions.append(session)
    session.clear_index()
    ui_root()
    return session.get_index()

@flask_app.route('/<path:path>')
def files(path):
    return send_from_directory("static", path)

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

        max_file_size = 5 * 1024 * 1024
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
    return send_from_directory("js", path)

def add_static_route(route, osDirPath):
    print("Route Path:",osDirPath)  # Ensure the path is correct
    dir_routes[route] = osDirPath

@flask_app.route('/<route>/<path:file_path>')
def custom_files(route, file_path):
    if route not in dir_routes:
        abort(404)
    return send_from_directory(dir_routes[route], file_path)

def add_custom_route(route, ui_class, middlewares=[]):
    @flask_app.route(route, endpoint=f"{ui_class.__name__}")
    def custom_route_func():
        session = Session(ui_class)
        un_init_sessions.append(session)
    
        # Apply all middleware decorators
        session.clear_index()
        ui_class()
        wrapped_func = session.get_index
        for middleware in reversed(middlewares):
            wrapped_func = middleware(wrapped_func)

        return wrapped_func()
    
    return custom_route_func

def run(ui = None, port=5000, debug=True):
    global ui_root
    assert ui is not None, "ui is None"
    ui_root = ui
    flask_app.run(host="0.0.0.0",port=port, debug=debug)

if __name__ == '__main__':
    run()
