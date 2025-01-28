from django.shortcuts import redirect, render
from django.contrib import messages
from .models import LogisNews
from .models import JogoHome
from rest_framework import viewsets
from catalogo.serializers import CatalogoSerializer
from catalogo.models import Catalogo
from .models import Contato

# Create your views here.
def home(request):
    jogos = JogoHome.objects.all()

    contexto = {
        'jogos_lancamento': jogos.filter(eh_lancamento=True),
        'jogos_nintendo': jogos.filter(categoria='nintendo'),
        'jogos_playstation': jogos.filter(categoria='playstation'),
        'jogos_pc': jogos.filter(categoria='pc'),
    }

    return render(
        request,
        'home/index.html',
        contexto
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

def salvar_contato(request):
    if request.method == "POST":
        nome = request.POST.get('name')
        email = request.POST.get('email')
        assunto = request.POST.get('subject')
        mensagem = request.POST.get('message')

        try:
            Contato.objects.create(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
            messages.success(request, "Sua mensagem foi enviada com sucesso!")
        except Exception as e:
            messages.error(request, "Ocorreu um erro ao enviar a mensagem. Tente novamente.")
            print(e)

        return redirect('home')