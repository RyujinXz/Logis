from django.shortcuts import redirect, render
from .models import LogisNews
from rest_framework import viewsets
from catalogo.serializers import CatalogoSerializer
from catalogo.models import Catalogo
import urllib.parse

# Create your views here.
def home(request):
    return render(
        request,
        'home/index.html'
    )

destinatarios = LogisNews.objects.all()

def cadastro(request):
    destinatarios = LogisNews.objects.all()

    contexto = {
    'title': 'Logis - Início',
    'destinario': destinatarios
    }

    return render(
        request,
        'home/index.html',
        contexto
    )   
    
def gravar(request):
    novoEnvio = LogisNews()
    novoEnvio.email = request.POST.get('email')
    novoEnvio.nome = request.POST.get('nome')
    novoEnvio.save()

    destinatarios = LogisNews.objects.all()

    contexto = {
    'title': 'Logis - Início',
    'destinario': destinatarios
    }

    return render(
        request,
        'home/index.html',
        contexto
    )

def sessao(request):
       
    if request.method == 'POST':
        # Obtém o valor do campo de formulário
        sessao = request.POST.get('usuario')


        # Define a chave na sessão com o valor obtido
        request.session['login'] = sessao


    return render(
        request,
        'home/sessao.html',
    )


def exibir_valor(request):


    # Obtenha o valor da sessão
    # Defina um valor padrão se a sessão estiver vazia
    login = request.session.get('login', 'Nenhum valor definido')
      
    contexto = {'login': login}
   
    return render(
        request,
        'home/exibir_valor.html',
        contexto,
    )

def encerrar_sessao(request):
    # Use o método clear() para limpar todos os dados da sessão
    request.session.clear()
    
    return exibir_valor(request)



