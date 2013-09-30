honbot-django
=============
HoN [Heroes of Newerth](http://www.heroesofnewerth.com/) Stats website written in django for the HoN api

###requirements
    Django==1.5.4
    MySQL-python==1.2.4
    PIL==1.1.7
    Pillow==2.1.0
    South==0.8.2
    beautifulsoup4==4.3.1
    django-datatables-view==1.6
    django-debug-toolbar==0.9.4
    django-pretty-times==0.1.0
    numpy==1.7.1
    requests==1.2.3

###honbot localsettings.py
Settings file requires a localsettings.py file with the following functions. It is required in main folder for server deployment and honbot-django/ for local testing.

* def is_debug(): returns true/false
* def get_token(): returns string of private [hon api token](http://api.heroesofnewerth.com/)
* get_avatar_session() returns string of session for HoN forums to pull avatars 

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