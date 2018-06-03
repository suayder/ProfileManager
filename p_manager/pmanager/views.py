from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *


class HomeView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
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
                return render(request, self.template_name, { "form": login, "user_form": user_form, "pessoa_form":pessoa_form})

    def get(self, request):

        if request.user.is_authenticated:
            print("logged in")
            args = {"pessoa": Pessoa.objects.get(userInstance_id= request.user.pk), "experienciaFields":Experiencia.objects.filter(user_id= request.user.pk)}
            #userinst = self.getPessoa(user)
            #print(userInstance.userInstance[1].username)
        else:
            args = { "form": Login(), "user_form": SignUpForm(), "pessoa_form":PessoaForm()}
        return render(request, self.template_name,args)

def editSkills(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            skillsform = SkillsForm(request.POST)
            obj = Pessoa.objects.get(userInstance_id= request.user.pk)
            if skillsform.is_valid():
                obj.organisationalskills = skillsform.cleaned_data['organisationalskills']
                obj.communicationalskills = skillsform.cleaned_data['communicationalskills']
                obj.projectmanagmentskills = skillsform.cleaned_data['projectmanagmentskills']
                obj.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("falied")
        context = {"form": SkillsForm(),"pessoa": Pessoa.objects.get(userInstance_id= request.user.pk), }
        html_form = render_to_string('skillsForm.html',
        context,request=request,)
        return JsonResponse({'html_form': html_form})

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
            return render(request, "pessoaFisicaForm.html", {"form": login,"user_form": user_form, "pessoa_form":pessoa_form })
    return render(request, "pessoaFisicaForm.html", { "form": Login(), "user_form": SignUpForm(), "pessoa_form":PessoaFisicaForm() })

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
            return render(request, "pessoaJuridicaForm.html", {"form": login,"user_form": user_form, "pessoa_form":pessoa_form })
    return render(request, "pessoaJuridicaForm.html", {"form": Login(), "user_form": SignUpForm(), "pessoa_form":PessoaJuridicaForm() })

@csrf_exempt
def experienceForm(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = request.POST
            if request.is_ajax() and request.method == 'PUT':
                obj = Experiencia.objects.get(user_id= form['id'])
            else:
                obj = Experiencia()
            if form.is_valid():
                obj.nome = form.cleaned_data['nome']
                obj.descricao = form.cleaned_data['descricao']
                obj.anoinicio = form.cleaned_data['anoinicio']
                obj.anofim = form.cleaned_data['anofim']
                obj.instituicao = form.cleaned_data['instituicao']
                obj.cidade = form.cleaned_data['cidade']
                obj.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("falied")
        if request.is_ajax():
            context = {"form": ExperienciaForm(), "content":Experiencia.objects.get(user_id= form['id'])}
        else:
            context = {"form": ExperienciaForm()}
        html_form = render_to_string('experienceForm.html',
        context,request=request,)
        return JsonResponse({'html_form': html_form})