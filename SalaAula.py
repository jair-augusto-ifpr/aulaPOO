from typing import List
from Estudante import Estudante
from Professor import Professor

class SalaAula:
    def __init__(self, professor: Professor, list_estudantes: List[Estudante] = None):
        self.professor = professor
        self.list_estudantes = list_estudantes if list_estudantes is not None else []

    def media_idade(self):
        total_idade = 0
        for estudante in self.list_estudantes:
            total_idade += int(estudante.idade)
        idade_media = total_idade / len(self.list_estudantes)
        print(f"A média de idade da sala é {idade_media}")

    def adicionar_estudantes(self, list_estudantes):
        self.list_estudantes = list_estudantes

        for est in list_estudantes:
            print(est)

        print('estudantes adicionados com sucesso!')
