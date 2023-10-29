from django.urls import path
from . import views


urlpatterns = [
    path("", views.lichniy_kabinet, name="usrpanel"),
    path("adminpanel/", views.adminarea, name="adminpanel"),
    path("addtest/", views.AddTest, name="addtest"),
    path("addcource/", views.AddCource, name="addcource")
]
