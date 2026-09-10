# ===========================================
#  Funções relacionadas a autenticação
# ===========================================

from utils.validações import cpf_validacao

def autenticar_aluno(alunos):
    tentativa = 0

    while tentativa < 3:
        cpf = input('Digite seu CPF: ')
        cpf = cpf_validacao(cpf)
        tentativa += 1

        for aluno in alunos:
            if aluno["documento"] == cpf:
                return aluno

        print("CPF não encontrado.")

    print("Número máximo de tentativas atingido. Acesso bloqueado.")