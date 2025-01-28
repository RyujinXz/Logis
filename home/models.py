from django.db import models
from catalogo.models import Catalogo

# Create your models here.
class LogisNews(models.Model):
    idNews = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
    
class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.assunto}"
    
class JogoHome(models.Model):
    CATEGORIAS = [
        ('nintendo', 'Nintendo'),
        ('playstation', 'PlayStation'),
        ('pc', 'PC'),
    ]

    tema = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='jogos_home/')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    eh_lancamento = models.BooleanField(default=False)

    def __str__(self):
        return self.tema