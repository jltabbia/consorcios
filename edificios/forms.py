from django import forms
from usuarios.models import Usuario
from modelos.models import Edificios

class EdificoForm(forms.ModelForm):
    class Meta:
        model=Edificios
        fields= "__all__"