honbot-django
=============
Hon Stats website written in django for the new api

###honbot db
Handled by [South](http://south.aeracode.org/)
Initial setup is the usual  

    python manage.py syncdb

Make model changes then run  

    python manage.py schemamigration honbot --auto

This generates a script in honbot/migrations  

    python manage.py migrate honbot 

####License
Included in license.md

Current Issues
-------
Player recent matches are loading entire match rather than PlayerMatch from DB
    * Issue with this is matches that aren't loaded into db
    * move to ajax and json
Advanced stats should be stored somehow  
* Chat can be json.dumped
* builds can be arrays or stored in individual columns
* Move away from small icons and use large icons only (not sure if good idea)
Items not being stored for matches  
__Banners need to be available, fuck casual and public players__  
    * Ajax modal
Top Matches of week  
    * load various player matches
    * Most kills
    * most deaths
    * longest
    * likes to ward
    * Most active
Figure out facebook likes  
Use Stripped down bootstrap with customizer  
Possible Typeahead on home page  
Consider Using Pronto
Possibly use clickjacking

Version 2.5 Planned Features
---------------------------
Tooltips
Hero Stats/pages
Item Pages
