from django.shortcuts import render_to_response
from honbot.models import PlayerStats
from django.db.models import Count
import numpy as np

def view(requst):
    players = PlayerStats.objects.values_list('mmr')
    mmr, bins = [], []
    for player in players:
        mmr.append(player[0])
    count = 1200
    for a in range(1,90):
        count = count + 10
        bins.append(count)
    mmr = np.histogram(mmr, bins=bins)
    return render_to_response('players_stats.html', {'mmr':mmr[0], 'bins':mmr[1]})