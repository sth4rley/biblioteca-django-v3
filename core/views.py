from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from .filters import LivroFilter

from rest_framework import generics

# Passo 1: FBV -> CBV

# livro
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter  # Passo 2.4 - Atualizando a view para usar o filtro personalizado
    search_fields = ("^titulo", )
    ordering_fields = ('titulo', 'autor', 'categoria', 'publicado_em') # Passo 2.5 - permite a ordenação por titulo, autor, categoria, publicado_em.
    ordering = ['titulo']
    name = "livro-list"

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

# categoria
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^nome", )
    ordering_fields = ['nome'] # Passo 2.5 - Possibilita a ordenação por nome
    ordering = ['nome']
    name = "categoria-list"

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

# autor
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    search_fields = ("^nome", )
    ordering_fields = ['nome'] # Passo 2.5 - Possibilita a ordenação por nome
    ordering = ['nome']
    name = "autor-list"

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"
