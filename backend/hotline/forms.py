from django import forms
from django.forms import TextInput

from . import models
class HotlineForm(forms.ModelForm):
    class Meta:
        model = models.Hotline
        fields = ['ticket' ,'designation','serialNumber', 'anomaly', 'date_entree', 'source', 'locality', 'updated_by', 'isMaintenance',]
        widgets = {
            'ticket': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'designation': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'serialNumber': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'anomaly': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'date_entree': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'source': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'locality': TextInput(attrs={
                'class': "form-control col-4",
                'type': 'date',
            }),
        }