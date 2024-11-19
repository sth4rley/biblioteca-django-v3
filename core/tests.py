from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from core.models import Colecao
from django.urls import reverse
from core.models import Livro
from core.models import Autor
from core.models import Categoria

class ColecaoTests(APITestCase):

    def setUp(self):
        # Criação de um usuário e autenticação via token
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.colecao = Colecao.objects.create(
            nome='Coleção de Teste',
            descricao='Descrição da coleção de teste',
            colecionador=self.user
        )

    # Testa a representação de uma coleção
    def test_colecao_str_representation(self):
        # Verifica se o método __str__ retorna a string esperada
        expected_representation = f"{self.colecao.nome} - {self.colecao.colecionador.username}"
        self.assertEqual(str(self.colecao), expected_representation)

 # Testa a criação de uma coleção
    def test_create_colecao(self):
        # Teste para criar uma nova coleção com livros
        url = reverse('colecao-list-create')
        data = {
            'nome': 'Minha Coleção',
            'descricao': 'Descrição da coleção',
            'livros': []
        }
        response = self.client.post(url, data, format='json')

        # Verifique se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Colecao.objects.count(), 2)  # Agora devem existir 2 coleções (uma criada no setUp e outra no teste)
        self.assertEqual(Colecao.objects.last().colecionador, self.user)

class ColecaoPermissoesTests(APITestCase):

    def setUp(self):
        # Criação de dois usuários: um dono da coleção e outro usuário aleatório
        self.user1 = User.objects.create_user(username='owner', password='password123')
        self.user2 = User.objects.create_user(username='otheruser', password='password456')

        # Tokens para ambos os usuários
        self.token_user1 = Token.objects.create(user=self.user1)
        self.token_user2 = Token.objects.create(user=self.user2)

        # Criação de uma coleção associada ao primeiro usuário
        self.colecao = Colecao.objects.create(
            nome='Coleção do Owner',
            descricao='Coleção criada pelo owner',
            colecionador=self.user1
        )

    # teste para verificar se um usuário não autenticado não pode acessar a coleção
    def test_edit_colecao(self):
        url = reverse('colecao-detail', args=[self.colecao.id])
        data = {
            'nome': 'Minha Coleção editada',
            'descricao': 'Descrição da coleção',
            'livros': []
        }
        # Tentar editar com o usuário que não é o dono
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user2.key)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # teste para verificar se o dono da coleção pode editar a coleção
    def test_delete_colecao(self):
        url = reverse('colecao-detail', args=[self.colecao.id])

        # Tentar deletar com o usuário que não é o dono
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user2.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Deletar com o usuário dono da coleção
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user1.key)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_safe_methods(self):
        # URL para o detalhe da coleção
        url = reverse('colecao-detail', args=[self.colecao.id])

        # Teste com métodos seguros sem autenticação
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Teste com métodos seguros autenticado como outro usuário
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user1.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_as_owner(self):
        # Autenticando como o colecionador
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user1.key)
        url = reverse('colecao-detail', args=[self.colecao.id])
        data = {
            'nome': 'Colecao Atualizada',
            'descricao': 'Descrição da coleção',
            'livros': []
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_edit_as_non_owner(self):
        # Autenticando como outro usuário
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user2.key)
        url = reverse('colecao-detail', args=[self.colecao.id])
        data = {
            'nome': 'Tentativa Atualizacao',
            'descricao': 'Descrição da coleção',
            'livros': []
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# Testa a listagem de coleções
class ColecaoListagemTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.token_user1 = Token.objects.create(user=self.user1)

        # Criação de uma coleção associada ao primeiro usuário
        self.colecao = Colecao.objects.create(
            nome='Coleção do User1',
            descricao='Coleção criada pelo User1',
            colecionador=self.user1
        )

    # verifica se um usuário autenticado pode acessar a listagem de coleções
    def test_list_colecoes_authenticated(self):
        url = reverse('colecao-list-create')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_user1.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # verifica se um usuário não autenticado não pode acessar a listagem de coleções
    def test_list_colecoes_unauthenticated(self):
        url = reverse('colecao-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ColecaoUpdateTests(APITestCase):
    def setUp(self):
        # Criação de um usuário e autenticação via token
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Criação de autor e categoria para os livros
        self.autor = Autor.objects.create(nome='Autor 1')
        self.categoria = Categoria.objects.create(nome='Categoria 1')

        # Criação de livros para serem usados na coleção
        self.livro1 = Livro.objects.create(
            titulo='Livro 1',
            autor=self.autor,
            categoria=self.categoria,
            publicado_em='2024-01-01'
        )
        self.livro2 = Livro.objects.create(
            titulo='Livro 2',
            autor=self.autor,
            categoria=self.categoria,
            publicado_em='2024-01-01'
        )

        # Criação de uma coleção associada ao usuário
        self.colecao = Colecao.objects.create(
            nome='Coleção Inicial',
            descricao='Descrição inicial',
            colecionador=self.user
        )
        self.colecao.livros.add(self.livro1)


    def test_update_colecao(self):
        url = reverse('colecao-detail', args=[self.colecao.id])
        data = {
            'nome': 'Coleção Atualizada',
            'descricao': 'Descrição atualizada',
            'livros': [self.livro2.id]
        }

        response = self.client.put(url, data, format='json')

        # Verifique se a resposta foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifique se os dados foram atualizados corretamente
        self.colecao.refresh_from_db()
        self.assertEqual(self.colecao.nome, 'Coleção Atualizada')
        self.assertEqual(self.colecao.descricao, 'Descrição atualizada')
        self.assertEqual(list(self.colecao.livros.all()), [self.livro2])
