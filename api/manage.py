from app import create_app
from config import db
from items import items
from heroes import heroes

from pymongo import MongoClient
from flask.ext.script import Manager, Shell, Server

app = create_app()
manager = Manager(app)
manager.add_command('items', items())
manager.add_command('heroes', heroes())


def _make_context():
    """Return context dict for a shell session so you can access
    app and db by default.
    """
    return {'app': app, 'db': db}


# Setting up the app database
@manager.command
def setup():
    db = MongoClient()
    db.hb.players.ensure_index("nickname")
    db.hb.matches.ensure_index("players.id")

manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
