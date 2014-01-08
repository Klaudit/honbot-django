from .models import PlayerMatches, PlayerMatchesPublic, PlayerMatchesCasual, PlayerHistory, Matches
from django.shortcuts import render_to_response
from django.http import HttpResponse
from api_call import get_json
from datetime import datetime
from json import dumps, loads
from match import multimatch

return_size = 25

def history_ranked(request, account_id, page):
    url = "/match_history/ranked/accountid/" + account_id
    pmobject = PlayerMatches
    return history(request, account_id, "rnk", url, page, pmobject)

def history_casual(request, account_id, page):
    url = '/match_history/casual/accountid/' + account_id
    pmobject = PlayerMatchesCasual
    return history(request, account_id, "cs", url, page, pmobject)

def history_public(request, account_id, page):
    url = '/match_history/public/accountid/' + account_id
    pmobject = PlayerMatchesPublic
    return history(request, account_id, "acc", url, page, pmobject)

def history(request, account_id, mode, url, page, pmobject):
    """
    this is the main function of player history
    """
    phistory = PlayerHistory.objects.filter(player_id=account_id, mode=mode)
    count = int(page) * return_size
    # if history exists check the age
    if phistory.exists():
        # find age
        existing = phistory.values()[0]
        old = existing['id']
        tdelta = datetime.now() - datetime.strptime(str(existing['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1080:
            data = loads(existing['history'])
        else:
            data = update_history(url, account_id, mode, True)
            delete = PlayerHistory.objects.get(id=old).delete()
    else:
        data = update_history(url, account_id, mode, False)
    verify_matches(data[(count-return_size):count], mode)
    matches = pmobject.objects.filter(match_id__in=data[(count-return_size):count], player_id=account_id).order_by('-date').values()
    if len(matches) != 0:
        return render_to_response('player_history.html', {'matches': matches})
    else:
        return HttpResponse('stop')

def update_history(url, account_id, mode, exists):
    """
    Updates a player's history and saves it to db. [] is saved if no result
    """
    raw = get_json(url)
    # if no recent matches just save an empty array
    try:
        raw = raw[0]['history']
    except:
        # try to fallback if api down
        if exists:
            data = loads(PlayerHistory.objects.filter(player_id=account_id, mode=mode).values()[0]['history'])
            PlayerHistory(player_id=account_id, history=dumps(data), mode=mode).save()
            return data
        else:
            PlayerHistory(player_id=account_id, history=dumps([]), mode=mode).save()
            return []
    data = []
    for match in raw.split(','):
        if len(match) > 20: # this fixes an error on broken player histories
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
        if raw != None:
            multimatch(raw, missing, mode)
