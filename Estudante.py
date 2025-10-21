from Pessoa import Pessoa
from Notas import Notas

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, notas: Notas):
        super().__init__(nome, idade)
        self.curso = curso
        self.notas = notas

    def __str__(self):
        return f"(Id: {self.id}) Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}, Notas: ({self.notas})"