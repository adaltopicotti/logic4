from django import forms
from .models import PessoaFisica


class PessoaFisicaForm(forms.ModelForm):

    class Meta:
        model = PessoaFisica
        fields = ('cpfnumber',)
