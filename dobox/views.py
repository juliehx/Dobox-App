from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms

def index(request):
    return render(request, 'dobox/index.html')

def signin(request):
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('dobox:success')
            else:
                print('user not found')
    else:
        form = forms.LoginForm()
    return render(request, 'dobox/signin.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dobox:success')
    else:
        form = forms.RegistrationForm()
    return render(request, 'dobox/signup.html', {'form': form})

def success(request):
    return render(request, 'dobox/success.html')