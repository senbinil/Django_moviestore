from django import forms
from django.db.models.fields import TextField
from django.forms.widgets import FileInput, TextInput
from .models import Details

class edit_form(forms.ModelForm):
    class Meta:
        model=Details
        fields=['name','title','year','img']
        widgets={
            'name':TextInput(attrs={'class':'form-control'}),
            'title':TextInput(attrs={'class':'form-control'}),
            'year':TextInput(attrs={'class':'form-control'}),
            'img':FileInput(attrs={'class':'form-control'}),
        }
        
