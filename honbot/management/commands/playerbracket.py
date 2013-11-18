from django.core.management.base import BaseCommand
from honbot.models import PlayerBrackets, PlayerStats
from django.db.models import Avg, Max, Min, StdDev


class Command(BaseCommand):
    help = 'Performs the math to create averages for player brackets'

    def handle(self, *args, **options):
        for mmr in xrange(600, 2300, 10):
            players = PlayerStats.objects.filter(mmr__range=(mmr, (mmr + 9.999999)), akills__lt=15, adeaths__lt=15, aassists__lt=20, matches__gt=15)
            if players.count() > 20:
                print str(players.count()) + " players found at: " + str(mmr)
                newbr = PlayerBrackets(mmr_bracket=mmr, count=players.count())
                kills = players.aggregate(Max('akills'), Avg('akills'), Min('akills'), StdDev('akills'))
                newbr.maxkills, newbr.akills, newbr.minkills, newbr.stdkills = kills['akills__max'], kills['akills__avg'], kills['akills__min'], kills['akills__stddev']
                assists = players.aggregate(Max('aassists'), Avg('aassists'), Min('aassists'), StdDev('aassists'))
                newbr.maxassists, newbr.aassists, newbr.minassists, newbr.stdassists = assists['aassists__max'], assists['aassists__avg'], assists['aassists__min'], assists['aassists__stddev']
                deaths = players.aggregate(Max('adeaths'), Avg('adeaths'), Min('adeaths'), StdDev('adeaths'))
                newbr.maxdeaths, newbr.adeaths, newbr.mindeaths, newbr.stddeaths = deaths['adeaths__max'], deaths['adeaths__avg'], deaths['adeaths__min'], deaths['adeaths__stddev']
                wards = players.aggregate(Max('awards'), Avg('awards'), Min('awards'), StdDev('awards'))
                newbr.maxwards, newbr.awards, newbr.minwards, newbr.stdwards = wards['awards__max'], wards['awards__avg'], wards['awards__min'], wards['awards__stddev']
                cs = players.aggregate(Max('acs'), Avg('acs'), Min('acs'), StdDev('acs'))
                newbr.maxcs, newbr.acs, newbr.mincs, newbr.stdcs = cs['acs__max'], cs['acs__avg'], cs['acs__min'], cs['acs__stddev']
                denies = players.aggregate(Max('adenies'), Avg('adenies'), Min('adenies'), StdDev('adenies'))
                newbr.maxdenies, newbr.adenies, newbr.mindenies, newbr.stddenies = denies['adenies__max'], denies['adenies__avg'], denies['adenies__min'], denies['adenies__stddev']
                actionsmin = players.aggregate(Max('aactionsmin'), Avg('aactionsmin'), Min('aactionsmin'), StdDev('aactionsmin'))
                newbr.maxactionsmin, newbr.aactionsmin, newbr.minactionsmin, newbr.stdactionsmin = actionsmin['aactionsmin__max'], actionsmin['aactionsmin__avg'], actionsmin['aactionsmin__min'], actionsmin['aactionsmin__stddev']
                newbr.atime = players.aggregate(Avg('atime')).values()[0]
                axpmin = players.aggregate(Max('axpmin'), Avg('axpmin'), Min('axpmin'), StdDev('axpmin'))
                newbr.maxxpm, newbr.axpm, newbr.minxpm, newbr.stdxpm =axpmin['axpmin__max'],axpmin['axpmin__avg'],axpmin['axpmin__min'],axpmin['axpmin__stddev']
                newbr.save()
