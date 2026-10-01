"""
Funções responsáveis pelo cadastro de alunos.
"""

from datetime import date
from dateutil.relativedelta import relativedelta

from alunos.estrutura_aluno import (
    criar_estrutura_aluno,
    ler_caminho_cadastro,
    salvar_cadastro_aluno,
)

from utils.validações import (
    validar_nome,
    validar_cpf,
    validar_data_nascimento,
    validar_sexo,
    validar_telefone,
    validar_email,
    validar_endereço,
    validar_plano,
    validar_metodo_pagamento,
    verificar_duplicidade_documento,
)


# Cadastrar aluno - Parte 1: Dados iniciais
def dados_iniciais_aluno(alunos, funcionarios):
    maior_id = 0
    alunos.sort(key=lambda aluno: aluno["id"])

    for aluno in alunos:
        if aluno["id"] >= maior_id:
            maior_id = aluno["id"]

    id_aluno = maior_id + 1

    while True:
        nome = input("Nome do Aluno: ")
        nome = validar_nome(nome, alunos)

        if nome:
            break

    while True:
        cpf = input("Digite seu CPF: ")
        cpf = validar_cpf(cpf)

        if cpf is None:
            continue

        if verificar_duplicidade_documento(cpf, alunos, funcionarios):
            print("CPF já cadastrado.")
            continue

        break

    status = True

    return {"id": id_aluno, "nome": nome, "documento": cpf, "ativo": status}


# Cadastrar aluno - Parte 2: Dados pessoais
def dados_pessoais(alunos, funcionarios):
    data_nascimento, idade = validar_data_nascimento()

    while True:
        sexo = input("Digite o Sexo: [M/F/Outros] ")
        sexo = validar_sexo(sexo)

        if sexo:
            break

    while True:
        telefone = input("Digite seu telefone com DDD: ")
        telefone = validar_telefone(telefone, alunos, funcionarios)

        if telefone:
            break

    while True:
        email = input("E-mail: ")
        email = validar_email(email, alunos, funcionarios)

        if email:
            break

    while True:
        cidade = input("Cidade: ")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        cep = input("CEP: ")

        endereço = validar_endereço(cidade, logradouro, numero, cep)
        if endereço:
            break

    return {
        "data_nascimento": str(data_nascimento),
        "idade": idade,
        "sexo": sexo,
        "telefone": telefone,
        "email": email,
        "endereço": endereço,
    }


# Cadastrar aluno - Parte 3: Plano e pagamento
def dados_plano_pagamento():
    while True:
        plano = input("Plano: [Mensal/Trimestral/Anual] ")
        plano = validar_plano(plano)

        if plano:
            break

    data_inicio = date.today()

    if plano == "mensal":
        data_vencimento = data_inicio + relativedelta(months=1)

    elif plano == "trimestral":
        data_vencimento = data_inicio + relativedelta(months=3)

    elif plano == "anual":
        data_vencimento = data_inicio + relativedelta(years=1)

    while True:
        pagamento = input(
            "Pagamento: [Pix/Dinheiro/Cartão de crédito/Cartão de débito] "
        )
        pagamento = validar_metodo_pagamento(pagamento)

        if pagamento:
            break

    status_pagamento = "pago"

    return {
        "plano": {
            "tipo": plano,
            "data_inicio": str(data_inicio),
            "data_vencimento": str(data_vencimento),
            "metodo_pagamento": pagamento,
            "status_pagamento": status_pagamento,
        }
    }


# Cadastra a parte inicial do aluno
def cadastrar_base(alunos, funcionarios):
    dados_iniciais = dados_iniciais_aluno(alunos, funcionarios)
    criar_estrutura_aluno(dados_iniciais["id"], dados_iniciais)

    return dados_iniciais


# Junta todas as partes do cadastro
def cadastrar_aluno(id_aluno, alunos, funcionarios):
    dados_cadastrais = ler_caminho_cadastro(id_aluno)
    dados_pessoais_aluno = dados_pessoais(alunos, funcionarios)
    dados_plano = dados_plano_pagamento()

    dados_cadastrais.update(dados_pessoais_aluno)
    dados_cadastrais.update(dados_plano)

    salvar_cadastro_aluno(id_aluno, dados_cadastrais)

    return dados_cadastrais
