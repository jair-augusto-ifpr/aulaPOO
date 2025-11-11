from Pessoa import Pessoa
class Livro:
    id = 0
    def __init__(self, nome):
        self.id = Livro.id
        Livro.id += 1
        self.nome = nome
        self.autores = []

    def __str__(self):
        str = self.nome
        for autor in self.autores:
            str += f"\n - {autor}"
        return str

    def adicionar(self, nomes):
        for nome in nomes:
            autor = Pessoa(nome)
            self.autores.append(autor)
