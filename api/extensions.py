"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""
from flask_limiter import Limiter
limiter = Limiter()

from flask.ext.cors import CORS
cors = CORS()

from raven.contrib.flask import Sentry
sentry = Sentry()
