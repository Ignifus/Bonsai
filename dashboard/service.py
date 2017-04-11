import json

import time
from django.core import serializers
from itertools import chain
from django.http import JsonResponse, HttpResponse
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
    app = request.POST.get('app', False)
    fromseconds = request.POST.get('from', False)
    if app and fromseconds:
        found_app = App.objects.filter(name=app)
        if found_app.exists():
            http_data = Http.objects.filter(app_id=found_app.first().id, timestamp__gte=float(time.time())-float(fromseconds))
            logs = Log.objects.filter(app_id=found_app.first().id, timestamp__gte=float(time.time())-float(fromseconds))
            combinedlogs = list(chain(http_data, logs))
            data = serializers.serialize('json', combinedlogs)
            return HttpResponse(data)
        else:
            raise ObjectDoesNotExist
    else:
        return render(request, "dashboard/get-logs.html")


@login_required(login_url='/')
@csrf_exempt
def get_server_logs(request):
    last_log = ServerLog.objects.latest()
    totaldownload = psutil.net_io_counters().bytes_recv
    totalupload = psutil.net_io_counters().bytes_sent

    netdownload = totaldownload - last_log.net_download_total
    netupload = totalupload - last_log.net_upload_total

    obj = ServerLog(cpu_usage=psutil.cpu_percent(),
                    ram_usage=psutil.virtual_memory().used/1000000, ram_total=psutil.virtual_memory().total/1000000,
                    hdd_usage=psutil.disk_usage('/').used/1000000, hdd_total=psutil.disk_usage('/').total/1000000,
                    net_download=netdownload, net_upload=netupload,
                    net_download_total=totaldownload, net_upload_total=totalupload,
                    timestamp=time.time())
    obj.save()
    data = serializers.serialize('json', [obj, ])
    return HttpResponse(data)

