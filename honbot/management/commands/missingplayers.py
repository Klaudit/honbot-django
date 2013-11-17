from django.core.management.base import BaseCommand
from honbot.api_call import get_json
from .models import PlayerStats
from honbot.player import player_math, player_save, update_player_count
from time import sleep


class Command(BaseCommand):
    help = 'This will find players that are missing and slam them into our database'

    def handle(self, *args, **options):
        players = PlayerStats.objects.raw("""SELECT DISTINCT B.`player_id`
                                             FROM honbot_playerstats A
                                             RIGHT JOIN honbot_playermatches B
                                             ON A.`player_id` = B.`player_id`
                                             WHERE A.`player_id` is NULL""")
        count = 0
        for player in players:
            sleep(.1)
            data = get_json('/player_statistics/ranked/accountid/' + str(player.player_id))
            if data is not None:
                data = player_math(data, 'rnk')
                player_save(data, 'rnk')
                update_player_count()
            count += 1
            if count == 100:
                break
        self.stdout.write("success on " + str(count))
