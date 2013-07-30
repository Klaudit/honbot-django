from django.shortcuts import render_to_response
import api_call
from random import randint
from honbot.models import Matches, PlayerStats
from django.views.decorators.cache import cache_page


@cache_page(60 * 5)
def home(request):
    random = randint(1, 74)
    matches = Matches.objects.count()
    json = api_call.pure('/items/id/10')
    test = """{"cli_name":"Item_CrushingClaws","attributes":{"icon":"Item_CrushingClaws.jpg","cost":"150","isPassive":false,"recipeCost":"150","usedIn":["Item_Strength5","Item_BloodChalice"],"strings":{"effect_header":"Status Effect(s)","shop_categories":"Filter_Strength","shop_flavor":"Crushing Claws are filled with clockwork gears, sprockets, and springs that give a boost of strength to whomever wears them.  Despite their role in numerous practical jokes gone awry, these gauntlets remain in widespread use in the ranks."},"name":"Crushing Claws"}}"""
    try:
        if json.text == test:
            server_status = True
        else:
            server_status = False
    except:
        server_status = False
    players = PlayerStats.objects.count()
    return render_to_response('home.html', {'random': random, 'matches': matches, 'players': players, 'server': server_status})
