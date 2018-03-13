from django import forms
from utilisateur.models import User 
from courtier.models import Courtier


class CreateCourtierAdministrateur(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

