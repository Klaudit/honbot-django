![honbot](http://i.imgur.com/eniKwWN.jpg)
HonBot
=============
HonBot is a [Heroes of Newerth (HoN)](http://www.heroesofnewerth.com/) statistics website for the [HoN API](http://api.heroesofnewerth.com/).

While the website was formerly a django project. It is now split between frontend and backend using [flask](http://flask.pocoo.org/) and [angularjs](https://angularjs.org/).

####API Setup
Create a virtualenv  
Install the requirements with pip  
Add the following to the bottom of your virtualenv's script. This setup is for two different IP addresses and tokens.
``` bash
API_TOKEN="APITOKENHERE"
DEBUG="true"
PHPSESSID="session cookies from forums.heroesofnewerth.com for authentication"
SENTRY_DSN="used for error reporting getsentry.com for info"
export SENTRY_DSN
export DEBUG
export PHPSESSID
export API_TOKEN
```

####honbot server
these are for my reference more than anything

    ps ax|grep gunicorn
    kill -HUP masterpid
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-python manage.py run_gunicorn --workers=10 -b 127.0.0.1:8000 --timeout 30

