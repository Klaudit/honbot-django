from django.http import Http404

from .api import get_json
from .models import Match
from .utils import pmoselect, divmin, div
from .serializers import MatchSerializer

from datetime import datetime
from json import dumps

from rest_framework.decorators import api_view
from rest_framework.response import Response
from pytz import utc, timezone


@api_view(['GET'])
def match(request, mid):
    """
    Returns a single match from ID  
    Players are returned in an array and their items are a json array dumped into a string
    """
    m = Match.objects.filter(match_id=mid).first()
    if m is None:
        raw = get_json('/match/all/matchid/' + mid)
        if raw:
            m = single_match(raw, mid)
        else:
            raise Http404
    serializer = MatchSerializer(m)
    PMObj = pmoselect(m.mode)
    serializer.data['players'] = PMObj.objects.filter(match_id=mid).order_by('position').values()
    return Response(serializer.data)


def multimatch(matches):
    raw = get_json('/multi_match/all/matchids/' + '+'.join(str(x) for x in matches))
    if raw is None:
        return None
    for m in raw[0]:
        temp = []
        temp.append([m])
        c = m['match_id']
        temp.append([x for x in raw[1] if x['match_id'] == c])
        temp.append([x for x in raw[2] if x['match_id'] == c])
        temp.append([x for x in raw[3] if x['match_id'] == c])
        single_match(temp, c)


def single_match(raw, mid):
    m = Match(match_id=mid)
    if raw[0][0]['officl'] == "1" and raw[0][0]['cas'] == "1":
        m.mode = 'cs'
    elif raw[0][0]['officl'] == "1" and raw[0][0]['cas'] == "0":
        m.mode = "rnk"
    else:
        m.mode = "acc"
    v = raw[3][0]['version'].split('.')
    if len(v) > 1:
        m.major = int(v[0])
        m.minor = int(v[1])
        if len(v) > 2:
            m.revision = int(v[2])
            if len(v) > 3:
                m.build = int(v[3])
    m.map_used = raw[3][0]['map']
    m.length = raw[3][0]['time_played']
    # '2014-07-27 01:31:18'
    unaware_date = datetime.strptime(raw[3][0]['mdt'], '%Y-%m-%d %H:%M:%S')
    aware_date = timezone('US/Eastern').localize(unaware_date, is_dst=True)
    m.date = aware_date.astimezone(utc)
    m.save()
    PMObj = pmoselect(m.mode)
    pdict = {}
    for p in raw[2]:
        pdict[p['account_id']] = PMObj(player_id=p['account_id'], match_id=mid)
        pdict[p['account_id']].nickname = p['nickname']
        pdict[p['account_id']].clan_id = p['clan_id']
        pdict[p['account_id']].hero_id = p['hero_id']
        pdict[p['account_id']].date = m.date
        pdict[p['account_id']].position = p['position']
        pdict[p['account_id']].team = p['team']
        pdict[p['account_id']].level = p['level']
        pdict[p['account_id']].win = bool(int(p['wins']))
        pdict[p['account_id']].losses = p['losses']
        pdict[p['account_id']].concedes = p['concedes']
        pdict[p['account_id']].concedevotes = p['concedevotes']
        pdict[p['account_id']].buybacks = p['buybacks']
        pdict[p['account_id']].discos = p['discos']
        pdict[p['account_id']].kicked = p['kicked']
        pdict[p['account_id']].mmr_change = p['amm_team_rating']
        pdict[p['account_id']].herodmg = p['herodmg']
        pdict[p['account_id']].kills = p['herokills']
        pdict[p['account_id']].assists = p['heroassists']
        pdict[p['account_id']].deaths = p['deaths']
        pdict[p['account_id']].kdr = div(p['herokills'], p['deaths'])
        pdict[p['account_id']].goldlost2death = p['goldlost2death']
        pdict[p['account_id']].secs_dead = p['secs_dead']
        pdict[p['account_id']].cs = int(p['teamcreepkills']) + int(p['neutralcreepkills'])
        pdict[p['account_id']].bdmg = p['bdmg']
        pdict[p['account_id']].denies = p['denies']
        pdict[p['account_id']].gpm = divmin(p['gold'], m.length)
        pdict[p['account_id']].xpm = divmin(p['exp'], m.length)
        pdict[p['account_id']].apm = divmin(p['actions'], m.length)
        pdict[p['account_id']].consumables = p['consumables']
        pdict[p['account_id']].wards = p['wards']
    for p in raw[1]:
        items = []
        for item in range(1, 7):
            if p['slot_' + str(item)] is not None:
                items.append(p['slot_' + str(item)])
        if len(items) > 0:
            pdict[p['account_id']].items = dumps(items)
        else:
            pdict[p['account_id']].items = None
    bulk = list(pdict.values())
    PMObj.objects.bulk_create(bulk)
    return m
