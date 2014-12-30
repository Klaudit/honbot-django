from app import db
from models import Player

from flask.ext.rq import job
import requests

from datetime import datetime


@job
def avatar(player_id):
    req = requests.get("https://www.heroesofnewerth.com/getAvatar_SSL.php?id=" + str(player_id))
    db.session.query(Player).filter_by(id=player_id).update({'avatar': req.url, 'avatar_updated': datetime.utcnow()})
    db.session.commit()
