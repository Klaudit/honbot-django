from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


def recent(request):
    matches = Matches.objects.order_by('-date').all()
    paginator = Paginator(matches, 25)  # Show 25 contacts per page

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
