class Notas:
    def __init__(self, mat: int, port: int, ing: int):
        self.mat = mat
        self.port = port
        self.ing = ing

    def media(self):
        return (self.port + self.mat + self.ing) / 3

    def __str__(self):
        return f"matemática: {self.mat}, português: {self.port} e inglês: {self.ing}. média: {self.media():.2f}"