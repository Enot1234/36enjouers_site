from django.urls import path
from django.contrib.auth import views as vi
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("laborinfo/", laborinfo, name="laborinfo"),
    path("tariffs/", tariffs, name="tariffs"),
    path("register/", registerSchool, name="registerschool"),
    path("organization/<str:pk>/", organization, name="organization"),
    path("registeruser/", regUser),
    path("login/", vi.LoginView.as_view(template_name='register/login.html'), name="log"),
    path("logout/", vi.LogoutView.as_view(template_name='register/logout.html'), name="out")
]
