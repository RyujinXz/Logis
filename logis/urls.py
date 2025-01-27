from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings
from rest_framework import routers
from catalogo.views import CatalogoViewSet

router = routers.DefaultRouter()
router.register('jogo',CatalogoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('catalogo/', include('catalogo.urls')),
]

#Adicione URLs de autenticação de site Django (para login, logout, gerenciamento de senha)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
