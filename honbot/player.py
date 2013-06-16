import api_call
from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import PlayerStats, PlayerStatsCasual, PlayerStatsPublic
from error import error
from datetime import datetime
import json


def players(request, name):
    """
    controls the player show
    """
    mode = request.get_full_path().split('/')[1]
    if mode == "c":
        url = '/player_statistics/casual/nickname/' + name
        mode = "cs"
        p = PlayerStatsCasual.objects.filter(nickname=name)
    elif mode == "p":
        url = '/player_statistics/public/nickname/' + name
        mode = "acc"
        p = PlayerStatsPublic.objects.filter(nickname=name)
    else:
        url = '/player_statistics/ranked/nickname/' + name
        mode = "rnk"
        p = PlayerStats.objects.filter(nickname=name)
    if p.exists():
        tdelta = datetime.utcnow() - datetime.strptime(str(p.values()[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1000:
            s = p.values()[0]
            new = False
            data = True
        else:
            new = True
            data = api_call.get_json(url)
    else:
        new = True
        data = api_call.get_json(url)
    if data is not None:
        if new:
            s = player_math(data, name, mode)
            player_save(s, mode)
        ### deliver to view ###
        t = loader.get_template('player.html')
        c = Context({'stats': s, 'mode': mode})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or name is incorrect. Try another name or try gently refreshing the page.")


def player_save(stats, mode):
    if mode == "rnk":
        PlayerStats(player_id=stats['player_id'], nickname=stats['nickname'],
                    cccalls=stats['cccalls'], deaths=stats['deaths'], cc=stats['cc'],
                    assists=stats['assists'], TSR=stats['TSR'], kdr=stats['kdr'],
                    adenies=stats['adenies'], aconsumables=stats['aconsumables'],
                    kills=stats['kills'], winpercent=stats['winpercent'], kadr=stats['kadr'],
                    akills=stats['akills'], kicked=stats['kicked'], agoldmin=stats['agoldmin'],
                    matches=stats['matches'], mmr=stats['mmr'], hours=stats['hours'],
                    awards=stats['awards'], atime=stats['atime'], left=stats['left'],
                    aactionsmin=stats['aactionsmin'], axpmin=stats['axpmin'], adeaths=stats['adeaths'],
                    acs=stats['acs'], wins=stats['wins'], losses=stats['losses'], aassists=stats['aassists']).save()
    elif mode == "acc":
        PlayerStatsPublic(player_id=stats['player_id'], nickname=stats['nickname'],
                          cccalls=stats['cccalls'], deaths=stats['deaths'], cc=stats['cc'],
                          assists=stats['assists'], TSR=stats['TSR'], kdr=stats['kdr'],
                          adenies=stats['adenies'], aconsumables=stats['aconsumables'],
                          kills=stats['kills'], winpercent=stats['winpercent'], kadr=stats['kadr'],
                          akills=stats['akills'], kicked=stats['kicked'], agoldmin=stats['agoldmin'],
                          matches=stats['matches'], mmr=stats['mmr'], hours=stats['hours'],
                          awards=stats['awards'], atime=stats['atime'], left=stats['left'],
                          aactionsmin=stats['aactionsmin'], axpmin=stats['axpmin'], adeaths=stats['adeaths'],
                          acs=stats['acs'], wins=stats['wins'], losses=stats['losses'], aassists=stats['aassists']).save()
    elif mode == "cs":
        PlayerStatsCasual(player_id=stats['player_id'], nickname=stats['nickname'],
                          cccalls=stats['cccalls'], deaths=stats['deaths'], cc=stats['cc'],
                          assists=stats['assists'], TSR=stats['TSR'], kdr=stats['kdr'],
                          adenies=stats['adenies'], aconsumables=stats['aconsumables'],
                          kills=stats['kills'], winpercent=stats['winpercent'], kadr=stats['kadr'],
                          akills=stats['akills'], kicked=stats['kicked'], agoldmin=stats['agoldmin'],
                          matches=stats['matches'], mmr=stats['mmr'], hours=stats['hours'],
                          awards=stats['awards'], atime=stats['atime'], left=stats['left'],
                          aactionsmin=stats['aactionsmin'], axpmin=stats['axpmin'], adeaths=stats['adeaths'],
                          acs=stats['acs'], wins=stats['wins'], losses=stats['losses'], aassists=stats['aassists']).save()


def player_math(data, nick, mode):
    """
    This will get all the right information for the players view and store it in dict
    returns dict
    TSR calculation
    """
    stats = {}
    stats['player_id'] = int(data['account_id'])  # account id
    try:
        stats['nickname'] = str(data['nickname'])  # name
    except:
        stats['nickname'] = nick
    stats['matches'] = int(data[mode + '_games_played'])  # matches
    stats['wins'] = int(data[mode + '_wins'])  # wins
    stats['losses'] = int(data[mode + '_losses'])  # losses
    if mode == "cs" or mode == "rnk":
        stats['mmr'] = int(float(data[mode + '_amm_team_rating']))  # mmr
    else:
        stats['mmr'] = int(float(data['acc_pub_skill']))
    stats['kills'] = int(data[mode + '_herokills'])  # total kills
    stats['deaths'] = int(data[mode + '_deaths'])  # total deaths
    stats['assists'] = int(data[mode + '_heroassists'])  # total deaths
    stats['cc'] = int(data[mode + '_concedes'])  # total concedes
    stats['cccalls'] = int(data[mode + '_concedevotes'])  # total concede votes
    stats['left'] = int(data[mode + '_discos'])  # disconnects
    stats['kicked'] = int(data[mode + '_kicked'])  # kicked
    if stats['matches'] > 0:
        stats['hours'] = (int(data[mode + '_secs']) / 60) / 60  # hours played
        stats['acs'] = round(int(data[mode + '_teamcreepkills']) / float(stats['matches']), 1)  # average creep score
        if stats['deaths'] > 0 and stats['kills'] > 0:
            stats['kadr'] = round((float(stats['kills']) + float(stats['assists'])) / float(stats['deaths']), 2)  # k+A : d
            stats['kdr'] = round(float(stats['kills']) / float(stats['deaths']), 2)  # kill death ratio
        else:
            stats['kadr'] = 0
            stats['kdr'] = 0
        stats['winpercent'] = str(int(float(stats['wins']) / float(stats['wins'] + stats['losses']) * 100)) + '%'  # win percent
        stats['atime'] = int(data[mode + '_secs']) / stats['matches'] / 60  # average time
        stats['akills'] = round(float(stats['kills']) / stats['matches'], 1)  # average kills
        stats['adeaths'] = round(float(stats['deaths']) / stats['matches'], 1)  # average deaths
        stats['aassists'] = round(float(stats['assists']) / stats['matches'], 1)  # average assists
        stats['aconsumables'] = round(float(data[mode + '_consumables']) / stats['matches'], 1)  # average consumables
        stats['awards'] = round(float(data[mode + '_wards']) / stats['matches'], 1)  # average wards
        stats['acs'] = round(float(data[mode + '_teamcreepkills']) / stats['matches'], 1)  # average creep score
        stats['adenies'] = round(float(data[mode + '_denies']) / stats['matches'], 1)  # average creep score
        stats['axpmin'] = int(float(data[mode + '_exp']) / (float(data[mode + '_secs']) / 60))  # average xp / min
        stats['agoldmin'] = int(float(data[mode + '_gold']) / (float(data[mode + '_secs']) / 60))  # average gold / min
        stats['aactionsmin'] = int(float(data[mode + '_actions']) / (float(data[mode + '_secs']) / 60))  # average actions / min
        ### TSR CALC ###
        # How many Kills per Death you have, scaled by 1.1/1.15 KpD - 13% of your TSR
        # How many Assits per Death you have, scaled by 1.5/1.55 ApD - 24% of your TSR
        # The percent of games you win, scaled by 0.55 -18% of your TSR
        # How much Gold you earn per Minute played, scaled by 190/230 - 7% of your TSR
        # How much EXP you get per Minute played, scaled by 420/380
        # The rest of the steps
        if stats['matches'] > 5:
            stats['TSR'] = (float(stats['kills'])/(float(stats['deaths'])/1.15)*0.65) \
                + (float(stats['assists'])/(float(stats['deaths'])/1.55)*1.20) \
                + (((float(stats['wins'])/(float(stats['wins'])+float(stats['losses'])))/0.55)*0.9) \
                + ((float(stats['agoldmin'])/230)*0.35) \
                + (((float(stats['axpmin']))/380)*0.40) \
                + ((((((float(data[mode + '_denies'])/float(stats['matches']))/12))*0.70)
                + ((((float(data[mode + '_teamcreepkills'])/float(stats['matches']))/93))*0.50)
                + ((float(data[mode + '_wards'])/float(stats['matches']))/1.45*0.30))*(37.5/(float(data[mode + '_secs'])/float(stats['matches'])/60)))
            stats['TSR'] = round(stats['TSR'], 1)
            if stats['TSR'] > 10:
                stats['TSR'] = 10
        else:
            stats['TSR'] = None
    else:
        stats['TSR'] = 0.0
    return stats
