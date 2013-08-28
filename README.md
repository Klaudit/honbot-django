honbot-django
=============
Hon Stats website written in django for the HoN api

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

###Querries
__Find most used heroes__  

    PlayerMatches.objects.filter(player_id=s['player_id'], mode=mode).values('hero').annotate(Count('hero')).order_by('-hero__count')

__Most total recent matches__

    PlayerMatches.objects.filter(date__range=[startdate, enddate]).values('player_id', 'nickname').annotate(Count('player_id')).order_by('-player_id__count')[:5]

__Find most assists__

    PlayerMatches.objects.filter(date__range=[startdate, enddate]).order_by('-assists')[:5]

More can be found in top.py