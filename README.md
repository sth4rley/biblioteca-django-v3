# Exercício Prático - Unidade 6 - Trilha Backend

**Nome:** Stharley Santos Leite

## Instruções

### 1. Clone do Repositório

```bash
git clone https://github.com/sth4rley/biblioteca-django-v2
cd biblioteca-django-v2
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
