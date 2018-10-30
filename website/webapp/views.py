import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader

from .forms import AuthenticationForm

# To be replaced once we have the API on the production server
API_URL = "http://127.0.0.1:8000/"


def home(request):
    if request.method == 'GET':
        current_user_id = str(request.session.get('loggedin', 0))
        if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
            # two cases: logged in or no. Render two different templates depending on the session
            form = AuthenticationForm()
            template_name = "webapp/splash.html"
            return render(request, template_name, {'form': form})
        else:
            template = loader.get_template("webapp/home.html")
            request.session.set_expiry(5)
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
                request.session.set_expiry(5)
                print("In database")
                template = loader.get_template("webapp/home.html")
            return HttpResponse(template.render())
        else:
            print("form is not valid")


def agenda(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/agenda.html")
        return HttpResponse(template.render())


def booths(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/booths.html")
        return HttpResponse(template.render())


def icebreaker(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/icebreaker.html")
        return HttpResponse(template.render())


def metaverse(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/metaverse.html")
        return HttpResponse(template.render())


def committee(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/committee.html")
        return HttpResponse(template.render())


def team_programming(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/team_programming.html")
        return HttpResponse(template.render())


def team_logistics(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/team_logistics.html")
        return HttpResponse(template.render())


def team_agenda(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/team_agenda.html")
        return HttpResponse(template.render())


def team_graphics(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/team_graphics.html")
        return HttpResponse(template.render())


def about(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        template = loader.get_template("webapp/about.html")
        return HttpResponse(template.render())


def splash(request):
    current_user_id = str(request.session.get('logged_user_id', 0))
    if (current_user_id == "0"):  # The session field will be storing a zero if no user is logged in
        return HttpResponseRedirect("/../home")
    else:
        if request.method == 'GET':
            template = loader.get_template("webapp/splash.html")
            return HttpResponse(template.render())

        elif (request.method == "POST"):
            form = AdminLoginForm(data=request.POST)
            print("This is a post request in the authentication page")
            if form.is_valid():
                print("form is valid")
                # Creates an object from the form. Doesn't save it though!
                obj = form.save(commit=False)

                # Getting data that is formatted properly so we can pass it to the API/database
                sessionID = form.cleaned_data['sessionID']

                dic = {"sessionID": sessionID}

                r = requests.post(API_URL + 'authenticate/', data=dic)
                print("test")
                if (len(r.text) == 0):  # None was returned
                    print("Not in database")
                else:
                    print("In database")
