from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.db.models import Avg, Max, Min
from honbot.models import Heroes, HeroUse, HeroData
from datetime import date, timedelta
import json


def main(request):
    heroes = Heroes.objects.all().values()
    today = (date.today()-timedelta(days=1)).strftime("%Y-%m-%d")
    data = HeroData.objects.all().order_by('hero_id').values('cli_name')
    use = list(HeroUse.objects.filter(date=today).order_by('hero_id').values())
    for index, hero in enumerate(heroes):
        hero['popularity'] = use[index]['popularity']
        hero['cli_name'] = data[index]['cli_name']
    return render_to_response('heroes.html', {'heroes': heroes})


def hero(request, name):
    h = HeroData.objects.filter(cli_name=name).values()[0]
    use = HeroUse.objects.filter(hero_id=h['hero_id'])[:10]
    popularity = HeroUse.objects.filter(hero_id=h['hero_id'])[:1][0]
    minmax = HeroData.objects.aggregate(Max('movespeed'),Min('movespeed'),
        Max('turnrate'),Min('turnrate'),
        Max('strengthperlevel'),Min('strengthperlevel'),
        Max('agilityperlevel'),Min('agilityperlevel'),
        Max('intelligenceperlevel'),Min('intelligenceperlevel'),
        Max('attackcooldown'),Min('attackcooldown'),
        Max('attackduration'),Min('attackduration'),
        Max('attackactiontime'),Min('attackactiontime'),
        )
    return render_to_response('hero.html', {'hero': h, 'use': use, 'popularity': popularity, 'minmax': minmax})