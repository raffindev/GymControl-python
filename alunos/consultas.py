# =================================
#  Funções relacionadas a Buscar.
# =================================

# Verificar ID
def verificar_id_aluno(alunos, novo_aluno):
    for aluno in alunos:

        if novo_aluno["id"] == aluno["id"]:
            return True
        
    return False