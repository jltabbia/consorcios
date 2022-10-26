from django import forms
from usuarios.models import Usuario

class EdificoForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields= "__all__"