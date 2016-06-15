from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from lib.config import Config

app = Flask(__name__)
cfg = Config('config.db')

app.debug = (__name__ == '__main__')
app.config['SECRET'] = cfg.get('socket-key')
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def route_index():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def route_chat():
    return render_template('chat.html')



@app.route('/api/login', methods=['POST'])
def api_login():
	print request.form

@app.route('/api/signup', methods=['POST'])
def api_signup():
	print request.form



@socketio.on('test')
def sock_test(obj):
	pass

@socketio.on('create_room')
def create_room(data):
    pass

if __name__ == '__main__':
    socketio.run(app)
