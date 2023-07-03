from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import connection
import index_gen
import os
flask_app = Flask(__name__)
socketio = SocketIO(flask_app)
connection.socket = socketio
CORS(flask_app)

ui_root = None

@socketio.on('connect')
def handle_from_client(json):
    print('Socket connected')
    if connection.clientHandler is not None:
        connection.clientHandler('myapp', 'connect', 'connect')    


@socketio.on('from_client')
def handle_from_client(json):
    print('Received json: ' + str(json))
    if json['id'] == "myapp":
        if json['value'] == "init":
            connection.send("myapp", ui_root.render(), "init-content")
    if connection.clientHandler is not None:
        connection.clientHandler(json['id'], json['value'], json['event_name'])    

@flask_app.route('/')
def home():
    return index_gen.generate_index()

@flask_app.route('/<path:path>')
def files(path):
    return send_from_directory("static", path)


def run(ui = None, debug=True):
    global ui_root
    if ui is not None:
        ui_root = ui        
    flask_app.run(host="0.0.0.0",port=5002, debug=debug)

if __name__ == '__main__':
    run()