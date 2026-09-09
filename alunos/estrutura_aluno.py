# =======================================================
#  Funções relacionadas a estrutura de cadastro do aluno
# =======================================================

from pathlib import Path
from utils.arquivos import salvar_json, ler_json

def criar_estrutura_aluno(id_aluno, dados):

    # 1. Cria pasta do aluno
    pasta_aluno = Path("dados") / "alunos" / f"{id_aluno:03}"
    pasta_aluno.mkdir(parents=True, exist_ok=True)

    # 2. Cria pasta cadastro
    pasta_cadastro = pasta_aluno / "cadastro"
    pasta_cadastro.mkdir(parents=True, exist_ok=True)

    # 3. Cria dados_cadastrais.json
    caminho_do_arquivo = pasta_cadastro / "dados_cadastrais.json"
    salvar_json(caminho_do_arquivo, dados)

def ler_caminho_cadastro(id_aluno):

    caminho_cadastro = (
        Path("dados")
        / "alunos"
        / f"{id_aluno:03}"
        / "cadastro"
        / "dados_cadastrais.json"
    )

    return ler_json(caminho_cadastro)

def salvar_cadastro_aluno(id_aluno, dados):

    caminho_cadastro = (
        Path("dados")
        / "alunos"
        / f"{id_aluno:03}"
        / "cadastro"
        / "dados_cadastrais.json"
    )

    salvar_json(caminho_cadastro, dados)