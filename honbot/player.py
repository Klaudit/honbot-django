import match
import api_call
import pretty
import datetime


def player_math(data, nick, mode):
    """
    This will get all the right information for the players view and store it in dict
    returns dict
    TSR calculation
    """
    stats = {}
    stats['id'] = int(data['account_id'])  # account id
    try:
        stats['nickname'] = str(data['nickname'])  # name
    except:
        stats['nickname'] = nick
    stats['matches'] = int(data[mode + '_games_played'])  # matches
    stats['wins'] = int(data[mode + '_wins'])  # wins
    stats['losses'] = int(data[mode + '_losses'])  # losses
    stats['mmr'] = int(float(data[mode + '_amm_team_rating']))  # mmr
    stats['kills'] = int(data[mode + '_herokills'])  # total kills
    stats['deaths'] = int(data[mode + '_deaths'])  # total deaths
    stats['assists'] = int(data[mode + '_heroassists'])  # total deaths
    stats['cc'] = int(data[mode + '_concedes'])  # total concedes
    stats['cccalls'] = int(data[mode + '_concedevotes'])  # total concede votes
    stats['left'] = int(data[mode + '_discos'])  # disconnects
    stats['kicked'] = int(data[mode + '_kicked'])  # kicked
    if stats['matches'] > 0:
        stats['hours'] = (int(data[mode + '_secs']) / 60) / 60  # hours played
        stats['acs'] = round(int(data[mode + '_teamcreepkills']) / float(stats['matches']), 1)  # average creep score
        if stats['deaths'] > 0 and stats['kills'] > 0:
            stats['kadr'] = round((float(stats['kills']) + float(stats['assists'])) / float(stats['deaths']), 2)  # k+A : d
            stats['kdr'] = round(float(stats['kills']) / float(stats['deaths']), 2)  # kill death ratio
        else:
            stats['kadr'] = 0
            stats['kdr'] = 0
        stats['winpercent'] = str(int(float(stats['wins']) / float(stats['wins'] + stats['losses']) * 100)) + '%'  # win percent
        stats['atime'] = int(data[mode + '_secs']) / stats['matches'] / 60  # average time
        stats['akills'] = round(float(stats['kills']) / stats['matches'], 1)  # average kills
        stats['adeaths'] = round(float(stats['deaths']) / stats['matches'], 1)  # average deaths
        stats['aassists'] = round(float(stats['assists']) / stats['matches'], 1)  # average assists
        stats['aconsumables'] = round(float(data[mode + '_consumables']) / stats['matches'], 1)  # average consumables
        stats['awards'] = round(float(data[mode + '_wards']) / stats['matches'], 1)  # average wards
        stats['acs'] = round(float(data[mode + '_teamcreepkills']) / stats['matches'], 1)  # average creep score
        stats['adenies'] = round(float(data[mode + '_denies']) / stats['matches'], 1)  # average creep score
        stats['axpmin'] = int(float(data[mode + '_exp']) / (float(data[mode + '_secs']) / 60))  # average xp / min
        stats['agoldmin'] = int(float(data[mode + '_gold']) / (float(data[mode + '_secs']) / 60))  # average gold / min
        stats['aactionsmin'] = int(float(data[mode + '_actions']) / (float(data[mode + '_secs']) / 60))  # average actions / min
        ### TSR CALC ###
        # How many Kills per Death you have, scaled by 1.1/1.15 KpD - 13% of your TSR
        # How many Assits per Death you have, scaled by 1.5/1.55 ApD - 24% of your TSR
        # The percent of games you win, scaled by 0.55 -18% of your TSR
        # How much Gold you earn per Minute played, scaled by 190/230 - 7% of your TSR
        # How much EXP you get per Minute played, scaled by 420/380
        # The rest of the steps
        if stats['matches'] > 5:
            stats['TSR'] = (float(stats['kills'])/(float(stats['deaths'])/1.15)*0.65) \
                + (float(stats['assists'])/(float(stats['deaths'])/1.55)*1.20) \
                + (((float(stats['wins'])/(float(stats['wins'])+float(stats['losses'])))/0.55)*0.9) \
                + ((float(stats['agoldmin'])/230)*0.35) \
                + (((float(stats['axpmin']))/380)*0.40) \
                + ((((((float(data[mode + '_denies'])/float(stats['matches']))/12))*0.70)
                + ((((float(data[mode + '_teamcreepkills'])/float(stats['matches']))/93))*0.50)
                + ((float(data[mode + '_wards'])/float(stats['matches']))/1.45*0.30))*(37.5/(float(data[mode + '_secs'])/float(stats['matches'])/60)))
            stats['TSR'] = round(stats['TSR'], 1)
            if stats['TSR'] > 10:
                stats['TSR'] = 10
        else:
            stats['TSR'] = None
    else:
        stats['TSR'] = 0.0
    return stats


def match_history_data(history, account_id):
    """
    this will take a player history and decide which matches need to be downloaded and pass
    them to a multimatch api call this will auto call the function to parse a single players match history
    """
    url = '/multi_match/all/matchids/'
    plus = False
    count = 0
    needed = []
    for m in history:
        if not match.checkfile(m[0]):
            if plus:
                url = url + '+' + str(m[0])
            else:
                url = url + str(m[0])
                plus = True
            count += 1
            needed.append(m)
    if count > 0:
        data = api_call.get_json(url)
        if data is not None:
            match.multimatch(data, needed)
            return get_player_from_matches(history, account_id)
        else:
            return get_player_from_matches(history, account_id)
    else:
        return get_player_from_matches(history, account_id)


def get_player_from_matches(history, account_id):
    """
    this takes a list of matches and returns that player's stats in that match
    """
    matches = []
    for m in history:
        temp = {}
        raw = match.load_match(m[0])
        if raw is not None and int(m[0]) > 60000000:
            try:
                temp = raw['players'][str(account_id)]
                temp['match_id'] = m[0]
                temp['date'] = pretty.date(datetime.datetime.strptime(raw['mdt'], '%Y-%m-%d %H:%M:%S'))
                matches.append(temp)
            except KeyError:
                pass
    return matches
