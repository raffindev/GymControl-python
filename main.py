# Teste de cadastro.

from utils.arquivos import ler_json, salvar_json
from alunos.cadastro import cadastrar_aluno, cadastrar_base
from alunos.consultas import listar_alunos


alunos = ler_json("dados/alunos.json")
listar_alunos(alunos)
base = cadastrar_base(alunos)
alunos.append(base)
salvar_json("dados/alunos.json", alunos)
cadastro = cadastrar_aluno(base["id"], alunos)