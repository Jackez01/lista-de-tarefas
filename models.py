from database import Base
from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship


# classe tarefa, contendo os seguintes campos
class Tarefa(Base):
    __tablename__ = 'tarefas'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String)
    status = Column(String)

