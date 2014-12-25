from flask import Flask
from flask.ext.cors import CORS
from flask.ext.marshmallow import Marshmallow
from flask.ext.rq import RQ
from flask.ext.sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from raven.contrib.flask import Sentry

app = Flask(__name__)

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hb'
db = SQLAlchemy(app)

# task queue
rq = RQ(app)

# api limiting
limiter = Limiter(app)

# serializing models
ma = Marshmallow(app)

# cross origin requests
cors = CORS(app)

# bug tracking
sentry = Sentry(app)
