from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

def index(request):
    if(request.method == 'POST'):
        user_form = SignUpForm(request.POST)
        pessoa_form = PessoaForm(request.POST)
        
        if user_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.user = usr
            usrpessoa.userInstance_id = usr.pk
            usrpessoa.save()

            return HttpResponse("Sucesso")
        else:
            return render(request, "index.html", { "form": login, "user_form": user_form, "pessoa_form":pessoa_form})
    return render(request, 'index.html',{ "form": Login(), "user_form": SignUpForm(), "pessoa_form":PessoaForm() })


def signup(request):

    if(request.method == 'POST'):
        user_form = SignUpForm(request.POST)
        pessoa_form = PessoaFisicaForm(request.POST)

        if user_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            obj_pessoa = Pessoa()
            obj_pessoa.usertype = 1
            obj_pessoa.userInstance = usr
            obj_pessoa.save()

            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.usuario = obj_pessoa
            usrpessoa.save()
            
            return HttpResponse("SUCESSO")
        else:
            return render(request, "signup.html", {"user_form": user_form, "pessoa_form":pessoa_form })
    return render(request, "signup.html", { "user_form": SignUpForm(), "pessoa_form":PessoaFisicaForm() })

# def login_user(request):

#     if(request.method=='POST'):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponse("Sucess")
#         else:
#             return HttpResponse("Something Wrong")
#     return render(request, "login.html", {"login_form":LoginForm()})

def signuppf(request):
    if(request.method == 'POST'):
        user_form = SignUpForm(request.POST)
        pessoa_form = PessoaFisicaForm(request.POST)

        if user_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            obj_pessoa = Pessoa()
            obj_pessoa.usertype = 1
            obj_pessoa.userInstance = usr
            obj_pessoa.save()

            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.usuario = obj_pessoa
            usrpessoa.save()
            
            return HttpResponse("SUCESSO")
        else:
            return render(request, "pessoaFisicaForm.html", {"user_form": user_form, "pessoa_form":pessoa_form })
    return render(request, "pessoaFisicaForm.html", { "user_form": SignUpForm(), "pessoa_form":PessoaFisicaForm() })

def signuppj(request):
    if(request.method == 'POST'):
        user_form = SignUpForm(request.POST)
        pessoa_form = PessoaJuridicaForm(request.POST)

        if user_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            obj_pessoa = Pessoa()
            obj_pessoa.usertype = 2
            obj_pessoa.userInstance = usr
            obj_pessoa.save()

            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.usuario = obj_pessoa
            usrpessoa.save()
            
            return HttpResponse("SUCESSO")
        else:
            return render(request, "pessoaJuridicaForm.html", {"user_form": user_form, "pessoa_form":pessoa_form })
    return render(request, "pessoaJuridicaForm.html", { "user_form": SignUpForm(), "pessoa_form":PessoaJuridicaForm() })