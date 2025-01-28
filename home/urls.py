from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gravar/', views.gravar, name='gravar'),
    path('sessao/', views.sessao, name='sessao'),
    path('exibir_valor', views.exibir_valor, name='exibir_valor'), 
    path('salvar-contato', views.salvar_contato, name="salvar_contato") 
]