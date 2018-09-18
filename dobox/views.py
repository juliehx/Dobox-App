from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

def index(request):
    return render(request, 'dobox/index.html')

def signin(request):
    return HttpResponse('this is the sign-in page')

def signup(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dobox:signin')
    else:
        form = forms.RegistrationForm()
    return render(request, 'dobox/signup.html', {'form': form})