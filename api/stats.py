from app import db, redis_store
from models import Player, Match

from flask import jsonify, Blueprint
from datetime import datetime, timedelta


stats = Blueprint('stats', __name__)


@stats.route('/collection_count/')
def collection_count():
    res = {
        'matches': match_increment(0),
        'players': player_increment(0)
    }
    return jsonify(res)


def count_increment(collection):
    last_hour = datetime.utcnow() - timedelta(hours=1)


def player_increment(inc):
    players = redis_store.get('player_count')
    if not players:
        players = db.session.query(Player).count()
        redis_store.set('player_count', players)
    else:
        redis_store.set('player_count', int(players) + inc)
    return int(players) + inc


def match_increment(inc):
    matches = redis_store.get('match_count')
    if not matches:
        matches = db.session.query(Match).count()
        redis_store.set('match_count', matches)
    else:
        redis_store.set('match_count', int(matches) + inc)
    return int(matches) + inc
