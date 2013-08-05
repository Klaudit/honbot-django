from django.shortcuts import render_to_response
import match
from error import error


def match_view(request, match_id):
    stats = match.match(match_id)
    if stats is not None:
        return render_to_response('match.html', {'match_id': match_id, 'stats': stats})
    else:
        return error(request, "S2 Servers down or match id is incorrect. Try another match or gently refreshing the page.")
