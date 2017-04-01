import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core.exceptions import PermissionDenied


def receive_logs(request):
    data = json.loads(request.body)
    app = App.objects.filter(name=data['app'], apikey=data['key'])
    if app.exists():
        for http_log in data['http']:
            http_logs = Http(code=http_log['code'], route=http_log['route'], timestamp=http_log['timestamp'], app=app)
            http_logs.save()

        for log in data['logs']:
            logs = Log(method=log['method'], description=log['description'], timestamp=log['timestamp'], app=app)
            logs.save()

    context = {'data': data}
    return render(request, "dashboard/receive-logs.html", context)
    raise PermissionDenied


def get_logs(request):
    return render(request, "dashboard/get-logs.html")


def get_server_logs(request):
    obj = ServerLog(cpu_usage=15)
    data = serializers.serialize('json', [obj, ])
    return JsonResponse(data, safe=False)

