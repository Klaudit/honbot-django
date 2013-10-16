honbot-django
=============
HoN [Heroes of Newerth](http://www.heroesofnewerth.com/) Stats website written in django for the [HoN API](http://api.heroesofnewerth.com/).

###Run a local copy of HonBot
Settings file requires a localsettings.py file with the following functions. It is required in main folder for production and honbot-django/ for dev.

* def is_debug(): returns true/false
* def get_token(): returns string of private [hon api token](http://api.heroesofnewerth.com/)
* get_avatar_session() returns string of session for HoN forums to pull avatars 

__make sure you install everything in requirements.txt__ no known version specific requirements

###honbot db
Handled by [South](http://south.aeracode.org/)  
Initial Setup 

    python manage.py syncdb
Create Migrations for any db changes  

    python manage.py schemamigration honbot --auto  
Apply Changes  

    python manage.py migrate honbot   

###honbot server
Stop / start the fastcgi server. The third line is if using new relic's monitoring service

    pkill -f "runfcgi"
    python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings


####License
Copyright (c) 2013 Scott Cooper

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.