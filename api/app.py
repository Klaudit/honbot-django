from players import players
from matches import matches
from history import history
from banner import bannerapp
from extensions import limiter, cors, sentry

from flask import Flask


def create_app():
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    limiter.init_app(app)
    cors.init_app(app)
    sentry.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(players)
    app.register_blueprint(matches)
    app.register_blueprint(history)
    app.register_blueprint(bannerapp)
    return None

if __name__ == '__main__':
    app = create_app()
    app.run()
