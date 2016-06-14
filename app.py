from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from lib.config import Config

app = Flask(__name__)
cfg = Config('config.db')

app.debug = (__name__ == '__main__')
app.config['SECRET'] = cfg.get('socket-key')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def index():
    return render_template('chat.html')

@app.route('/api/login')
def login():
    # todo authenticate

@socketio.on('test')
def sock_test(obj):
    print obj

@socketio.on('create_room')
def create_room(data):
    pass

if __name__ == '__main__':
    socketio.run(app)
