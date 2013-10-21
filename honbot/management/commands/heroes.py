from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json
from honbot.models import Heroes


class Command(BaseCommand):
    help = 'This will get hero data'

    def handle(self, *args, **options):
        heroes = get_json('/heroes/all')
        bulk = []
        for hero in heroes:
            bulk.append(Heroes(
                hero_id=heroes[hero]['hero_id'],
                disp_name=heroes[hero]['disp_name'],
                description=heroes[hero]['description'],
                primaryattribute=heroes[hero]['primaryattribute'],
                attacktype=heroes[hero]['attacktype'],
                team=heroes[hero]['team']
            ))
        Heroes.objects.all().delete()
        Heroes.objects.bulk_create(bulk)
        self.stdout.write("success")
