from django.shortcuts import render_to_response
import api_call


def player_hero(request, name):
    return render_to_response('player_hero.html', {'player': name})


def player_hero_stats(request, name, hero):
    url = "/hero_statistics/ranked/nickname/" + name + "/heroid/" + hero
    data = api_call.get_json(url)[0]
    return render_to_response('player_hero_stats.html', {'data': data})
