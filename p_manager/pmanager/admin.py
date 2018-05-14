from django.contrib import admin
from .models import PessoaFisica, Vaga, Projeto, PJuridica,User, Pessoa
# Register your models here.

admin.site.register({PessoaFisica, PJuridica,Vaga, Projeto,Pessoa})