from django.shortcuts import render_to_response
from honbot.models import PlayerStats
import numpy as np

def view(requst):
    players = PlayerStats.objects.values_list('mmr', 'TSR')
    kills, mmr, bins = [], [], []
    for player in players:
        mmr.append(player[0])
        print player[1]
        kills.append(player[1])
    count = 1200
    for a in range(1,90):
        count = count + 10
        bins.append(count)
    mmr = np.histogram(mmr, bins=bins)
    kills = np.histogram(kills, bins=20, density=True)
    print kills
    return render_to_response('players_stats.html', {'mmr':mmr[0], 'mlable':mmr[1], 'kills':kills[0], 'klable':kills[1]})