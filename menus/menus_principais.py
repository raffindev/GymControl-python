"""
Funções responsáveis pelo menu principal do sistema.
"""

from utils.arquivos import ler_json
from utils.auxiliares import cabeçalho
from utils.validações import validar_opcao
from operacional.acesso.autenticação import autenticar_aluno


def menu_inicial():
    alunos = ler_json("dados/indice_alunos.json")
    opçoes = {1: "aluno", 2: "funcionario"}

    while True:
        print(cabeçalho("GymControl"))
        print("""1 - Entrar como aluno
2 - Entrar como funcionário
0 - Sair""")

        opcao = validar_opcao(opçoes, "Escolha uma opção: ")

        if opcao == 0:
            print("Encerrando o GymControl...")
            break

        if opcao == "aluno":
            aluno = autenticar_aluno(alunos)

            if aluno:
                print(f'Bem-vindo, {aluno["nome"]}')

        elif opcao == "funcionario":
            print("Autenticação de funcionário ainda não implementada.")
