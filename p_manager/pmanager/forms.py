from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PessoaFisica, PJuridica, Experiencia, Pessoa, Education,Contato

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'password1', 'password2')

class PessoaForm(forms.ModelForm):    
    class Meta:
        model = Pessoa
        fields = ('usertype',)

class PessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PJuridica
        fields = ('cnpj', 'ramo')

class PessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica
        fields = ('cpf', 'sexo')

class Login(forms.ModelForm):
     class Meta:
         model = User
         fields = ('username', 'password')

class SkillsForm(forms.Form):
    organisationalskills = forms.IntegerField()
    communicationalskills = forms.IntegerField()
    projectmanagmentskills = forms.IntegerField()

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ('nome', 'descricao', 'anoinicio', 'anofim', 'instituicao', 'cidade','nacao')

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('coursename', 'anoinicio', 'anofim', 'instituicao', 'cidade','nacao')

class ContatoForm(forms.ModelForm):
    class Meta:
        model=Contato
        fields = ('ddd', 'numero', 'email')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('foto',)