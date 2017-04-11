from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def landing(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return render(request, 'dashboard/landing.html')


@login_required(login_url='/')
def home(request):
    context = {'server_charts': True}
    return render(request, 'dashboard/server.html', context)


@login_required(login_url='/')
def server(request):
    context = {'server_charts': True}
    return render(request, 'dashboard/server.html', context)


@login_required(login_url='/')
def apps(request):
    context = {'app_charts': True}
    return render(request, 'dashboard/apps.html', context)
