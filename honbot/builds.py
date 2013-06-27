from django.template import Context, loader
from django.http import HttpResponse
import advanced
from match import match
from error import error


def build(request, match_id):
    data = advanced.main(match_id)
    if data is not None:
        stats = match(match_id)
        builds = data.builds()
        for i, p in enumerate(stats['players']):
            if p is None:
                stats['players'].pop(i)
        for i, build in enumerate(builds):
            if build is not None:
                build.insert(0, stats['players'][0])
                stats['players'].pop(0)
        t = loader.get_template('build.html')
        c = Context({'builds': builds, 'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "Match is more than 28 days old or the replay is not available.")
