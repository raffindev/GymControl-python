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

    # 3. Salva dados cadastrais
    caminho_cadastro = pasta_cadastro / "dados_cadastrais.json"
    salvar_json(caminho_cadastro, dados)

    # 4. Cria pasta treinos
    pasta_treinos = pasta_aluno / "treinos"
    pasta_treinos.mkdir(parents=True, exist_ok=True)

    # 5. Cria arquivos de treinos
    salvar_json(pasta_treinos / "treino_atual.json", {})
    salvar_json(pasta_treinos / "historico_treinos.json", [])

    # 6. Cria pasta avaliações
    pasta_avaliacoes = pasta_aluno / "avaliações"
    pasta_avaliacoes.mkdir(parents=True, exist_ok=True)

    # 7. Cria arquivos de avaliações
    salvar_json(pasta_avaliacoes / "avaliacao_atual.json", {})
    salvar_json(pasta_avaliacoes / "historico_avaliacoes.json", [])

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