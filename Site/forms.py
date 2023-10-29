from django import forms
from .models import school

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegSchoolForm(forms.ModelForm):


    class Meta:
        model = school
        fields = ('name', 'tel', 'email', 'INN', 'adress', 'FIO',)



class RegUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'password1', 'password2']

