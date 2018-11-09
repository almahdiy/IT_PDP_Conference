import requests
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from rest_framework.response import Response
import json
from uuid import getnode as get_mac



from .forms import AuthenticationForm, NewQuestionForm

# To be replaced once we have the API on the production server
BACKEND_URL = "http://127.0.0.1:10000/"
NOT_LOGGED_IN = "0"


def authenticate(view_function):
    """
    A wrapper to authenticate a view function.

    :param view_function: Function, a django view function.
    :return: Function that has authentication.
    """
    def wrapper(request):
        current_user_id = str(request.session.get('loggedin', 0))
        if current_user_id == NOT_LOGGED_IN:
            return HttpResponseRedirect("/../home")
        else:
            return view_function(request)
    return wrapper


def respondGeneric(request, url):
    template = loader.get_template(url)
    return HttpResponse(template.render())


def home(request):
    if request.method == 'GET':
        current_user_id = str(request.session.get('loggedin', 0))
        if (current_user_id == NOT_LOGGED_IN):
            # two cases: logged in or no. Render two different templates depending on the session
            form = AuthenticationForm()
            template_name = "webapp/splash.html"
            return render(request, template_name, {'form': form})
        else:
            template = loader.get_template("webapp/home.html")
            #request.session.set_expiry(600)
            return HttpResponse(template.render())

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # print("This is a post request in the authentication page")
        if form.is_valid():
            # print("form is valid")
            # Creates an object from the form. Doesn't save it though!
            obj = form.save(commit=False)

            # Getting data that is formatted properly so we can pass it to the API/database
            sessionID = form.cleaned_data['sessionID']

            dic = {"sessionID": sessionID}

            r = requests.post(BACKEND_URL + 'authenticate/', data=dic)
            print(r.text)
            if (r.text == "false"):  # None was returned
                # print("wrong session ID")  # need to display an error message e.g. "wrong session ID try again" will do this later
                form = AuthenticationForm()
                template_name = "webapp/splash.html"
                return render(request, template_name, {'form': form})
            else:
                # Submitted session ID is correct, set the current browser session and redirect to home
                request.session['loggedin'] = 1
                request.session['mac_address'] = get_mac()
                #request.session.set_expiry(600)
                # print("In database")
                template = loader.get_template("webapp/home.html")
            return HttpResponse(template.render())
        else:
            print("form is not valid")


@authenticate
def agenda(request):
    return respondGeneric(request, "webapp/agenda.html")


@authenticate
def booths(request):
    return respondGeneric(request, "webapp/booths.html")


@authenticate
def icebreaker(request):
    current_user_id = str(request.session.get('loggedin', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        r = requests.get(BACKEND_URL + "mcqs/")
        # I am trying to store the json in a string variable
        s = json.dumps(r.json(), indent=4)
        list_of_questions = r.json()
        for question in list_of_questions:
            question["options"] = requests.get(BACKEND_URL + "mcqsoptions/" + str(question["id"])).json()

        #print(list_of_questions)
        template = loader.get_template("webapp/icebreaker.html")
        context = {
            'questions': list_of_questions,
        }

        return HttpResponse(template.render(context, request))


@authenticate
def QA(request):
    template = loader.get_template("webapp/q&a.html")
    if request.method == 'GET':
        r = requests.get(BACKEND_URL + "questions/")
        # I am trying to store the json in a string variable
        s = json.dumps(r.json(), indent=4)
        list_of_questions = r.json()
        for question in list_of_questions:
            question["ajaxId"] = "ajaxId" + str(question["id"])

        # print(list_of_questions[0])
        #Filtering inappropriate questions
        list_of_appropriate_questions = [question for question in list_of_questions if question["isAppropriate"]]
        list_of_appropriate_questions = sorted(list_of_appropriate_questions, key=lambda k: k['votes'], reverse=True)

        # print(list_of_questions)
        # r.json() returns a list of dictionaries, where every dictionary represents an object
        context = {
            'questions': list_of_appropriate_questions,
        }

        return HttpResponse(template.render(context, request))
    return HttpResponseRedirect('QA')


@authenticate
def metaverse(request):
    return respondGeneric(request, "webapp/metaverse.html")


@authenticate
def committee(request):
        return respondGeneric(request, "webapp/committee.html")


@authenticate
def team_programming(request):
        return respondGeneric(request, "webapp/team_programming.html")


@authenticate
def team_logistics(request):
        return respondGeneric(request, "webapp/team_logistics.html")


@authenticate
def team_agenda(request):
        return respondGeneric(request, "webapp/team_agenda.html")


@authenticate
def team_graphics(request):
        return respondGeneric(request, "webapp/team_graphics.html")


@authenticate
def about(request):
        return respondGeneric(request, "webapp/about.html")



def create_question(request):
    form = NewQuestionForm(data=request.POST)
    if form.is_valid():
        #print("Form is valid")
        # if True:
        # Creates an object from the form. Doesn't save it though!
        qa = form.save(commit=False)
        # Getting data that is formatted properly so we can pass it to the API/database
        question = form.cleaned_data['body']
        #print("Create_question is called")
        # This gets you the stuff.. Now we need to put them in a json file and send them to the API
        dic = {"body": question}
        # iles = {"image": open(request.FILES['myfile'], 'rb')}

        r = requests.post(BACKEND_URL + 'questions/', data=dic)
    return HttpResponseRedirect('QA')


def question_voting(request):
    try:
        message = {"votes" : dict(request.POST)["checkbox"], "mac_address": get_mac()}
        r = requests.post(BACKEND_URL + 'vote/', data=message)
        return HttpResponseRedirect('QA')
    except:
        return HttpResponseRedirect('QA')


def vote_count_ajax(request, pk):
    # echo in PHP.. I'm going to try returning concatinated string and see if that works...
    if request.method == 'GET':
        r = requests.get(BACKEND_URL + "vote_count_ajax/" + str(pk))
        return HttpResponse(r, content_type="application/xml")


def vote_count_ajax_all(request):
    # echo in PHP.. I'm going to try returning concatinated string and see if that works...
    if request.method == 'GET':
        r = requests.get(BACKEND_URL + "vote_count_ajax_all/")
        return HttpResponse(r, content_type="application/json")


def question_count(request):
    # echo in PHP.. I'm going to try returning concatinated string and see if that works...
    if request.method == 'GET':
        r = requests.get(BACKEND_URL + "question_count")
        return HttpResponse(r, content_type="application/xml")


def icebreaker_submit(request):
    optionID = dict(request.POST)["radio"][0] #We're using radio buttons so it'll always be 1
    dic = {"mac_address": get_mac()}
    r = requests.put(BACKEND_URL + 'option_vote/' + optionID + "/", data=dic)
    return HttpResponseRedirect('icebreaker')
