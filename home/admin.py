from django.contrib import admin
from .models import JogoHome
# Register your models here.

@admin.register(JogoHome)
class JogoHomeAdmin(admin.ModelAdmin):
    list_display = ('tema', 'categoria', 'eh_lancamento', 'preco')
    list_filter = ('categoria', 'eh_lancamento')
    search_fields = ('tema',)