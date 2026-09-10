# ===========================================
#  Funções relacionadas a autenticação
# ===========================================

from alunos.consultas import cpf_validacao

def autenticar_aluno(alunos):
    tentativa = 0

    while tentativa < 3:
        cpf = cpf_validacao()
        tentativa += 1

        for aluno in alunos:
            if aluno["documento"] == cpf:
                return aluno

        print("CPF não encontrado.")

    print("Número máximo de tentativas atingido. Acesso bloqueado.")