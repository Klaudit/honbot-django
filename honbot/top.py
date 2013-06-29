from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches
from datetime import timedelta, datetime
from django.db.models import Count
import json


def main(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=5)
    kills = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-kills')[:5]
    for p in kills:
        p.items = json.loads(p.items)
    wards = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-wards')[:5]
    assists = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-assists')[:5]
    deaths = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-deaths')[:5]
    gpm = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-gpm')[:5]
    apm = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-apm')[:5]
    cs = PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-cs')[:5]
    t = loader.get_template('top.html')
    c = Context({'kills': kills, 'wards': wards, 'deaths': deaths, 'assists': assists, 'gpm': gpm, 'apm': apm, 'cs': cs})
    return HttpResponse(t.render(c))
