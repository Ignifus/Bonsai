from django.shortcuts import render


def receive_logs(request):
    return render(request, "dashboard/receive-logs.html")


def get_logs(request):
    return render(request, "dashboard/get-logs.html")
