from django.shortcuts import render_to_response


def player_hero(request, name):
    return render_to_response('player_hero.html', {})
