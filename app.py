from flask import Flask, render_template, request, make_response, abort, current_app
from flask_socketio import SocketIO, emit, join_room, leave_room
from json import dumps

from lib.config import Config
from lib.auth import Auth
from lib.model.room import Room

app = Flask(__name__)
cfg = Config('config.db')

app.debug = (__name__ == '__main__')
app.config['SECRET'] = cfg.get('socket-key')
socketio = SocketIO(app)

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

@socketio.on('create_room')
def create_room(data):
    roomName = data['name']
    r = Room(config, roomName)
    r.create()
    emit('new_room', {'roomId': r.rid, 'name': r.name, 'color': r.color})


@socketio.on('join')
def on_join(data):
    login = data['login']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    login = data['login']
    room = data['roomId']
    leave_room(room)
    send(username + ' has left the room.', room=room)

@socketio.on('message')
def on_message(data):
    pass

@socketio.on('test')
def sock_test(obj):
    print obj
    pass

if __name__ == '__main__':
    socketio.run(app)
