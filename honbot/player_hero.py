from django.shortcuts import render_to_response
import api_call
from django.http import HttpResponse


def player_hero(request, name):
    return render_to_response('player_hero.html', {'player': name})


def player_hero_stats(request, name, hero):
    url = "/hero_statistics/ranked/nickname/" + name + "/heroid/" + hero
    data = api_call.get_json(url)
    if data is not None:
        hero = {}
        hero['id'] = data[0]['hero_id']
        hero['wins'] = data[0]['rnk_ph_wins']
        hero['losses'] = data[0]['rnk_ph_losses']
        hero['percent'] = int((float(data[0]['rnk_ph_wins']) / float(data[0]['rnk_ph_used'])) * 100)
        hero['kills'] = round(float(data[0]['rnk_ph_herokills']) / float(data[0]['rnk_ph_used']), 1)
        return render_to_response('player_hero_stats.html', {'hero': hero})
    else:
        return HttpResponse('Error! Stats not found')
