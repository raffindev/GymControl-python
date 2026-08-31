from utils.arquivos import ler_json, salvar_json
from alunos.cadastro import cadastrar_aluno, base_aluno


alunos = ler_json("dados/alunos.json")
lista_cadastro = ler_json("dados/cadastro.json")

cadastro = cadastrar_aluno(lista_cadastro, alunos)

base = base_aluno(cadastro)

alunos.append(base)
lista_cadastro.append(cadastro)

salvar_json("dados/alunos.json", alunos)
salvar_json("dados/cadastro.json", lista_cadastro)