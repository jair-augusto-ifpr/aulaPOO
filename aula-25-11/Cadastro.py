class Cadastro:
    def __init__(self):
        self.familias = []

    def adicionar_familia(self, fam):
        self.familias.append(fam)

    def maior_renda(self):
        maior = -1
        result = None

        for fam in self.familias:
            media = fam.renda_media()
            if media > maior:
                maior = media
                result = fam

        return result
