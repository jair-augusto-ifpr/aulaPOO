from Livro import Livro

def main():
    l1 = Livro('teste1')
    l2 = Livro('teste2')
    l3 = Livro('teste3')
    l1.adicionar(["A11", "A12", "A13"])
    l2.adicionar(["A21", "A22", "A23"])
    l3.adicionar(["A31", "A32", "A33"])
    print(l1)
    print(l2)
    print(l3)

main()