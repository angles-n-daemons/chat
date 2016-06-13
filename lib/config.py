import os
import sqlite3

class Config:

    def __init__(self, config_file):
        if not config_file:
            raise Exception('No configuration file name provided.')
        self.conn = sqlite3.connect(config_file)

    def get(self, cfg_id):
        """ Fetches a configuration value by id if config item exists. """

        if not cfg_id:
            raise Exception("No configuration item id given.")

        query = "SELECT val FROM Config WHERE id = '%s'" % cfg_id
        c = self.conn.cursor()
        c.execute(query)

        row = c.fetchone()
        if not row:
            raise Exception("Invalid Configuration item: '%s'" % cfg_id)
        else:
            return row[0]