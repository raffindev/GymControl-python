# ==============================================
#  Funções relacionadas a informações do treino
# ==============================================

from alunos.consultas import buscar_aluno_por_id
from utils.auxiliares import cabeçalho
from utils.arquivos import ler_json
from utils.validações import validar_opcao
from pathlib import Path

def carregar_treino(alunos, arquivo):
    aluno = buscar_aluno_por_id(alunos)
    if aluno == 0:
        return None
    
    id_aluno = aluno["id"]

    caminho_treino = (
        Path("dados")
        / "alunos"
        / f"{id_aluno:03}"
        / "treinos"
        / arquivo
    )

    treinos = ler_json(caminho_treino)
    if treinos:
        return treinos
    
    return None

def escolher_treino_atual(treinos):
    opções = {}

    for numero, treino in treinos.items():
        opções[int(numero)] = treino

    for numero, treino in opções.items():
        print(numero, "-", treino["nome"])

    print("\n0 - Voltar")

    treino = validar_opcao(opções, "Escolha o treino desejado: ")
    if treino == 0:
        print("Voltando para o menu anterior.")
        return

    return treino


def mostrar_detalhes_treino(treino):
    print(f'\nTreino: {treino["nome"]}')

    for numero, exercicio in enumerate(treino["exercicios"], start=1):

        print(f"\n{numero:02} - {exercicio['nome_exercicio']}")
        print(f"     Séries: {exercicio['series']}")
        print(f"     Repetições: {exercicio['repeticoes']}")
        print(f"     Carga: {exercicio['carga']} kg")
        print('-'*40)


def treino_atual(alunos):
    treinos = carregar_treino(alunos, "treino_atual.json")
    if treinos is None:
        return

    treino = escolher_treino_atual(treinos)
    if treino is None:
        return

    print(cabeçalho("Treino Atual"))   
    mostrar_detalhes_treino(treino)

def mostrar_historico_treino(alunos):

    treinos = carregar_treino(alunos, "historico_treinos.json")
    if treinos is None:
        return

    print(cabeçalho("Histórico de Treinos"))

    for ficha in treinos:
        print(
            f'Início: {ficha["data_inicio"]} - '
            f'Fim: {ficha["data_fim"]}'
        )

        for treino in ficha["treinos"].values():
            mostrar_detalhes_treino(treino)
