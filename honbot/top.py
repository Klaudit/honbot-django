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
    mostplays = PlayerMatches.objects.filter(date__range=[startdate, enddate]).values('player_id', 'nickname').annotate(Count('player_id')).order_by('-player_id__count')[:5]
    t = loader.get_template('top.html')
    c = Context({'kills': kills, 'wards': wards, 'mostplays': mostplays, 'assists': assists})
    return HttpResponse(t.render(c))
