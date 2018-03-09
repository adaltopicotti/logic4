from django import forms
from .models import PessoaFisica


class PessoaFisicaForm(forms.ModelForm):

    cpfnumber = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Informe o CPF para consulta!'}))

    class Meta:
        model = PessoaFisica
        fields = ('cpfnumber',)
