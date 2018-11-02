import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader

from .forms import AuthenticationForm

# To be replaced once we have the API on the production server
API_URL = "http://127.0.0.1:8000/"
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
            request.session.set_expiry(600)
            return HttpResponse(template.render())

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print("This is a post request in the authentication page")
        if form.is_valid():
            print("form is valid")
            # Creates an object from the form. Doesn't save it though!
            obj = form.save(commit=False)

            # Getting data that is formatted properly so we can pass it to the API/database
            sessionID = form.cleaned_data['sessionID']

            dic = {"sessionID": sessionID}

            r = requests.post(API_URL + 'authenticate/', data=dic)
            print(r.text)
            if (r.text == "false"):  # None was returned
                print("wrong session ID")  # need to display an error message e.g. "wrong session ID try again" will do this later
                form = AuthenticationForm()
                template_name = "webapp/splash.html"
                return render(request, template_name, {'form': form})
            else:
                # Submitted session ID is correct, set the current browser session and redirect to home
                request.session['loggedin'] = 1
                request.session.set_expiry(600)
                print("In database")
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
        template = loader.get_template("webapp/icebreaker.html")
        """
        I'll write my thoughts here so I don't get confused XD
        ....
        Users are going to get an initial screen with just a game description
        We start the game manually from the backend and ask them to refresh
        They 
        """
        return HttpResponse(template.render())


@authenticate
def QA(request):
    return respondGeneric(request, "webapp/q&a.html")


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

# def splash(request):
#     current_user_id = str(request.session.get('loggedin', 0))
#     if (current_user_id == NOT_LOGGED_IN):
#         return HttpResponseRedirect("/../home")
#     else:
#         if request.method == 'GET':
#             template = loader.get_template("webapp/splash.html")
#             return HttpResponse(template.render())
#
#         elif (request.method == "POST"):
#             form = AdminLoginForm(data=request.POST)
#             print("This is a post request in the authentication page")
#             if form.is_valid():
#                 print("form is valid")
#                 # Creates an object from the form. Doesn't save it though!
#                 obj = form.save(commit=False)
#
#                 # Getting data that is formatted properly so we can pass it to the API/database
#                 sessionID = form.cleaned_data['sessionID']
#
#                 dic = {"sessionID": sessionID}
#
#                 r = requests.post(API_URL + 'authenticate/', data=dic)
#                 print("test")
#                 if (len(r.text) == 0):  # None was returned
#                     print("Not in database")
#                 else:
#                     print("In database")
