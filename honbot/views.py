from django.http import HttpResponse
from django.template import Context, loader
from random import randint
import advanced
import match
from error import error
import json


def home(request):
    t = loader.get_template('newhome.html')
    random = randint(1, 74)
    c = Context({'random': random})
    return HttpResponse(t.render(c))


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
