from django.template import Context, loader
from django.http import HttpResponse
from advanced import main
from match import match
from error import error


def build(request, match_id):
    data = main(match_id)
    if data is not None:
        stats = match(match_id)
        builds = data.builds()
        for i, build in enumerate(builds):
            build.insert(0, stats['players'][i])
        t = loader.get_template('build.html')
        c = Context({'builds': builds, 'match_id': match_id, 'stats': stats})
        return HttpResponse(t.render(c))
    else:
        return error(request, "Match is more than 28 days old or the replay is not available.")
