from .models import Livro, Categoria, Autor, Colecao
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer, ColecaoSerializer
from .filters import LivroFilter
from rest_framework import generics, permissions
from .serializers import ColecaoSerializer
from . import custom_permissions
from rest_framework.authentication import TokenAuthentication

# livro
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ("^titulo", )
    ordering_fields = ('titulo', 'autor', 'categoria', 'publicado_em')
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
    ordering_fields = ['nome']
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
    ordering_fields = ['nome']
    ordering = ['nome']
    name = "autor-list"

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

# Listagem e Cadastro de Coleções
class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-list-create"
    permission_classes = [permissions.IsAuthenticated]  # Segundo enunciado, apenas usuarios autenticados podem acessar todas as coleções de livros (de todos os colecionadores)
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        # Define o usuário autenticado como o colecionador
        serializer.save(colecionador=self.request.user)

# Recuperação, Edição e Exclusão de Coleção
class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-detail"
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )
    authentication_classes = [TokenAuthentication]
