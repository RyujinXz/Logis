from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.exibirCarrinho, name='carrinho'),
    path('adicionar/<int:jogoId>/', views.adicionarCarrinho, name='adicionarCarrinho'),  
    path('remover/<int:jogoId>/', views.removerCarrinho, name='removerCarrinho'),  
    path('finalizar/', views.finalizarCompra, name='finalizarCompra'), 
]