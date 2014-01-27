from django.shortcuts import render_to_response, redirect
from datetime import datetime, timedelta
from error import error
from .models import Chat, Matches, PlayerMatches, PlayerMatchesPublic, PlayerMatchesCasual
from json import loads
from logparse import download, parse


def chat_view(request, match_id):
    match = Matches.objects.filter(match_id=match_id).values()
    if len(match) > 0:
        chat = Chat.objects.filter(match_id=match_id).values()
        if len(chat) > 0:
            match, chat = match[0], chat[0]
            match['date'] = datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
            chat['json'] = loads(chat['json'])
            PMObj = pmoselect(match['mode'])
            players = PMObj.objects.filter(match=match_id).order_by('position')[:1]
            return render_to_response('chat.html', {'chat': chat['json'], 'match': match, 'players': players})
        else:
            PMObj = pmoselect(match[0]['mode'])
            players = PMObj.objects.filter(match_id=match_id).order_by('position').values()
            if download(match_id, match[0]['replay_url']):
                if parse(match_id, players):
                    return chat_view(request, match_id)
                else:
                    return error(request, "The chat logs had trouble somewhere.<br> We all have bad days sometimes. Sorry")
            else:
                return error(request, "Downloading the chat log failed.<br> It could be too old (28 days) or too new. Try again soon.")
    else:
        return redirect('/match/' + match_id + '/')


def pmoselect(mode):
    if mode == "rnk":
        return PlayerMatches
    elif mode == "cs":
        return PlayerMatchesCasual
    elif mode == "acc":
        return PlayerMatchesPublic