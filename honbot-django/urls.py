# project wide urls
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

# import your urls from each app here, as needed
import honbot.urls

urlpatterns = patterns('',
                       url('', include(honbot.urls)),
                       )
