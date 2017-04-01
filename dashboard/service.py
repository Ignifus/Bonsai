import json
from django.shortcuts import render
from .models import *
from django.core.exceptions import PermissionDenied


def receive_logs(request):
    json_str = '{"app": "TestApp", "key": "sarasacosmica", "http": [{"code": "404", "route": "/firuli", "timestamp": 1}], "logs": [{"method": "","description": "","timestamp": 1}]}'
    data = json.loads(json_str)
    app_found = App.objects.filter(name=data['app'], apikey=data['key']).exists()
    if app_found:
        return render(request, "dashboard/receive-logs.html")
    raise PermissionDenied


def get_logs(request):
    return render(request, "dashboard/get-logs.html")
