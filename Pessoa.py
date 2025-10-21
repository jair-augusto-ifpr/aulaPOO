class Pessoa:

    contador_id = 0

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.id = Pessoa.contador_id 
        Pessoa.contador_id  += 1
    def __str__(self):
        return f"(Id: {self.id}) Nome: {self.nome}, Idade: {self.idade}"