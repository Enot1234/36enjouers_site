from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def fd(request):
    return render(request, "fd.html")