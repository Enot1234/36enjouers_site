from django.shortcuts import render
from .models import *
from .forms import RegSchool


def home(request):
    return render(request, "index.html")

def laborinfo(request):
    return render(request, "laborinfo.html")

def tariffs(request):
    return render(request, "tariffs.html")

def register(request):
    return render(request, "register/RegisterSchool.html", {"model": school.objects.all()})

def organization(request):
    pass