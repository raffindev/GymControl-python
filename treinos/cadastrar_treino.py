"""
Funções responsáveis pela criação de treinos.
"""

from datetime import date, timedelta
from treinos.informações_treino import carregar_treino


def preparar_criação_treino(alunos):
    treino_atual = carregar_treino(alunos, "treino_atual.json")
    historico_treino = carregar_treino(alunos, "historico_treinos.json")

    if historico_treino:
        data_fim = date.today() - timedelta(days=1)
        historico_treino[-1]["data_fim"] = str(data_fim)

    else:
        historico_treino = []

    data_inicio = date.today()
    treino = {"data_inicio": str(data_inicio), "data_fim": None}

    historico_treino.append(treino)

    return treino_atual, historico_treino


def adicionar_treino():
    treino = {}
