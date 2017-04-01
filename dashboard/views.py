from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def landing(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/landing.html')
    else:
        return redirect('home', request)


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home', request)
    else:
        return redirect('landing', request)


def logout_auth(request):
    logout(request)
    return redirect('landing', request)


@login_required(login_url='/')
def home(request):
    return render(request, 'dashboard/home.html')


def server(request):
    return render(request, 'dashboard/server.html')


def apps(request):
    return render(request, 'dashboard/apps.html')
