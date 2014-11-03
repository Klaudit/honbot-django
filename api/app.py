from flask import Flask, g, abort, jsonify, request
from flask.ext.cors import CORS
from flask_limiter import Limiter
from redis import Redis
from rethinkdb.errors import RqlDriverError
from rq import Queue
import rethinkdb as r

from os import environ


app = Flask(__name__)
app.config.from_object(__name__)
limiter = Limiter(app)
cors = CORS(app)

PHP = environ.get('PHPSESSID')

# database settings
RDB_HOST = environ.get('RDB_HOST') or 'localhost'
RDB_PORT = environ.get('RDB_PORT') or 28015
HB_DB = 'honbot'

# redis queue
q = Queue(connection=Redis())


@app.before_request
def before_request():
    try:
        g.rconn = r.connect(host=RDB_HOST, port=RDB_PORT, db=HB_DB)
    except RqlDriverError:
        abort(503, "No database connection could be established.")


@app.teardown_request
def teardown_request(exception):
    try:
        g.rconn.close()
    except AttributeError:
        pass


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
