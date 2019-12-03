from django.shortcuts import render
from django.views.generic import ListView,UpdateView,CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.
class ProdutosCreateView(CreateView):
    template_name = "criarbolos.html"
    form_class = InsereBoloForm
    success_url = reverse_lazy("lista_produtos")


class ProdutosListView(ListView):
    template_name = "lista_produtos.html"
    model = ModelDoces
    context_object_name = "produtos"

def filtrar_produto(request,pk):
    context = {}
    try:
        context["produtos"] = ModelDoces.objects.all().filter(categoria__pk=pk)
        context["categorias"] = ModelCategoria.objects.all()
    except:
        return render(request,"lista_produtos.html")
    return render(request,"filtrarProdutos.html",context)

class ProdutosUpdateView(UpdateView):
    template_name = "updatedebolos.html"
    model = ModelDoces
    fields = [
        'nome',
        'preco',
        'descricao'
    ]
    success_url = reverse_lazy("todosProdutos")