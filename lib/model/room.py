import MySQLdb
import uuid
from json import loads

class Room:
    def __init__(self, config, name=None):
        self.config = config

        self.name = name
        self.rid = None
        self.color = None

    def create(self):
        """ Creates a room in the system. """

        self.rid = str(uuid.uuid4())
        sql = """INSERT INTO Room (rid, name) VALUES (%s, %s)"""
        params = (self.rid, self.name)

        db = self.get_connection()
        
        c = db.cursor()
        c.execute(sql, params)
        db.commit()

        c.close()
        db.close()


    def list(self, offset=0):
        """ Populates object from row retrieved from database. """

        def row_to_room(row):
            return {'roomId': row[0], 'name': row[1]}

        sql = """SELECT rid, name FROM Room ORDER BY created ASC LIMIT 20 OFFSET %s"""
        params = (offset,)

        db = self.get_connection()

        c = db.cursor()
        c.execute(sql, params)

        rows = c.fetchall()
        c.close()
        db.close()

        rooms = map(row_to_room, rows)

        return {'rooms': rooms}


    def get_connection(self):
        """ Returns a db connection for use. """
        fields = loads(self.config.get('mysql-config'))
        return MySQLdb.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])