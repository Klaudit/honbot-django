from django.shortcuts import render_to_response, redirect
from datetime import datetime, timedelta
from error import error
from honbot.models import Chat, Matches, PlayerMatches
from json import loads
from logparse import download, parse

def chat_view(request, match_id):
    match = Matches.objects.filter(match_id=match_id).values()
    if match.exists():
        chat = Chat.objects.filter(match_id=match_id).values('json')
        if chat.exists():
            chat = chat[0]
            match = match[0]
            match['date'] = datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - timedelta(hours=1)
            chat['json'] = loads(chat['json'])
            players = PlayerMatches.objects.filter(match=match_id).order_by('position')
            return render_to_response('chat.html', {'chat': chat['json'], 'match':match, 'players':players})
        else:
            if download(match_id, match[0]['replay_url']):
                if parse(match_id):
                    return chat_view(request, match_id)
                else:
                    return error(request, "The chat logs had trouble somewhere.<br> We all have bad days sometimes. Sorry")
            else:
                return error(request, "Downloading the chat log failed.<br> It could be too old (28 days) or too new. Try again soon.")
    else:
        return redirect('/match/' + match_id + '/')