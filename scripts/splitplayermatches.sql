INSERT INTO `honbot_playermatchespublic` (
    honbot_playermatchespublic.player_id,
    honbot_playermatchespublic.match_id,
    honbot_playermatchespublic.deaths,
    honbot_playermatchespublic.win,
    honbot_playermatchespublic.apm,
    honbot_playermatchespublic.cs,
    honbot_playermatchespublic.buybacks,
    honbot_playermatchespublic.bloodlust,
    honbot_playermatchespublic.razed,
    honbot_playermatchespublic.triplekill,
    honbot_playermatchespublic.doublekill,
    honbot_playermatchespublic.quadkill,
    honbot_playermatchespublic.annihilation,
    honbot_playermatchespublic.smackdown,
    honbot_playermatchespublic.gold_spent,
    honbot_playermatchespublic.exp_denied,
    honbot_playermatchespublic.bgold,
    honbot_playermatchespublic.secsdead,
    honbot_playermatchespublic.gpm,
    honbot_playermatchespublic.bdmg,
    honbot_playermatchespublic.herodmg,
    honbot_playermatchespublic.xpm,
    honbot_playermatchespublic.kdr,
    honbot_playermatchespublic.mmr_change,
    honbot_playermatchespublic.goldlost2death,
    honbot_playermatchespublic.denies,
    honbot_playermatchespublic.hero,
    honbot_playermatchespublic.kills,
    honbot_playermatchespublic.consumables,
    honbot_playermatchespublic.assists,
    honbot_playermatchespublic.nickname,
    honbot_playermatchespublic.level,
    honbot_playermatchespublic.wards,
    honbot_playermatchespublic.team,
    honbot_playermatchespublic.position,
    honbot_playermatchespublic.items,
    honbot_playermatchespublic.mode,
    honbot_playermatchespublic.date)
SELECT honbot_playermatches.player_id,
    honbot_playermatches.match_id,
    honbot_playermatches.deaths,
    honbot_playermatches.win,
    honbot_playermatches.apm,
    honbot_playermatches.cs,
    honbot_playermatches.buybacks,
    honbot_playermatches.bloodlust,
    honbot_playermatches.razed,
    honbot_playermatches.triplekill,
    honbot_playermatches.doublekill,
    honbot_playermatches.quadkill,
    honbot_playermatches.annihilation,
    honbot_playermatches.smackdown,
    honbot_playermatches.gold_spent,
    honbot_playermatches.exp_denied,
    honbot_playermatches.bgold,
    honbot_playermatches.secsdead,
    honbot_playermatches.gpm,
    honbot_playermatches.bdmg,
    honbot_playermatches.herodmg,
    honbot_playermatches.xpm,
    honbot_playermatches.kdr,
    honbot_playermatches.mmr_change,
    honbot_playermatches.goldlost2death,
    honbot_playermatches.denies,
    honbot_playermatches.hero,
    honbot_playermatches.kills,
    honbot_playermatches.consumables,
    honbot_playermatches.assists,
    honbot_playermatches.nickname,
    honbot_playermatches.level,
    honbot_playermatches.wards,
    honbot_playermatches.team,
    honbot_playermatches.position,
    honbot_playermatches.items,
    honbot_playermatches.mode,
    honbot_playermatches.date
FROM honbot_playermatches
WHERE honbot_playermatches.mode = "acc";

INSERT INTO `honbot_playermatchescasual` (
    honbot_playermatchescasual.player_id,
    honbot_playermatchescasual.match_id,
    honbot_playermatchescasual.deaths,
    honbot_playermatchescasual.win,
    honbot_playermatchescasual.apm,
    honbot_playermatchescasual.cs,
    honbot_playermatchescasual.buybacks,
    honbot_playermatchescasual.bloodlust,
    honbot_playermatchescasual.razed,
    honbot_playermatchescasual.triplekill,
    honbot_playermatchescasual.doublekill,
    honbot_playermatchescasual.quadkill,
    honbot_playermatchescasual.annihilation,
    honbot_playermatchescasual.smackdown,
    honbot_playermatchescasual.gold_spent,
    honbot_playermatchescasual.exp_denied,
    honbot_playermatchescasual.bgold,
    honbot_playermatchescasual.secsdead,
    honbot_playermatchescasual.gpm,
    honbot_playermatchescasual.bdmg,
    honbot_playermatchescasual.herodmg,
    honbot_playermatchescasual.xpm,
    honbot_playermatchescasual.kdr,
    honbot_playermatchescasual.mmr_change,
    honbot_playermatchescasual.goldlost2death,
    honbot_playermatchescasual.denies,
    honbot_playermatchescasual.hero,
    honbot_playermatchescasual.kills,
    honbot_playermatchescasual.consumables,
    honbot_playermatchescasual.assists,
    honbot_playermatchescasual.nickname,
    honbot_playermatchescasual.level,
    honbot_playermatchescasual.wards,
    honbot_playermatchescasual.team,
    honbot_playermatchescasual.position,
    honbot_playermatchescasual.items,
    honbot_playermatchescasual.mode,
    honbot_playermatchescasual.date)
SELECT honbot_playermatches.player_id,
    honbot_playermatches.match_id,
    honbot_playermatches.deaths,
    honbot_playermatches.win,
    honbot_playermatches.apm,
    honbot_playermatches.cs,
    honbot_playermatches.buybacks,
    honbot_playermatches.bloodlust,
    honbot_playermatches.razed,
    honbot_playermatches.triplekill,
    honbot_playermatches.doublekill,
    honbot_playermatches.quadkill,
    honbot_playermatches.annihilation,
    honbot_playermatches.smackdown,
    honbot_playermatches.gold_spent,
    honbot_playermatches.exp_denied,
    honbot_playermatches.bgold,
    honbot_playermatches.secsdead,
    honbot_playermatches.gpm,
    honbot_playermatches.bdmg,
    honbot_playermatches.herodmg,
    honbot_playermatches.xpm,
    honbot_playermatches.kdr,
    honbot_playermatches.mmr_change,
    honbot_playermatches.goldlost2death,
    honbot_playermatches.denies,
    honbot_playermatches.hero,
    honbot_playermatches.kills,
    honbot_playermatches.consumables,
    honbot_playermatches.assists,
    honbot_playermatches.nickname,
    honbot_playermatches.level,
    honbot_playermatches.wards,
    honbot_playermatches.team,
    honbot_playermatches.position,
    honbot_playermatches.items,
    honbot_playermatches.mode,
    honbot_playermatches.date
FROM honbot_playermatches
WHERE honbot_playermatches.mode = "cs";

DELETE FROM honbot_playermatches
WHERE mode = "cs"
OR mode = "acc";