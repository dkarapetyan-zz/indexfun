from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app, db

__author__ = 'davidkarapetyan'

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server)

if __name__ == '__main__':
    manager.run()
