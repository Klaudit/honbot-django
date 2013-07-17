from django.template import Context, loader
from django.http import HttpResponse
from honbot.models import PlayerMatches
from datetime import timedelta, datetime
from json import loads


def seven(request):
    enddate = datetime.today()
    startdate = enddate - timedelta(days=5)
    inrange = PlayerMatches.objects.filter(date__range=[startdate, enddate], mode='rnk')
    kills = inrange.order_by('-kills')[:10]
    for p in kills:
        p.items = loads(p.items)
    wards = inrange.order_by('-wards').values('wards', 'nickname', 'win', 'match_id', 'hero')[:5]
    assists = inrange.order_by('-assists').values('assists', 'nickname', 'win', 'match_id', 'hero')[:5]
    deaths = inrange.order_by('-deaths').values('deaths', 'nickname', 'win', 'match_id', 'hero')[:5]
    cs = inrange.order_by('-cs').values('cs', 'nickname', 'win', 'match_id', 'hero')[:5]
    denies = inrange.order_by('-denies').values('denies', 'nickname', 'win', 'match_id', 'hero')[:5]
    apm = inrange.order_by('-apm').values('apm', 'nickname', 'win', 'match_id', 'hero')[:5]
    gpm = inrange.order_by('-gpm').values('gpm', 'nickname', 'win', 'match_id', 'hero')[:5]
    lost = inrange.order_by('-goldlost2death').values('goldlost2death', 'nickname', 'win', 'match_id', 'hero')[:5]
    smackdown = inrange.order_by('-smackdown').values('smackdown', 'nickname', 'win', 'match_id', 'hero')[:5]
    t = loader.get_template('top.html')
    c = Context({'kills': kills, 'wards': wards, 'deaths': deaths, 'assists': assists, 'cs': cs, 'apm': apm, 'gpm': gpm, 'lost': lost, 'denies': denies, 'smackdown': smackdown})
    return HttpResponse(t.render(c))
