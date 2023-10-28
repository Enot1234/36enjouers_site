from django.shortcuts import render
from .models import *


def home(request):
    return render(request, "index.html")

def laborinfo(request):
    return render(request, "laborinfo.html")

def tariffs(request):
    return render(request, "tariffs.html")

def register(request):
    return render(request, "RegisterSchool.html", {"model": school.objects.all()})