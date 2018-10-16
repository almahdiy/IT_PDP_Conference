from django.shortcuts import render
import json
import requests
from django.template import Context, loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.
def home(request):
	template = loader.get_template("webapp/home.html")
	return HttpResponse(template.render())


def agenda(request):
	template = loader.get_template("webapp/agenda.html")
	return HttpResponse(template.render())


def booths(request):
	template = loader.get_template("webapp/booths.html")
	return HttpResponse(template.render())


def splash(request):
	template = loader.get_template("webapp/splash.html")
	return HttpResponse(template.render())