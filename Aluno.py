from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str):
        super().__init__(nome, idade)
        self.curso = curso

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"
