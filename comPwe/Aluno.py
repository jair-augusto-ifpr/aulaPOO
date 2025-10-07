from peewee import *
from database import BaseModel
from Pessoa import Pessoa

class Aluno(Pessoa):
    curso = CharField()

    def __str__(self):
        return f"Aluno: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"
