import os
import hashlib
import MySQLdb
import uuid
import traceback
from binascii import hexlify
from json import loads, dumps
from flask import current_app
from model.user import User

class Auth:
    def __init__(self, config):
        self.config = config


    def register(self, login, password):
        """ Attempt to register user to dillsapp's directory. """
        if not login:
            return None
        if not password:
            return None

        u = User(self.config, login=login)
        if u.uid:
            return dumps({'error': 'User with username already exists.'})

        u.create(login)
        u.login = login

        try:
            u.iterations = self.config.get('pw-hashing-iter')
            u.salt = hexlify(os.urandom(16))

            dk = hashlib.pbkdf2_hmac('sha256', password, u.salt, int(u.iterations))
            u.hash_val = hexlify(dk)

            u.save()

            return {'user_id': u.uid}
        except:
            current_app.logger.error(traceback.format_exc())
            return None


    def login(self, login, password):
        """ Attempt to authenticate to dillsapp's directory. """

        u = User(self.config, login=login)
        if not u.uid:
            return dumps({'error': 'No user with login exists.'})

        try:
            (hash_val, salt, iterations) = u.get_credentials()
            dk = hashlib.pbkdf2_hmac('sha256', password, u.salt, int(iterations))
            
            if hash_val == hexlify(dk):
                return {'user_id': u.uid}
            else:
                return None
        except:
            current_app.logger.error(traceback.format_exc())
            return None
