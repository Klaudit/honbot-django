from django.template import Context, loader
from django.http import HttpResponse
from api_call import get_json
from match import recent_matches
from player import match_history_data
from honbot.models import *
from datetime import datetime
import json


def history(request, number):
    ### Get Match history ### api.heroesofnewerth.com/match_history/ranked/accountid/123456/?token=yourtoken
    return_size = 10  # total result size
    count = int(request.GET.get('more', '')) * return_size
    mode = str(request.GET.get('mode', ''))
    m = PlayerHistory.objects.filter(player_id=number, mode=mode)
    if bool(m):
        tdelta = datetime.utcnow() - datetime.strptime(str(m.values()[0]['updated']), "%Y-%m-%d %H:%M:%S+00:00")
        if tdelta.seconds + (tdelta.days * 86400) < 1080:
            data = json.loads(m.values()[0]['history'])
        else:
            data = None
    else:
        data = None
    if data is None:
        print "new history"
        if mode == "rnk":
            url = '/match_history/ranked/accountid/' + number
        elif mode == "cs":
            url = '/match_history/casual/accountid/' + number
        elif mode == "acc":
            url = '/match_history/public/accountid/' + number
        data = get_json(url)
        if bool(m):
            m[0].history = json.dumps(data)
            m[0].save()
        else:
            PlayerHistory(player_id=number, history=json.dumps(data), mode=mode).save()
    history = []
    if data is not None:
        history = recent_matches(data, return_size, count)
    ### Get Match History Data ###
    history_detail = match_history_data(history, number, mode)
    ### deliver to view ###
    if len(history_detail) is not 0:
        t = loader.get_template('match_history.html')
        c = Context({'mdata': history_detail, 'count': count})
        return HttpResponse(t.render(c))
    else:
        return HttpResponse('stop')
