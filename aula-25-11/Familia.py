class Familia:
    ID = 0

    def __init__(self, pai, mae, renda):
        self.id = Familia.ID
        self.filhos = []
        self.pai = pai
        self.mae = mae
        self.renda = renda
        Familia.ID += 1

    def adicionar_filho(self, nome):
        self.filhos.append(nome)

    def renda_media(self):
        num = len(self.filhos) + 2
        return self.renda / num

    def __str__(self):
        ret = f"Família ID: {self.id}\n"
        ret += f"Pai: {self.pai}\n"
        ret += f"Mãe: {self.mae}\n"
        ret += f"Filhos: {self.filhos}\n"
        ret += f"Rendimento: {self.renda}\n"
        ret += f"Per Capita: {self.renda_media()}\n"
        return ret
