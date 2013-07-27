from django.http import HttpResponse
from django.shortcuts import render_to_response
import advanced
import match
from error import error


def match_view(request, match_id):
    stats = match.match(match_id)
    if stats is not None:
        t = loader.get_template('match.html')
        c = Context({'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or gently refreshing the page.")
