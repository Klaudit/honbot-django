from honbot.models import Matches, PlayerMatches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
import datetime


def recent(request):
    paginator = Paginator(Matches.objects.all(), 20)  # Show 20 matches a page
    page = request.GET.get('page')
    try:
        pag = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pag = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pag = paginator.page(paginator.num_pages)
    matches = Matches.objects.all().values()[(pag.start_index()-1):pag.end_index()]
    # get heroes
    for m in matches:
        players = PlayerMatches.objects.filter(match=m['match_id']).values("hero", "team", "win").order_by('position')
        m['legion'] = []
        m['hellborne'] = []
        m['date'] = datetime.datetime.strptime(str(m['date']), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=1)
        for p in players:
            if p['team'] == 1:
                m['legion'].append(p['hero'])
            else:
                m['hellborne'].append(p['hero'])
        try:
            m['winner'] = players[0]['win']
        except:
            m['winner'] = 1
    return render_to_response('recent.html', {"matches": matches, "pag": pag})
