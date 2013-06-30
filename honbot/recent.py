from honbot.models import Matches, PlayerMatches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


def recent(request):
    matches = Matches.objects.order_by('-date').all().values()
    paginator = Paginator(matches, 20)  # Show 20 matches a page
    # get heroes
    for m in matches:
        m['legion'] = PlayerMatches.objects.filter(match=m['match_id'], team=1).values("hero")
        m['hellborne'] = PlayerMatches.objects.filter(match=m['match_id'], team=2).values("hero")
        m['winner'] = PlayerMatches.objects.filter(match=m['match_id'], team=1).values("win")[0]['win']

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
