from django.conf import settings
from django.http import Http404
from django.utils.timezone import now

from .api import get_json
from .avatar import avatar
from .models import Player
from .serializers import PlayerSerializer
from .utils import div

from django_rq import enqueue
from rest_framework import viewsets
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

debug = settings.DEBUG


class PlayerViewSet(viewsets.ViewSet):
    """
    Viewset for retreiving players
    """
    throttle_classes = (AnonRateThrottle,)

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset, fallback = get_or_update_player(pk, 800)
        serializer = PlayerSerializer(queryset)
        serializer.data['fallback'] = fallback
        return Response(serializer.data)


@api_view(['GET'])
@throttle_classes([])
def tooltip(request, *pid):
    players = Player.objects.filter(pk__in=list(pid))
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)


def get_or_update_player(nickname, age):
    player = Player.objects.filter(nickname=nickname.lower()).first()
    if player is None:
        new = get_player(Player(nickname=nickname))
        # TODO add error for none
        if new:
            enqueue(avatar, new)
            return (new, False)
        else:
            raise Http404
    nowutc = now()
    tdelta = nowutc - player.updated
    if tdelta.seconds + (tdelta.days * 86400) > age:
        updated = get_player(player)
        if updated:
            try:
                adelta = nowutc - player.avatar_updated
                if adelta.seconds + (adelta.days * 86400) > 604800:
                    enqueue(avatar, updated)
            except:
                enqueue(avatar, updated)
            return (updated, False)
        else:
            player.fallback = True
            return (player, True)
    return (player, False)


def get_player(p, raw=None):
    if raw is None:
        raw = get_json('/player_statistics/all/nickname/' + p.nickname)
    if raw:
        # player is banned or something
        if int(raw['account_id']) is 0:
            return None
        p.nickname = raw['nickname'].lower()
        p.player_id = int(raw['account_id'])
        p.rnk_games_played = int(raw['rnk_games_played'])
        p.rnk_wins = int(raw['rnk_wins'])
        p.rnk_losses = int(raw['rnk_losses'])
        p.rnk_concedes = int(raw['rnk_concedes'])
        p.rnk_concedevotes = int(raw['rnk_concedevotes'])
        p.rnk_buybacks = int(raw['rnk_buybacks'])
        p.rnk_discos = int(raw['rnk_discos'])
        p.rnk_kicked = int(raw['rnk_kicked'])
        p.rnk_mmr = float(raw['rnk_amm_team_rating'])
        p.rnk_herokills = int(raw['rnk_herokills'])
        p.rnk_herodmg = int(raw['rnk_herodmg'])
        p.rnk_heroexp = int(raw['rnk_heroexp'])
        p.rnk_herokillsgold = int(raw['rnk_herokillsgold'])
        p.rnk_heroassists = int(raw['rnk_heroassists'])
        p.rnk_deaths = int(raw['rnk_deaths'])
        p.rnk_goldlost2death = int(raw['rnk_goldlost2death'])
        p.rnk_secs_dead = int(raw['rnk_secs_dead'])
        p.rnk_teamcreepkills = int(raw['rnk_teamcreepkills'])
        p.rnk_teamcreepdmg = int(raw['rnk_teamcreepdmg'])
        p.rnk_teamcreepexp = int(raw['rnk_teamcreepexp'])
        p.rnk_teamcreepgold = int(raw['rnk_teamcreepgold'])
        p.rnk_neutralcreepkills = int(raw['rnk_neutralcreepkills'])
        p.rnk_neutralcreepdmg = int(raw['rnk_neutralcreepdmg'])
        p.rnk_neutralcreepexp = int(raw['rnk_teamcreepexp'])
        p.rnk_neutralcreepgold = int(raw['rnk_neutralcreepgold'])
        p.rnk_bdmg = int(raw['rnk_bdmg'])
        p.rnk_razed = int(raw['rnk_razed'])
        p.rnk_bgold = int(raw['rnk_bgold'])
        p.rnk_denies = int(raw['rnk_denies'])
        p.rnk_exp_denied = int(raw['rnk_exp_denied'])
        p.rnk_gold = int(raw['rnk_gold'])
        p.rnk_gold_spent = int(raw['rnk_gold_spent'])
        p.rnk_exp = int(raw['rnk_exp'])
        p.rnk_actions = int(raw['rnk_actions'])
        p.rnk_secs = int(raw['rnk_secs'])
        p.rnk_consumables = int(raw['rnk_consumables'])
        p.rnk_wards = int(raw['rnk_wards'])
        p.rnk_level = int(raw['rnk_level'])
        p.rnk_level_exp = int(raw['rnk_level_exp'])
        p.rnk_min_exp = int(raw['rnk_min_exp'])
        p.rnk_max_exp = int(raw['rnk_max_exp'])
        p.rnk_time_earning_exp = int(raw['rnk_time_earning_exp'])
        p.rnk_bloodlust = int(raw['rnk_bloodlust'])
        p.rnk_doublekill = int(raw['rnk_doublekill'])
        p.rnk_triplekill = int(raw['rnk_triplekill'])
        p.rnk_quadkill = int(raw['rnk_quadkill'])
        p.rnk_annihilation = int(raw['rnk_annihilation'])
        p.rnk_ks3 = int(raw['rnk_ks3'])
        p.rnk_ks4 = int(raw['rnk_ks4'])
        p.rnk_ks5 = int(raw['rnk_ks5'])
        p.rnk_ks6 = int(raw['rnk_ks6'])
        p.rnk_ks7 = int(raw['rnk_ks7'])
        p.rnk_ks8 = int(raw['rnk_ks8'])
        p.rnk_ks9 = int(raw['rnk_ks9'])
        p.rnk_ks10 = int(raw['rnk_ks10'])
        p.rnk_ks15 = int(raw['rnk_ks15'])
        p.rnk_smackdown = int(raw['rnk_smackdown'])
        p.rnk_humiliation = int(raw['rnk_humiliation'])
        p.rnk_nemesis = int(raw['rnk_nemesis'])
        p.rnk_retribution = int(raw['rnk_retribution'])
        p.rnk_avg_kills = div(p.rnk_herokills, p.rnk_games_played)
        p.rnk_avg_deaths = div(p.rnk_deaths, p.rnk_games_played)
        p.rnk_avg_assists = div(p.rnk_heroassists, p.rnk_games_played)
        p.rnk_avg_creeps = div((p.rnk_neutralcreepkills + p.rnk_teamcreepkills), p.rnk_games_played)
        p.rnk_avg_denies = div(p.rnk_denies, p.rnk_games_played)
        rnk_minutes = div(p.rnk_secs, 60)
        p.rnk_avg_xpm = div(p.rnk_exp, rnk_minutes)
        p.rnk_avg_apm = div(p.rnk_actions, rnk_minutes)
        p.rnk_avg_gpm = div(p.rnk_gold, rnk_minutes)
        p.rnk_avg_consumables = div(p.rnk_consumables, p.rnk_games_played)
        p.rnk_avg_time = div(rnk_minutes, p.rnk_games_played)
        p.rnk_winpercent = div(p.rnk_wins, p.rnk_games_played)
        p.rnk_kdr = div(p.rnk_herokills, p.rnk_deaths)
        p.rnk_avg_wards = div(p.rnk_wards, p.rnk_games_played)
        p.rnk_kadr = div((p.rnk_herokills + p.rnk_heroassists), p.rnk_deaths)
        try:
            p.rnk_tsr = ((p.rnk_herokills / p.rnk_deaths / 1.15) * 0.65) + ((p.rnk_heroassists / p.rnk_deaths / 1.55) * 1.20) + (((p.rnk_wins / (p.rnk_wins + p.rnk_losses)) / 0.55) * 0.9) + (((p.rnk_gold / p.rnk_secs * 60) / 230) * 0.35) + ((((p.rnk_exp / p.rnk_time_earning_exp * 60) / 380)) * 0.40) + (
                        (((((p.rnk_denies / p.rnk_games_played) / 12)) * 0.70) + ((((p.rnk_teamcreepkills / p.rnk_games_played) / 93)) * 0.50) + ((p.rnk_wards / p.rnk_games_played) / 1.45 * 0.30)) * (37.5 / (p.rnk_secs / p.rnk_games_played / 60)))
        except:
            p.rnk_tsr = 0
        p.cs_games_played = int(raw['cs_games_played'])
        p.cs_wins = int(raw['cs_wins'])
        p.cs_losses = int(raw['cs_losses'])
        p.cs_concedes = int(raw['cs_concedes'])
        p.cs_concedevotes = int(raw['cs_concedevotes'])
        p.cs_buybacks = int(raw['cs_buybacks'])
        p.cs_discos = int(raw['cs_discos'])
        p.cs_kicked = int(raw['cs_kicked'])
        p.cs_mmr = float(raw['cs_amm_team_rating'])
        p.cs_herokills = int(raw['cs_herokills'])
        p.cs_herodmg = int(raw['cs_herodmg'])
        p.cs_heroexp = int(raw['cs_heroexp'])
        p.cs_herokillsgold = int(raw['cs_herokillsgold'])
        p.cs_heroassists = int(raw['cs_heroassists'])
        p.cs_deaths = int(raw['cs_deaths'])
        p.cs_goldlost2death = int(raw['cs_goldlost2death'])
        p.cs_secs_dead = int(raw['cs_secs_dead'])
        p.cs_teamcreepkills = int(raw['cs_teamcreepkills'])
        p.cs_teamcreepdmg = int(raw['cs_teamcreepdmg'])
        p.cs_teamcreepexp = int(raw['cs_teamcreepexp'])
        p.cs_teamcreepgold = int(raw['cs_teamcreepgold'])
        p.cs_neutralcreepkills = int(raw['cs_neutralcreepkills'])
        p.cs_neutralcreepdmg = int(raw['cs_neutralcreepdmg'])
        p.cs_neutralcreepexp = int(raw['cs_teamcreepexp'])
        p.cs_neutralcreepgold = int(raw['cs_neutralcreepgold'])
        p.cs_bdmg = int(raw['cs_bdmg'])
        p.cs_bdmgexp = int(raw['cs_bdmgexp'])
        p.cs_razed = int(raw['cs_razed'])
        p.cs_bgold = int(raw['cs_bgold'])
        p.cs_denies = int(raw['cs_denies'])
        p.cs_exp_denied = int(raw['cs_exp_denied'])
        p.cs_gold = int(raw['cs_gold'])
        p.cs_gold_spent = int(raw['cs_gold_spent'])
        p.cs_exp = int(raw['cs_exp'])
        p.cs_actions = int(raw['cs_actions'])
        p.cs_secs = int(raw['cs_secs'])
        p.cs_consumables = int(raw['cs_consumables'])
        p.cs_wards = int(raw['cs_wards'])
        p.cs_level = int(raw['cs_level'])
        p.cs_level_exp = int(raw['cs_level_exp'])
        p.cs_min_exp = int(raw['cs_min_exp'])
        p.cs_max_exp = int(raw['cs_max_exp'])
        p.cs_time_earning_exp = int(raw['cs_time_earning_exp'])
        p.cs_bloodlust = int(raw['cs_bloodlust'])
        p.cs_doublekill = int(raw['cs_doublekill'])
        p.cs_triplekill = int(raw['cs_triplekill'])
        p.cs_quadkill = int(raw['cs_quadkill'])
        p.cs_annihilation = int(raw['cs_annihilation'])
        p.cs_ks3 = int(raw['cs_ks3'])
        p.cs_ks4 = int(raw['cs_ks4'])
        p.cs_ks5 = int(raw['cs_ks5'])
        p.cs_ks6 = int(raw['cs_ks6'])
        p.cs_ks7 = int(raw['cs_ks7'])
        p.cs_ks8 = int(raw['cs_ks8'])
        p.cs_ks9 = int(raw['cs_ks9'])
        p.cs_ks10 = int(raw['cs_ks10'])
        p.cs_ks15 = int(raw['cs_ks15'])
        p.cs_smackdown = int(raw['cs_smackdown'])
        p.cs_humiliation = int(raw['cs_humiliation'])
        p.cs_nemesis = int(raw['cs_nemesis'])
        p.cs_retribution = int(raw['cs_retribution'])
        p.cs_avg_kills = div(p.cs_herokills, p.cs_games_played)
        p.cs_avg_deaths = div(p.cs_deaths, p.cs_games_played)
        p.cs_avg_assists = div(p.cs_heroassists, p.cs_games_played)
        p.cs_avg_creeps = div((p.cs_neutralcreepkills + p.cs_teamcreepkills), p.cs_games_played)
        p.cs_avg_denies = div(p.cs_denies, p.cs_games_played)
        cs_minutes = div(p.cs_secs, 60)
        p.cs_avg_xpm = div(p.cs_exp, cs_minutes)
        p.cs_avg_apm = div(p.cs_actions, cs_minutes)
        p.cs_avg_gpm = div(p.cs_gold, cs_minutes)
        p.cs_avg_consumables = div(p.cs_consumables, p.cs_games_played)
        p.cs_avg_time = div(cs_minutes, p.cs_games_played)
        p.cs_winpercent = div(p.cs_wins, p.cs_games_played)
        p.cs_kdr = div(p.cs_herokills, p.cs_deaths)
        p.cs_avg_wards = div(p.cs_wards, p.cs_games_played)
        p.cs_kadr = div((p.cs_herokills + p.cs_heroassists), p.cs_deaths)
        try:
            p.cs_tsr = ((p.cs_herokills / p.cs_deaths / 1.15) * 0.65) + ((p.cs_heroassists / p.cs_deaths / 1.55) * 1.20) + (((p.cs_wins / (p.cs_wins + p.cs_losses)) / 0.55) * 0.9) + (((p.cs_gold / p.cs_secs * 60) / 230) * 0.35) + ((((p.cs_exp / p.cs_time_earning_exp * 60) / 380)) * 0.40) + (
                        (((((p.cs_denies / p.cs_games_played) / 12)) * 0.70) + ((((p.cs_teamcreepkills / p.cs_games_played) / 93)) * 0.50) + ((p.cs_wards / p.cs_games_played) / 1.45 * 0.30)) * (37.5 / (p.cs_secs / p.cs_games_played / 60)))
        except:
            p.cs_tsr = 0
        p.acc_games_played = int(raw['acc_games_played'])
        p.acc_wins = int(raw['acc_wins'])
        p.acc_losses = int(raw['acc_losses'])
        p.acc_concedes = int(raw['acc_concedes'])
        p.acc_concedevotes = int(raw['acc_concedevotes'])
        p.acc_buybacks = int(raw['acc_buybacks'])
        p.acc_discos = int(raw['acc_discos'])
        p.acc_kicked = int(raw['acc_kicked'])
        p.acc_mmr = float(raw['acc_pub_skill'])
        p.acc_herokills = int(raw['acc_herokills'])
        p.acc_herodmg = int(raw['acc_herodmg'])
        p.acc_heroexp = int(raw['acc_heroexp'])
        p.acc_herokillsgold = int(raw['acc_herokillsgold'])
        p.acc_heroassists = int(raw['acc_heroassists'])
        p.acc_deaths = int(raw['acc_deaths'])
        p.acc_goldlost2death = int(raw['acc_goldlost2death'])
        p.acc_secs_dead = int(raw['acc_secs_dead'])
        p.acc_teamcreepkills = int(raw['acc_teamcreepkills'])
        p.acc_teamcreepdmg = int(raw['acc_teamcreepdmg'])
        p.acc_teamcreepexp = int(raw['acc_teamcreepexp'])
        p.acc_teamcreepgold = int(raw['acc_teamcreepgold'])
        p.acc_neutralcreepkills = int(raw['acc_neutralcreepkills'])
        p.acc_neutralcreepdmg = int(raw['acc_neutralcreepdmg'])
        p.acc_neutralcreepexp = int(raw['acc_teamcreepexp'])
        p.acc_neutralcreepgold = int(raw['acc_neutralcreepgold'])
        p.acc_bdmg = int(raw['acc_bdmg'])
        p.acc_bdmgexp = int(raw['acc_bdmgexp'])
        p.acc_razed = int(raw['acc_razed'])
        p.acc_bgold = int(raw['acc_bgold'])
        p.acc_denies = int(raw['acc_denies'])
        p.acc_exp_denied = int(raw['acc_exp_denied'])
        p.acc_gold = int(raw['acc_gold'])
        p.acc_gold_spent = int(raw['acc_gold_spent'])
        p.acc_exp = int(raw['acc_exp'])
        p.acc_actions = int(raw['acc_actions'])
        p.acc_secs = int(raw['acc_secs'])
        p.acc_consumables = int(raw['acc_consumables'])
        p.acc_wards = int(raw['acc_wards'])
        p.acc_time_earning_exp = int(raw['acc_time_earning_exp'])
        p.acc_bloodlust = int(raw['acc_bloodlust'])
        p.acc_doublekill = int(raw['acc_doublekill'])
        p.acc_triplekill = int(raw['acc_triplekill'])
        p.acc_quadkill = int(raw['acc_quadkill'])
        p.acc_annihilation = int(raw['acc_annihilation'])
        p.acc_ks3 = int(raw['acc_ks3'])
        p.acc_ks4 = int(raw['acc_ks4'])
        p.acc_ks5 = int(raw['acc_ks5'])
        p.acc_ks6 = int(raw['acc_ks6'])
        p.acc_ks7 = int(raw['acc_ks7'])
        p.acc_ks8 = int(raw['acc_ks8'])
        p.acc_ks9 = int(raw['acc_ks9'])
        p.acc_ks10 = int(raw['acc_ks10'])
        p.acc_ks15 = int(raw['acc_ks15'])
        p.acc_smackdown = int(raw['acc_smackdown'])
        p.acc_humiliation = int(raw['acc_humiliation'])
        p.acc_nemesis = int(raw['acc_nemesis'])
        p.acc_retribution = int(raw['acc_retribution'])
        p.acc_avg_kills = div(p.acc_herokills, p.acc_games_played)
        p.acc_avg_deaths = div(p.acc_deaths, p.acc_games_played)
        p.acc_avg_assists = div(p.acc_heroassists, p.acc_games_played)
        p.acc_avg_creeps = div((p.acc_neutralcreepkills + p.acc_teamcreepkills), p.acc_games_played)
        p.acc_avg_denies = div(p.acc_denies, p.acc_games_played)
        acc_minutes = div(p.acc_secs, 60)
        p.acc_avg_xpm = div(p.acc_exp, acc_minutes)
        p.acc_avg_apm = div(p.acc_actions, acc_minutes)
        p.acc_avg_gpm = div(p.acc_gold, acc_minutes)
        p.acc_avg_consumables = div(p.acc_consumables, p.acc_games_played)
        p.acc_avg_time = div(acc_minutes, p.acc_games_played)
        p.acc_winpercent = div(p.acc_wins, p.acc_games_played)
        p.acc_kdr = div(p.acc_herokills, p.acc_deaths)
        p.acc_avg_wards = div(p.acc_wards, p.acc_games_played)
        p.acc_kadr = div((p.acc_herokills + p.acc_heroassists), p.acc_deaths)
        try:
            p.acc_tsr = ((p.acc_herokills / p.acc_deaths / 1.15) * 0.65) + ((p.acc_heroassists / p.acc_deaths / 1.55) * 1.20) + (((p.acc_wins / (p.acc_wins + p.acc_losses)) / 0.55) * 0.9) + (((p.acc_gold / p.acc_secs * 60) / 230) * 0.35) + ((((p.acc_exp / p.acc_time_earning_exp * 60) / 380)) * 0.40) + (
                        (((((p.acc_denies / p.acc_games_played) / 12)) * 0.70) + ((((p.acc_teamcreepkills / p.acc_games_played) / 93)) * 0.50) + ((p.acc_wards / p.acc_games_played) / 1.45 * 0.30)) * (37.5 / (p.acc_secs / p.acc_games_played / 60)))
        except:
            p.acc_tsr = 0
        p.save()
        return p
    else:
        return None
