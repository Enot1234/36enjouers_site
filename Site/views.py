from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def laborinfo(request):
    return render(request, "laborinfo.html")

def tariffs(request):
    return render(request, "tariffs.html")