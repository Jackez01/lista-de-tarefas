from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas, database, models
from database import engine, SessionLocal
from models import Tarefa
from typing import List

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
@app.get('/tarefas/', response_model = List[schemas.TarefaResponse])
def lista_tarefas(db: Session = Depends(get_db)):
    tarefas = db.query(models.Tarefa).all()
    return tarefas
    

# criando a tabela no postgreSQL
database.Base.metadata.create_all(bind=engine)

@app.post('/tarefas/', response_model = schemas.TarefaResponse)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    db_tarefas = models.Tarefa(titulo = tarefa.titulo, descricao = tarefa.descricao, status = tarefa.status)
    db.add(db_tarefas)
    db.commit()
    db.refresh(db_tarefas)
    return db_tarefas

# Criando rota para deletar
@app.delete('/tarefas/{id}')
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    excluir = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()

    db.delete(excluir)
    db.commit()
    return excluir

# Rota Update
@app.put('/tarefas/{id}')
def alterar_tarefas(id: int, db: Session = Depends(get_db)):
   alterar = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
   alterar.titulo = titulo
   alterar.descricao = descricao
   alterar.status = status
