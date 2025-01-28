from django.shortcuts import render
from rest_framework import viewsets
from catalogo.serializers import CatalogoSerializer
from catalogo.models import Catalogo

# Create your views here.
def jogo(request):
    contexto = {
        'title' : 'Catálogo | Logis',
        'jogos': Catalogo.objects.all(),
    }

    return render(
        request,
        'catalogo/index.html',
        contexto,
    )

class CatalogoViewSet(viewsets.ModelViewSet):
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer
