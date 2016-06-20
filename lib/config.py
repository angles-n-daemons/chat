import os
import sqlite3

class Config:

    def __init__(self, config_file):
        if not config_file:
            raise Exception('No configuration file name provided.')
        self.conn = sqlite3.connect(config_file)

        if not self.check_config_table():
            self.create_config_table()
            
    def check_config_table(self):
        """ Returns boolean value of existence of config table. """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Config'"
        c = self.conn.cursor()
        c.execute( query )
        row = c.fetchone()
        
        if not row:
            return False
        else:
            return True

    def create_config_table(self):
        """ Creates the config table for the app. """

        query = "CREATE TABLE Config (id VARCHAR(50) NOT NULL, val VARCHAR(400) NOT NULL, PRIMARY KEY (id))"
        c = self.conn.cursor()
        c.execute( query )
        self.conn.commit()

    def get(self, cfg_id):
        """ Fetches a configuration value by id if config item exists. """

        if not cfg_id:
            raise Exception("No configuration item id given.")

        query = "SELECT val FROM Config WHERE id = ?"
        c = self.conn.cursor()
        c.execute( query, (cfg_id,) )

        row = c.fetchone()
        if not row:
            raise Exception("Invalid Configuration item: '%s'" % cfg_id)
        else:
            return row[0]

    def set(self, cfg_id, val):
        """ Sets a configuration value in the sqlite db. """

        if not cfg_id:
            raise Exception("No configuration item id given.")

        if not val:
            raise Exception("No value for item given.")

        c = self.conn.cursor()

        query = "DELETE FROM Config WHERE id=?;"
        params = ( cfg_id, )
        c.execute( query, params )

        query="INSERT INTO Config (id, val) VALUES (?,?)"
        params = (cfg_id, val)
        c.execute( query, params )

        self.conn.commit()