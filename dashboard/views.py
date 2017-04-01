from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def landing(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return render(request, 'dashboard/landing.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'dashboard/home.html')


def server(request):
    return render(request, 'dashboard/server.html')


def apps(request):
    return render(request, 'dashboard/apps.html')
