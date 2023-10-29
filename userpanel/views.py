from django.shortcuts import render, redirect
from .models import Study
from .models import Result
from .models import Test
from Site.models import school
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def lichniy_kabinet(request):
    usr = request.user
    tests = Test.objects.filter(user=usr)
    results = Result.objects.filter(user=usr)
    courses = Study.objects.filter(user=usr)
    group = list(usr.groups.all())[0]

    if str(group) == "Преподователь":
        return redirect('adminpanel')
    else:
        return render(request, "office/PersonalArea.html", {"tests": tests, "results": results, "courses": courses, "user": usr, "group": group})


@login_required
def adminarea(request):
    usr = request.user
    group = list(usr.groups.all())[0]
    org = school.objects.filter(user=usr)
    orgname = org[0].name

    return render(request, "office/PersonalAdminArea.html", {"orgname": orgname, "user": usr, "group": group})

def AddCource(request):
    if request.method == "POST":
        form = AddCorceForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            post.save()
    
            return redirect('adminpanel')
    else:
        form = AddCorceForm()

    return render(request, "office/add/cource.html", {"form": form})


def AddTest(request):
    if request.method == "POST":
        form = AddTestForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            post.save()
    
            return redirect('adminpanel')
    else:
        form = AddTestForm()

    return render(request, "office/add/tests.html", {"form": form})
