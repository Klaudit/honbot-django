from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

from .models import PlayerStats, PlayerStatsCasual, PlayerStatsPublic, PlayerCount, PlayerIcon
from api_call import get_json
from avatar import avatar
from error import error
from utils import psoselect, fullmode

from numpy import histogram
from datetime import date, datetime


def player_view(request, name, mode):
    url = '/player_statistics/' + fullmode(mode) + '/nickname/' + name
    PSObj = psoselect(mode)
    p = PSObj.objects.filter(nickname=name).first()
    exists = False
    if p is not None:
        exists = True
        tdelta = datetime.now() - datetime.strptime(str(p.updated), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 900:
            return render_to_response('player.html', {'stats': p, 'mode': mode, 'view': "player"})
    else:
        if mode is "rnk":
            update_player_count()
    data = get_json(url)
    if data is not None:
        # if account id is 0 send fancy error page.
        if int(data['account_id']) is 0:
            return render_to_response('player_error.html', {'name': name})
        p = player_math(data, mode)
        player_save(p, mode)
        return render_to_response('player.html', {'stats': p, 'mode': mode, 'view': "player"})
    else:
        # server down, show old results
        if exists:
            return render_to_response('player.html', {'stats': p, 'mode': mode, 'view': "player", 'fallback': True})
        else:
            return error(request, "S2 server down or name is incorrect. Try another name or gently refreshing page.")


def tooltip(request, account_id, mode):
    PSObj = psoselect(mode)
    player = PSObj.objects.filter(player_id=account_id).first()
    if player is not None:
        icon = PlayerIcon.objects.filter(player_id=account_id).first()
        if icon is None:
            icon = {'avatar': "/static/img/default_avatar.png"}
        return render_to_response('player_tooltip.html', {'player': player, 'avatar': icon})
    else:
        return HttpResponse(status=202)


@cache_page(10000)
def distribution(requst):
    players = PlayerStats.objects.filter(matches__gte=10).values_list('mmr', 'TSR')
    tsr, mmr, bins = [], [], []
    for player in players:
        mmr.append(player[0])
        tsr.append(player[1])
    count = 1200
    for a in range(1, 90):
        count = count + 10
        bins.append(count)
    mmr = histogram(mmr, bins=bins)
    tsr = histogram(tsr, bins=20)
    return render_to_response('distribution.html', {'mmr': mmr[0], 'mlable': mmr[1], 'tsr': tsr[0], 'tlable': tsr[1]})


def player_save(stats, mode):
    global p
    if mode == "rnk":
        p = PlayerStats
    elif mode == "acc":
        p = PlayerStatsPublic
    elif mode == "cs":
        p = PlayerStatsCasual
    p(player_id=stats['player_id'],
        nickname=stats['nickname'],
        cccalls=stats['cccalls'],
        deaths=stats['deaths'],
        cc=stats['cc'],
        assists=stats['assists'],
        TSR=stats['TSR'],
        kdr=stats['kdr'],
        adenies=stats['adenies'],
        aconsumables=stats['aconsumables'],
        kills=stats['kills'],
        winpercent=stats['winpercent'],
        kadr=stats['kadr'],
        akills=stats['akills'],
        kicked=stats['kicked'],
        agoldmin=stats['agoldmin'],
        matches=stats['matches'],
        mmr=stats['mmr'],
        hours=stats['hours'],
        awards=stats['awards'],
        atime=stats['atime'],
        left=stats['left'],
        razed=stats['razed'],
        aactionsmin=stats['aactionsmin'],
        axpmin=stats['axpmin'],
        adeaths=stats['adeaths'],
        ks3=stats['ks3'],
        ks4=stats['ks4'],
        ks5=stats['ks5'],
        ks6=stats['ks6'],
        ks7=stats['ks7'],
        ks8=stats['ks8'],
        ks9=stats['ks9'],
        ks10=stats['ks10'],
        ks15=stats['ks15'],
        bloodlust=stats['bloodlust'],
        doublekill=stats['doublekill'],
        triplekill=stats['triplekill'],
        quadkill=stats['quadkill'],
        annihilation=stats['annihilation'],
        smackdown=stats['smackdown'],
        humiliation=stats['humiliation'],
        nemesis=stats['nemesis'],
        retribution=stats['retribution'],
        level=stats['level'],
        level_exp=stats['level_exp'],
        min_exp=stats['min_exp'],
        max_exp=stats['max_exp'],
        acs=stats['acs'],
        wins=stats['wins'],
        losses=stats['losses'],
        aassists=stats['aassists']).save()


def update_check(player, mode):
    """
    checks if a player needs an update
    """
    PSObj = psoselect(mode)
    result = PSObj.objects.filter(player_id=player).first()
    if result is not None:
        tdelta = datetime.now() - datetime.strptime(str(result.updated), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) > 12000:
            avatar(None, player, 10)
            update_player(player, mode)
    else:
        avatar(None, player, 10)
        update_player(player, mode)


def update_player(pid, mode):
    """
    updates players without rendering
    """
    if mode == 'rnk':
        url = "/player_statistics/ranked/accountid/" + str(pid)
    elif mode == 'cs':
        url = '/player_statistics/casual/accountid/' + str(pid)
    elif mode == 'acc':
        url = '/player_statistics/public/accountid/' + str(pid)
    data = get_json(url)
    p = player_math(data, mode)
    player_save(p, mode)


def update_player_count():
    today = date.today().strftime("%Y-%m-%d")
    current_count = PlayerCount.objects.filter(date=today)
    if current_count.exists():
        current_count.update(count=F('count') + 1)
    else:
        count = PlayerStats.objects.count()
        PlayerCount(count=count).save()


def divide(num1, num2, rounder):
    try:
        answer = round(float(num1) / float(num2), rounder)
    except ZeroDivisionError:
        return 0
    return answer


def player_math(data, mode):
    """
    This will get all the right information for the players view and store it in dict
    returns dict
    TSR calculation
    """
    stats = {}
    stats['player_id'] = int(data['account_id'])  # account id
    try:
        stats['nickname'] = str(data['nickname'])  # name
    except KeyError:
        stats['nickname'] = "Not Found"
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
    stats['razed'] = int(data[mode + '_razed'])  # buildings
    # kill streaks
    stats['ks3'] = int(data[mode + '_ks3'])
    stats['ks4'] = int(data[mode + '_ks4'])
    stats['ks5'] = int(data[mode + '_ks5'])
    stats['ks6'] = int(data[mode + '_ks6'])
    stats['ks7'] = int(data[mode + '_ks7'])
    stats['ks8'] = int(data[mode + '_ks8'])
    stats['ks9'] = int(data[mode + '_ks9'])
    stats['ks10'] = int(data[mode + '_ks10'])
    stats['ks15'] = int(data[mode + '_ks15'])
    stats['bloodlust'] = int(data[mode + '_bloodlust'])
    stats['doublekill'] = int(data[mode + '_doublekill'])
    stats['triplekill'] = int(data[mode + '_triplekill'])
    stats['quadkill'] = int(data[mode + '_quadkill'])
    stats['annihilation'] = int(data[mode + '_annihilation'])
    stats['smackdown'] = int(data[mode + '_smackdown'])
    stats['humiliation'] = int(data[mode + '_humiliation'])
    stats['nemesis'] = int(data[mode + '_nemesis'])
    stats['retribution'] = int(data[mode + '_retribution'])
    if mode == "rnk" or mode == "cas":
        stats['level'] = int(data[mode + '_level'])
        stats['level_exp'] = int(data[mode + '_level_exp'])
        stats['min_exp'] = int(data[mode + '_min_exp'])
        stats['max_exp'] = int(data[mode + '_max_exp'])
    else:
        stats['level'] = 0
        stats['level_exp'] = 0
        stats['min_exp'] = 0
        stats['max_exp'] = 0
    if stats['matches'] > 0:
        stats['hours'] = (int(data[mode + '_secs']) / 60) / 60  # hours played
        # average creep score
        stats['acs'] = round(
            int(data[mode + '_teamcreepkills']) / float(stats['matches']), 1)
        if stats['deaths'] > 0 and stats['kills'] > 0:
            # k+A : d
            stats['kadr'] = round((float(stats['kills']) + float(stats['assists'])) / float(stats['deaths']), 2)
            # kill death ratio
            stats['kdr'] = round(float(stats['kills']) / float(stats['deaths']), 2)
        else:
            stats['kadr'] = 0
            stats['kdr'] = 0
        # win percent
        if int(stats['losses']) != 0:
            stats['winpercent'] = str(
                int(round(float(stats['wins']) / float(stats['wins'] + stats['losses']) * 100))) + '%'
        else:
            stats['winpercent'] = "100%"
        # average time
        stats['atime'] = int(data[mode + '_secs']) / stats['matches'] / 60
        # average kills
        stats['akills'] = divide(stats['kills'], stats['matches'], 1)
        # average deaths
        stats['adeaths'] = round(float(stats['deaths']) / stats['matches'], 1)
        # average assists
        stats['aassists'] = round(float(stats['assists']) / stats['matches'], 1)
        # average consumables
        stats['aconsumables'] = round(float(data[mode + '_consumables']) / stats['matches'], 1)
        # average wards
        stats['awards'] = round(float(data[mode + '_wards']) / stats['matches'], 2)
        # average creep score
        stats['acs'] = round(float(data[mode + '_teamcreepkills']) / stats['matches'], 1)
        # average creep score
        stats['adenies'] = round(float(data[mode + '_denies']) / stats['matches'], 1)
        # average xp / min
        stats['axpmin'] = divide(data[mode + '_exp'], divide(data[mode + '_secs'], 60, 9), 0)
        # average gold / min
        stats['agoldmin'] = divide(data[mode + '_gold'], (float(data[mode + '_secs']) / 60), 1)
        # average actions / min
        stats['aactionsmin'] = divide(data[mode + '_actions'], divide(data[mode + '_secs'], 60, 9), 1)
        # TSR CALC ###
        if stats['matches'] > 10:
            try:
                stats['TSR'] = ((float(data[mode + '_herokills']) / float(data[mode + '_deaths']) / 1.15) * 0.65) + ((float(data[mode + '_heroassists']) / float(data[mode + '_deaths']) / 1.55) * 1.20) + (((float(data[mode + '_wins']) / (float(data[mode + '_wins']) + float(data[mode + '_losses']))) / 0.55) * 0.9) + (((float(data[mode + '_gold']) / float(data[mode + '_secs']) * 60) / 230) * (1 - ((230 / 195) * ((float(data[mode + '_em_played']) / float(data[mode + '_games_played']))))) * 0.35) + ((((float(data[mode + '_exp']) / float(data[mode + '_time_earning_exp']) * 60) / 380) * (1 - ((380 / 565) * (float(data[mode + '_em_played']) / float(data[mode + '_games_played']))))) * 0.40) + (
                    (((((float(data[mode + '_denies']) / float(data[mode + '_games_played'])) / 12) * (1 - ((4.5 / 8.5) * (float(data[mode + '_em_played']) / float(data[mode + '_games_played']))))) * 0.70) + ((((float(data[mode + '_teamcreepkills']) / float(data[mode + '_games_played'])) / 93) * (1 - ((63 / 81) * (float(data[mode + '_em_played']) / float(data[mode + '_games_played']))))) * 0.50) + ((float(data[mode + '_wards']) / float(data[mode + '_games_played'])) / 1.45 * 0.30)) * (37.5 / (float(data[mode + '_secs']) / float(data[mode + '_games_played']) / 60)))
            except:
                stats['TSR'] = 0
            stats['TSR'] = round(stats['TSR'], 1)
            if stats['TSR'] > 10:
                stats['TSR'] = 10
        else:
            stats['TSR'] = 0
    else:
        # no matches on account
        stats['TSR'], stats['kdr'], stats['kadr'], stats['winpercent'], stats['atime'], stats['akills'], stats['adeaths'], stats['aassists'], stats['aconsumables'], stats[
            'awards'], stats['acs'], stats['adenies'], stats['axpmin'], stats['agoldmin'], stats['aactionsmin'], stats['hours'] = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    return stats
