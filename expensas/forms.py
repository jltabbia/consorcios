from django import forms

class ExpensasForm(forms.ModelForm):
    class Meta:
        model=Propietarios
        fields= "__all__"