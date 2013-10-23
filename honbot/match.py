import json
import api_call
import time
from datetime import timedelta, datetime, date
from django.shortcuts import render_to_response
from honbot.models import Matches, PlayerMatches, MatchCount, PlayerMatchCount, PlayerIcon, PlayerStats, PlayerStatsCasual, PlayerStatsPublic
from django.db.models import F
from error import error
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from player import player_math, player_save
from avatar import avatar
import thread


def match_view(request, match_id):
    """
    /match/####/ url leads here
    """
    match = Matches.objects.filter(match_id=match_id)
    if match.exists():
        team1, team2 = [], []
        # get match and setup data for view
        match = match.values()[0]
        # get players and setup for view
        players = PlayerMatches.objects.filter(match_id=match_id).order_by('position').values()
        for player in players:
            player['items'] = json.loads(player['items'])
            if player['kdr'] == 999:
                player['kdr'] = "Inf"
            if player['team'] == 1:
                team1.append(player)
            else:
                team2.append(player)
            if len(team1) > 0:
                t1exist = True
            else:
                t1exist = False
            if len(team2) > 0:
                t2exist = True
            else:
                t2exist = False
            thread.start_new_thread(update_check, (player['player_id'], match['mode']))
        return render_to_response('match.html', {'match_id': match_id, 'match': match, 'players': players, 'team1': team1, 'team2': team2, 't1exist': t1exist, 't2exist': t2exist})
    else:
        # grab solo match for fucks sake
        url = '/multi_match/all/matchids/' + str(match_id)
        data = api_call.get_json(url)
        h = [str(match_id)]
        if data is not None:
            mode = "rnk"
            if int(data[0][0]['cas']) == 1:
                mode = "cs"
            if int(data[0][0]['nl']) == 0:
                mode = "acc"
            multimatch(data, h, mode)
            return match_view(request, match_id)
        else:
            return error(request, "S2 Servers down or match id is incorrect. Try another match or gently refreshing the page.")


def update_check(player, mode):
    if mode == 'rnk':
        result = PlayerStats.objects.filter(player_id=player)
    elif mode == 'cs':
        result = PlayerStatsCasual.objects.filter(player_id=player)
    elif mode == 'acc':
        result = PlayerStatsPublic.objects.filter(player_id=player)
    if result.exists():
        result = result.values('updated')[0]
        tdelta = datetime.now() - datetime.strptime(str(result['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) > 12000:
            avatar(None, player, 10)
            update_player(player, mode)
    else:
        avatar(None, player, 10)
        update_player(player, mode)


def update_player(pid, mode):
    if mode == 'rnk':
        url = "/player_statistics/ranked/accountid/" + str(pid)
    elif mode == 'cs':
        url = '/player_statistics/casual/accountid/' + str(pid)
    elif mode == 'acc':
        url = '/player_statistics/public/accountid/' + str(pid)
    data = api_call.get_json(url)
    p = player_math(data, mode)
    player_save(p, mode)



def match_save(data, match_id, mode):
    print match_id
    try:
        data['realtime']
    except KeyError:
        data['realtime'] = 0
    try:
        data['date']
    except KeyError:
        date['date'] = "2000-01-01 11:11:11"
    m = Matches(
        match_id=match_id, date=data['date'], replay_url=data['replay_url'],
        realtime=data['realtime'], mode=mode, major=data['major'],
        minor=data['minor'], revision=data[
            'revision'], build=data['build'],
        map_used=data['map'])
    m.save()
    update_match_count()
    update_players_in_matches(len(data['players']))
    bulk = []
    for p in data['players']:
        if data['players'][p]['kdr'] == "Inf.":
            data['players'][p]['kdr'] = 999
        if data['players'][p]['nickname'] is None:
            data['players'][p]['nickname'] = p
        bulk.append(PlayerMatches(player_id=int(p), match=m,
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
                                  goldlost2death=data['players'][
                                      p]['goldlost2death'],
                                  denies=data['players'][p]['denies'],
                                  hero=data['players'][p]['hero'],
                                  consumables=data['players'][
                                      p]['consumables'],
                                  assists=data['players'][p]['assists'],
                                  bloodlust=data['players'][p]['bloodlust'],
                                  doublekill=data['players'][p]['doublekill'],
                                  triplekill=data['players'][p]['triplekill'],
                                  annihilation=data['players'][
                                      p]['annihilation'],
                                  bgold=data['players'][p]['bgold'],
                                  exp_denied=data['players'][p]['exp_denied'],
                                  gold_spent=data['players'][p]['gold_spent'],
                                  razed=data['players'][p]['razed'],
                                  quadkill=data['players'][p]['quadkill'],
                                  nickname=data['players'][p]['nickname'],
                                  level=data['players'][p]['level'],
                                  buybacks=data['players'][p]['buybacks'],
                                  mmr_change=data['players'][p]['mmr_change'],
                                  wards=data['players'][p]['wards'],
                                  team=data['players'][p]['team'],
                                  position=data['players'][p]['position'],
                                  items=json.dumps(
                                      data['players'][p]['items']),
                                  mode=mode, date=data['date']))
    if len(bulk) > 0:
        PlayerMatches.objects.bulk_create(bulk)


def update_match_count():
    today = date.today().strftime("%Y-%m-%d")
    current_count = MatchCount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        count = Matches.objects.count()
        MatchCount(count=count).save()


def update_players_in_matches(count):
    today = date.today().strftime("%Y-%m-%d")
    current_count = PlayerMatchCount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + count)
    else:
        count = PlayerMatches.objects.count()
        PlayerMatchCount(count=count).save()


def recent(request):
    paginator = Paginator(Matches.objects.all(), 20)  # Show 20 matches a page
    page = request.GET.get('page')
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pag = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pag = paginator.page(paginator.num_pages)
    matches = Matches.objects.all().values()[
        (pag.start_index() - 1):pag.end_index()]
    # get heroes
    for m in matches:
        players = PlayerMatches.objects.filter(match=m['match_id']).values(
            "hero", "team", "win").order_by('position')
        m['legion'] = []
        m['hellbourne'] = []
        m['date'] = datetime.strptime(str(m['date']), '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
        for p in players:
            if p['team'] == 1:
                m['legion'].append(p['hero'])
            else:
                m['hellbourne'].append(p['hero'])
        try:
            m['winner'] = players[0]['win']
        except:
            m['winner'] = 1
    return render_to_response('recent.html', {"matches": matches, "pag": pag})


def multimatch(data, history, mode):
    """
    pass this multimatch api results and the number of matches. it will parse and save the useful bits
    """
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
        match['match_id'] = m
        match['mode'] = mode
        allmatches[str(m)] = match
        players = {}
        allmatches[str(m)]['players'] = players
    for m in data[2]:
        matchlength = round(float(m['secs']) / 60, 1)
        allmatches[m['match_id']]['matchlength'] = matchlength
        allmatches[m['match_id']]['realtime'] = time.strftime(
            '%H:%M:%S', time.gmtime(int(m['secs'])))
        if int(allmatches[m['match_id']]['realtime'].split(':')[0]) == 0:
            allmatches[m['match_id']]['realtime'] = allmatches[
                m['match_id']]['realtime'][3:]
        player = {}
        player['id'] = m['account_id']
        player['kills'] = m['herokills']
        player['deaths'] = m['deaths']
        player['assists'] = m['heroassists']
        player['herodmg'] = m['herodmg']
        player['hero'] = m['hero_id']
        player['position'] = m['position']
        player['doublekill'] = m['doublekill']
        player['triplekill'] = m['triplekill']
        player['razed'] = m['razed']
        player['quadkill'] = m['quadkill']
        player['annihilation'] = m['annihilation']
        player['gold_spent'] = m['gold_spent']
        player['exp_denied'] = m['exp_denied']
        player['bgold'] = m['bgold']
        player['team'] = m['team']
        player['bloodlust'] = m['bloodlust']
        player['consumables'] = m['consumables']
        player['mmr_change'] = float(m['amm_team_rating'])
        player['level'] = m['level']
        player['goldlost2death'] = m['goldlost2death']
        player['secsdead'] = m['secs_dead']
        player['wards'] = m['wards']
        player['buybacks'] = m['buybacks']
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
            player['kdr'] = round(
                float(player['kills']) / float(player['deaths']), 1)
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
        items = [None] * 6
        items[0] = m['slot_1']
        items[1] = m['slot_2']
        items[2] = m['slot_3']
        items[3] = m['slot_4']
        items[4] = m['slot_5']
        items[5] = m['slot_6']
        try:
            allmatches[m['match_id']]['players'][
                m['account_id']]['items'] = items
        except:
            pass
        try:
            allmatches[m['match_id']]['players'][
                m['account_id']]['nickname'] = m['nickname']
        except KeyError:
            pass
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
    # Save to file ###
    for m in history:
        match_save(allmatches[str(m)], m, s2mode)
