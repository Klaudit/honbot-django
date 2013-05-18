from django.template import Context, loader
from django.http import HttpResponse
from api_call import get_json
from match import recent_matches
from player import match_history_data
import json


def ranked(request, number):
    ### Get Match history ### api.heroesofnewerth.com/match_history/ranked/accountid/123456/?token=yourtoken
    return_size = 10  # total result size
    count = int(request.GET.get('more', '')) * return_size
    mode = str(request.GET.get('mode', ''))
    if mode == "rnk":
        url = '/match_history/ranked/accountid/' + number
    elif mode == "cs":
        url = '/match_history/casual/accountid/' + number
    elif mode == "acc":
        url = '/match_history/public/accountid/' + number
    data = get_json(url)
    history = []
    if data is not None:
        history = recent_matches(data, return_size, count)
    ### Get Match History Data ###
    history_detail = match_history_data(history, number)
    ### deliver to view ###
    if len(history_detail) is not 0:
        t = loader.get_template('match_history.html')
        c = Context({'mdata': history_detail, 'count': count})
        return HttpResponse(t.render(c))
    else:
        return HttpResponse('stop')
