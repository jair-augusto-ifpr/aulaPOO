from peewee import *
from database import BaseModel

class Pessoa(BaseModel):
    nome = CharField()
    idade = IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"
