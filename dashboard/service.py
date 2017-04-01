import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def receive_logs(request):
    json_str = (request.body.decode('utf-8'))
    data = json.loads(json_str)
    app = App.objects.filter(name=data['app'], apikey=data['key'])
    if app.exists():
        for http_log in data['http']:
            http_logs = Http(code=http_log['code'], timestamp=http_log['timestamp'], app=app.first())
            http_logs.save()

        for log in data['logs']:
            logs = Log(method=log['method'], description=log['description'], timestamp=log['timestamp'], app=app.first())
            logs.save()
        return JsonResponse({'status': 'ok'})
    raise PermissionDenied


@csrf_exempt
def get_logs(request):
    return render(request, "dashboard/get-logs.html")


@csrf_exempt
def get_server_logs(request):
    obj = ServerLog(cpu_usage=15)
    data = serializers.serialize('json', [obj, ])
    return JsonResponse(data, safe=False)

