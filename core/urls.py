from django.urls import path
from . import views
from .views import ColecaoListCreate, ColecaoDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [

    path('livros/', views.LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),

    path('categorias/', views.CategoriaList.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),

    path('autores/', views.AutorList.as_view(), name='autores-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),

    path('colecoes/', ColecaoListCreate.as_view(), name='colecao-list-create'),
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),

    # Documentação da API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
