from honbot.models import Matches, PlayerMatches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
import json


def recent(request):
    paginator = Paginator(Matches.objects.all(), 5)  # Show 20 matches a page
    matches = list(Matches.objects.all().values('match_id', 'realtime')[:5])
    # get heroes
    for m in matches:
        m['legion'] = []
        m['hellborne'] = []
        players = PlayerMatches.objects.filter(match=m['match_id']).values("hero", "win", "team")
        for p in players:
            if p['team'] == 1:
                m['legion'].append(p['hero'])
            else:
                m['hellborne'].append(p['hero'])
    print json.dumps(matches)

    page = request.GET.get('page')
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        matches = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        matches = paginator.page(paginator.num_pages)
    return render_to_response('recent.html', {"matches": matches})
