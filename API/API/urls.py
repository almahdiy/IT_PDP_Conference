"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from PDPAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^questions/$', views.QuestionList.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)$', views.QuestionDetail.as_view()),
    url(r'^mcqs/$', views.MCQList.as_view()),
    url(r'^mcqs/(?P<pk>[0-9]+)$', views.MCQDetail.as_view()),
    url(r'^options/$', views.MCQOptionList.as_view()),
    url(r'^options/(?P<pk>[0-9]+)$', views.MCQOptionDetail.as_view()),
    url(r'^mcqsoptions/(?P<pk>[0-9]+)/$', views.get_MCQ_options),
    url(r'^authenticate/$', views.authenticate),
    url(r'^vote/$', views.vote),
    url(r'^question_count/$', views.question_count),
    url(r'^vote_count_ajax/(?P<pk>[0-9]+)/$', views.vote_count_ajax),
    url(r'^option_vote/(?P<pk>[0-9]+)/$', views.option_vote),
    #url(r'^icebreaker_status/$', views.icebreaker_status),

]
