from django.shortcuts import render
from .models import Study
from .models import Result
from .models import Test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def lichniy_kabinet(request):
    tests = Test.objects.filter(user=request.user)
    results = Result.objects.filter(user=request.user)
    courses = Study.objects.filter(user=request.user)

    return render(request, "office/lichniy_kabinet.html", {"tests": tests, "results": results, "courses": courses})
