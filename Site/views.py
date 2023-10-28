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
    form = RegSchool()
    return render(request, "register/RegisterSchool.html", {"model": form})

def organization(request):
    pass