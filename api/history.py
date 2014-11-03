from app import app, not_found
from api import get_json
from matches import multimatch

from flask import g, jsonify
from pytz import utc
import rethinkdb as r

from datetime import datetime

return_size = 25


@app.route('/history/<int:pid>/<int:page>/<mode>/')
def player_history(pid, page, mode):
    """
    this is the main function of player history
    returns 404 if user doesn't already exist in db
    """
    count = int(page) * return_size
    player = get_or_update_history(pid)
    # loads up history and trims it to size
    hist = player[mode + '_history'][(count - return_size):count]
    ph = verify_matches(hist, mode)
    res = {
        'matches': len(ph),
        'page': page,
        'mode': mode,
        'result': ph
    }
    return jsonify(res)


@app.route('/player_cache/<int:pid>/<mode>/')
def get_cached(pid, mode):
    matches = list(r.table('matches').get_all(pid, index='player').run(g.rconn))
    res = {
        'matches': len(matches),
        'mode': mode,
        'result': matches
    }
    return jsonify(res)


def get_or_update_history(pid):
    p = r.table('players').get(pid).run(g.rconn)
    url = '/match_history/all/accountid/' + str(pid)
    if p is None:
        return not_found()
    if 'history_updated' not in p:
        raw = get_json(url)
        if raw:
            return update_history(p, raw)
        else:
            return not_found()
    nowutc = datetime.now(utc)
    tdelta = nowutc - p['history_updated']
    if tdelta.seconds + (tdelta.days * 86400) > 800:
        raw = get_json(url)
        if raw:
            return update_history(p, raw)
    return p


def update_history(p, raw):
    parsed = [[], [], []]
    for idx, history in enumerate(raw):
        parsed[idx] = [int(m.split('|')[0]) for m in history['history'].split(',')]
    p['rnk_history'] = parsed[0][::-1]
    p['cs_history'] = parsed[1][::-1]
    p['acc_history'] = parsed[2][::-1]
    r.table('players').get(p['id']).update(
        {'history_updated': datetime.now(utc), 'cs_history': p['cs_history'], 'acc_history': p['acc_history'], 'rnk_history': p['rnk_history']}).run(g.rconn)
    return p


def verify_matches(hist, mode):
    """
    checks for matches exist in the database. If they not exist, they soon will.
    """
    print(hist)
    findexisting = list(r.table('matches').get_all(r.args(hist)).run(g.rconn))
    existing = set([int(match['id']) for match in findexisting])
    missing = [x for x in hist if x not in existing]
    # if any are missing USE SPECIAL SET OF SKILLS
    if len(missing) > 0:
        others = multimatch(missing)
        if others is not None:
            for o in others:
                findexisting.append(o)
    return findexisting
