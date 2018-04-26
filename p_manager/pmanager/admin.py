from django.contrib import admin
from .models import PessoaFisica, Vaga, Projeto, PJuridica,User
# Register your models here.

admin.site.register({PessoaFisica, PJuridica,Vaga, Projeto})