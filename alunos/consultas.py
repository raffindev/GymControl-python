"""
Funções responsáveis pela consulta de dados dos alunos.
"""

from utils.auxiliares import cabeçalho


def verificar_id_aluno(alunos, novo_aluno):
    for aluno in alunos:

        if novo_aluno["id"] == aluno["id"]:
            return True

    return False


def listar_alunos(alunos):
    print(cabeçalho("ALUNOS"))

    for aluno in alunos:
        print(f'\nID: {aluno["id"]}' f'\nNome: {aluno["nome"]}')

        if aluno["ativo"]:
            print("Status: Ativo")

        else:
            print("Status: Inativo")
        print("-" * 25)


def buscar_aluno_por_id(alunos):
    while True:
        try:
            id_aluno = int(input("ID do aluno (0 - Voltar): "))

            if id_aluno == 0:
                return 0

            if id_aluno < 0:
                print("ID inválido.")
                continue

            for aluno in alunos:
                if id_aluno == aluno["id"]:
                    return aluno

            print("Aluno não encontrado.")

        except ValueError:
            print("Digite um ID válido.")
