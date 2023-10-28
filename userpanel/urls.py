from django.urls import path
from . import views


urlpatterns = [
    path("", views.lichniy_kabinet, name="home")
]
