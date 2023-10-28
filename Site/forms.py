from django import forms
from .models import school

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegSchool(forms.ModelForm):


    class Meta:
        model = school
        fields = ('name', 'tel', 'email', 'INN', 'adress', 'FIO',)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']