# =================================
#  Funções relacionadas a Buscar.
# =================================

# Verificar ID
def verificar_id_aluno(alunos, novo_aluno):
    for aluno in alunos:

        if novo_aluno["id"] == aluno["id"]:
            return True
        
    return False

def listar_alunos(alunos):

    for aluno in alunos:
        print(
            f'\nID: {aluno["id"]}'
            f'\nNome: {aluno["nome"]}'
        )

        if aluno["ativo"]:
            print('Status: Ativo')

        else:
            print('Status: Inativo')
        print('-'*25)

def buscar_aluno_por_id(alunos):
    while True:
        try:
            id_aluno = int(input("ID: "))
            if id_aluno > 0:
                break

        except ValueError:
            print("ID Inválido")

    for aluno in alunos:
        if id_aluno == aluno["id"]:
            return aluno
        
    return "Aluno não encontrado"

