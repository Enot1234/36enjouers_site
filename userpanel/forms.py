from django import forms
from .models import *


class AddTestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('title', 'link',)


class AddCorceForm(forms.ModelForm):
    

    class Meta:
         model = Study
         fields = ('title', 'link',)