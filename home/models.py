from django.db import models
from catalogo.models import Catalogo

# Create your models here.
class LogisNews(models.Model):
    idNews = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email