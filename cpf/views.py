from django.shortcuts import render, redirect
from .forms import PessoaFisicaForm
from .models import PessoaFisica
from django.http import JsonResponse, HttpResponse
import json, requests
from website.forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.

@login_required
def cpf_app(request):
    if request.method == "POST":
        form = PessoaFisicaForm(request.POST)
        if form.is_valid():
            cpf = request.POST['cpfnumber']
            if validateCPF(cpf) == True:
                try:
                    result = PessoaFisica.objects.get(cpfnumber=cpf)
                    form = PessoaFisicaForm()
                    return render(request, "cpf/cpf_search.html", {'result':result, 'form': form, 'channel':"db"})
                except:
                    result = consulta_cpf(cpf)
                    form = form.save(commit=False)
                    form.status = result['status']
                    #form.formattedcpf = result['cpf']
                    form.nome = result['nome']
                    form.consultaID = result['consultaID']
                    form.save()
                    form = PessoaFisicaForm()
                    return render(request, "cpf/cpf_search.html", {'result':result, 'form': form, 'channel':"new"})
    else:
        form = PessoaFisicaForm()
        return render(request, "cpf/cpf_search.html", {'form': form})
    return render(request, "cpf/cpf_search.html", {'form': form, 'erro': "CPF Inválido!"})



def consulta_cpf(cpfNumber):

    url = "https://api.cpfcnpj.com.br/" + ENV.key +"/1/json/" + cpfNumber
    result = requests.get(url)
    cpfJson = result.json()
    return cpfJson




def validateCPF(cpfNumber):
        """
        Method to validate a brazilian cpfNumber number
        Based on Pedro Werneck source avaiable at
        www.PythonBrasil.com.br
        Tests:
        >>> print cpfNumber().validate('91289037736')
        True
        >>> print cpfNumber().validate('91289037731')
        False
        """
        cpfNumber_invalidos = [11*str(i) for i in range(10)]
        if cpfNumber in cpfNumber_invalidos:
            return False

        if not cpfNumber.isdigit():
            """ Verifica se o cpfNumber contem pontos e hifens """
            cpfNumber = cpfNumber.replace( ".", "" )
            cpfNumber = cpfNumber.replace( "-", "" )

        if len( cpfNumber ) < 11:
            """ Verifica se o cpfNumber tem 11 digitos """
            return False
        if len( cpfNumber ) > 11:
            """ cpfNumber tem que ter 11 digitos """
            return False
        selfcpfNumber = [int( x ) for x in cpfNumber]
        cpfNumber = selfcpfNumber[:9]
        while len( cpfNumber ) < 11:
            r =  sum( [( len( cpfNumber )+1-i )*v for i, v in [( x, cpfNumber[x] ) for x in range( len( cpfNumber ) )]] ) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpfNumber.append( f )


        return bool( cpfNumber == selfcpfNumber )
