# needs to be re-written
# deletes before checking if a new call can be secured
# poorly written
# must try to get a new one before removing old one and fucking oneself

from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import PlayerHistory, Matches
from api_call import get_json
from match import multimatch
from utils import pmoselect, fullmode

from datetime import datetime, timedelta
from json import dumps, loads

return_size = 25


def history(request, account_id, page, mode):
    """
    this is the main function of player history
    """
    phistory = PlayerHistory.objects.filter(player_id=account_id, mode=mode).first()
    count = int(page) * return_size
    # if history exists check the age
    if phistory is not None:
        # find age
        old = phistory.id
        tdelta = datetime.now() - datetime.strptime(str(phistory.updated), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1080:
            data = loads(phistory.history)
        else:
            data = update_history(account_id, mode, phistory)
            try:
                PlayerHistory.objects.get(id=old).delete()
            except:
                pass
    else:
        data = update_history(account_id, mode, phistory)
    verify_matches(data[(count - return_size):count], mode)
    PMObj = pmoselect(mode)
    matches = PMObj.objects.filter(
        match_id__in=data[(count - return_size):count], player_id=account_id).order_by('-date').values()
    for match in matches:
        match['date'] = datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
    if len(matches) != 0:
        return render_to_response('player_history.html', {'matches': matches})
    else:
        return HttpResponse('stop')


def update_history(account_id, mode, phistory):
    """
    Updates a player's history and saves it to db. [] is saved if no result
    """
    url = '/match_history/' + fullmode(mode) + '/accountid/' + account_id
    raw = get_json(url)
    # if no recent matches just save an empty array
    try:
        raw = raw[0]['history']
    except:
        # try to fallback if api down
        if phistory is not None:
            return phistory
        else:
            PlayerHistory(player_id=account_id, history=dumps([]), mode=mode).save()
            return []
    data = []
    for match in raw.split(','):
        if len(match) > 20:   # this fixes an error on broken player histories
            data.append(int(match.split('|')[0]))
    PlayerHistory(player_id=account_id, history=dumps(data[::-1]), mode=mode).save()
    return data[::-1]


def verify_matches(data, mode):
    """
    this checks for matches to exist in the database. If they do not exist they are then downloaded.
    """
    findexisting = Matches.objects.filter(match_id__in=data).values('match_id')
    existing = set([int(match['match_id']) for match in findexisting])
    missing = [x for x in data if x not in existing]
    # if any are missing FIND THEM
    if len(missing) != 0:
        strmatches = ''
        for match in missing:
            strmatches += str(match)
            if match != missing[-1]:
                strmatches += '+'
        url = '/multi_match/all/matchids/' + strmatches
        raw = get_json(url)
        if raw is not None:
            multimatch(raw, missing, mode)
