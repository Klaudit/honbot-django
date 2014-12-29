from app import db
from sqlalchemy.dialects.postgresql import JSONB


class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('PlayerMatch', backref='match', lazy='joined')
    version = db.Column(db.String(10), index=True)
    map_used = db.Column(db.String(20), index=True)
    length = db.Column(db.Integer)
    date = db.Column(db.DateTime())
    # mode 1 Ranked 2 casual 3 public
    mode = db.Column(db.Integer, index=True)


class PlayerMatch(db.Model):
    __tablename__ = 'playermatch'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer)
    nickname = db.Column(db.String(20))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    deaths = db.Column(db.Integer)
    win = db.Column(db.Boolean)
    apm = db.Column(db.Float)
    cs = db.Column(db.Integer)
    concedevotes = db.Column(db.Integer)
    kdr = db.Column(db.Float)
    denies = db.Column(db.Integer)
    discos = db.Column(db.Integer)
    kicked = db.Column(db.Integer)
    gpm = db.Column(db.Float)
    bdmg = db.Column(db.Integer)
    herodmg = db.Column(db.Integer)
    xpm = db.Column(db.Float)
    secs_dead = db.Column(db.Integer)
    clan_id = db.Column(db.Integer)
    goldlost2death = db.Column(db.Integer)
    hero_id = db.Column(db.Integer)
    concedes = db.Column(db.Integer)
    mmr_change = db.Column(db.Float)
    kills = db.Column(db.Integer)
    consumables = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    buybacks = db.Column(db.Integer)
    level = db.Column(db.Integer)
    items = db.Column(JSONB)
    wards = db.Column(db.Integer)
    team = db.Column(db.Integer)
    position = db.Column(db.Integer)
    exp_denied = db.Column(db.Integer)


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), index=True)
    avatar = db.Column(db.Text())
    avatar_updated = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    history_updated = db.Column(db.DateTime())
    rnk_history = db.Column(JSONB)
    acc_history = db.Column(JSONB)
    cs_history = db.Column(JSONB)
    acc_actions = db.Column(db.Integer)
    acc_annihilation = db.Column(db.Integer)
    acc_avg_apm = db.Column(db.Float)
    acc_avg_assists = db.Column(db.Float)
    acc_avg_consumables = db.Column(db.Float)
    acc_avg_creeps = db.Column(db.Float)
    acc_avg_deaths = db.Column(db.Float)
    acc_avg_denies = db.Column(db.Float)
    acc_avg_gpm = db.Column(db.Float)
    acc_avg_kills = db.Column(db.Float)
    acc_avg_time = db.Column(db.Float)
    acc_avg_wards = db.Column(db.Float)
    acc_avg_xpm = db.Column(db.Float)
    acc_bdmg = db.Column(db.Integer)
    acc_bdmgexp = db.Column(db.Integer)
    acc_bgold = db.Column(db.Integer)
    acc_bloodlust = db.Column(db.Integer)
    acc_buybacks = db.Column(db.Integer)
    acc_concedes = db.Column(db.Integer)
    acc_concedevotes = db.Column(db.Integer)
    acc_consumables = db.Column(db.Integer)
    acc_deaths = db.Column(db.Integer)
    acc_denies = db.Column(db.Integer)
    acc_discos = db.Column(db.Integer)
    acc_doublekill = db.Column(db.Integer)
    acc_exp = db.Column(db.Integer)
    acc_exp_denied = db.Column(db.Integer)
    acc_games_played = db.Column(db.Integer)
    acc_gold = db.Column(db.Integer)
    acc_gold_spent = db.Column(db.Integer)
    acc_goldlost2death = db.Column(db.Integer)
    acc_heroassists = db.Column(db.Integer)
    acc_herodmg = db.Column(db.Integer)
    acc_heroexp = db.Column(db.Integer)
    acc_herokills = db.Column(db.Integer)
    acc_herokillsgold = db.Column(db.Integer)
    acc_humiliation = db.Column(db.Integer)
    acc_kadr = db.Column(db.Integer)
    acc_kdr = db.Column(db.Float)
    acc_kicked = db.Column(db.Integer)
    acc_ks10 = db.Column(db.Integer)
    acc_ks15 = db.Column(db.Integer)
    acc_ks3 = db.Column(db.Integer)
    acc_ks4 = db.Column(db.Integer)
    acc_ks5 = db.Column(db.Integer)
    acc_ks6 = db.Column(db.Integer)
    acc_ks7 = db.Column(db.Integer)
    acc_ks8 = db.Column(db.Integer)
    acc_ks9 = db.Column(db.Integer)
    acc_losses = db.Column(db.Integer)
    acc_mmr = db.Column(db.Float)
    acc_nemesis = db.Column(db.Integer)
    acc_neutralcreepdmg = db.Column(db.Integer)
    acc_neutralcreepgold = db.Column(db.Integer)
    acc_neutralcreepkills = db.Column(db.Integer)
    acc_quadkill = db.Column(db.Integer)
    acc_razed = db.Column(db.Integer)
    acc_retribution = db.Column(db.Integer)
    acc_secs = db.Column(db.Integer)
    acc_secs_dead = db.Column(db.Integer)
    acc_smackdown = db.Column(db.Integer)
    acc_teamcreepdmg = db.Column(db.Integer)
    acc_teamcreepexp = db.Column(db.Integer)
    acc_teamcreepgold = db.Column(db.Integer)
    acc_teamcreepkills = db.Column(db.Integer)
    acc_time_earning_exp = db.Column(db.Integer)
    acc_triplekill = db.Column(db.Integer)
    acc_tsr = db.Column(db.Float)
    acc_wards = db.Column(db.Integer)
    acc_winpercent = db.Column(db.Float)
    acc_wins = db.Column(db.Integer)
    cs_actions = db.Column(db.Integer)
    cs_annihilation = db.Column(db.Integer)
    cs_avg_apm = db.Column(db.Float)
    cs_avg_assists = db.Column(db.Float)
    cs_avg_consumables = db.Column(db.Float)
    cs_avg_creeps = db.Column(db.Float)
    cs_avg_deaths = db.Column(db.Float)
    cs_avg_denies = db.Column(db.Float)
    cs_avg_gpm = db.Column(db.Float)
    cs_avg_kills = db.Column(db.Float)
    cs_avg_time = db.Column(db.Float)
    cs_avg_wards = db.Column(db.Float)
    cs_avg_xpm = db.Column(db.Float)
    cs_bdmg = db.Column(db.Integer)
    cs_bdmgexp = db.Column(db.Integer)
    cs_bgold = db.Column(db.Integer)
    cs_bloodlust = db.Column(db.Integer)
    cs_buybacks = db.Column(db.Integer)
    cs_concedes = db.Column(db.Integer)
    cs_concedevotes = db.Column(db.Integer)
    cs_consumables = db.Column(db.Integer)
    cs_deaths = db.Column(db.Integer)
    cs_denies = db.Column(db.Integer)
    cs_discos = db.Column(db.Integer)
    cs_doublekill = db.Column(db.Integer)
    cs_exp = db.Column(db.Integer)
    cs_exp_denied = db.Column(db.Integer)
    cs_games_played = db.Column(db.Integer)
    cs_gold = db.Column(db.Integer)
    cs_gold_spent = db.Column(db.Integer)
    cs_goldlost2death = db.Column(db.Integer)
    cs_heroassists = db.Column(db.Integer)
    cs_herodmg = db.Column(db.Integer)
    cs_heroexp = db.Column(db.Integer)
    cs_herokills = db.Column(db.Integer)
    cs_herokillsgold = db.Column(db.Integer)
    cs_humiliation = db.Column(db.Integer)
    cs_kadr = db.Column(db.Integer)
    cs_kdr = db.Column(db.Float)
    cs_kicked = db.Column(db.Integer)
    cs_ks10 = db.Column(db.Integer)
    cs_ks15 = db.Column(db.Integer)
    cs_ks3 = db.Column(db.Integer)
    cs_ks4 = db.Column(db.Integer)
    cs_ks5 = db.Column(db.Integer)
    cs_ks6 = db.Column(db.Integer)
    cs_ks7 = db.Column(db.Integer)
    cs_ks8 = db.Column(db.Integer)
    cs_ks9 = db.Column(db.Integer)
    cs_level = db.Column(db.Integer)
    cs_level_exp = db.Column(db.Integer)
    cs_losses = db.Column(db.Integer)
    cs_mmr = db.Column(db.Float)
    cs_nemesis = db.Column(db.Integer)
    cs_neutralcreepdmg = db.Column(db.Integer)
    cs_neutralcreepgold = db.Column(db.Integer)
    cs_neutralcreepkills = db.Column(db.Integer)
    cs_quadkill = db.Column(db.Integer)
    cs_razed = db.Column(db.Integer)
    cs_retribution = db.Column(db.Integer)
    cs_secs = db.Column(db.Integer)
    cs_secs_dead = db.Column(db.Integer)
    cs_smackdown = db.Column(db.Integer)
    cs_teamcreepdmg = db.Column(db.Integer)
    cs_teamcreepexp = db.Column(db.Integer)
    cs_teamcreepgold = db.Column(db.Integer)
    cs_teamcreepkills = db.Column(db.Integer)
    cs_time_earning_exp = db.Column(db.Integer)
    cs_triplekill = db.Column(db.Integer)
    cs_tsr = db.Column(db.Float)
    cs_wards = db.Column(db.Integer)
    cs_winpercent = db.Column(db.Float)
    cs_wins = db.Column(db.Integer)
    rnk_actions = db.Column(db.Integer)
    rnk_annihilation = db.Column(db.Integer)
    rnk_avg_apm = db.Column(db.Float)
    rnk_avg_assists = db.Column(db.Float)
    rnk_avg_consumables = db.Column(db.Float)
    rnk_avg_creeps = db.Column(db.Float)
    rnk_avg_deaths = db.Column(db.Float)
    rnk_avg_denies = db.Column(db.Float)
    rnk_avg_gpm = db.Column(db.Float)
    rnk_avg_kills = db.Column(db.Float)
    rnk_avg_time = db.Column(db.Float)
    rnk_avg_wards = db.Column(db.Float)
    rnk_avg_xpm = db.Column(db.Float)
    rnk_bdmg = db.Column(db.Integer)
    rnk_bgold = db.Column(db.Integer)
    rnk_bloodlust = db.Column(db.Integer)
    rnk_buybacks = db.Column(db.Integer)
    rnk_concedes = db.Column(db.Integer)
    rnk_concedevotes = db.Column(db.Integer)
    rnk_consumables = db.Column(db.Integer)
    rnk_deaths = db.Column(db.Integer)
    rnk_denies = db.Column(db.Integer)
    rnk_discos = db.Column(db.Integer)
    rnk_doublekill = db.Column(db.Integer)
    rnk_exp = db.Column(db.Integer)
    rnk_exp_denied = db.Column(db.Integer)
    rnk_games_played = db.Column(db.Integer)
    rnk_gold = db.Column(db.Integer)
    rnk_gold_spent = db.Column(db.Integer)
    rnk_goldlost2death = db.Column(db.Integer)
    rnk_heroassists = db.Column(db.Integer)
    rnk_herodmg = db.Column(db.Integer)
    rnk_heroexp = db.Column(db.Integer)
    rnk_herokills = db.Column(db.Integer)
    rnk_herokillsgold = db.Column(db.Integer)
    rnk_humiliation = db.Column(db.Integer)
    rnk_kadr = db.Column(db.Integer)
    rnk_kdr = db.Column(db.Float)
    rnk_kicked = db.Column(db.Integer)
    rnk_ks10 = db.Column(db.Integer)
    rnk_ks15 = db.Column(db.Integer)
    rnk_ks3 = db.Column(db.Integer)
    rnk_ks4 = db.Column(db.Integer)
    rnk_ks5 = db.Column(db.Integer)
    rnk_ks6 = db.Column(db.Integer)
    rnk_ks7 = db.Column(db.Integer)
    rnk_ks8 = db.Column(db.Integer)
    rnk_ks9 = db.Column(db.Integer)
    rnk_level = db.Column(db.Integer)
    rnk_level_exp = db.Column(db.Integer)
    rnk_losses = db.Column(db.Integer)
    rnk_mmr = db.Column(db.Float)
    rnk_nemesis = db.Column(db.Integer)
    rnk_neutralcreepdmg = db.Column(db.Integer)
    rnk_neutralcreepgold = db.Column(db.Integer)
    rnk_neutralcreepkills = db.Column(db.Integer)
    rnk_quadkill = db.Column(db.Integer)
    rnk_razed = db.Column(db.Integer)
    rnk_retribution = db.Column(db.Integer)
    rnk_secs = db.Column(db.Integer)
    rnk_secs_dead = db.Column(db.Integer)
    rnk_smackdown = db.Column(db.Integer)
    rnk_teamcreepdmg = db.Column(db.Integer)
    rnk_teamcreepexp = db.Column(db.Integer)
    rnk_teamcreepgold = db.Column(db.Integer)
    rnk_teamcreepkills = db.Column(db.Integer)
    rnk_time_earning_exp = db.Column(db.Integer)
    rnk_triplekill = db.Column(db.Integer)
    rnk_tsr = db.Column(db.Float)
    rnk_wards = db.Column(db.Integer)
    rnk_winpercent = db.Column(db.Float)
    rnk_wins = db.Column(db.Integer)
