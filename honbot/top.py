from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import Matches, PlayerMatches
from datetime import timedelta, datetime


def main(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=5)
    kills = list(PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-kills')[:5])
    t = loader.get_template('top.html')
    c = Context({'kills': kills})
    return HttpResponse(t.render(c))
