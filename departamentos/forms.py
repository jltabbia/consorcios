from django import forms
#from usuarios.models import Usuario
from modelos.models import Departamentos

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamentos
        fields= "__all__"