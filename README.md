![honbot](http://i.imgur.com/eniKwWN.jpg)
HonBot
=============
HonBot is a [Heroes of Newerth (HoN)](http://www.heroesofnewerth.com/) statistics website for the [HoN API](http://api.heroesofnewerth.com/).

Frontend and backend using [flask](http://flask.pocoo.org/) and [angularjs](https://angularjs.org/).

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

