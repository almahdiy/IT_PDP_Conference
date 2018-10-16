from django.conf.urls import url
#from django.contrib import admin
from . import views # import a file called views from the same directory that I am in


urlpatterns = [
    #look for the url that matches the user's request
    url(r'^$', views.home, name="home"), #default homepage; they didn't request anything
    url(r'^agenda$', views.agenda, name="agenda"),
    url(r'^booths$', views.booths, name="booths"),
    url(r'^splash$', views.splash, name="splash"),
]