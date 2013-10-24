from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json
from honbot.models import PlayerStats


class Command(BaseCommand):
    help = 'This will find players that are missing and slam them into our database'

    def handle(self, *args, **options):
        players = PlayerStats.objects.raw("""SELECT A.`player_id` FROM honbot_playerstats A LEFT JOIN honbot_playermatches B ON A.`player_id` = B.`player_id` WHERE B.`player_id` is NULL and A.`player_id` != 0""")
        for player in players:
            print player.player_id
        self.stdout.write("success")
