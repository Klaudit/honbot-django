import json
import api_call
import time
import pretty
import datetime
from honbot.models import Matches, PlayerMatches
from django.conf import settings


directory = settings.MEDIA_ROOT


def match(match_id):
    """
    initial hit for match view makes some decisions based on if the match is parsed already
    """
    if checkfile(match_id):
        return prepare_match(load_match(match_id), match_id)
    else:
        url = '/multi_match/all/matchids/' + str(match_id)
        data = api_call.get_json(url)
        h = [[str(match_id), '1/1/1']]
        if data is not None:
            multimatch(data, h, "rnk")
            return match(match_id)
        else:
            return None


def prepare_match(data, match_id):
    """
    prepares match data for match view
    """
    match = {}
    players = [None]*10
    for p in data['players']:
        players[int(data['players'][p]['position'])] = data['players'][p]
    match['matchlength'] = data['realtime']
    match['date'] = pretty.date(datetime.datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'))
    match['players'] = players
    match['mode'] = data['mode']
    match['map'] = data['_map']
    if match['mode'] == "rnk":
        match['mode'] = "Ranked"
    elif match['mode'] == "cs":
        match['mode'] = "Casual"
    elif match['mode'] == "acc":
        match['mode'] = "Public"
    return match


def checkfile(match_id):
    """
    check if match has been parsed before returns bool
    """
    if Matches.objects.filter(match_id=match_id).exists():
        return True
    else:
        return False


def match_save(data, match_id, mode):
    """
    save match to directory in json format
    """
    m = Matches(match_id=match_id, date=data['date'], replay_url=data['replay_url'],
                realtime=data["realtime"], mode=mode, major=data['major'],
                minor=data['minor'], revision=data['revision'], build=data['build'],
                _map=data['map'])
    m.save()
    for p in data['players']:
        if data['players'][p]['kdr'] == "Inf.":
            data['players'][p]['kdr'] = 999
        if data['players'][p]['nickname'] is None:
            data['players'][p]['nickname'] = p
        PlayerMatches(player_id=int(p), match=m,
                      deaths=data['players'][p]['deaths'],
                      kills=data['players'][p]['kills'],
                      win=bool(data['players'][p]['win']),
                      apm=float(data['players'][p]['apm']),
                      cs=data['players'][p]['cs'],
                      smackdown=data['players'][p]['smackdown'],
                      secsdead=data['players'][p]['secsdead'],
                      gpm=float(data['players'][p]['gpm']),
                      bdmg=data['players'][p]['bdmg'],
                      herodmg=data['players'][p]['herodmg'],
                      xpm=float(data['players'][p]['xpm']),
                      kdr=float(data['players'][p]['kdr']),
                      goldlost2death=data['players'][p]['goldlost2death'],
                      denies=data['players'][p]['denies'],
                      hero=data['players'][p]['hero'],
                      consumables=data['players'][p]['consumables'],
                      assists=data['players'][p]['assists'],
                      nickname=data['players'][p]['nickname'],
                      level=data['players'][p]['level'],
                      wards=data['players'][p]['wards'],
                      team=data['players'][p]['team'],
                      position=data['players'][p]['position'],
                      items=json.dumps(data['players'][p]['items']),
                      mode=mode, date=data['date']).save()


def load_match(match_id):
    """
    open match from directory and return json
    """
    m = Matches.objects.filter(match_id=match_id).values()[0]
    m['players'] = {}
    m['date'] = datetime.datetime.strftime(m['date'], "%Y-%m-%d %H:%M:%S")
    p = {}
    for player in PlayerMatches.objects.filter(match_id=match_id).values():
        p[str(player['player_id'])] = player
        p[str(player['player_id'])]['items'] = json.loads(p[str(player['player_id'])]['items'])
        if p[str(player['player_id'])]['kdr'] == 999:
            p[str(player['player_id'])]['kdr'] = "Inf."
    m['players'] = p
    return m


def multimatch(data, history, mode):
    """
    pass this multimatch api results and the number of matches. it will parse and save the useful bits
    """
    print "multimatch"
    s2mode = mode
    if mode == "rnk":
        mode = "Ranked"
    elif mode == "cs":
        mode = "Casual"
    elif mode == "acc":
        mode = "Public"
    allmatches = {}
    for m in history:
        match = {}
        match['match_id'] = m[0]
        match['mode'] = mode
        allmatches[str(m[0])] = match
        players = {}
        allmatches[m[0]]['players'] = players
    for m in data[2]:
        matchlength = round(float(m['secs']) / 60, 1)
        allmatches[m['match_id']]['matchlength'] = matchlength
        allmatches[m['match_id']]['realtime'] = time.strftime('%H:%M:%S', time.gmtime(int(m['secs'])))
        if int(allmatches[m['match_id']]['realtime'].split(':')[0]) == 0:
            allmatches[m['match_id']]['realtime'] = allmatches[m['match_id']]['realtime'][3:]
        player = {}
        player['id'] = m['account_id']
        player['kills'] = m['herokills']
        player['deaths'] = m['deaths']
        player['assists'] = m['heroassists']
        player['herodmg'] = m['herodmg']
        player['hero'] = m['hero_id']
        player['position'] = m['position']
        player['team'] = m['team']
        player['consumables'] = m['consumables']
        player['level'] = m['level']
        player['goldlost2death'] = m['goldlost2death']
        player['secsdead'] = m['secs_dead']
        player['wards'] = m['wards']
        player['denies'] = m['denies']
        player['herodmg'] = m['herodmg']
        if int(matchlength) > 0:
            player['gpm'] = round(int(m['gold']) / matchlength, 1)
            player['xpm'] = round(int(m['exp']) / matchlength, 1)
            player['apm'] = round(int(m['actions']) / matchlength, 1)
        else:
            player['gpm'] = 0
            player['xpm'] = 0
            player['apm'] = 0
        player['cs'] = m['teamcreepkills']
        try:
            player['kdr'] = round(float(player['kills']) / float(player['deaths']), 1)
        except ZeroDivisionError:
            player['kdr'] = 'Inf.'
        player['win'] = bool(int(m['wins']))
        player['smackdown'] = m['smackdown']
        player['bdmg'] = m['bdmg']
        try:
            player['nickname'] = m['nickname']
        except:
            player['nickname'] = None
        allmatches[m['match_id']]['players'][m['account_id']] = player
        allmatches[m['match_id']]['players'][m['account_id']]['items'] = None
    for m in data[1]:
        items = [None]*6
        items[0] = m['slot_1']
        items[1] = m['slot_2']
        items[2] = m['slot_3']
        items[3] = m['slot_4']
        items[4] = m['slot_5']
        items[5] = m['slot_6']
        allmatches[m['match_id']]['players'][m['account_id']]['items'] = items
        try:
            allmatches[m['match_id']]['players'][m['account_id']]['nickname'] = m['nickname']
        except KeyError:
            allmatches[m['match_id']]['players'][m['account_id']]['nickname'] = None
    for m in data[0]:
        if m['cas'] == 1:
            allmatches[m['match_id']]['type'] = "Casual"
        elif m['officl'] == 1:
            allmatches[m['match_id']]['type'] = "Ranked"

    for m in data[3]:
        try:
            allmatches[m['match_id']]['replay_url'] = m['replay_url']
        except:
            allmatches[m['match_id']]['replay_url'] = None
        v = m['version'].split('.')
        allmatches[m['match_id']]['major'] = int(v[0])
        allmatches[m['match_id']]['minor'] = int(v[1])
        if len(v) > 2:
            allmatches[m['match_id']]['revision'] = int(v[2])
        else:
            allmatches[m['match_id']]['revision'] = 0
        if len(v) > 3:
            allmatches[m['match_id']]['build'] = int(v[3])
        else:
            allmatches[m['match_id']]['build'] = 0
        allmatches[m['match_id']]['date'] = m['mdt']
        allmatches[m['match_id']]['map'] = m['map']
    ### Save to file ###
    for m in history:
        match_save(allmatches[m[0]], m[0], s2mode)
