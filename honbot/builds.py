import logparse
from honbot.models import Builds, Matches, PlayerMatches
from django.shortcuts import redirect
import datetime
from error import error
from django.shortcuts import render_to_response
import json

def build_view(request, match_id):
    match = Matches.objects.filter(match_id=match_id).values()
    if match.exists():
        builds = Builds.objects.filter(match_id=match_id).values('json')
        if builds.exists():
            match = match[0]
            match['date'] = datetime.datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=1)
            # this needs to be a template
            if match['mode'] == "rnk":
                match['mode'] = "Ranked"
            elif match['mode'] == "cs":
                match['mode'] = "Casual"
            elif match['mode'] == "acc":
                match['mode'] = "Public"
            for build in builds:
                build['json'] = json.loads(build['json'])
            return render_to_response('build.html', {'builds': builds, 'match':match})
        else:
            if logparse.download(match_id, match[0]['replay_url']):
                logparse.parse(match_id)
                return build_view(request, match_id)
            else:
                return error(request, "Match replay failed to download. It could be too old (28 days), too new, or S2 hates you")
    else:
        return redirect('/match/' + match_id + '/')