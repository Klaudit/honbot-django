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

####License
Included in license.md

Current Issues
-------
Use Stripped down bootstrap with customizer  


Version 2.5 Planned Features
---------------------------
Tooltips
Social Share Modal
Find More fun querries
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
Top Matches of week  
    * load various player matches
    * Most kills
    * most deaths
    * longest
    * likes to ward
    * Most active


###Querries
__Find most used heroes__  

    PlayerMatches.objects.filter(player_id=s['player_id'], mode=mode).values('hero').annotate(Count('hero')).order_by('-hero__count')

