from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Create Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Reconfirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            raise ValidationError('This email is already associated with an account')
        elif data == '':
            raise ValidationError('Please enter a valid email')
        return data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class AddTransForm(forms.Form):
    transaction_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sandwich'}))
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'14.00'}))

class BudgetForm(forms.Form):
    budget = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '100.00'}))
