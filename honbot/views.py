from django.http import HttpResponse
from django.shortcuts import render_to_response
from random import randint
import advanced
import match
from error import error
import json


def home(request):
    random = randint(1, 74)
    return render_to_response('home.html', {'random': random})


def match_view(request, match_id):
    stats = match.match(match_id)
    if stats is not None:
        t = loader.get_template('match.html')
        c = Context({'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or gently refreshing the page.")


def adv(request, match_id):
    data = advanced.main(match_id)
    if data is not None:
        t = loader.get_template('advanced.html')
        c = Context({'data': data, 'match_id': match_id})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or gently refreshing the page.")
