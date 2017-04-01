from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext
from .models import User
from django.template import loader


loggedIn = False # used to tell if user is loggedIn
# ???
currentUser = User()

def login(request):
    # every time before logging in: loggedIn is false
    global loggedIn
    loggedIn = False
    template = loader.get_template('notesTaker/login.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

