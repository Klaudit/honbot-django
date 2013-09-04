# This file is intended for extra pages like site stats and possibly an about page
from django.shortcuts import render_to_response
from honbot.models import PlayerMatchCount, PlayerCount

def stats(request):
    players = PlayerCount.objects.all()
    return render_to_response('sitestats.html', {'players':players})