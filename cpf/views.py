from django.shortcuts import render, redirect
from .forms import PessoaFisicaForm

# Create your views here.

def home(request):
    if request.method == "POST":
        form = PessoaFisicaForm(request.POST)
        if form.is_valid():
            pf= form.save(commit=False)
            pf.status = "1"
            pf.formattedcpf = "051.959.909-80"
            pf.nome = "Adalto Picotti Junior"
            pf.consultaID = "6FZ.1M1M.K2C.2L2L"
            pf.save()
            return render(request, "structure/base.html", {'msg':"Saved"})
    else:
        form = PessoaFisicaForm()
    return render(request, "cpf/home.html", {'form': form})

def res(request, msg):
    return render(request, "structure/base.html", {'msg': msg})
