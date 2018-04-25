from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PessoaFisica, PJuridica, Projeto

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2')
    
class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ('cpf', 'sexo')

class Login(forms.ModelForm):
     class Meta:
         model = User
         fields = ('username', 'password')