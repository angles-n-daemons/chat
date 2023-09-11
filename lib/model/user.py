import MySQLdb
import uuid
from json import loads

class User:
    def __init__(self, config, uid=None, login=None):
        self.config = config
        self.uid = None
        self.login = None
        self.hash_val = None
        self.salt = None
        self.iterations = None


        identity = uid if uid else login
        id_col = 'uid' if uid else 'login'
        self.set_user(id_col, identity)


    def create(self, login):
        """ Creates a user in the system. """
        
        if self.uid:
            raise Exception('User already exists.')
        
        user_id = str(uuid.uuid4())
        sql = """INSERT INTO User (uid, login, hash, salt) VALUES (%s, %s, '', '')"""
        params = (user_id, login)

        db = self.get_connection()

        c = db.cursor()
        c.execute(sql, params)
        db.commit()

        self.uid = user_id

        c.close()
        db.close()


    def save(self):
        """ Save user info to database. """

        if not self.uid:
            raise Exception('User not in db.')

        sql = """UPDATE User SET hash = %s, salt = %s, iterations = %s WHERE uid = %s;"""
        params = (self.hash_val, self.salt, self.iterations, self.uid)

        db = self.get_connection()
        
        c = db.cursor()
        c.execute(sql, params)
        db.commit()

        c.close()
        db.close()


    def set_user(self, id_col, identity):
        """ Sets all metadata info for given user. """

        sql = """ SELECT uid, login, hash, salt, iterations FROM User WHERE {0} = %s""".format(id_col)
        params = (identity,)

        db = self.get_connection()
        
        c = db.cursor()
        c.execute(sql, params)

        if c.rowcount:
            row = c.fetchone()
            self.uid = row[0]; self.login = row[1]; self.hash_val = row[2]; self.salt = row[3]; self.iterations = row[4]

        c.close()
        db.close()

    def get_credentials(self):
        """ Returns an easily useable tuple for authentication. """

        return (self.hash_val, self.salt, self.iterations)

    def get_connection(self):
        """ Returns a db connection for use. """
        fields = loads(self.config.get('mysql-config'))
        return MySQLdb.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])
