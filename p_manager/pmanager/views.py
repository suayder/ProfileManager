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
        pessoaf_form = PessoaFisicaForm(request.POST)
        
        if user_form.is_valid() and pessoaf_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            usrpessoaf = pessoaf_form.save(commit=False)
            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.user = usr
            usrpessoa.userInstance_id = usr.pk
            usrpessoa.save()
            usrpessoaf.usuario = usrpessoa
            usrpessoaf.usuario_id = usrpessoa.pk
            usrpessoaf.save()
            
            return HttpResponse("SUCESSO")
        else:
            return render(request, "index.html", { "form": login, "user_form": user_form, "pessoaf_form": pessoaf_form, "pessoa_form":pessoa_form})
    return render(request, 'index.html',{ "form": Login(), "user_form": SignUpForm(), "pessoaf_form":PessoaFisicaForm(), "pessoa_form":PessoaForm() })

def signup(request):

    if(request.method == 'POST'):
        user_form = SignUpForm(request.POST)
        pessoa_form = PessoaForm(request.POST)
        pessoaf_form = PessoaFisicaForm(request.POST)
        if user_form.is_valid() and pessoaf_form.is_valid() and pessoa_form.is_valid():

            usr = user_form.save()
            usrpessoaf = pessoaf_form.save(commit=False)
            usrpessoa = pessoa_form.save(commit=False)
            usrpessoa.user = usr
            usrpessoa.userInstance_id = usr.pk
            usrpessoa.save()
            usrpessoaf.usuario = usrpessoa
            usrpessoaf.usuario_id = usrpessoa.pk
            usrpessoaf.save()
                
            return HttpResponse("SUCESSO")
        else:
            return render(request, "signup.html", {"user_form": user_form, "pessoaf_form": pessoaf_form, "pessoa_form":pessoa_form })
    return render(request, "signup.html", { "user_form": SignUpForm(), "pessoaf_form":PessoaFisicaForm(), "pessoa_form":PessoaForm() })

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