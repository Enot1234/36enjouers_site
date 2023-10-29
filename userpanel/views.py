from django.shortcuts import render
from .models import Study
from .models import Result
from .models import Test
from Site.models import school
from django.contrib.auth.decorators import login_required

@login_required
def lichniy_kabinet(request):
    usr = request.user
    tests = Test.objects.filter(user=usr)
    results = Result.objects.filter(user=usr)
    courses = Study.objects.filter(user=usr)
    group = list(usr.groups.all())[0]

    return render(request, "office/PersonalArea.html", {"tests": tests, "results": results, "courses": courses, "user": usr, "group": group})

@login_required
def adminarea(request):
    usr = request.user
    org = school.objects.filter(user=usr)
    orgname = org[0].name

    return render(request, "office/PersonalAdminArea.html", {"orgname": orgname, "user": usr})
