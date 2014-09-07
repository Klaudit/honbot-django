from django.http import Http404
from django.utils.timezone import now

from .api import get_json
from .models import Player, Match
from .match import multimatch
from .utils import pmoselect

from json import dumps, loads
from rest_framework.decorators import api_view
from rest_framework.response import Response


return_size = 25


@api_view(['GET'])
def player_history(request, pid, page, mode):
    """
    this is the main function of player history
    returns 404 if user doesn't already exist in db
    """
    count = int(page) * return_size
    pl = get_or_update_history(pid)
    his = loads(pl.__history__()[mode])[(count - return_size):count]
    if len(his) > 0:
        verify_matches(his, mode)
    ph = pmoselect(mode).objects.filter(match_id__in=his, player_id=pid).values()
    return Response(ph)


def get_or_update_history(pid):
    p = Player.objects.filter(pk=pid).first()
    if p is None:
        raise Http404
    if p.history_updated is None:
        raw = get_json('/match_history/all/accountid/' + pid)
        if raw:
            return update_history(p, raw)
        else:
            raise Http404
    nowutc = now()
    tdelta = nowutc - p.history_updated
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
    p.history_updated = now()
    p.save(update_fields=['history_updated', 'cs_history', 'acc_history', 'rnk_history'])
    return p


def verify_matches(hist, mode):
    """
    this checks for matches to exist in the database. If they do not exist they are then downloaded.
    """
    findexisting = Match.objects.filter(match_id__in=hist).values('match_id')
    existing = set([int(match['match_id']) for match in findexisting])
    missing = [x for x in hist if x not in existing]
    # if any are missing FIND THEM
    if len(missing) != 0:
        multimatch(missing)


@api_view(['GET'])
def get_cached(request, pid, mode):
    matches = pmoselect(mode).objects.filter(player_id=pid).values()
    return Response(matches)
