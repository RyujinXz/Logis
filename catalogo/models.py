from django.db import models

# Create your models here.
class Catalogo(models.Model):
    id   = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30)
    foto = models.ImageField()
    conteudo = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.tema
