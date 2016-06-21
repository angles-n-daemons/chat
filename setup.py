""" This file allows the user to setup their system prior to run. """
import json
import sys
import os
import _mysql
from lib.config import Config

class Setup:
    def __init__(self):
        self.config = Config('config.db')
        self.setup_opts = ['mysql', 'password-hashing-iterations', 'socket-key']


    def prompt_setup(self):
        """ Prompt user to select item to setup. """
        msg = 'Select an option...'
        for i, val in enumerate(self.setup_opts):
            msg += '\n%s: Setup %s' % (i, val)
        msg += '\n\nt: Test Configuration\nx: Exit program\n'
        item = None

        while True:
            try:
                self.clear_screen()
                item = raw_input(msg)
                if item == 'x':
                    return False
                if item == 't':
                    self.test_configuration()
                    continue

                item = int(item)
                if item < 0 or item >= len(self.setup_opts):
                    raise Exception()
            except:
                self.clear_screen()
                import traceback
                traceback.print_exc()
                raw_input('"%s" not a valid option. Press Enter...\n' % item)
                continue

            if not self.setup_item(self.setup_opts[item]):
                return False


    def setup_item(self, item):
        """ Use as a decoder to select an item to setup. """
        if item == 'mysql':
            return self.setup_mysql()
        if item == 'password-hashing-iterations':
            return self.setup_pw_hash_iterations()
        if item == 'socket-key':
            return self.setup_socket_key()


    def setup_mysql(self):
        """ Get and confirm mysql credentials from user. """
        db = None
        fields = None
        self.clear_screen()
        print 'Setting up MySQL...'

        while True:
            fieldNames = ['host', 'port', 'user', 'password', 'database']
            fields = { f: self.collect_field(f) for f in fieldNames }

            try:
                db = _mysql.connect(host=fields['host'], port=int(fields['port']),
                    user=fields['user'], passwd=fields['password'], db=fields['database'])
                break
            except Exception as e:
                self.clear_screen()
                raw_input('%s \nMySQL setup failed...Press Enter.\n' % e)

                cont = self.prompt_continue()
                if not cont:
                    return False

        deploy_script = open('db/deployment.sql', 'r').read()
        deploy_queries = deploy_script.split(';')
        for query in filter(None, deploy_queries):
            db.query(query)
        db.commit()

        self.config.set('mysql-config', json.dumps(fields))
        raw_input('\nMySQL setup successful! Press Enter.\n')
        return True


    def setup_pw_hash_iterations(self):
        """ Get and confirm desired password hashing iterations. """
        self.clear_screen()
        print 'Setting up Password Hashing Iterations...'

        iterations = None
        while True:
            iterations = raw_input('Num Iterations (recommended 100,000): ')
            try:
                iterations = int(iterations)
                if iterations <= 0:
                    raise Exception()
                break;
            except:
                self.clear_screen()
                raw_input('"%s" not a valid option. Press Enter...\n' % iterations)

                cont = self.prompt_continue()
                if not cont:
                    return False

        self.config.set('pw-hashing-iter', iterations)
        raw_input('\nIterations setup successful! Press Enter.\n')
        return True

    def setup_socket_key(self):
        """ Get and confirm socket key. """
        self.clear_screen()
        print 'Setting up Socket Key...'

        key = None
        while True:
            key = raw_input('Key Value (ideally complex password len > 10): ')
            try:
                if not key:
                    raise Exception()
                break;
            except:
                self.clear_screen()
                raw_input('"%s" not a valid option. Press Enter...\n' % key)

                cont = self.prompt_continue()
                if not cont:
                    return False

        self.config.set('socket-key', key)
        raw_input('\nIterations setup successful! Press Enter.\n')
        return True


    def collect_field(self, field):
        """ Gets a single field value from the user. """
        return raw_input('Enter "%s": ' % field)


    def prompt_continue(self):
        """ Prompts user to continue and returns a boolean value. """
        while True:
            self.clear_screen()
            val = raw_input('Continue? (y/n)').lower().strip()
            if val == 'y':
                return True
            elif val == 'n':
                return False
            else:
                raw_input('"%s" not a valid character response...Press Enter.' % val)


    def clear_screen(self):
        """ Removes all printed output from terminal. """
        os.system('cls' if os.name == 'nt' else 'clear')


    def test_configuration(self):
        """ Test Configuration for running dillsapp application. """
        self.clear_screen()
        try:
            mysql_config = self.config.get('mysql-config')
            iterations = self.config.get('pw-hashing-iter')
            socket_key = self.config.get('socket-key')

            msg = ''
            if not (mysql_config and iterations and socket_key):
                raise Exception()
            msg = 'Configuration Valid! Feel free to start Dillsapp'
        except:
            msg = 'Configuration Invalid. Reattempt Setup.'

        print msg
        raw_input('Press Enter...')

if __name__ == '__main__':
    s = Setup()
    while True:
        if not s.prompt_setup():
            sys.exit()