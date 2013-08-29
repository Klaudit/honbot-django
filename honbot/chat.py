import codecs
import os
from time import strftime, gmtime
#new requirements
import logparse
from honbot.models import Chat, Matches
from django.shortcuts import redirect
import datetime
from error import error
from django.shortcuts import render_to_response
import json

directory = str(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'match')) + '/'


def chat(request, match_id):
    match = Matches.objects.filter(match_id=match_id)
    if match.exists():
        chat = Chat.objects.filter(match_id=match_id)
        if chat.exists():
            match = match.values()
            match['date'] = datetime.datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=1)
            # this needs to be a template
            if match['mode'] == "rnk":
                match['mode'] = "Ranked"
            elif match['mode'] == "cs":
                match['mode'] = "Casual"
            elif match['mode'] == "acc":
                match['mode'] = "Public"
            return render_to_response('chat.html', {'chat': chat, 'match':match})
        else:
            if logparse.download(match_id, match[0].replay_url):
                logparse.parse(match_id)
            else:
                return error(request, "Match replay failed to download. It could be too old (28 days), too new, or S2 hates you")
    else:
        return redirect('/match/' + match_id + '/')

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
