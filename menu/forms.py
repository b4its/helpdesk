from django import forms
from .models import List_User



class manageRegistration(forms.ModelForm):
     class Meta:
        model = List_User
        fields = ['nama' , 'no_hp' ,'status']
        widgets = {
            'nama': forms.TextInput(attrs={'class':'form-control'}),
            'no_hp': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})
        }


