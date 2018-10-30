from django.conf.urls import url
#from django.contrib import admin
from . import views # import a file called views from the same directory that I am in


urlpatterns = [
    #look for the url that matches the user's request
    url(r'^$', views.home, name="home"), #default homepage; they didn't request anything
    url(r'^agenda$', views.agenda, name="agenda"),
    url(r'^booths$', views.booths, name="booths"),
    #url(r'^splash$', views.splash, name="splash"),
    url(r'^icebreaker$', views.icebreaker, name="icebreaker"),
    url(r'^metaverse$', views.metaverse, name="metaverse"),
    url(r'^team_programming$', views.team_programming, name="team_programming"),
    url(r'^team_logistics$', views.team_logistics, name="team_logistics"),
    url(r'^team_agenda$', views.team_agenda, name="team_agenda"),
    url(r'^team_graphics$', views.team_graphics, name="team_graphics"),
]
