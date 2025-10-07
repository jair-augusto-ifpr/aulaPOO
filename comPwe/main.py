from Aluno import Aluno
from Professor import Professor
from database import criar_tabelas
from SalaAula import SalaAula

def criar_aluno():
    print("\n Criar novo aluno:")

    nome = input("Informe o nome do aluno: ")
    idade = int(input("Informe a idade do aluno: "))
    curso = input("Informe o curso do aluno: ")

    aluno = Aluno.create(nome=nome, idade=idade, curso=curso)
    print("Aluno cadastrado com sucesso!\n")
    print(aluno, "\n")

def listar_estudantes():
    print("\n Lista de Estudantes:")
    alunos = Aluno.select()
    if alunos.count() == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. {aluno}")
    print("\n")

def menu():
    criar_tabelas()

    while True:
        print("===== MENU PRINCIPAL =====")
        print("1. Criar Estudante")
        print("2. Listar Estudante")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_aluno()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
