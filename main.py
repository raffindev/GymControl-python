# Teste do programa temporariamente

from utils.arquivos import carregar_dados
from alunos.cadastro import cadastrar_base, cadastrar_aluno
from utils.arquivos import salvar_json

alunos, funcionarios = carregar_dados()

base = cadastrar_base(alunos, funcionarios)
alunos.append(base)
cadastro = cadastrar_aluno(base["id"], alunos, funcionarios)
salvar_json("dados/alunos.json", alunos)