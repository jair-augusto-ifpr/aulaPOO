from SalaAula import SalaAula
from Professor import Professor
from Estudante import Estudante
from Notas import Notas
import os
import csv

def add_est(nome, idade, curso, mat, port, ing):
    notas = Notas(mat=mat, port=port, ing=ing)
    estudante = Estudante(nome=nome, idade=idade, curso=curso, notas=notas)
    return estudante

def ler_config():
    arq_csv = "alunos.csv"
    list_estudantes = []
    if os.path.exists(arq_csv):
        with open(arq_csv, mode='r', encoding='utf-8') as arquivo:
            estudantes = csv.reader(arquivo)
            next(estudantes, None)
            for estudante in estudantes:
                nome, idade, curso, mat, port, ing = estudante
                if curso == 'info':
                    est = add_est(nome, idade, curso, mat, port, ing)
                    list_estudantes.append(est)
            return list_estudantes
    else:
        print(f"Arquivo {arq_csv} não encontrado.")
        

if __name__ == "__main__":
    professor = Professor(nome="João", idade="18", curso="info", temp_exp="10")
    sala = SalaAula(professor=professor)
    list_estudantes = ler_config()
    sala.adicionar_estudantes(list_estudantes)