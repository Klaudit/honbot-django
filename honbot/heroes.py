# some functions borrowed from https://github.com/theli-ua/hondiff

from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from django.db.models import Avg, Max, Min
from .models import Heroes, HeroUse, HeroData
from datetime import date
from math import floor
from json import loads


def dmgreduction(armor):
    if armor >= 0:
        r = (0.06 * armor) / ( 1 + 0.06 * armor )
    else:
        r = 0.94**abs(armor) - 1
    return '{0}%'.format(round(r,4) * 100)


def iterable_attribute(name, supername, a, ability):
    try:
        a[name] = ability['attributes'][supername]
        if ',' in a[name]:
            a[name] = a[name].split(',')
            for c in a[name]:
                c = float(c) / 1000
            a[name] = ' / '.join(a[name])
    except KeyError:
        a[name] = None

def isDigit(c):
    return c in ['0','1','2','3','4','5','6','7','8','9']


def hon2html(msg):
    hon_colors = ["00","1C","38","54","70","8C","A8","C4","E0","FF"]
    msg = msg.replace('\\n','<br>')
    parts = msg.split('^')
    base = '<span>'
    #msg = '<span style="color: white;">' + parts[0]
    msg = base + parts[0]
    for part in parts[1:]:
        if len(part) < 1:
            msg += '^'
        elif part[0] == 'w' or part[0] == 'W':
            msg += '</span><span style="color: white;">' + part[1:]
        elif part[0] == 'r' or part[0] == 'R':
            msg += '</span><span style="color: #FF4C4C;">' + part[1:]
        elif part[0] == 'y' or part[0] == 'Y':
            msg += '</span><span style="color: #FFFF19;">' + part[1:]
        elif part[0] == 'g' or part[0] == 'G':
            msg += '</span><span style="color: #008000;">' + part[1:]
        elif part[0] == 'k' or part[0] == 'K':
            msg += '</span><span style="color: #000000;">' + part[1:]
        elif part[0] == 'c' or part[0] == 'C':
            msg += '</span><span style="color: #00FFFF;">' + part[1:]
        elif part[0] == 'b' or part[0] == 'B':
            msg += '</span><span style="color: #4C4CFF;">' + part[1:]
        elif part[0] == 't' or part[0] == 'T':
            msg += '</span><span style="color: teal;">' + part[1:]
        elif part[0] == 'o' or part[0] == 'O':
            msg += '</span><span style="color: orange;">' + part[1:]
        elif part[0] == 'm' or part[0] == 'M':
            msg += '</span><span style="color: #FF00FF;">' + part[1:]
        elif len(part) >= 3 and isDigit(part[0]) and isDigit(part[1]) and isDigit(part[2]):
            msg += '</span><span style="color: #%s%s%s;">' % (hon_colors[int(part[0])],hon_colors[int(part[1])],hon_colors[int(part[2])]) + part[3:]
        elif part[0] == '*':
            msg += '</span>' + base + part[1:]
        elif part[0] in [';',':']:
            msg += part[1:]
        else:
            msg += part
    return msg + '</span>'


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
    use = HeroUse.objects.filter(hero_id=h['hero_id']).order_by('-date')[:15]
    use = use[::-1]
    popularity = HeroUse.objects.get(hero_id=h['hero_id'], date=date.today().strftime("%Y-%m-%d"))
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
    lvl25['healthpoints'] = h['maxhealth'] + (19 * (h['strength'] + 20 + floor(h['strengthperlevel'] * 24)))
    lvl1['manapoints'] = h['maxmana'] + (13 * h['intelligence'])
    lvl25['manapoints'] = h['maxmana'] + (13 * (h['intelligence'] + 20 + floor(h['intelligenceperlevel'] * 24)))
    lvl1['hpregeneration'] = h['healthregen']  + (0.03 * h['strength'])
    lvl25['hpregeneration'] = h['healthregen'] + (0.03 * (h['strength'] + 20 + floor(h['strengthperlevel'] * 24)))
    lvl1['mpregeneration'] = h['manaregen'] + (0.04 * h['intelligence'])
    lvl25['mpregeneration'] = h['manaregen'] + (0.04 * (h['intelligence'] + 20 + floor(h['intelligenceperlevel'] * 24)))
    abilities = [0] * 4
    for ability in [loads(h['ability1'])[1], loads(h['ability2'])[1], loads(h['ability3'])[1], loads(h['ability4'])[1]]:
        a = {}
        name = ability['cli_ab_name']
        try:
            a['name'] = ability['STRINGTABLE'][name + '_name']
        except KeyError:
            a['name'] = ''
        try:
            a['description'] = ability['STRINGTABLE'][name + '_description']
        except KeyError:
            a['description'] = ability['STRINGTABLE'][name + '_description_simple']
        if ability['attributes'] != False:
            a['actiontype'] = ability['attributes']['ACTIONTYPE'].replace('_', ' ').title()
            try:
                a['targetscheme'] = ability['attributes']['TARGETSCHEME'].replace('_', ' ').title()
            except KeyError:
                a['targetscheme'] = None
            try:
                a['casteffecttype'] = ability['attributes']['CASTEFFECTTYPE'].replace('_', ' ').title()
            except KeyError:
                a['casteffecttype'] = None
            iterable_attribute('range', 'RANGE', a, ability)
            iterable_attribute('casttime', 'RANGE', a, ability)
            iterable_attribute('manacost', 'MANACOST', a, ability)
            iterable_attribute('cooldown', 'COOLDOWN', a, ability)
            iterable_attribute('requiredlevel', 'REQUIREDLEVEL', a, ability)
        a['effect'] = hon2html(ability['STRINGTABLE'][name + '_description_simple'])
        try:
            a['impacteffect'] = hon2html(ability['STRINGTABLE'][name + '_IMPACT_effect'])
        except KeyError:
            a['impacteffect'] = None
        try:
            a['sotmeffect'] = hon2html(ability['STRINGTABLE'][name + '_description_simple:ult_boost'])
        except KeyError:
            a['sotmeffect'] = None
        abilities[int(ability['ab_slot'])] = a
    return render_to_response('hero.html',
        {'hero': h, 'use': use, 'popularity': popularity, 'minmax': minmax, 'lvl1': lvl1, 'lvl25': lvl25, 'abilities': abilities})
