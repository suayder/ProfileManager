from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signuppf', views.signuppf, name='signuppf'),
    path('signuppj', views.signuppj, name='signuppj'),
    path('upload_pic', views.upload_pic, name='upload_pic'),
    path('skillsform', views.editSkills, name='skillsform'),
    path('experienceform', views.experienceForm, name='experienceform'),
    path('educationform', views.educationForm, name='educationform'),
    path('contatoform', views.contatoForm, name='contatoform'),
    #path('logout/', auth_views.logout, name='logout'),
    ]