from django.template import Context, loader
from django.http import HttpResponse
from api_call import get_json
from honbot.models import *
from match import multimatch
import json
from pretty import date
from datetime import datetime


def history(request, account_id):
    ### Get Match history ### api.heroesofnewerth.com/match_history/ranked/accountid/123456/?token=yourtoken
    return_size = 25  # total result size
    count = int(request.GET.get('more', '')) * return_size
    mode = str(request.GET.get('mode', ''))
    m = PlayerHistory.objects.filter(player_id=account_id, mode=mode)
    if m.exists():
        tdelta = datetime.utcnow() - datetime.strptime(str(m.values()[0]['updated']), "%Y-%m-%d %H:%M:%S")
        if tdelta.seconds + (tdelta.days * 86400) < 1080:
            data = json.loads(m.values()[0]['history'])
        else:
            data = None
    else:
        data = None
    if data is None:
        if mode == "rnk":
            url = '/match_history/ranked/accountid/' + account_id
        elif mode == "cs":
            url = '/match_history/casual/accountid/' + account_id
        elif mode == "acc":
            url = '/match_history/public/accountid/' + account_id
        data = get_json(url)
        if bool(m):
            m[0].history = json.dumps(data)
            m[0].save()
        else:
            PlayerHistory(player_id=account_id, history=json.dumps(data), mode=mode).save()
    history = []
    if data is not None:
        if data[0]['history'] is not None:
            data = data[0]['history'].split(',')
            temp = []
            for i in data:
                temp = i.split('|')
                try:
                    temp.pop(1)
                except:
                    pass
                if len(history) > 0:
                    if history[-1][0] != temp[0]:
                        history.append(temp)
                else:
                    history.append(temp)
            history.reverse()
            history = history[count:return_size+count]
    ### Get Match History Data ###
    url = '/multi_match/all/matchids/'
    plus = False
    count = 0
    needed = []
    for m in history:
        if not Matches.objects.filter(match_id=m[0]).exists():
            if plus:
                url = url + '+' + str(m[0])
            else:
                url = url + str(m[0])
                plus = True
            count += 1
            needed.append(m)
    if count > 0:
        data = get_json(url)
        if data is not None:
            multimatch(data, needed, mode)
            history_detail = get_player_from_matches(history, account_id)
        else:
            history_detail = get_player_from_matches(history, account_id)
    else:
        history_detail = get_player_from_matches(history, account_id)
    ### deliver to view ###
    if len(history_detail) is not 0:
        t = loader.get_template('match_history.html')
        c = Context({'mdata': history_detail, 'count': count})
        return HttpResponse(t.render(c))
    else:
        return HttpResponse('stop')


def get_player_from_matches(history, account_id):
    """
    this takes a list of matches and returns that player's stats in that match
    """
    matches = []
    for m in history:
        temp = {}
        load = PlayerMatches.objects.filter(match_id=m[0], player_id=account_id)
        if load.exists():
            temp = load.values()[0]
            temp['match_id'] = m[0]
            temp['date'] = date(datetime.strptime(str(load[0].match.date), '%Y-%m-%d %H:%M:%S'))
            matches.append(temp)
    return matches
