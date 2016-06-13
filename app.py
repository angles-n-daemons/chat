from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

from lib.config import Config

app = Flask(__name__)
cfg = Config('config.db')
app.config['SECRET'] = cfg.get('socket-key')