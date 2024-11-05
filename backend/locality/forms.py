from django import forms
from django.forms import TextInput
from locality.models import Locality

class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control col-4",
            }),
        }        