from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context import RequestContext
from .models import User
from django.template import loader
from .forms import userForm

username = ""
password = ""
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

def main(request):
    global loggedIn
    template = loader.get_template('notesTaker/main.html')
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['htmlusername']
            request.session['username'] = username
            password = form.cleaned_data['htmlpassword']
        else:
            username = ""
            password = ""
    else:
        username = request.session.get('username')
    userList = User.objects.all()
    userFound = False
    for user in userList:
        if loggedIn or username == user.username and password == user.password:
            userFound = True
            loggedIn = True
            password = user.password
            currentUser = user
            break
    if not userFound:
        query = User()
        query.username = username
        query.password = password
        currentUser = query
        query.save()

    context = {
        "username":username,
    }
    return HttpResponse(template.render(context, request))

def add_class(request):
    context = {

    }
    template = loader.get_template('notesTaker/add_class.html')
    return HttpResponse(template.render(context, request))

def add_notes(request):
    context = {

    }
    template = loader.get_template('notesTaker/main.html')
    return HttpResponse(template.render(context, request))
