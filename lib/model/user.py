import MySQLdb

class User:
    def __init__(self, config, login=None, uid=None):
        self.config = config
        self.uid = None
        self.login = None
        self.hash_val = None
        self.salt = None
        self.iterations = None

        sql = """ SELECT uid, hash, salt, iterations FROM User WHERE login = %s """
        params = (login,)

    def create(self):
        """ Creates a user in the system. """
        
        user_id = str(uuid.uuid4())
        sql = """INSERT INTO User (uid) VALUES (%s)"""
        params = (user_id,)

        db = self.get_connection()
        c = db.cursor()
        c.execute(sql, params)
        
        db.commit()

    def save(self):
        """ Save user info to database. """

        if not self.uid:
            raise Exception('User not in db.')

        sql = """UPDATE User """

    def is_stored(self):
        """ Check if user in database. """

        

    def get_connection(self):
        """ Returns a db connection for use. """
        fields = loads(self.config.get('mysql-config'))
        return MySQLdb.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])