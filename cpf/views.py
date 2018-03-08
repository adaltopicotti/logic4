from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "cpf/home.html")

def res(request):
    return render(request, "structure/base.html")
