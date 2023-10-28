from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home"),
    path("laborinfo", laborinfo, name="laborinfo"),
    path("tariffs", tariffs, name="tariffs")
]
