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
        new['hero'], new['used'] = h
        new['kills'], new['assists'], new['deaths'], new['wins'], new['mmr'], new['apm'], new['gpm'] = 0, 0, 0, 0, 0, 0, 0
        for m in matches:
            if m.hero == new['hero']:
                new['kills'] += m.kills
                new['assists'] += m.assists
                new['deaths'] += m.deaths
                new['wins'] += m.win
                new['mmr'] += m.mmr_change
                new['apm'] += m.apm
                new['gpm'] += m.gpm
        new['win_percent'] = int(float(new['wins']) / new['used'] * 100) 
        new['kills'] = new['kills'] / new['used']
        new['assists'] = new['assists'] / new['used']
        new['deaths'] = new['deaths'] / new['used']
        new['apm'] = int(new['apm'] / new['used'])
        new['gpm'] = int(new['gpm'] / new['used'])
        heroes.append(new)
    return render_to_response('chart.html', {'mmr':mmr, 'count':count, 'match_list':match_list, 'stats':stats, 'updated':updated, 'heroes':heroes})