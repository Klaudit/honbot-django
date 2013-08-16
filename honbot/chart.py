from django.shortcuts import render_to_response
from honbot.models import PlayerMatches, PlayerStats
from error import error
import pretty


def view(request, name):
    try:
        stats = PlayerStats.objects.filter(nickname=name).values()[0]
    except IndexError:
        return error(request, "You may have spelled the players name incorrectly. Player stats missing.")
    matches = list(PlayerMatches.objects.filter(player_id=stats['player_id'], mode='rnk').order_by('match').values()[:50])
    count = len(matches)
    mmr = [0] * (count+1)
    mmr[-1] = stats['mmr']
    i = count-1
    for match in matches:
        mmr[i] = mmr[i+1] + (match['mmr_change'] * -1)
        i = i-1
    mmr = mmr[1:]
    time = pretty.date(stats['updated'])
    match_list = [m['match_id'] for m in reversed(matches)]
    return render_to_response('chart.html', {'mmr':mmr, 'count':count, 'match_list':match_list, 'stats':stats, 'time':time})