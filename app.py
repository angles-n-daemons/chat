from flask import Flask, render_template, request, make_response, abort, current_app
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from json import dumps

from lib.config import Config
from lib.auth import Auth
from lib.model.room import Room
from lib.model.message import Message

app = Flask(__name__)
cfg = Config('config.db')

app.debug = (__name__ == '__main__')

app.config['SECRET'] = cfg.get('socket-key')
socketio = SocketIO(app)
socketio.server.eio.async_mode = 'gevent'

config = Config('config.db')
auth = Auth(config)

@app.before_request
def log_request():
    current_app.logger.debug(request.url)    

@app.route('/', methods=['GET'])
def route_index():
    return render_template('index.html')

@app.route('/app', methods=['GET'])
def route_chat():
    return render_template('app.html')



@app.route('/api/login', methods=['POST'])
def api_login():
    login = request.form.get('login')
    password = request.form.get('password')

    result = auth.login(login, password)
    if result:
        return dumps(result)
    else:
        abort(401)


@app.route('/api/signup', methods=['POST'])
def api_signup():
    login = request.form.get('login')
    password = request.form.get('password')

    result = auth.register(login, password)
    if result:
        return dumps(result)
    else:
        abort(401)

@app.route('/api/room/<action>', methods=['GET'])
def api_room(action):
    if action == 'list':
        r = Room(config)
        return dumps(r.list())

@app.route('/api/message/<action>/<room_id>', methods=['GET'])
def api_message(action, room_id):
    if action == 'list':
        r = Room(config)
        return dumps(r.getMessages(room_id))

@socketio.on('create_room')
def create_room(data):
    roomName = data['name']
    r = Room(config, roomName)
    r.create()
    emit('new_room', {'roomId': r.rid, 'name': r.name, 'color': r.color})


@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)

@socketio.on('leave')
def on_leave(data):
    room = data['roomId']
    leave_room(room)

@socketio.on('send_message')
def on_message(data):
    Message.create(config, data)
    emit('new_message', data, room=data['roomId'])

@socketio.on('test')
def sock_test(obj):
    print obj
    pass

if __name__ == '__main__':
    socketio.run(app, port=8000)
