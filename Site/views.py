from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def home(request):
    return render(request, "index.html")


def laborinfo(request):
    return render(request, "laborinfo.html")


def tariffs(request):
    return render(request, "tariffs.html")

@login_required
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

        if form.is_valid():
            form.save()
    
            messages.success(request, 'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('log')
    else:
        form = RegUserForm()

    return render(request, "register/RegisterUser.html", {"model": form})


@login_required
def organization(request, pk):
    bd = school.objects.filter(id = pk)

    return render(request, "office/organization.html", {"model": bd})

