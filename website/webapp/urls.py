from django.conf.urls import url
from . import views     # Relative importing


# Look for the url that matches the user's request
urlpatterns = [
    url(r'^$|^home$', views.home, name="home"),     # Default homepage; they didn't request anything
    url(r'^agenda$', views.agenda, name="agenda"),
    url(r'^booths$', views.booths, name="booths"),
    #url(r'^splash$', views.splash, name="splash"),
    url(r'^icebreaker$', views.icebreaker, name="icebreaker"),
    url(r'^QA$', views.QA, name="QA"),
    url(r'^create_question$', views.create_question, name="create_question"),
    url(r'^metaverse$', views.metaverse, name="metaverse"),
    url(r'^committee$', views.committee, name="committee"),
    url(r'^team_programming$', views.team_programming, name="team_programming"),
    url(r'^team_logistics$', views.team_logistics, name="team_logistics"),
    url(r'^team_agenda$', views.team_agenda, name="team_agenda"),
    url(r'^team_graphics$', views.team_graphics, name="team_graphics"),
    url(r'^about$', views.about, name="about"),
]
