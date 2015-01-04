from app import db

from flask import jsonify, Blueprint
from datetime import datetime, timedelta


stats = Blueprint('stats', __name__)


@stats.route('/collection_count/')
def collection_count():
    res = {
        'matches': db.matches.count(),
        'players': db.players.count()
    }
    return jsonify(res)


def count_increment(collection):
    last_hour = datetime.utcnow() - timedelta(hours=1)
