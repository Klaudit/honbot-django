honbot-django
=============
Hon Stats website written in django for the new api

honbot db
----------
Handled by [South](http://south.aeracode.org/)
Initial setup is the usual  

    python manage.py syncdb
Make model changes then run  

    python manage.py schemamigration honbot --auto
This generates a script in honbot/migrations  

    python manage.py migrate honbot 

####License
Included in license.md
