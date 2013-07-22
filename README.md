honbot-django
=============
Hon Stats website written in django for the new api

###honbot db
Handled by [South](http://south.aeracode.org/)
Initial setup is the usual  

    python manage.py syncdb

Make model changes then run  

    python manage.py schemamigration honbot --auto

This generates a script in honbot/migrations  

    python manage.py migrate honbot 

End the fastcgi processes  

    pkill -f "runfcgi"

Start the server up again  

    python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings

####License
Included in license.md

Version 2.5 Planned Features
---------------------------
Tooltips
Social Share Modal
Move recent matches to ajax and json
Hero Stats/pages
Item Pages
Recent Matches
Possible Typeahead on home page  
Check out s2r2 and see if it can work
switch to numpy
Have a queue of players to be updated and pull down matches when idle
Compare side by side players stats for heroes/matches
Try to fall back when servers not available, show error
Share tab
* Advanced stats should be stored somehow  
    * Chat can be json.dumped
    * builds can be arrays or stored in individual columns
Fix match view for 3vs3 add if !player to all graphs to prevent spawn of non existant player


###Querries
__Find most used heroes__  

    PlayerMatches.objects.filter(player_id=s['player_id'], mode=mode).values('hero').annotate(Count('hero')).order_by('-hero__count')

__Most total recent matches__

    PlayerMatches.objects.filter(date__range=[startdate, enddate]).values('player_id', 'nickname').annotate(Count('player_id')).order_by('-player_id__count')[:5]

__Find most assists__

    PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-assists')[:5]

More can be found in top.py


