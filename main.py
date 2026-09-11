# Teste do programa temporariamente

from utils.arquivos import carregar_dados, salvar_json
from alunos.cadastro import cadastrar_base, cadastrar_aluno


alunos, funcionarios = carregar_dados()
base = cadastrar_base(alunos, funcionarios)
alunos.append(base)

cadastro = cadastrar_aluno(base["id"], alunos, funcionarios)
salvar_json("dados/indice_alunos.json", alunos)