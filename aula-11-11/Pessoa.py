class Pessoa:

    id = 0

    def __init__(self, nome):
        self.id = Pessoa.id
        Pessoa.id += 1
        self.nome = nome
    
    def __str__(self):
        return self.nome