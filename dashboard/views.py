from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def landing(request):
    return render(request, 'dashboard/landing.html')


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'dashboard/home.html')
    else:
        return render(request, 'dashboard/landing.html')


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


def server(request):
    return render(request, 'dashboard/server.html')


def apps(request):
    return render(request, 'dashboard/apps.html')
