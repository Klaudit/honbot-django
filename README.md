honbot-django
=============
HonBot is a [Heroes of Newerth](http://www.heroesofnewerth.com/) (HoN) Statistics website written in [django](https://www.djangoproject.com/) for the [HoN API](http://api.heroesofnewerth.com/).

####Run a local copy of HonBot
Settings file requires a localsettings.py file with the following functions. It is required in main folder for production and honbot-django/ for dev.

* def is_debug(): returns true/false for production/dev
* def get_token(): returns string of private [hon api token](http://api.heroesofnewerth.com/)
* get_avatar_session() returns string of session for HoN forums to pull avatars

__make sure you install everything in requirements.txt__ no known version specific requirements

####honbot db
Handled by [South](http://south.aeracode.org/)
Initial Setup + use of django_cron

    python manage.py syncdb
    python manage.py migrate django_cron
Create Migrations for any db changes

    python manage.py schemamigration honbot --auto
Apply Changes

    python manage.py migrate honbot

####honbot server
Stop / start the fastcgi server. The third option is if using new relic's monitoring service

    pkill -f "runfcgi"
    python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python manage.py runfcgi host=127.0.0.1 port=8081 --settings=settings

####cron job
Using django_cron involves calling it every 5 minutes

    crontab -e
    */5 * * * * python /home/honbot/honbot.com/honbot-django/manage.py runcrons

####License
Copyright (c) 2013 Scott Cooper

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
