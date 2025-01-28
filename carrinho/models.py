from django.db import models
from catalogo.models import Catalogo

# Create your models here.

class ItemCarrinho(models.Model): 
    id = models.AutoField(primary_key=True)
    jogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    adicionado_em = models.DateTimeField(auto_now_add=True)