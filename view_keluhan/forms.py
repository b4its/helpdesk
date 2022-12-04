from django import forms
from setuptools import Require
from .models import FileUpload

class MyfileUploadForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pembahasan = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class TeknisiFileUploadForm(forms.ModelForm):
     class Meta:
        model = FileUpload
        fields = [ 'status','my_file2' ]
        widgets = {
            'status': forms.Select, 
        }
    