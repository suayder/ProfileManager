from django.contrib import admin
from .models import PessoaFisica, Vaga, PJuridica,User, Pessoa, Experiencia
# Register your models here.

admin.site.register({PessoaFisica, PJuridica,Vaga, Experiencia, Pessoa})