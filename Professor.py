from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, temp_exp: str):
        super().__init__(nome, idade)
        self.curso = curso
        self.temp_exp = temp_exp

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}, Tempo de Experiência: {self.temp_exp}"
