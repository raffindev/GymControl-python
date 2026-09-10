# =================================
#  Funções relacionadas a Buscar.
# =================================

from alunos.estrutura_aluno import ler_caminho_cadastro

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


def verificar_duplicidade_documento(dado, alunos):

    for aluno in alunos:
        if aluno["documento"] == dado:
            return True

    return False

def verificar_duplicidade_cadastral(dado, campo, alunos):

    for aluno in alunos:
        id_aluno = aluno["id"]
        
        dados_cadastrais = ler_caminho_cadastro(id_aluno)
        if dados_cadastrais.get(campo) == dado:
            return True

    return False

def cpf_validacao():
    while True:
        cpf = input('Digite seu CPF: ').replace('.', '').replace('-', '')

        if len(cpf) != 11 or not cpf.isnumeric():
            print("CPF inválido")
        else:
            return cpf

        