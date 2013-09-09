import logparse
from honbot.models import Chat, Matches
from django.shortcuts import redirect
import datetime
from error import error
from django.shortcuts import render_to_response
import json

def chat_view(request, match_id):
    match = Matches.objects.filter(match_id=match_id).values()
    if match.exists():
        chat = Chat.objects.filter(match_id=match_id).values('json')
        if chat.exists():
            chat = chat[0]
            match = match[0]
            match['date'] = datetime.datetime.strptime(str(match['date']), '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=1)
            # this needs to be a template
            if match['mode'] == "rnk":
                match['mode'] = "Ranked"
            elif match['mode'] == "cs":
                match['mode'] = "Casual"
            elif match['mode'] == "acc":
                match['mode'] = "Public"
            chat['json'] = json.loads(chat['json'])
            return render_to_response('chat.html', {'chat': chat['json'], 'match':match})
        else:
            if logparse.download(match_id, match[0]['replay_url']):
                if logparse.parse(match_id):
                    return chat_view(request, match_id)
                else:
                    return error(request, "The chat logs had trouble somewhere. We all have bad days sometimes.")
            else:
                return error(request, "Match replay failed to download. It could be too old (28 days), too new, or S2 hates you")
    else:
        return redirect('/match/' + match_id + '/')