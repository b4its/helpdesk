from dataclasses import fields
from pyexpat import model
from tkinter.tix import Select
from django.core import validators
from django import forms
from .models import Biodata


class BioRegistration(forms.ModelForm):
     class Meta:
        model = Biodata
        fields = ['user','email' , 'alamat']
        widgets = {
            'user': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'alamat': forms.TextInput(attrs={'class':'form-control'}),
        }




