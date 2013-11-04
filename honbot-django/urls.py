# project wide urls
from django.conf.urls import patterns, url, include
from django.contrib import admin

# import your urls from each app here, as needed
import honbot.urls

urlpatterns = patterns('',
                       url('', include(honbot.urls)),
                       )
