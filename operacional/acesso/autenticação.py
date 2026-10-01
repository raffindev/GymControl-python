"""
Funções responsáveis pela autenticação de usuários.
"""

from utils.validações import validar_cpf


def autenticar_aluno(alunos):
    tentativa = 0

    while tentativa < 3:
        cpf = input("Digite seu CPF: ")
        cpf = validar_cpf(cpf)
        tentativa += 1

        if cpf is None:
            continue

        for aluno in alunos:
            if aluno["documento"] == cpf:
                return aluno

        print("CPF não encontrado.")

    print("Número máximo de tentativas atingido. Acesso bloqueado.")
