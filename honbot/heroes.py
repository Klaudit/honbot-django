from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.db.models import Avg, Max, Min
from honbot.models import Heroes, HeroUse, HeroData
from datetime import date
from math import floor


def dmgreduction(armor):
    if armor >= 0:
        r = (0.06 * armor) / ( 1 + 0.06 * armor )
    else:
        r = 0.94**abs(armor) - 1
    return '{0}%'.format(round(r,4) * 100)


def main(request):
    heroes = Heroes.objects.all().values()
    today = date.today().strftime("%Y-%m-%d")
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
    lvl1 = {}
    lvl25 = {}
    lvl1['armor'] = h['armor'] + (0.14 * h['agility'])
    lvl25['armor'] = h['armor'] + 0.14 * floor(h['agility'] + 20 + (h['agilityperlevel'] * 24))
    lvl1['dmgreduction'] = dmgreduction(lvl1['armor'])
    lvl25['dmgreduction'] = dmgreduction(lvl25['armor'])
    lvl1['healthpoints'] = h['maxhealth'] + (19 * h['strength'])
    lvl25['healthpoints'] = h['maxhealth'] + ( 19 * (h['strength'] + 20 + floor(h['strengthperlevel'] * 24)))
    lvl1['manapoints'] = h['maxmana'] + (13 * h['intelligence'])
    lvl25['manapoints'] = h['maxmana'] + (13 * (h['intelligence'] + 20 + floor(h['intelligenceperlevel'] * 24)))
    lvl1['hpregeneration'] = h['healthregen']  + (0.03 * h['strength'])
    lvl25['hpregeneration'] = h['healthregen'] + (0.03 * (h['strength'] + 20 + floor(h['strengthperlevel'] * 24)))
    lvl1['mpregeneration'] = h['manaregen'] + (0.04 * h['intelligence'])
    lvl25['mpregeneration'] = h['manaregen'] + (0.04 * (h['intelligence'] + 20 + floor(h['intelligenceperlevel'] * 24)))
    return render_to_response('hero.html', {'hero': h, 'use': use, 'popularity': popularity, 'minmax': minmax, 'lvl1': lvl1, 'lvl25': lvl25})