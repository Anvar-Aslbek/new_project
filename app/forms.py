from dataclasses import fields
from django import forms
from .models import Viloyat

class ViloyatForm(forms.ModelForm):
    
    class Meta:
        model = Viloyat
        fields = '__all__'