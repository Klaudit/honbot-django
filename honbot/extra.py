# This file is intended for extra pages like site stats and possibly an about page
from django.shortcuts import render_to_response
from honbot.models import PlayerMatchCount, PlayerCount, MatchCount
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)
def stats(request):
    players = PlayerCount.objects.all()
    matches = MatchCount.objects.all()
    playermatches = PlayerMatchCount.objects.all()
    return render_to_response('sitestats.html', {'players':players, 'matches':matches, 'playermatches':playermatches})