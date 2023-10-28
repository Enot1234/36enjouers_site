from django.shortcuts import render
from .models import Test

def lichniy_kabinet(request):
    tests = Test.objects.all()
    for i in tests:
        print(i.title)
    return render(request, "lichniy_kabinet.html", {"tests":tests})
