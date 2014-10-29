from flask.ext.script import Manager
from app import app, RDB_HOST, RDB_PORT, HB_DB
from rethinkdb.errors import RqlRuntimeError
import rethinkdb as r
import players
import matches

manager = Manager(app)

# RethinkDB server.


# Setting up the app database
@manager.command
def setup():
    conn = r.connect(host=RDB_HOST, port=RDB_PORT)
    try:
        r.db_create(HB_DB).run(conn)
        r.db(HB_DB).table_create('players', durability='soft').run(conn)
        r.db(HB_DB).table('players').index_create('nickname').run(conn)
        r.db(HB_DB).table_create('matches', durability='soft').run(conn)
        r.db(HB_DB).table('matches').index_create('player', r.row['players']['id'], multi=True).run(conn)
        print('Database setup completed.')
    except RqlRuntimeError:
        print('App database already exists.')
    finally:
        conn.close()

if __name__ == "__main__":
    manager.run()
