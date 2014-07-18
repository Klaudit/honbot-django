![honbot-django](http://i.imgur.com/eniKwWN.jpg)
HonBot-Django
=============
HonBot is a [Heroes of Newerth](http://www.heroesofnewerth.com/) (HoN) Statistics website written in [django](https://www.djangoproject.com/) for the [HoN API](http://api.heroesofnewerth.com/).

####Run a local copy of HonBot
Create a virtualenv  
Install the requirements with pip  
Add the following to the bottom of your virtualenv's script. This setup is for two different IP addresses and tokens.
``` bash
ADDRESS=$(dig +short myip.opendns.com @resolver1.opendns.com)
if [ $ADDRESS = 'my address here' ]
then
  echo "vpn"
  API_TOKEN="APITOKENHERE"
fi
if [ $ADDRESS = 'my other address here' ]
then
  echo "work"
  API_TOKEN="APITOKENHERE"
fi
DEBUG="true"
PHPSESSID='cookies on forums.heroesofnewerth.com for authentication'
export DEBUG
export PHPSESSID
export API_TOKEN
```
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
these are for my reference more than anything

    ps ax|grep gunicorn
    kill -HUP masterpid
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python manage.py run_gunicorn --workers=10 -b 127.0.0.1:8000 --timeout 30

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
