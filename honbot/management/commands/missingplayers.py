from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json
from honbot.models import PlayerStats
from honbot.player import player_math, player_save, update_player_count


class Command(BaseCommand):
    help = 'This will find players that are missing and slam them into our database'

    def handle(self, *args, **options):
        players = PlayerStats.objects.raw("""SELECT A.`player_id` FROM honbot_playerstats A LEFT JOIN honbot_playermatches B ON A.`player_id` = B.`player_id` WHERE B.`player_id` is NULL and A.`player_id` != 0""")
        count = 0
        for player in players:
            data = get_json('/player_statistics/ranked/accountid/' + str(player.player_id))
            if data != None:
                data = player_math(data, 'rnk')
                player_save(data, 'rnk')
                update_player_count()
                count += 1
            if count >= 100:
                break
        self.stdout.write("success on " + str(count))
