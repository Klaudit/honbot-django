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
        p = PlayerStatsCasual.objects.filter(nickname=name).values()
    elif mode == "p":
        url = '/player_statistics/public/nickname/' + name
        mode = "acc"
        p = PlayerStatsPublic.objects.filter(nickname=name).values()
    else:
        url = '/player_statistics/ranked/nickname/' + name
        mode = "rnk"
        p = PlayerStats.objects.filter(nickname=name).values()
    if p:
        tdelta = datetime.now() - datetime.strptime(str(p[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1000:
            s = p[0]
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
        return error(request, "S2 Servers down or name is incorrect. Try another name or gently refreshing the page.")


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
        # ((rnk_herokills/rnk_deaths/1.15)*0.65)
        # ((rnk_heroassists/rnk_deaths/1.55)*1.20)
        # ( ( ( rnk_wins / ( rnk_wins+rnk_losses ) ) / 0.55 ) *0.9 )
        # (((rnk_gold/rnk_secs*60)/230)*(1-((230/195)*((rnk_em_played/rnk_games_played))))*0.35)
        # ((((rnk_exp/rnk_time_earning_exp*60)/380)*(1-((380/565)*(rnk_em_played/rnk_games_played))))*0.40)
        # ((((((rnk_denies/rnk_games_played)/12)*(1-((4.5/8.5)*(rnk_em_played/rnk_games_played))))*0.70)
        # ((((rnk_teamcreepkills/rnk_games_played)/93)*(1-((63/81)*(rnk_em_played/rnk_games_played))))*0.50)
        # ((rnk_wards/rnk_games_played)/1.45*0.30))*(37.5/(rnk_secs/rnk_games_played/60)))
        # Max wards of 5.0.
        # Max creep kills of 200.
        # Max creep denies of 30.
        if mode == 'rnk':
            if stats['matches'] > 5:
                stats['TSR'] = ((float(data['rnk_herokills'])/float(data['rnk_deaths'])/1.15)*0.65)+((float(data['rnk_heroassists'])/float(data['rnk_deaths'])/1.55)*1.20)+(((float(data['rnk_wins'])/(float(data['rnk_wins'])+float(data['rnk_losses'])))/0.55)*0.9)+(((float(data['rnk_gold'])/float(data['rnk_secs'])*60)/230)*(1-((230/195)*((float(data['rnk_em_played'])/float(data['rnk_games_played'])))))*0.35)+((((float(data['rnk_exp'])/float(data['rnk_time_earning_exp'])*60)/380)*(1-((380/565)*(float(data['rnk_em_played'])/float(data['rnk_games_played'])))))*0.40)+((((((float(data['rnk_denies'])/float(data['rnk_games_played']))/12)*(1-((4.5/8.5)*(float(data['rnk_em_played'])/float(data['rnk_games_played'])))))*0.70)+((((float(data['rnk_teamcreepkills'])/float(data['rnk_games_played']))/93)*(1-((63/81)*(float(data['rnk_em_played'])/float(data['rnk_games_played'])))))*0.50)+((float(data['rnk_wards'])/float(data['rnk_games_played']))/1.45*0.30))*(37.5/(float(data['rnk_secs'])/float(data['rnk_games_played'])/60)))
                stats['TSR'] = round(stats['TSR'], 1)
                if stats['TSR'] > 10:
                    stats['TSR'] = 10
            else:
                stats['TSR'] = 0
                stats['kdr'] = 0
        else:
                stats['TSR'] = 0
                stats['kdr'] = 0
    else:
        stats['TSR'] = 0
        stats['kdr'] = 0
        stats['kadr'] = 0
        stats['winpercent'] = 0
        stats['atime'] = 0
        stats['akills'] = 0
        stats['adeaths'] = 0
        stats['aassists'] = 0
        stats['aconsumables'] = 0
        stats['awards'] = 0
        stats['acs'] = 0
        stats['adenies'] = 0
        stats['axpmin'] = 0
        stats['agoldmin'] = 0
        stats['aactionsmin'] = 0
        stats['hours'] = 0
    return stats
