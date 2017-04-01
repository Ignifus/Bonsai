from django.shortcuts import render


def receive_logs(request):
    return render(request, "dashboard/receive-logs.html")
