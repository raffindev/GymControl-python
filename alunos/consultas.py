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

# Listar alunos
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

# Buscar aluno especifico
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
        
    return None

# Verificar duplicidade do documento
def verificar_duplicidade_documento(dado, alunos):

    for aluno in alunos:
        if aluno["documento"] == dado:
            return True

    return False

# verificar duplicidade dos dados
def verificar_duplicidade_cadastral(dado, campo, alunos):

    for aluno in alunos:
        id_aluno = aluno["id"]
        
        dados_cadastrais = ler_caminho_cadastro(id_aluno)
        if dados_cadastrais.get(campo) == dado:
            return True

    return False
        