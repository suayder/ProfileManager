from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signuppf', views.signuppf, name='signuppf'),
    path('signuppj', views.signuppj, name='signuppj'),
    path('skillsform', views.editSkills, name='skillsform'),
    path('experienceform', views.experienceForm, name='experienceform'),
    path('educationform', views.educationForm, name='educationform'),
    #path('logout/', auth_views.logout, name='logout'),
    ]