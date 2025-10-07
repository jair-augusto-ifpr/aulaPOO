from typing import List
from Aluno import Aluno
from Professor import Professor

class SalaAula:
    def __init__(self, professor: Professor, list_alunos: List[Aluno] = None):
        self.professor = professor
        self.list_alunos = list_alunos if list_alunos is not None else []

    # def adicionar_aluno(self, aluno: Aluno):
    #     self.list_alunos.append(aluno)

    # def listar_alunos(self):
    #     for aluno in self.list_alunos:
    #         print(aluno)

