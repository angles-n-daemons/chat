import os
import hashlib
import _mysql
import uuid
from binascii import hexlify

class Auth:
    def __init__(self, config):
        self.config = config
        
        fields = config.get('mysql-config')
        self.db = _mysql.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])

    def register(self, login, password):
        """ Attempt to register user to dillsapp's directory. """
        if not login:
            return {'error': 'No login supplied'}
        if not password:
            return {'error': 'No password supplied'}

        iterations = self.config.get('pw-hashing-iter')
        salt = hexlify(os.urandom(16))
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, iterations)

        user_id = uuid.uuid4()
        sql = """INSERT INTO User (uid, login, hash, salt, iterations)
                 VALUES (?, ?, ?, ?, ?)"""
        params = (user_id, login, hexlify(dk), salt, iterations)

        self.db.query(sql, params)
        self.db.commit()

        return {'user_id': user_id}

    def login(self, login, password):
        """ Attempt to authenticate to dillsapp's directory. """

        sql = """ SELECT uid, hash, salt, iterations FROM Users WHERE login = ? """
        params = (login,)

        self.db.query(query)
        r = db.use_result()

        (user_id, hash_hex, salt, iterations) = r.fetch_row()
        dk = hashlib.pbkdf2_hmac('sha256', password, salt, iterations)

        if hexlify(dk) == hash_hex:
            return {'user_id': user_id}
        else:
            return {'error': 'Invalid Credentials'}