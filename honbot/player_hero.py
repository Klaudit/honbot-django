from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Heroes, PlayerHeroStats
from utils import psoselect
from api_call import get_json

from datetime import datetime
from json import loads, dumps


def divided(num1, num2):
    try:
        return float(num1) / float(num2)
    except ZeroDivisionError:
        return 0


def base_view(request, name, mode):
    PSObj = psoselect(mode)
    stats = PSObj.objects.filter(nickname=name).first()
    heroes = Heroes.objects.all().order_by('disp_name')
    return render_to_response('player_hero.html', {'player': name, 'stats': stats, 'mode': mode, 'view': "player_hero", 'heroes': heroes})


def player_hero_stats(request, name, hero, mode, modename):
    search = PlayerHeroStats.objects.filter(nickname=name, hero_id=hero, mode=mode)
    if search.exists():
        tdelta = datetime.now() - datetime.strptime(str(search.values('updated')[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1000:
            data = loads(search.values('data')[0]['data'])
        else:
            url = "/hero_statistics/" + modename + "/nickname/" + name + "/heroid/" + hero
            data = get_json(url)
            search.delete()
            PlayerHeroStats(nickname=name, hero_id=hero, data=dumps(data), mode=mode).save()
    else:
        url = "/hero_statistics/" + modename + "/nickname/" + name + "/heroid/" + hero
        data = get_json(url)
        PlayerHeroStats(nickname=name, hero_id=hero, data=dumps(data), mode=mode).save()
    if data is not None:
        if mode is "acc":
            mode = ""
        else:
            mode = mode + '_'
        hero = {}
        hero['id'] = data[0]['hero_id']
        hero['wins'] = data[0][mode + 'ph_wins']
        hero['losses'] = data[0][mode + 'ph_losses']
        hero['percent'] = int(divided(data[0][mode + 'ph_wins'], data[0][mode + 'ph_used']) * 100)
        hero['kills'] = round(divided(data[0][mode + 'ph_herokills'], data[0][mode + 'ph_used']), 1)
        hero['deaths'] = round(divided(data[0][mode + 'ph_deaths'], data[0][mode + 'ph_used']), 1)
        hero['kdr'] = round(divided(data[0][mode + 'ph_herokills'], data[0][mode + 'ph_deaths']), 2)
        hero['consume'] = round(divided(data[0][mode + 'ph_consumables'], data[0][mode + 'ph_used']), 1)
        hero['gpm'] = round(divided(data[0][mode + 'ph_gold'], divided(data[0][mode + 'ph_secs'], 60)), 1)
        hero['apm'] = round(divided(data[0][mode + 'ph_actions'], divided(data[0][mode + 'ph_secs'], 60)), 1)
        hero['exp'] = round(divided(data[0][mode + 'ph_exp'], divided(data[0][mode + 'ph_secs'], 60)), 1)
        hero['cs'] = round(divided(data[0][mode + 'ph_teamcreepkills'], data[0][mode + 'ph_used']), 1)
        hero['cd'] = round(divided(data[0][mode + 'ph_denies'], data[0][mode + 'ph_used']), 1)
        hero['wards'] = round(divided(data[0][mode + 'ph_wards'], data[0][mode + 'ph_used']), 1)
        return render_to_response('player_hero_stats.html', {'hero': hero})
    else:
        return HttpResponse('Error! Returned no stats with this hero.')
