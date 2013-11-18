from django.core.management.base import BaseCommand
from honbot.api_call import get_json
from honbot.models import HeroUse
from datetime import date, timedelta
from collections import OrderedDict
import json

class Command(BaseCommand):
    help = 'This will get hero usage'

    def handle(self, *args, **options):
        heroes = get_json('/heroes/usage')
        today = (date.today()+timedelta(days=1)).strftime("%Y-%m-%d")
        bulk = []
        del heroes['total']
        del heroes['0']
        print json.dumps(heroes)
        order = sorted(heroes, key=lambda key: heroes[key])
        for index, hero in enumerate(order[::-1]):
            bulk.append(HeroUse(
                date=today,
                hero_id=hero,
                popularity=index+1,
                usage=heroes[hero]
            ))
        HeroUse.objects.bulk_create(bulk)
        self.stdout.write("success")
