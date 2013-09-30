honbot-django
=============
HoN [Heroes of Newerth](http://www.heroesofnewerth.com/) Stats website written in django for the [HoN API](http://api.heroesofnewerth.com/).

###honbot localsettings.py
Settings file requires a localsettings.py file with the following functions. It is required in main folder for server deployment and honbot-django/ for local testing.

* def is_debug(): returns true/false
* def get_token(): returns string of private [hon api token](http://api.heroesofnewerth.com/)
* get_avatar_session() returns string of session for HoN forums to pull avatars 

__make sure you install everything in requirements.txt__

###honbot db
Handled by [South](http://south.aeracode.org/)  
Initial Setup  
Create Migrations for any db changes  
Apply Changes  

    python manage.py syncdb  
    python manage.py schemamigration honbot --auto  
    python manage.py migrate honbot   

###honbot server
Stop / start the fastcgi server

    pkill -f "runfcgi"
    python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings


####License
Included in license.md