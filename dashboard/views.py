from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'dashboard/login.html')


def home(request):
    return render(request, 'dashboard/home.html')


def server(request):
    return render(request, 'dashboard/server.html')


def apps(request):
    return render(request, 'dashboard/apps.html')

