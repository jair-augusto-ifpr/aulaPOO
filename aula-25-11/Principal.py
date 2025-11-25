from Cadastro import Cadastro
from Familia import Familia

class Principal:

    def main():
        cadastro = Cadastro()
        F1 = Familia("P1", "M1", 4000)
        F1.adicionar_filho("F1")
        F1.adicionar_filho("F2")
        F1.adicionar_filho("F3")
        cadastro.adicionar_familia(F1)

        F2 = Familia("P2", "M2", 4000)
        F2.adicionar_filho("F4")
        F2.adicionar_filho("F5")
        cadastro.adicionar_familia(F2)

        F3 = Familia("P3", "M3", 4000)
        F3.adicionar_filho("F6")
        cadastro.adicionar_familia(F3)

        maior = cadastro.maior_renda()
        print("Família com maior renda per capita:")
        print(maior)


    main()
