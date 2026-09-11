# ================================
#  Funções relacionados a alunos
# ================================

from utils.auxiliares import cabeçalho
from utils.validações import validar_opcao
from treinos.informações_treino import treino_atual, mostrar_historico_treino

def menu_treino(cargo, alunos):
    opção_treino = {
    1: treino_atual(alunos),
    2: mostrar_historico_treino(alunos),
    3: atualizar_treino,
    4: criar_treino,
    0: função_sair
}

    print(cabeçalho("Menu de Treinos"))
    while True:
        print('''
1 - Listar treino
2 - Ver histórico
3 - Atualizar treino''')
        if cargo in ("Personal Trainer", "Instrutor"):
            print('4 - Criar treino')
        print('0 - Voltar\n')
        
        opção = validar_opcao(opção_treino, "Escolha o menu desejado: ")
        if cargo not in ("Personal Trainer", "Instrutor") and opção == 4:
            print("Opção inválida para aluno")
            continue

        return opção

def atualizar_treino(opção_menu_treino):
    opção_atualizar_treino = {
    1: atualizar_exercicio,
    2: adicionar_exercicio,
    3: remover_exercicio,
    0: função_sair
}

    print(cabeçalho("Atualização de Treinos"))
    while True:
        print('''
1 - Atualizar exercício
2 - Adicionar exercício
3 - Remover exercício
0 - Voltar
''')
        
        opção = validar_opcao(opção_atualizar_treino, "Escolha o menu desejado: ")
        return opção