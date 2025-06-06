from tracker.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # zamień na swoją nazwę url po zalogowaniu
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})