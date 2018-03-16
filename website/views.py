from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from website.forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views, forms


def home(request):
    return render(request, 'website/structure/home.html', {'form': LoginForm} )




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/accounts/signup.html', {'form': form})
