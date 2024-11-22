# Exercício Prático - Unidade 9 - Trilha Backend

**Exercício Prático 3:** Exposição Virtual de Coleções, Autenticação e Testes Automatizados.

**Nome:** Stharley Santos Leite


## Objetivos
- ✅ Implementar um modelo de coleção de livros associado a um usuário (colecionador).
- ✅ Adicionar autenticação baseada em Token e permissões para garantir que apenas o colecionador possa gerenciar sua coleção.
- ✅ Documentar a API com drf-spectacular.
- ✅ Desenvolver testes automatizados para a funcionalidade de coleções


## Instruções 

### 1. Clone do Repositório

```bash
git clone https://github.com/sth4rley/biblioteca-django-v3
cd biblioteca-django-v3
```

### 2. Criação do Ambiente Virtual e Instalação de Dependências

```bash
python -m venv venv
```
Para ativar o ambiente virtual, execute:

- No Linux/macOS:
  ```bash
  source venv/bin/activate
  ```
- No Windows:
  ```bash
  venv\Scripts\activate
  ```

Agora, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 3. Migrações e População do Banco de Dados

Execute os seguintes comandos para criar as migrações e popular o banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db
```

### 4. Executar o Servidor

Por fim, inicie o servidor com o comando:

```bash
python manage.py runserver
```

## Documentação Interativa (Swagger)

A API conta com uma documentação interativa gerada automaticamente pelo drf-spectacular. Ao iniciar o servidor Django, você poderá acessar a documentação em: http://localhost:8000/api/docs/

## Testes Unitários
O projeto possui testes automatizados para verificar o funcionamento da API. Para executá-los, use o comando:
```bash
python manage.py test
```

