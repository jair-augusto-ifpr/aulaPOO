class Ordenacao:

    def ordenar_notas(lista):
        dc = {}

        for i, est in enumerate(lista):
            dc[i] = [est]

        chaves = list(dc.keys())

        for i in range(len(chaves)):
            for j in range(i + 1, len(chaves)):
                media_i = dc[chaves[i]][0].notas.media()
                media_j = dc[chaves[j]][0].notas.media()

                if media_j > media_i:
                    temp = chaves[i]
                    chaves[i] = chaves[j]
                    chaves[j] = temp

        dc_ordenado = {}
        for chave in chaves:
            dc_ordenado[chave] = dc[chave]
            est = dc_ordenado[chave][0]
            print(f"{est.nome} - Média: {est.notas.media():.2f}")

        return dc_ordenado