import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import application, db


application.config.from_object(os.environ.get(
    'APP_SETTINGS', 'config.DevelopmentConfig'))

migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
