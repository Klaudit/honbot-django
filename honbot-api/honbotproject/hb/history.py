from django.utils.timezone import utc
from django.http import Http404
from .models import Player
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from json import dumps, loads
from .api import get_json


return_size = 25


@api_view(['GET'])
def player_history(request, pid, page, mode):
    """
    this is the main function of player history
    returns 404 if user doesn't already exist in db
    """
    count = page * return_size
    p = get_or_update_history(pid)
    return Response(Player.objects.filter(player_id=p.player_id).values('rnk_history', 'cs_history', 'acc_history', 'history_updated'))

def get_or_update_history(pid):
    p = Player.objects.filter(player_id=pid).first()
    if p is None:
        raise Http404
    if p.history_updated is None:
        raw = get_json('/match_history/all/accountid/' + pid)
        if raw:
            return update_history(p, raw)
        else:
            raise Http404
    now = datetime.utcnow().replace(tzinfo=utc)
    tdelta = now - p.history_updated
    if tdelta.seconds + (tdelta.days * 86400) > 800:
        raw = get_json('/match_history/all/accountid/' + pid)
        if raw:
            return update_history(p, raw)
        else:
            # update failed return old
            return p
    else:
        # not old
        return p

def update_history(p, raw):
    parsed = [[], [], []]
    for idx, history in enumerate(raw):
        parsed[idx] = [int(m.split('|')[0]) for m in history['history'].split(',')]
    p.rnk_history = dumps(parsed[0][::-1])
    p.cs_history = dumps(parsed[1][::-1])
    p.acc_history = dumps(parsed[2][::-1])
    p.history_updated = datetime.utcnow().replace(tzinfo=utc)
    p.save()
    return p

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