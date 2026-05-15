from sqlalchemy import create_engine #cria uma conexão com o PostgreSQL
from sqlalchemy.ext.declarative import declarative_base #cria a classe base dos models
from sqlalchemy.orm import sessionmaker # cria as sessões para executar CRUD

# criar a URL
DATABASE_URL = "postgresql://postgres:lucas0612@localhost:5432/lista_de_tarefas"
# Criar a engine
engine = create_engine(DATABASE_URL)

# essas sessões devem usar essa conexão com o banco de dados 
SessionLocal = sessionmaker(bind=engine)

# Classe mãe
Base = declarative_base()