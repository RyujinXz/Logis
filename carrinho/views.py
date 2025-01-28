from django.shortcuts import redirect, render

from catalogo.models import Catalogo
from carrinho.models import ItemCarrinho
import urllib.parse

# Create your views here.
def adicionarCarrinho(request, jogoId):
    jogo = Catalogo.objects.get(id=jogoId)
    item, created = ItemCarrinho.objects.get_or_create(jogo=jogo)
    if not created:
        item.quantidade += 1
    item.save()
    return redirect('carrinho')

def exibirCarrinho(request):
    itens = ItemCarrinho.objects.all()
    total = 0
    for item in itens:
        item.totalPreco = item.jogo.preco * item.quantidade
        total += item.totalPreco

    return render(request, 'carrinho/index.html', {'itens': itens, 'total': total})

def finalizarCompra(request):
    itens = ItemCarrinho.objects.all()
    mensagem = "Resumo da Compra: \n"
    for item in itens:
        mensagem += f"{item.jogo.tema} (x{item.quantidade}): R$ {item.jogo.preco * item.quantidade:.2f}\n"
    mensagem += f"\n Total: R$ {sum(item.jogo.preco * item.quantidade for item in itens):.2f}"

    ItemCarrinho.objects.filter(id__in=[item.id for item in itens]).delete()

    url = f"https://api.whatsapp.com/send?phone=+5521972392745&text={urllib.parse.quote(mensagem)}"
    return redirect(url, target="blank")

def removerCarrinho(request, jogoId):
    itens = ItemCarrinho.objects.filter(id=jogoId)
    if itens.exists():
        item = itens.first()
        if item.quantidade > 1:
            item.quantidade -= 1
            item.save()
        else:
            item.delete()

    return exibirCarrinho(request)