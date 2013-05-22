from django.template import Context, loader
from django.http import HttpResponse
import advanced
import match
from error import error


def build(request, match_id):
    data = advanced.main(match_id)
    stats = match.match(match_id)
    if data is not None:
        t = loader.get_template('build.html')
        c = Context({'data': data, 'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "Match is more than 28 days old or the replay is not available.")
