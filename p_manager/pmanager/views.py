from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Pessoa

def index(request):

    #usuario = User.objects.get(pk = 1)
    return HttpResponse("Hello, world. You're at the polls index.")

