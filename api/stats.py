from config import db

from flask import jsonify, Blueprint
from datetime import datetime, timedelta
from bson import ObjectId


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
    lh = ObjectId.from_datetime(last_hour)
    db[collection].find_and_modify(query={'_id': {'$gt': lh}}, update={'$inc': {"seq":1}}, upsert=True)
