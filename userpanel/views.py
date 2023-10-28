from django.shortcuts import render
from .models import Study
from .models import Result
from .models import Test

def lichniy_kabinet(request):
    tests = Test.objects.all()
    results = Result.objects.all()
    courses = Study.objects.all()

    return render(request, "office/lichniy_kabinet.html", {"tests": tests, "results": results, "courses": courses})
