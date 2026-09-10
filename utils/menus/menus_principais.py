# ===========================================
#  Funções relacionadas a menus principais
# ===========================================

from utils.arquivos import ler_json
from utils.auxiliares import cabeçalho
from operacional.acesso.autenticação import autenticar_aluno

def menu_inicial():
    alunos = ler_json("dados/alunos.json")

    while True:
        print(cabeçalho("GymControl"))
        print(
            """1 - Entrar como aluno
2 - Entrar como funcionário
0 - Sair"""
        )

        try:
            opção = int(input("Escolha uma opção: "))

            if opção not in (1, 2, 0):
                print("Opção inválida.")
                continue

            if opção == 1:
                print("Escolheu opção Aluno")
                aluno = autenticar_aluno(alunos)
                if aluno:
                    print(f'Bem-vindo, {aluno["nome"]}')
                else:
                    break

            if opção == 2:
                print("Autenticação de funcionário ainda não implementada.")
                continue

            if opção == 0:
                print("Encerrando o GymControl...")
                break

        except ValueError:
            print("Por favor, digite uma opção válida.")

