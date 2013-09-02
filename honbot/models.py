from django.db import models


class Matches(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    date = models.DateTimeField()
    replay_url = models.URLField(max_length=120, default="")
    realtime = models.CharField(max_length=10, default="")
    mode = models.CharField(max_length=10, default="")
    map_used = models.CharField(max_length=30, default="")
    major = models.PositiveSmallIntegerField(default=0)
    minor = models.PositiveSmallIntegerField(default=0)
    revision = models.PositiveSmallIntegerField(default=0)
    build = models.PositiveSmallIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, default=0)

    class Meta:
        ordering = ['-match_id']


class PlayerMatches(models.Model):
    player_id = models.PositiveIntegerField(default=0, db_index=True)
    match = models.ForeignKey(Matches)
    deaths = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    apm = models.FloatField(default=0)
    cs = models.PositiveSmallIntegerField(default=0)
    buybacks = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveSmallIntegerField(default=0)
    razed = models.PositiveSmallIntegerField(default=0)
    triplekill = models.PositiveSmallIntegerField(default=0)
    doublekill = models.PositiveSmallIntegerField(default=0)
    quadkill = models.PositiveSmallIntegerField(default=0)
    annihilation = models.PositiveSmallIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    gold_spent = models.PositiveIntegerField(default=0)
    exp_denied = models.PositiveIntegerField(default=0)
    bgold = models.PositiveIntegerField(default=0)
    secsdead = models.PositiveIntegerField(default=0)
    gpm = models.FloatField(default=0)
    bdmg = models.PositiveSmallIntegerField(default=0)
    herodmg = models.PositiveIntegerField(default=0)
    xpm = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    mmr_change = models.FloatField(default=0)
    goldlost2death = models.PositiveSmallIntegerField(default=0)
    denies = models.PositiveSmallIntegerField(default=0)
    hero = models.PositiveSmallIntegerField(default=0)
    kills = models.PositiveSmallIntegerField(default=0)
    consumables = models.PositiveSmallIntegerField(default=0)
    assists = models.PositiveSmallIntegerField(default=0)
    nickname = models.TextField(max_length=25, default="")
    level = models.PositiveSmallIntegerField(default=0)
    wards = models.PositiveSmallIntegerField(default=0)
    team = models.PositiveSmallIntegerField(default=0)
    position = models.PositiveSmallIntegerField(default=0)
    items = models.CharField(max_length=50, default="")
    mode = models.CharField(max_length=10, default="")
    date = models.DateTimeField(db_index=True, blank=True, null=True)


class PlayerIcon(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    avatar = models.URLField(max_length=300, default="")
    updated = models.DateTimeField(auto_now=True, default=0)


class PlayerHistory(models.Model):
    player_id = models.PositiveIntegerField(default=0)
    history = models.TextField(default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    mode = models.CharField(max_length=10, default="")


class PlayerStats(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    razed = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveSmallIntegerField(default=0)
    ks10 = models.PositiveSmallIntegerField(default=0)
    ks15 = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)


class PlayerStatsCasual(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    razed = models.PositiveIntegerField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveSmallIntegerField(default=0)
    ks10 = models.PositiveSmallIntegerField(default=0)
    ks15 = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)


class PlayerStatsPublic(models.Model):
    player_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True)
    nickname = models.CharField(max_length=30, default="")
    updated = models.DateTimeField(auto_now=True, default=0)
    cccalls = models.PositiveIntegerField(default=0)
    deaths = models.PositiveIntegerField(default=0)
    cc = models.PositiveIntegerField(default=0)
    assists = models.FloatField(default=0)
    TSR = models.FloatField(default=0, null=True)
    razed = models.PositiveIntegerField(default=0)
    kdr = models.FloatField(default=0)
    adenies = models.FloatField(default=0)
    aconsumables = models.FloatField(default=0)
    kills = models.PositiveIntegerField(default=0)
    winpercent = models.CharField(max_length=4, default="")
    kadr = models.FloatField(default=0)
    akills = models.FloatField(default=0)
    kicked = models.PositiveIntegerField(default=0)
    agoldmin = models.PositiveIntegerField(default=0)
    matches = models.PositiveIntegerField(default=0)
    mmr = models.PositiveIntegerField(default=0)
    hours = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    awards = models.PositiveIntegerField(default=0)
    atime = models.PositiveIntegerField(default=0)
    aactionsmin = models.PositiveIntegerField(default=0)
    axpmin = models.PositiveIntegerField(default=0)
    adeaths = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    left = models.PositiveIntegerField(default=0)
    aassists = models.FloatField(default=0)
    ks3 = models.PositiveIntegerField(default=0)
    ks4 = models.PositiveIntegerField(default=0)
    ks5 = models.PositiveIntegerField(default=0)
    ks6 = models.PositiveIntegerField(default=0)
    ks7 = models.PositiveIntegerField(default=0)
    ks8 = models.PositiveIntegerField(default=0)
    ks9 = models.PositiveSmallIntegerField(default=0)
    ks10 = models.PositiveSmallIntegerField(default=0)
    ks15 = models.PositiveSmallIntegerField(default=0)
    bloodlust = models.PositiveIntegerField(default=0)
    doublekill = models.PositiveIntegerField(default=0)
    triplekill = models.PositiveIntegerField(default=0)
    quadkill = models.PositiveIntegerField(default=0)
    annihilation = models.PositiveIntegerField(default=0)
    smackdown = models.PositiveIntegerField(default=0)
    humiliation = models.PositiveIntegerField(default=0)
    nemesis = models.PositiveIntegerField(default=0)
    retribution = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    level_exp = models.PositiveIntegerField(default=0)
    min_exp = models.PositiveIntegerField(default=0)
    max_exp = models.PositiveIntegerField(default=0)


class PlayerHeroStats(models.Model):
    nickname = models.CharField(max_length=30, default="")
    data = models.TextField(default="")
    hero_id = models.SmallIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, default=0)
    mode = models.CharField(max_length=10, default="rnk")

class Chat(models.Model):
    match_id = models.PositiveIntegerField(primary_key=True, null=False, unique=True, db_index=True)
    json = models.TextField(default="")

class Builds(models.Model):
    match_id = models.PositiveIntegerField(null=False, default=1, db_index=True)
    hero = models.PositiveSmallIntegerField(default=0, db_index=True)
    json = models.TextField(default="")
    nickname = models.CharField(max_length=30, default="")
    position = models.PositiveSmallIntegerField(default=0)
    win = models.BooleanField(default=False)
    mmr = models.PositiveIntegerField(default=0)
    lvl1 = models.PositiveSmallIntegerField(default=0)
    lvl2 = models.PositiveSmallIntegerField(default=0)
    lvl3 = models.PositiveSmallIntegerField(default=0)
    lvl4 = models.PositiveSmallIntegerField(default=0)
    lvl5 = models.PositiveSmallIntegerField(default=0)
    lvl6 = models.PositiveSmallIntegerField(default=0)
    lvl7 = models.PositiveSmallIntegerField(default=0)
    lvl8 = models.PositiveSmallIntegerField(default=0)
    lvl9 = models.PositiveSmallIntegerField(default=0)
    lvl10 = models.PositiveSmallIntegerField(default=0)
    lvl11 = models.PositiveSmallIntegerField(default=0)
    lvl12 = models.PositiveSmallIntegerField(default=0)
    lvl13 = models.PositiveSmallIntegerField(default=0)
    lvl14 = models.PositiveSmallIntegerField(default=0)
    lvl15 = models.PositiveSmallIntegerField(default=0)
    lvl16 = models.PositiveSmallIntegerField(default=0)
    lvl17 = models.PositiveSmallIntegerField(default=0)
    lvl18 = models.PositiveSmallIntegerField(default=0)
    lvl19 = models.PositiveSmallIntegerField(default=0)
    lvl20 = models.PositiveSmallIntegerField(default=0)
    lvl21 = models.PositiveSmallIntegerField(default=0)
    lvl22 = models.PositiveSmallIntegerField(default=0)
    lvl23 = models.PositiveSmallIntegerField(default=0)
    lvl24 = models.PositiveSmallIntegerField(default=0)
    lvl25 = models.PositiveSmallIntegerField(default=0)

class PlayerCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)

class MatchCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)

class PlayerMatchCount(models.Model):
    date = models.DateField(primary_key=True, auto_now=True, unique=True, db_index=True)
    count = models.PositiveIntegerField(default=0)