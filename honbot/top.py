from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches
from datetime import timedelta, datetime
from django.db.models import Count


def main(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=5)
    kills = list(PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-kills')[:5])
    wards = list(PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-wards')[:5])
    mostplays = PlayerMatches.objects.filter(date__range=[startdate, enddate]).values('player_id', 'nickname').annotate(Count('player_id')).order_by('-player_id__count')[:5]
    t = loader.get_template('top.html')
    c = Context({'kills': kills, 'wards': wards, 'mostplays': mostplays})
    return HttpResponse(t.render(c))
