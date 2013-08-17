from django.shortcuts import render_to_response
from honbot.models import PlayerMatches, PlayerStats
from error import error
import pretty
from collections import Counter


def view(request, name):
    try:
        stats = PlayerStats.objects.filter(nickname=name).values()[0]
    except IndexError:
        return error(request, "You may have spelled the players name incorrectly. Player stats missing.")
    matches = PlayerMatches.objects.filter(player_id=stats['player_id'], mode='rnk').order_by('match')[:50]
    count = matches.count()
    mmr = [0] * (count+1)
    mmr[-1] = stats['mmr']
    i = count-1
    for match in matches:
        mmr[i] = mmr[i+1] + (match.mmr_change * -1)
        i = i-1
    mmr = mmr[1:]
    updated = pretty.date(stats['updated'])
    match_list = [m.match_id for m in reversed(matches)]
    top_heroes = Counter([m.hero for m in matches]).most_common(6)
    heroes = []
    for h in top_heroes:
        new = {}
        new['hero'] = h[0]
        new['used'] = h[1]
        new['kills'] = sum([i.kills for i in matches if i.hero == new['hero']]) / new['used']
        heroes.append(new)
    return render_to_response('chart.html', {'mmr':mmr, 'count':count, 'match_list':match_list, 'stats':stats, 'updated':updated, 'heroes':heroes})