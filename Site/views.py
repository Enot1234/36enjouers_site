from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    return render(request, "index.html")


def laborinfo(request):
    return render(request, "laborinfo.html")


def tariffs(request):
    return render(request, "tariffs.html")


def registerSchool(request):
    if request.method == "POST":
        form = RegSchoolForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        
        return redirect('organization', pk=post.id)
    else:
        form = RegSchoolForm()

    return render(request, "register/RegisterSchool.html", {"model": form})


def regUser(request):
    if request.method == "POST":
        form = RegUserForm(request.POST)
    else:
        form = RegUserForm()

    return render(request, "register/RegisterUser.html", {"model": form})


def organization(request, pk):
    bd = school.objects.filter(id = pk)

    return render(request, "office/organization.html", {"model": bd})

def login(request):
    if request.method == "POST":
        return redirect('home')

    return render(request, "register/login.html")