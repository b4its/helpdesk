from dataclasses import fields
from pyexpat import model
from tkinter.tix import Select
from django.core import validators
from django import forms
from .models import List_keluhan

class KeluhanForms(forms.ModelForm):
     class Meta:
        model = List_keluhan
        fields = ['judul' , 'pembahasan' ]
        widgets = {
            'judul': forms.Select(attrs={'class':'form-control'}),
            'pembahasan': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class TeknisiKeluhan(forms.ModelForm):
     class Meta:
        model = List_keluhan
        fields = ['teknisi' , 'status' ]
        widgets = { 
            'teknisi': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            
        }


