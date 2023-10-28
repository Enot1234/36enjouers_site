from django.shortcuts import render, redirect
from .models import *
from .forms import RegSchool


def home(request):
    return render(request, "index.html")


def laborinfo(request):
    return render(request, "laborinfo.html")


def tariffs(request):
    return render(request, "tariffs.html")


def register(request):
    if request.method == "POST":
        form = RegSchool(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.fio = request.user
            post.save()
        
        return redirect('organization', pk=post.id)
    else:
        form = RegSchool()

    return render(request, "register/RegisterSchool.html", {"model": form})


def organization(request, pk):
    bd = school.objects.filter(id = pk)

    return render(request, "ofice/organization.html", {"model": bd})

