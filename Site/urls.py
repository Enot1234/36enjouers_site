from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("laborinfo/", laborinfo, name="laborinfo"),
    path("tariffs/", tariffs, name="tariffs"),
    path("register/", registerSchool, name="registerschool"),
    path("organization/<str:pk>/", organization, name="organization"),
    path("registeruser/", regUser)
]
