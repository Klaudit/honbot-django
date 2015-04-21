from flask.ext.script import Command
import pyprind
from app import db
from serialize import MatchSchema
from models import Match
from pymongo import MongoClient


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))


class mongoimport(Command):
    def run(self):
        findexisting = db.engine.execute('select id from match')
        exists = [int(m[0]) for m in findexisting]
        print(len(exists))
        setexists = set(exists)

        mon = MongoClient()
        matches = set(mon.hb.matches.distinct('id'))

        filtered = list(setexists - matches)
        print(len(filtered))

        prbar = pyprind.ProgBar(len(filtered), monitor=True, title="sqlpull")
        for group in chunker(filtered, 100):
            matches = Match.query.filter(Match.id.in_(group))
            result = MatchSchema().dump(matches, many=True)[0]
            mon.hb.matches.insert(result)
            prbar.update()

