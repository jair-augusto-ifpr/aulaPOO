from peewee import *
from Aluno import Aluno

class Professor(Aluno):
    tempo_experiencia = CharField()

    def __str__(self):
        return f"Professor: {self.nome}, Idade: {self.idade}, Curso: {self.curso}, Exp: {self.tempo_experiencia}"
