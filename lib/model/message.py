import MySQLdb
import uuid
from json import loads

class Message:

    @staticmethod
    def create(config, data):
        """ Save a message to MySQL database for future retrieval. """
        mid = str(uuid.uuid4())
        sql = """INSERT INTO Message (mid, rid, uid, content, login, sent_when) VALUES (%s, %s, %s, %s, %s, NOW())"""
        params = (mid, data['roomId'], data['userId'], data['content'], data['login'])

        fields = loads(config.get('mysql-config'))
        db = MySQLdb.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])
        c = db.cursor()
        c.execute(sql, params)
        db.commit()

        c.close()
        db.close()
        
        return True