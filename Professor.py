from Aluno import Aluno

class Professor(Aluno):
    def __init__(self, nome: str, idade: int, curso: str, temp_exp: str):
        super().__init__(nome, idade, curso)
        self.temp_exp = temp_exp

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}, Tempo de Experiência: {self.temp_exp}"
