from django import forms
from django.forms import TextInput

from . import models
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = models.Maintenance
        fields = ['ticket' ,'designation','serialNumber', 'anomaly', 'status', 'observation', 'date_entree', 'date_sortie', 'source', 'locality',]
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
            'status': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'observation': TextInput(attrs={
                'class': "form-control col-4",
            }),
            'date_entree': TextInput(attrs={
                'class': "form-control col-4",
                'type': 'date',
            }),
            'date_sortie': TextInput(attrs={
                'class': "form-control col-4",
                'type': 'date',
            }),
        }