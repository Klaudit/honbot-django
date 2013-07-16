from django.shortcuts import render_to_response
import api_call
from django.http import HttpResponse
from honbot.models import PlayerMatches, PlayerStats, PlayerHeroStats
from datetime import datetime
import json


def divided(num1, num2):
    try:
        return float(num1) / float(num2)
    except ZeroDivisionError:
        return 0


def player_hero(request, name):
    stats = PlayerStats.objects.filter(nickname=name).values()[0]
    return render_to_response('player_hero.html', {'player': name, 'stats': stats})


def player_hero_stats(request, name, hero):
    search = PlayerHeroStats.objects.filter(nickname=name, hero_id=hero)
    if search.exists():
        tdelta = datetime.now() - datetime.strptime(str(search.values('updated')[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1000:
            data = json.loads(search.values('data')[0]['data'])
        else:
            url = "/hero_statistics/ranked/nickname/" + name + "/heroid/" + hero
            data = api_call.get_json(url)
            search.delete()
            PlayerHeroStats(nickname=name, hero_id=hero, data=json.dumps(data)).save()
    else:
        url = "/hero_statistics/ranked/nickname/" + name + "/heroid/" + hero
        data = api_call.get_json(url)
        PlayerHeroStats(nickname=name, hero_id=hero, data=json.dumps(data)).save()
    if data is not None:
        hero = {}
        hero['id'] = data[0]['hero_id']
        hero['wins'] = data[0]['rnk_ph_wins']
        hero['losses'] = data[0]['rnk_ph_losses']
        hero['percent'] = int(divided(data[0]['rnk_ph_wins'], data[0]['rnk_ph_used']) * 100)
        hero['kills'] = round(divided(data[0]['rnk_ph_herokills'], data[0]['rnk_ph_used']), 1)
        hero['deaths'] = round(divided(data[0]['rnk_ph_deaths'], data[0]['rnk_ph_used']), 1)
        hero['kdr'] = round(divided(data[0]['rnk_ph_herokills'], data[0]['rnk_ph_deaths']), 1)
        hero['consume'] = round(divided(data[0]['rnk_ph_consumables'], data[0]['rnk_ph_used']), 1)
        hero['gpm'] = round(divided(data[0]['rnk_ph_gold'], divided(data[0]['rnk_ph_secs'], 60)), 1)
        hero['apm'] = round(divided(data[0]['rnk_ph_actions'], divided(data[0]['rnk_ph_secs'], 60)), 1)
        hero['exp'] = round(divided(data[0]['rnk_ph_exp'], divided(data[0]['rnk_ph_secs'], 60)), 1)
        hero['cs'] = round(divided(data[0]['rnk_ph_teamcreepkills'], data[0]['rnk_ph_used']), 1)
        hero['cd'] = round(divided(data[0]['rnk_ph_denies'], data[0]['rnk_ph_used']), 1)
        hero['wards'] = round(divided(data[0]['rnk_ph_wards'], data[0]['rnk_ph_used']), 1)
        return render_to_response('player_hero_stats.html', {'hero': hero})
    else:
        return HttpResponse('Error! Returned no stats with this hero.')
