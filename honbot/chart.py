from django.shortcuts import render_to_response
from .models import HeroData
from error import error
from collections import Counter
import numpy as np
from utils import pmoselect, psoselect

error_missing = "You may have spelled the player's name incorrectly. Player stats missing."


def chart_default(request, name, limit, mode):
    PSObj = psoselect(mode)
    stats = PSObj.objects.filter(nickname=name).first()
    if stats is not None:
        return chart_view(request, name, mode, stats, limit)
    else:
        return error(request, error_missing)


def chart_view(request, name, mode, stats, limit):
    # set player in match object before calling
    if limit < 1:
        limit = 1
    PMObj = pmoselect(mode)
    matches = PMObj.objects.filter(player_id=stats.player_id).exclude(hero=0).order_by('match').values('hero', 'gpm', 'team', 'mmr_change', 'win', 'match_id', 'apm', 'wards', 'kills', 'player_id', 'cs', 'deaths', 'razed', 'secsdead', 'assists')
    available = matches.count()
    # return error if no matches available
    if available == 0:
        return error(request, "You don't seem to have enough matches for us to display this.")
    if limit > available:
        limit = available
    else:
        matches = matches[:limit]
    limit = len(matches)
    # calculate mmr backwards
    # set first point to current mmr from stats
    mmr = [0]
    mmr[0] = stats.mmr
    for idx, m in enumerate(matches):
        mmr.append(mmr[idx] + (m['mmr_change'] * -1))
    # mmr - min max avg
    mmrhigh = int(max(mmr))
    mmrlow = int(min(mmr))
    mmravg = int(sum(mmr) / float(len(mmr)))
    # mmr flip so the oldest is first trim off extra match
    mmr = mmr[::-1][1:]
    match_list, apmtemp, gpmtemp = [], [], []
    assists, wards, kills, deaths, razed, mmr_change, sdead, cs = (0,) * 8
    # create total for columns and then divide by total. Averages yo
    s = {'assists': 0, 'wards': 0, 'kills': 0, 'deaths': 0, 'razed': 0, 'mmr_change': 0, 'sdead': 0, 'cs': 0}
    for m in reversed(matches):
        match_list.append(m['match_id'])
        apmtemp.append(m['apm'])
        gpmtemp.append(m['gpm'])
        s['assists'] += m['assists']
        s['wards'] += m['wards']
        s['kills'] += m['kills']
        s['deaths'] += m['deaths']
        s['razed'] += m['razed']
        s['mmr_change'] += m['mmr_change']
        s['sdead'] += m['secsdead']
        s['cs'] += m['cs']
    # calc for APM box plot
    apm = {}
    apmtemp = np.array(apmtemp)
    apm['min'] = np.amin(apmtemp)
    apm['lower'] = np.percentile(apmtemp, 25)
    apm['median'] = np.percentile(apmtemp, 50)
    apm['upper'] = np.percentile(apmtemp, 75)
    apm['max'] = np.amax(apmtemp)
    apm['mean'] = round(np.average(apmtemp))
    # calc for GPM box plot
    gpm = {}
    gpmtemp = np.array(gpmtemp)
    gpm['min'] = np.amin(gpmtemp)
    gpm['lower'] = np.percentile(gpmtemp, 25)
    gpm['median'] = np.percentile(gpmtemp, 50)
    gpm['upper'] = np.percentile(gpmtemp, 75)
    gpm['max'] = np.amax(gpmtemp)
    gpm['mean'] = round(np.average(gpmtemp))
    # calculate averages
    s['akills'] = round(float(s['kills']) / limit, 2)
    s['adeaths'] = round(float(s['deaths']) / limit, 2)
    s['aassists'] = round(float(s['assists']) / limit, 2)
    s['awards'] = round(float(s['wards']) / limit, 2)
    s['arazed'] = round(float(s['razed']) / limit, 2)
    try:
        s['kdr'] = round(float(s['kills']) / s['deaths'], 2)
    except:
        s['kdr'] = "-"
    s['ammr_change'] = round(float(s['mmr_change']) / limit, 2)
    s['sdead'] = round(float(s['sdead']) / 60)
    s['asdead'] = round((float(s['sdead']) / 60) / limit, 2)
    s['acs'] = round(float(s['cs']) / limit, 2)
    top_heroes = Counter([m['hero'] for m in matches]).most_common(6)
    heronames = HeroData.objects.filter(hero_id__in=[x[0] for x in top_heroes]).values('cli_name', 'hero_id', 'disp_name')
    # get hero names and assign later
    heroes = []
    for h in top_heroes:
        new = {}
        new['hero'], new['used'] = h
        herod = filter(lambda x: x['hero_id'] == new['hero'], heronames)[0]
        new['cli_name'] = herod['cli_name']
        new['disp_name'] = herod['disp_name']
        new['kills'], new['assists'], new['deaths'], new['wins'], new['losses'], new['mmr'], new['apm'], new['gpm'], new['cs'] = (0,) * 9
        for m in filter(lambda x: x['hero'] == new['hero'], matches):
            new['kills'] += m['kills']
            new['assists'] += m['assists']
            new['deaths'] += m['deaths']
            new['wins'] += m['win']
            new['mmr'] += m['mmr_change']
            new['apm'] += m['apm']
            new['gpm'] += m['gpm']
            new['cs'] += m['cs']
        new['win_percent'] = int(float(new['wins']) / new['used'] * 100)
        new['losses'] = new['used'] - new['wins']
        new['kills'] = new['kills'] / new['used']
        new['assists'] = new['assists'] / new['used']
        new['deaths'] = new['deaths'] / new['used']
        new['apm'] = int(new['apm'] / new['used'])
        new['gpm'] = int(new['gpm'] / new['used'])
        new['cs'] = int(new['cs'] / new['used'])
        heroes.append(new)
    # find possible friends / non-friends
    allplayers = PMObj.objects.filter(match_id__in=match_list).values('mmr_change', 'player_id', 'nickname', 'team', 'match_id')
    friends, enemies = {}, {}
    for m in match_list:
        for ps in filter(lambda x: x['match_id'] == m, allplayers):
            curteam = filter(lambda x: x['match_id'] == ps['match_id'], matches)[0]['team']
            sameteam = (ps['team'] == curteam)
            if sameteam:
                friendsetup(friends, ps, sameteam)
            else:
                friendsetup(enemies, ps, sameteam)
    # delete self.
    del friends[str(matches[0]['player_id'])]
    # setup arrays for display
    friends = [friends[x] for x in friends]
    friends = filter(lambda x: x['matches'] > 1, friends)
    friends = sorted(friends, key=lambda friends: friends['matches'], reverse=True)[:5]
    enemies = [enemies[x] for x in enemies]
    enemies = filter(lambda x: x['matches'] > 1, enemies)
    enemies = sorted(enemies, key=lambda enemies: enemies['matches'], reverse=True)[:5]
    return render_to_response('chart.html', {
                              'mmr': mmr, 'available': available, 'apm': apm, 'gpm': gpm, 's': s,
                              'match_list': match_list, 'stats': stats, 'heroes': heroes, 'view': "chart", 'mode': mode,
                              'mmrhigh': mmrhigh, 'mmrlow': mmrlow, 'mmravg': mmravg, 'allplayers': allplayers,
                              'limit': limit, 'mmr_change': mmr_change, 'enemies': enemies, 'friends': friends})


def friendsetup(grp, ps, sameteam):
    grp.setdefault(str(ps['player_id']), {})
    grp[str(ps['player_id'])].setdefault('mmr_change', 0)
    grp[str(ps['player_id'])].setdefault('matches', 0)
    grp[str(ps['player_id'])].setdefault('wins', 0)
    grp[str(ps['player_id'])].setdefault('losses', 0)
    grp[str(ps['player_id'])]['nickname'] = ps['nickname']
    grp[str(ps['player_id'])]['player_id'] = ps['player_id']
    grp[str(ps['player_id'])]['mmr_change'] += round(ps['mmr_change'], 2)
    grp[str(ps['player_id'])]['matches'] += 1
    if ps['mmr_change'] > 0:
        grp[str(ps['player_id'])]['wins'] += 1
    else:
        grp[str(ps['player_id'])]['losses'] += 1
