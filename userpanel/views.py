from django.shortcuts import render
from .models import Test

def lichniy_kabinet(request):
    tests = Test.objects.all()
    for i in tests:
        print(i.title)
    return render(request, "office/lichniy_kabinet.html", {"tests": tests})
