import os
import hashlib
import MySQLdb
import uuid
import traceback
from binascii import hexlify
from json import loads

class Auth:
    def __init__(self, config):
        self.config = config


    def register(self, login, password):
        """ Attempt to register user to dillsapp's directory. """
        if not login:
            return None
        if not password:
            return None

        iterations = self.config.get('pw-hashing-iter')
        salt = hexlify(os.urandom(16))
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, int(iterations))

        user_id = str(uuid.uuid4())
        sql = """INSERT INTO User (uid, login, hash, salt, iterations)
                 VALUES (%s, %s, %s, %s, %s)"""
        params = (user_id, login, hexlify(dk), salt, iterations)

        db = self.get_connection()
        c = db.cursor()
        c.execute(sql, params)
        
        db.commit()

        return {'user_id': user_id}


    def login(self, login, password):
        """ Attempt to authenticate to dillsapp's directory. """

        sql = """ SELECT uid, hash, salt, iterations FROM User WHERE login = %s """
        params = (login,)

        db = self.get_connection()
        c = db.cursor()
        c.execute(sql, params)

        try:
            (user_id, hash_hex, salt, iterations) = c.fetchone()
            dk = hashlib.pbkdf2_hmac('sha256', password, salt, int(iterations))

            if hexlify(dk) == hash_hex:
                return {'user_id': user_id}
            else:
                return None
        except:
            traceback.print_exc()
            return None


    def get_connection(self):
        """ Returns a db connection for use. """
        fields = loads(self.config.get('mysql-config'))
        return MySQLdb.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])