from django import forms
from django.forms import TextInput
from source.models import Source

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control col-4",
            }),
        }        