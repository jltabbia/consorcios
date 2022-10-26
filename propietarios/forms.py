from django import forms
#from usuarios.models import Usuario
from modelos.models import Propietarios

class PropietarioForm(forms.ModelForm):
    class Meta:
        model=Propietarios
        fields= "__all__"