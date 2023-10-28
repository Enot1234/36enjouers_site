from django import forms
from .models import school


class RegSchool(forms.ModelForm):


    class Meta:
        model = school
        fields = ('name', 'tel', 'email', 'INN', 'adress', 'FIO',)

