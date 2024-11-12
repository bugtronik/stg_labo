from django import forms
from django.forms import TextInput

from . import models
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = models.Maintenance
        fields = ['diagnostic', 'observation', 'date_entree', 'date_sortie', 'updated_by',]
        widgets = {
            'designation': TextInput(attrs={
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