from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches
from datetime import timedelta, datetime
from django.db.models import Count
import json


def main(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=5)
    kills = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk').order_by('-kills')[:5]
    for p in kills:
        p.items = json.loads(p.items)
    wards = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk').order_by('-wards').values('wards', 'nickname', 'win', 'match_id', 'hero')[:5]
    assists = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk').order_by('-assists').values('assists', 'nickname', 'win', 'match_id', 'hero')[:5]
    deaths = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk').order_by('-deaths').values('deaths', 'nickname', 'win', 'match_id', 'hero')[:5]
    cs = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk').order_by('-cs').values('cs', 'nickname', 'win', 'match_id', 'hero')[:5]
    t = loader.get_template('top.html')
    c = Context({'kills': kills, 'wards': wards, 'deaths': deaths, 'assists': assists, 'cs': cs})
    return HttpResponse(t.render(c))
