from app import db, app
from main import register_blueprints
from items import items
from heroes import heroes

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

register_blueprints(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('items', items())
manager.add_command('heroes', heroes())
manager.add_command('db', MigrateCommand)


def _make_context():
    """Return context dict for a shell session so you can access
    app and db by default.
    """
    return {'app': app, 'db': db}


# Setting up the app database
@manager.command
def setup():
    print('setup')

manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
