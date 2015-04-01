![honbot](http://i.imgur.com/eniKwWN.jpg)
HonBot
=============
HonBot is a [Heroes of Newerth (HoN)](http://www.heroesofnewerth.com/) statistics website for the [HoN API](http://api.heroesofnewerth.com/).

Frontend and backend using [flask](http://flask.pocoo.org/) and [angularjs](https://angularjs.org/).

#/api backend  
```bash
make virtualenv
pip install requirements.txt
python manage.py runserver -d
```

#/client frontend
```bash
npm install gulp -g
npm install bower -g
npm install
bower install
gulp serve
```

####honbot server

gunicorn -b 127.0.0.1:5000 manage:app