from django.core.management.base import BaseCommand
from honbot.api_call import get_json
from honbot.models import HeroUse
from datetime import date, timedelta
from collections import OrderedDict
import json

class Command(BaseCommand):
    help = 'This will get hero usage'

    def handle(self, *args, **options):
        today = date.today().strftime("%Y-%m-%d")
        print HeroUse.objects.filter(date=today).count()
        if HeroUse.objects.filter(date=today).count() < 1:
            heroes = get_json('/heroes/usage')
            bulk = []
            del heroes['total']
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
        else:
            self.stdout.write("success")

