honbot-django
=============
Hon Stats website written in django for the new api

<<<<<<< HEAD
#License
Copyright (c) 2013 Scott Cooper
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
=======
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

>>>>>>> honbot-2.0
