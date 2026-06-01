# API de Gerenciamento de Tarefas

API REST desenvolvida com **FastAPI**, **PostgreSQL** e **SQLAlchemy** para gerenciamento de tarefas. O projeto permite criar, listar, atualizar e remover tarefas por meio de endpoints REST, seguindo boas práticas de desenvolvimento backend.

## Funcionalidades

- Criar tarefas
- Listar todas as tarefas
- Atualizar tarefas existentes
- Remover tarefas
- Validação de dados com Pydantic
- Integração com PostgreSQL
- Documentação automática com Swagger

## Tecnologias Utilizadas

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Estrutura do Projeto

```text
lista-de-tarefas/
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── requirements.txt
└── venv/
```

## Instalação

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

Crie um banco PostgreSQL chamado:

```sql
CREATE DATABASE lista_de_tarefas;
```

Configure a string de conexão em `database.py`:

```python
DATABASE_URL = "postgresql://usuario:senha@localhost/lista_de_tarefas"
```

## Executando o Projeto

Inicie o servidor:

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000
```

## Documentação da API

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Endpoints

### Listar tarefas

```http
GET /tarefas/
```

### Criar tarefa

```http
POST /tarefas/
```

Exemplo de requisição:

```json
{
  "titulo": "Estudar FastAPI",
  "descricao": "Aprender CRUD com FastAPI",
  "status": "Pendente"
}
```

### Atualizar tarefa

```http
PUT /tarefas/{id}
```

### Deletar tarefa

```http
DELETE /tarefas/{id}
```

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Desenvolvimento de APIs REST
- Integração com PostgreSQL
- SQLAlchemy ORM
- Modelagem de dados
- Operações CRUD
- Validação com Pydantic
- Injeção de dependências com FastAPI
- Documentação automática com Swagger

## Próximas Melhorias

- Autenticação com JWT
- Paginação de resultados
- Filtros de busca
- Testes automatizados
- Dockerização da aplicação

## Autor

**Lucas Geraldi Freitas**

LinkedIn: [www.linkedin.com/in/lucas-geraldi-freitas](https://www.linkedin.com/in/lucasgeraldi/)
