from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json
from honbot.models import HeroUseage
from datetime import date
from collections import OrderedDict


class Command(BaseCommand):
    help = 'This will get hero usage'

    def handle(self, *args, **options):
        heroes = get_json('/heroes/usage')
        today = date.today().strftime("%Y-%m-%d")
        bulk = []
        del heroes['total']
        heroes = OrderedDict(sorted(heroes.items(), key=lambda t: t[1]))
        for index, hero in enumerate(heroes):
            bulk.append(HeroUseage(
                date=today,
                hero_id=hero,
                popularity=index+1,
                usage=heroes[hero]
            ))
        HeroUseage.objects.bulk_create(bulk)
        self.stdout.write("success")
