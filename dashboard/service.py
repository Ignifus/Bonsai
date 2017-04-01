import json

import time
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import psutil


@csrf_exempt
def receive_logs(request):
    if request.method == "POST":
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
        else:
            raise PermissionDenied
    else:
        return render(request, "dashboard/receive-logs.html")


@login_required(login_url='/')
@csrf_exempt
def get_logs(request):
    #app = request.POST.get('app', False)
    app = "TestAppA"
    if app:
        found_app = App.objects.filter(name=app)
        if found_app.exists():
            http_data = Http.objects.filter(app=found_app.first().id)
            logs = Log.objects.filter(app=found_app.first().id)
            data = serializers.serialize('json', [logs, http_data])
            return JsonResponse(data, safe=False)
        else:
            raise ObjectDoesNotExist
    else:
        return render(request, "dashboard/get-logs.html")


@login_required(login_url='/')
@csrf_exempt
def get_server_logs(request):
    last_log = ServerLog.objects.latest('timestamp')
    netdownload = psutil.net_io_counters().bytes_recv - last_log.net_download
    netupload = psutil.net_io_counters().bytes_sent - last_log.net_upload

    obj = ServerLog(cpu_usage=psutil.cpu_percent(),
                    ram_usage=psutil.virtual_memory().used, ram_total=psutil.virtual_memory().total,
                    hdd_usage=psutil.disk_usage('/').used, hdd_total=psutil.disk_usage('/').total,
                    net_download=netdownload, net_upload=netupload,
                    timestamp=str(time.time()))
    obj.save()
    data = serializers.serialize('json', [obj, ])
    return JsonResponse(data, safe=False)

