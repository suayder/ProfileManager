from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .cpfValidation import validate_CPF, validate_CNPJ

class Pessoa(models.Model):
    userInstance = models.OneToOneField(User,on_delete=models.CASCADE, related_name='userinstance')
    usertype = models.SmallIntegerField(choices=[(1,'CPF'),(2,'CNPJ')])
    foto = models.ImageField(upload_to='thumbpath', blank=True)
    descricao = models.TextField(blank=True)

class PessoaFisica(models.Model):
    usuario = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='pessoaf')
    cpf = models.CharField(unique=True, max_length=14)
    sexo = models.SmallIntegerField(choices=[(1, 'FEMININO'),(2,'MASCULINO'),(3,'NÃO DECLARAR')])

class PJuridica(models.Model):
    usuario = models.OneToOneField(Pessoa, on_delete=models.CASCADE, related_name='dadospj')
    cnpj = models.CharField(unique=True, max_length=14)# validators=[validate_CNPJ]
    ramo = models.CharField(max_length=64)

class Vaga(models.Model):
    status = models.BooleanField(default=True) #True = disponível.
    descricao = models.TextField()
    prerequisitos = models.TextField()
    fk_pjuridica = models.ForeignKey(PJuridica, on_delete=models.CASCADE, related_name='vagas', blank=True)

class Telefone(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fone')
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=9)

# class TelefonePJ(models.Model):
#     pessoa = models.ForeignKey(PJuridica, on_delete=models.CASCADE, related_name='fone')
#     ddd = models.CharField(max_length=2)
#     numero = models.CharField(max_length=9)

class Projeto(models.Model):
    #id_projeto=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=64, blank=True)
    descricao = models.TextField()
    status = models.SmallIntegerField(choices=[(1,"EXECUTANTO"), (2,"FINALIZADO"), (3, "PAUSADO"), (4, "INTERRONPIDO")])
    datainicio = models.DateField()
    datafim = models.DateField()
    tipo = models.SmallIntegerField(choices=[(1,"PROJETO"), (2,"EMPREGO"), (3,"FACULDADE"), (4,"TRABALHO PESSOAL")])
    instituicao = models.CharField(max_length=64)

class PessoaProjeto(models.Model):
    fk_projeto= models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='fk_projeto')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fk_user')

class Experiencia(models.Model):
    user = models.ForeignKey(PessoaFisica, on_delete=models.CASCADE, related_name='fk_experienciapf')
    anoinicio = models.DateField()
    anofim = models.DateField()
    instituicao = models.TextField()
    cidade = models.TextField()
# class PessoaFisicaProjeto(PessoaProjeto):
#     fk_pessoa= models.ForeignKey(PessoaFisica, on_delete=models.CASCADE, related_name="fk_pfusuario")

# class PJuridicaProjeto(PessoaProjeto):
#     fk_pessoa= models.ForeignKey(PJuridica, on_delete=models.CASCADE, related_name="fk_pjusuario")

# class Foto(models.Model):
#     nome = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     path = models.CharField(max_length=255)