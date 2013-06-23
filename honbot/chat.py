import requests
from zipfile import ZipFile
import codecs
import os
from error import error
from time import strftime, gmtime
from django.template import Context, loader
from django.http import HttpResponse
from match import match
import json


directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'match')) + '/'


def chat(request, match_id):
    # download and parse logs
    if os.path.exists(directory + 'm' + str(match_id) + '.log'):
        logs = parse_chat_from_log(match_id)
    elif checkfile(match_id):
        url = get_download(match_id)
        if url is None:
            return error(request, "Match is older than 28 days or replay is unavailable.")
        url = url[:-9] + 'zip'
        # download file
        r = requests.get(url)
        if r.status_code == 404:
            return error(request, "Match is older than 28 days or replay is unavailable.")
        with open(directory + str(match_id)+".zip", "wb") as code:
            code.write(r.content)
        z = ZipFile(directory + str(match_id) + '.zip')
        z.extract(z.namelist()[0], directory)
        z.close()
        # cleanup zip
        os.remove(directory + str(match_id) + '.zip')
        logs = parse_chat_from_log(match_id)
    else:
        # this method is janky. hence all the 404 checks to back out quickly if things go south and is only used when they for some reason are going straight to chat?
        try:
            r = requests.get('http://replaydl.heroesofnewerth.com/replay_dl.php?file=&match_id=' + match_id, timeout=2)
            if r.status_code == 404:
                return error(request, "Match is older than 28 days or replay is unavailable.")
            url = r.url[:-9] + 'zip'
            r = requests.get(url)
            if r.status_code == 404:
                return error(request, "Match is older than 28 days or replay is unavailable.")
            with open(directory + str(match_id)+".zip", "wb") as code:
                code.write(r.content)
            z = ZipFile(directory + str(match_id) + '.zip')
            z.extract(z.namelist()[0], directory)
            z.close()
            # cleanup zip
            os.remove(directory + str(match_id) + '.zip')
            logs = parse_chat_from_log(match_id)
        except:
            return error(request, "Match is older than 28 days or replay is unavailable.")
    # deliver chat logs
    stats = match(match_id)
    names = {}
    heroes = {}
    for p in stats['players']:
        name = p['nickname']
        names[str(name)] = p['position']
        heroes[str(name)] = p['hero']
    for l in logs:
        name = l['name']
        l['player'] = names[name]
        l['hero'] = heroes[name]
    t = loader.get_template('chat.html')
    c = Context({'logs': logs, 'stats': stats, 'match_id': match_id})
    return HttpResponse(t.render(c))


def parse_chat_from_log(match_id):
    """
    damn codecs... open the file already and parse it
    """
    logfile = codecs.open(directory + 'm' + match_id + '.log', encoding='utf-16-le', mode='rb').readlines()
    logfile.pop(0)
    chatter = []
    players = []
    team = []
    # have log_parse access data
    for line in logfile:
        word = line.split()[0]
        if word == "PLAYER_CHAT":
            chatter.append(PLAYER_CHAT(line[12:]))
        elif word == "PLAYER_CONNECT":
            players.append(PLAYER_CONNECT(line))
        elif word == "PLAYER_TEAM_CHANGE":
            if line[-3] == '2':
                team.append('Hellborne')
            else:
                team.append('Legion')
    # validation on player # because of S2
    if chatter[-1]['player'] == 10:
        for player in chatter:
            player['player'] = int(player['player']) - 1
    # set player name and team name. change time from ms to datetime
    for chat in chatter:
        if chat['target'] == "team":
            chat['target'] = team[int(chat['player'])]
        else:
            chat['target'] = "All Chat"
        chat['name'] = players[int(chat['player'])]
        if chat['time'] is not None:
            if int(chat['time']) < 3599999:
                chat['time'] = strftime('%M:%S', gmtime(int(chat['time']) // 1000))
            else:
                chat['time'] = strftime('%H:%M:%S', gmtime(int(chat['time']) // 1000))
        else:
            chat['time'] = "Lobby"
    return chatter


def checkfile(match_id):
    """
    check if match has been parsed before returns bool
    """
    if os.path.exists(directory + str(match_id) + '.json'):
        return True
    else:
        return False


def get_download(match_id):
    with open(directory + str(match_id) + '.json', 'rb') as f:
        data = json.load(f)
    return data['replay_url']


def PLAYER_CHAT(line):
    """
    returns dict of chat line, two types of chat, one before start and after
    """
    chat = {}
    chat['msg'] = ''
    l = line.split()
    if l[0][0] == 'p':
        chat['player'] = l[0].split(':')[1]
        chat['target'] = l[1].split(':')[1][1:-1]
        chat['time'] = None
        for word in l[2:]:
            chat['msg'] = chat['msg'] + word + ' '
    else:
        chat['time'] = l[0].split(':')[1]
        chat['player'] = l[1].split(':')[1]
        chat['target'] = l[2].split(':')[1][1:-1]
        for word in l[3:]:
            chat['msg'] = chat['msg'] + word + ' '
    chat['msg'] = chat['msg'][5:-2]
    return chat


def PLAYER_CONNECT(line):
    """
    PLAYER_CONNECT player:0 name:"NAMENAMENAME" id:3252583 psr:1522.0000
    returns the player name as I don't believe I need any other data. Players do not connect in order
    """
    l = line.split()
    name = l[2].split(':')[1][1:-1]
    for l in name:
        if l == '[':
            name = name.split(']')[1]
        else:
            break
    return name
