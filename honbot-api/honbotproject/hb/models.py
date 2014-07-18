from django.db import models


class Player(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    nickname = models.CharField(max_length=16, null=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)
    avatar = models.URLField(max_length=100, default="")
    avatar_updated = models.DateTimeField(null=True)
    rnk_games_played = models.PositiveIntegerField(null=True)
    rnk_wins = models.PositiveIntegerField(null=True)
    rnk_losses = models.PositiveIntegerField(null=True)
    rnk_concedes = models.PositiveIntegerField(null=True)
    rnk_concedevotes = models.PositiveIntegerField(null=True)
    rnk_buybacks = models.PositiveIntegerField(null=True)
    rnk_discos = models.PositiveIntegerField(null=True)
    rnk_kicked = models.PositiveIntegerField(null=True)
    rnk_mmr = models.FloatField(null=True)
    rnk_herokills = models.PositiveIntegerField(null=True)
    rnk_herodmg = models.PositiveIntegerField(null=True)
    rnk_heroexp = models.PositiveIntegerField(null=True)
    rnk_herokillsgold = models.PositiveIntegerField(null=True)
    rnk_heroassists = models.PositiveIntegerField(null=True)
    rnk_deaths = models.PositiveIntegerField(null=True)
    rnk_goldlost2death = models.PositiveIntegerField(null=True)
    rnk_secs_dead = models.PositiveIntegerField(null=True)
    rnk_teamcreepkills = models.PositiveIntegerField(null=True)
    rnk_teamcreepdmg = models.PositiveIntegerField(null=True)
    rnk_teamcreepexp = models.PositiveIntegerField(null=True)
    rnk_teamcreepgold = models.PositiveIntegerField(null=True)
    rnk_neutralcreepkills = models.PositiveIntegerField(null=True)
    rnk_neutralcreepdmg = models.PositiveIntegerField(null=True)
    rnk_neutralcreepexp = models.PositiveIntegerField(null=True)
    rnk_neutralcreepgold = models.PositiveIntegerField(null=True)
    rnk_bdmg = models.PositiveIntegerField(null=True)
    rnk_razed = models.PositiveIntegerField(null=True)
    rnk_bgold = models.PositiveIntegerField(null=True)
    rnk_denies = models.PositiveIntegerField(null=True)
    rnk_exp_denied = models.PositiveIntegerField(null=True)
    rnk_gold = models.PositiveIntegerField(null=True)
    rnk_gold_spent = models.PositiveIntegerField(null=True)
    rnk_exp = models.PositiveIntegerField(null=True)
    rnk_actions = models.PositiveIntegerField(null=True)
    rnk_secs = models.PositiveIntegerField(null=True)
    rnk_consumables = models.PositiveIntegerField(null=True)
    rnk_wards = models.PositiveIntegerField(null=True)
    rnk_level = models.PositiveIntegerField(null=True)
    rnk_level_exp = models.PositiveIntegerField(null=True)
    rnk_min_exp = models.PositiveIntegerField(null=True)
    rnk_max_exp = models.PositiveIntegerField(null=True)
    rnk_time_earning_exp = models.PositiveIntegerField(null=True)
    rnk_bloodlust = models.PositiveIntegerField(null=True)
    rnk_doublekill = models.PositiveIntegerField(null=True)
    rnk_triplekill = models.PositiveIntegerField(null=True)
    rnk_quadkill = models.PositiveIntegerField(null=True)
    rnk_annihilation = models.PositiveIntegerField(null=True)
    rnk_ks3 = models.PositiveIntegerField(null=True)
    rnk_ks4 = models.PositiveIntegerField(null=True)
    rnk_ks5 = models.PositiveIntegerField(null=True)
    rnk_ks6 = models.PositiveIntegerField(null=True)
    rnk_ks7 = models.PositiveIntegerField(null=True)
    rnk_ks8 = models.PositiveIntegerField(null=True)
    rnk_ks9 = models.PositiveIntegerField(null=True)
    rnk_ks10 = models.PositiveIntegerField(null=True)
    rnk_ks15 = models.PositiveIntegerField(null=True)
    rnk_smackdown = models.PositiveIntegerField(null=True)
    rnk_humiliation = models.PositiveIntegerField(null=True)
    rnk_nemesis = models.PositiveIntegerField(null=True)
    rnk_retribution = models.PositiveIntegerField(null=True)
    rnk_avg_kills = models.FloatField(null=True)
    rnk_avg_deaths = models.FloatField(null=True)
    rnk_avg_assists = models.FloatField(null=True)
    rnk_avg_creeps = models.FloatField(null=True)
    rnk_avg_denies = models.FloatField(null=True)
    rnk_avg_xpm = models.FloatField(null=True)
    rnk_avg_apm = models.FloatField(null=True)
    rnk_avg_gpm = models.FloatField(null=True)
    rnk_avg_wards = models.FloatField(null=True)
    rnk_avg_consumables = models.FloatField(null=True)
    rnk_avg_time = models.FloatField(null=True)
    rnk_kdr = models.FloatField(null=True)
    rnk_kadr = models.FloatField(null=True)
    rnk_winpercent = models.FloatField(null=True)
    rnk_tsr = models.FloatField(null=True)
    cs_games_played = models.PositiveIntegerField(null=True)
    cs_wins = models.PositiveIntegerField(null=True)
    cs_losses = models.PositiveIntegerField(null=True)
    cs_concedes = models.PositiveIntegerField(null=True)
    cs_concedevotes = models.PositiveIntegerField(null=True)
    cs_buybacks = models.PositiveIntegerField(null=True)
    cs_discos = models.PositiveIntegerField(null=True)
    cs_kicked = models.PositiveIntegerField(null=True)
    cs_mmr = models.FloatField(null=True)
    cs_herokills = models.PositiveIntegerField(null=True)
    cs_herodmg = models.PositiveIntegerField(null=True)
    cs_heroexp = models.PositiveIntegerField(null=True)
    cs_herokillsgold = models.PositiveIntegerField(null=True)
    cs_heroassists = models.PositiveIntegerField(null=True)
    cs_deaths = models.PositiveIntegerField(null=True)
    cs_secs_dead = models.PositiveIntegerField(null=True)
    cs_teamcreepkills = models.PositiveIntegerField(null=True)
    cs_teamcreepdmg = models.PositiveIntegerField(null=True)
    cs_teamcreepexp = models.PositiveIntegerField(null=True)
    cs_teamcreepgold = models.PositiveIntegerField(null=True)
    cs_neutralcreepkills = models.PositiveIntegerField(null=True)
    cs_neutralcreepdmg = models.PositiveIntegerField(null=True)
    cs_neutralcreepexp = models.PositiveIntegerField(null=True)
    cs_neutralcreepgold = models.PositiveIntegerField(null=True)
    cs_bdmg = models.PositiveIntegerField(null=True)
    cs_bdmgexp = models.PositiveIntegerField(null=True)
    cs_razed = models.PositiveIntegerField(null=True)
    cs_bgold = models.PositiveIntegerField(null=True)
    cs_denies = models.PositiveIntegerField(null=True)
    cs_exp_denied = models.PositiveIntegerField(null=True)
    cs_gold = models.PositiveIntegerField(null=True)
    cs_gold_spent = models.PositiveIntegerField(null=True)
    cs_exp = models.PositiveIntegerField(null=True)
    cs_actions = models.PositiveIntegerField(null=True)
    cs_secs = models.PositiveIntegerField(null=True)
    cs_consumables = models.PositiveIntegerField(null=True)
    cs_wards = models.PositiveIntegerField(null=True)
    cs_level = models.PositiveIntegerField(null=True)
    cs_level_exp = models.PositiveIntegerField(null=True)
    cs_min_exp = models.PositiveIntegerField(null=True)
    cs_max_exp = models.PositiveIntegerField(null=True)
    cs_time_earning_exp = models.PositiveIntegerField(null=True)
    cs_bloodlust = models.PositiveIntegerField(null=True)
    cs_doublekill = models.PositiveIntegerField(null=True)
    cs_triplekill = models.PositiveIntegerField(null=True)
    cs_quadkill = models.PositiveIntegerField(null=True)
    cs_annihilation = models.PositiveIntegerField(null=True)
    cs_ks3 = models.PositiveIntegerField(null=True)
    cs_ks4 = models.PositiveIntegerField(null=True)
    cs_ks5 = models.PositiveIntegerField(null=True)
    cs_ks6 = models.PositiveIntegerField(null=True)
    cs_ks3 = models.PositiveIntegerField(null=True)
    cs_ks7 = models.PositiveIntegerField(null=True)
    cs_ks8 = models.PositiveIntegerField(null=True)
    cs_ks9 = models.PositiveIntegerField(null=True)
    cs_ks10 = models.PositiveIntegerField(null=True)
    cs_ks15 = models.PositiveIntegerField(null=True)
    cs_smackdown = models.PositiveIntegerField(null=True)
    cs_humiliation = models.PositiveIntegerField(null=True)
    cs_nemesis = models.PositiveIntegerField(null=True)
    cs_retribution = models.PositiveIntegerField(null=True)
    cs_avg_kills = models.FloatField(null=True)
    cs_avg_deaths = models.FloatField(null=True)
    cs_avg_assists = models.FloatField(null=True)
    cs_avg_creeps = models.FloatField(null=True)
    cs_avg_denies = models.FloatField(null=True)
    cs_avg_xpm = models.FloatField(null=True)
    cs_avg_apm = models.FloatField(null=True)
    cs_avg_gpm = models.FloatField(null=True)
    cs_avg_consumables = models.FloatField(null=True)
    cs_avg_time = models.FloatField(null=True)
    cs_avg_wards = models.FloatField(null=True)
    cs_kdr = models.FloatField(null=True)
    cs_kadr = models.FloatField(null=True)
    cs_winpercent = models.FloatField(null=True)
    cs_tsr = models.FloatField(null=True)
    acc_games_played = models.PositiveIntegerField(null=True)
    acc_wins = models.PositiveIntegerField(null=True)
    acc_losses = models.PositiveIntegerField(null=True)
    acc_concedes = models.PositiveIntegerField(null=True)
    acc_concedevotes = models.PositiveIntegerField(null=True)
    acc_buybacks = models.PositiveIntegerField(null=True)
    acc_discos = models.PositiveIntegerField(null=True)
    acc_kicked = models.PositiveIntegerField(null=True)
    acc_mmr = models.FloatField(null=True)
    acc_herokills = models.PositiveIntegerField(null=True)
    acc_herodmg = models.PositiveIntegerField(null=True)
    acc_heroexp = models.PositiveIntegerField(null=True)
    acc_herokillsgold = models.PositiveIntegerField(null=True)
    acc_heroassists = models.PositiveIntegerField(null=True)
    acc_deaths = models.PositiveIntegerField(null=True)
    acc_goldlost2death = models.PositiveIntegerField(null=True)
    acc_secs_dead = models.PositiveIntegerField(null=True)
    acc_teamcreepkills = models.PositiveIntegerField(null=True)
    acc_teamcreepdmg = models.PositiveIntegerField(null=True)
    acc_teamcreepexp = models.PositiveIntegerField(null=True)
    acc_teamcreepgold = models.PositiveIntegerField(null=True)
    acc_neutralcreepkills = models.PositiveIntegerField(null=True)
    acc_neutralcreepdmg = models.PositiveIntegerField(null=True)
    acc_neutralcreepexp = models.PositiveIntegerField(null=True)
    acc_neutralcreepgold = models.PositiveIntegerField(null=True)
    acc_bdmg = models.PositiveIntegerField(null=True)
    acc_bdmgexp = models.PositiveIntegerField(null=True)
    acc_razed = models.PositiveIntegerField(null=True)
    acc_bgold = models.PositiveIntegerField(null=True)
    acc_denies = models.PositiveIntegerField(null=True)
    acc_exp_denied = models.PositiveIntegerField(null=True)
    acc_gold = models.PositiveIntegerField(null=True)
    acc_gold_spent = models.PositiveIntegerField(null=True)
    acc_exp = models.PositiveIntegerField(null=True)
    acc_actions = models.PositiveIntegerField(null=True)
    acc_secs = models.PositiveIntegerField(null=True)
    acc_consumables = models.PositiveIntegerField(null=True)
    acc_wards = models.PositiveIntegerField(null=True)
    acc_time_earning_exp = models.PositiveIntegerField(null=True)
    acc_bloodlust = models.PositiveIntegerField(null=True)
    acc_doublekill = models.PositiveIntegerField(null=True)
    acc_triplekill = models.PositiveIntegerField(null=True)
    acc_quadkill = models.PositiveIntegerField(null=True)
    acc_annihilation = models.PositiveIntegerField(null=True)
    acc_ks3 = models.PositiveIntegerField(null=True)
    acc_ks4 = models.PositiveIntegerField(null=True)
    acc_ks5 = models.PositiveIntegerField(null=True)
    acc_ks6 = models.PositiveIntegerField(null=True)
    acc_ks7 = models.PositiveIntegerField(null=True)
    acc_ks8 = models.PositiveIntegerField(null=True)
    acc_ks9 = models.PositiveIntegerField(null=True)
    acc_ks10 = models.PositiveIntegerField(null=True)
    acc_ks15 = models.PositiveIntegerField(null=True)
    acc_smackdown = models.PositiveIntegerField(null=True)
    acc_humiliation = models.PositiveIntegerField(null=True)
    acc_nemesis = models.PositiveIntegerField(null=True)
    acc_retribution = models.PositiveIntegerField(null=True)
    acc_avg_kills = models.FloatField(null=True)
    acc_avg_deaths = models.FloatField(null=True)
    acc_avg_assists = models.FloatField(null=True)
    acc_avg_creeps = models.FloatField(null=True)
    acc_avg_denies = models.FloatField(null=True)
    acc_avg_xpm = models.FloatField(null=True)
    acc_avg_apm = models.FloatField(null=True)
    acc_avg_gpm = models.FloatField(null=True)
    acc_avg_consumables = models.FloatField(null=True)
    acc_avg_time = models.FloatField(null=True)
    acc_avg_wards = models.FloatField(null=True)
    acc_kdr = models.FloatField(null=True)
    acc_kadr = models.FloatField(null=True)
    acc_winpercent = models.FloatField(null=True)
    acc_tsr = models.FloatField(null=True)

    class meta:
        get_latest_by = "updated"
        ordering = ['updated']


class PlayerHistory(Player):
    rnk_history = models.TextField(default="")
    cs_history = models.TextField(default="")
    acc_history = models.TextField(default="")
    history_updated = models.DateTimeField(null=True, blank=True)
