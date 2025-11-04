from Estudante import Estudante

class Ordenacao:


    def ordenar_notas(lista):
        dc = {}

        for i, est in enumerate(lista):
            dc[i] = [est]
            print(dc[i])

        chaves = list(dc.keys())

        for i in range(len(chaves)):
            for j in range(i + 1, len(chaves)):
                if chaves[i] < chaves[j]:
                    temp = chaves[i]
                    chaves[i] = chaves[j]
                    chaves[j] = temp

        dc_ordenado = {}
        for chave in chaves:
            dc_ordenado[chave] = dc[chave]
            # print(dc_ordenado[chave].nome)

        return dc_ordenado