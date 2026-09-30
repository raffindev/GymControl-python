"""
Funções responsáveis pelos menus relacionados aos alunos.
"""

from utils.auxiliares import cabeçalho
from utils.validações import validar_opçao
from treinos.informações_treino import treino_atual, mostrar_historico_treino


def menu_treino(cargo, alunos):
    opçoes_treino = {
        1: treino_atual,
        2: mostrar_historico_treino,
        # 3: atualizar_treino,
    }

    # if cargo in ("Personal Trainer", "Instrutor"):
    # opçoes_treino[4] = criar_treino

    print(cabeçalho("Menu de Treinos"))

    while True:
        print("""
1 - Listar treino
2 - Ver histórico
3 - Atualizar treino""")

        if cargo in ("Personal Trainer", "Instrutor"):
            print("4 - Criar treino")

        print("0 - Voltar\n")

        opçao = validar_opçao(opçoes_treino, "Escolha o menu desejado: ")

        return opçao


def atualizar_treino():
    opçoes_atualizar_treino = {
        # 1: atualizar_exercicio,
        # 2: adicionar_exercicio,
        # 3: remover_exercicio,
    }

    print(cabeçalho("Atualização de Treinos"))

    while True:
        print("""
1 - Atualizar exercício
2 - Adicionar exercício
3 - Remover exercício
0 - Voltar
""")

        opçao = validar_opçao(opçoes_atualizar_treino, "Escolha o menu desejado: ")

        return opçao
