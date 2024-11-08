from django import forms
from django.forms import TextInput
from status.models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['libelle']
        widgets = {
            'libelle': TextInput(attrs={
                'class': "form-control col-4",
            }),
        }        