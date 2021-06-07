from django import forms
from django.forms import fields
from .models import Advertisment

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        #fields = ('company','address')
        exclude = ('user',)