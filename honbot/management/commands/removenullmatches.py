from honbot.models import Matches
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This will remove all matches that have a time length of 0 and probably no players'

    def handle(self, *args, **options):
        remove = Matches.objects.filter(realtime=0)
        count = remove.count()
        remove.delete()
        self.stdout.write("Success! Deleted: " + str(count) + ' matches')
