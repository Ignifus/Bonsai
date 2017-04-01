from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        return redirect('/')


def logout_auth(request):
    logout(request)
    return redirect('/')
