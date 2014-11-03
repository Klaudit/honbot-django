from api import get_json
from utils import divmin, div
from app import app, not_found

from pytz import utc
from flask import g, jsonify
import rethinkdb as r

from datetime import datetime


@app.route('/match/<int:mid>/')
def match(mid):
    """
    Returns a single match from ID
    Players are returned in an array and their items are a json array dumped into a string
    """
    m = r.table('matches').get(mid).run(g.rconn)
    if m is None:
        raw = get_json('/match/all/matchid/' + str(mid))
        if raw:
            m = single_match(raw, mid)
        else:
            return not_found()
    return jsonify(m)


def multimatch(matches):
    raw = get_json('/multi_match/all/matchids/' + '+'.join(str(x) for x in matches))
    if raw is None:
        return None
    result = []
    for m in raw[0]:
        temp = []
        temp.append([m])
        c = m['match_id']
        temp.append([x for x in raw[1] if x['match_id'] == c])
        temp.append([x for x in raw[2] if x['match_id'] == c])
        temp.append([x for x in raw[3] if x['match_id'] == c])
        result.append(single_match(temp, c))
    return result


def single_match(raw, mid):
    m = {'id': int(mid)}
    if raw[0][0]['officl'] == "1" and raw[0][0]['cas'] == "1":
        m['mode'] = 'cs'
    elif raw[0][0]['officl'] == "1" and raw[0][0]['cas'] == "0":
        m['mode'] = "rnk"
    else:
        m['mode'] = "acc"
    v = raw[3][0]['version'].split('.')
    if len(v) > 1:
        m['major'] = int(v[0])
        m['minor'] = int(v[1])
        if len(v) > 2:
            m['revision'] = int(v[2])
            if len(v) > 3:
                m['build'] = int(v[3])
    m['map_used'] = raw[3][0]['map']
    m['length'] = raw[3][0]['time_played']
    # '2014-07-27 01:31:18'
    unaware_date = datetime.strptime(raw[3][0]['mdt'], '%Y-%m-%d %H:%M:%S')
    m['date'] = utc.localize(unaware_date)
    pitems = {}
    for p in raw[1]:
        items = []
        for item in range(1, 7):
            if p['slot_' + str(item)]:
                items.append(p['slot_' + str(item)])
        pitems[p['account_id']] = items
    players = []
    for p in raw[2]:
        players.append({
            'id': int(p['account_id']),
            'nickname': p['nickname'],
            'mid': mid,
            'clan_id': int(p['clan_id']),
            'hero_id': int(p['hero_id']),
            'date': m['date'],
            'position': int(p['position']),
            'items': items,
            'team': int(p['team']),
            'level': int(p['level']),
            'win': bool(int(p['wins'])),
            'concedes': int(p['concedes']),
            'concedevotes': int(p['concedevotes']),
            'buybacks': int(p['buybacks']),
            'discos': int(p['discos']),
            'kicked': int(p['kicked']),
            'mmr_change': float(p['amm_team_rating']),
            'herodmg': int(p['herodmg']),
            'kills': int(p['herokills']),
            'assists': int(p['heroassists']),
            'deaths': int(p['deaths']),
            'kdr': div(p['herokills'], p['deaths']),
            'goldlost2death': int(p['goldlost2death']),
            'secs_dead': int(p['secs_dead']),
            'cs': int(p['teamcreepkills']) + int(p['neutralcreepkills']),
            'bdmg': p['bdmg'],
            'denies': p['denies'],
            'gpm': divmin(p['gold'], m['length']),
            'xpm': divmin(p['exp'], m['length']),
            'apm': divmin(p['actions'], m['length']),
            'consumables': int(p['consumables']),
            'wards': int(p['wards'])
        })

    m['players'] = players
    r.table('matches').insert(m).run(g.rconn)
    return m
