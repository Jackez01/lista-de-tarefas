from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas, database, models
from database import engine, SessionLocal
from models import Tarefa

# variavavel do app
app = FastAPI()

# Conexão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#criando a rota
@app.get('/tarefas/')
def lista_tarefas():
    tarefas = {'Tarefa': 'Lavar a casa'}
    return tarefas

# criando a tabela no postgreSQL
database.Base.metadata.create_all(bind=engine)

@app.post('/tarefas/')
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    db_tarefas = models.Tarefa(titulo = tarefa.titulo, descricao = tarefa.descricao, status = tarefa.status)
    db.add(db_tarefas)
    db.commit()
    db.refresh(db_tarefas)
    return db_tarefas