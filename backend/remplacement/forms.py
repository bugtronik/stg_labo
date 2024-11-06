from django import forms
from django.forms import TextInput

from . import models
class RemplacementForm(forms.ModelForm):
    class Meta:
        model = models.Remplacement
        fields = ['ancien' ,'etat','cause', 'nouveau', 'ticket']
        widgets = {
            'ancien': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'etat': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'cause': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'nouveau': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'ticket': TextInput(attrs={
                'class': "form-control col-4",
            }),
        }