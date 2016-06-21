from flask import Flask, render_template, request, make_response, abort
from flask_socketio import SocketIO, emit
from json import dumps

from lib.config import Config
from lib.auth import Auth

app = Flask(__name__)
cfg = Config('config.db')

app.debug = (__name__ == '__main__')
app.config['SECRET'] = cfg.get('socket-key')
socketio = SocketIO(app)

config = Config('config.db')
auth = Auth(config)

@app.route('/', methods=['GET'])
def route_index():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def route_chat():
    return render_template('chat.html')



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

@socketio.on('test')
def sock_test(obj):
    pass

@socketio.on('create_room')
def create_room(data):
    pass

if __name__ == '__main__':
    socketio.run(app)
