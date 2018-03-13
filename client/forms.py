from django import forms
from .models import Client 


class CreateClient(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('seller',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
