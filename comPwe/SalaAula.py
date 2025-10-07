from peewee import *
from database import BaseModel
from Professor import Professor
from Aluno import Aluno

class SalaAula(BaseModel):
    professor = ForeignKeyField(Professor, backref='salas')
    alunos = ManyToManyField(Aluno, backref='salas')

SalaAluno = SalaAula.alunos.get_through_model()
