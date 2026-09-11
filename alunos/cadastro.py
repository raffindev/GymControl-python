# =================================
#  Funções de cadastro de aluno.
# =================================

from datetime import date
from dateutil.relativedelta import relativedelta

from alunos.estrutura_aluno import criar_estrutura_aluno, ler_caminho_cadastro, salvar_cadastro_aluno

from utils.validações import (
    validar_nome,
    cpf_validacao,
    validar_data_nascimento,
    validar_opção_sexual,
    validar_telefone,
    validar_email,
    validar_endereço,
    validar_plano,
    validar_metodo_pagamento,
    verificar_duplicidade_documento
)

# Cadastrar aluno - Parte 1: Dados iniciais
def dados_iniciais_aluno(alunos, funcionarios):
    # Cadastro ID
    maior_id = 0
    alunos.sort(key=lambda aluno: aluno["id"])

    for aluno in alunos:
        if aluno["id"] >= maior_id:
            maior_id = aluno["id"]

    id_aluno = maior_id + 1

    # Cadastro Nome
    while True:
        nome = input('Nome do Aluno: ')
        nome = validar_nome(nome, alunos)

        if nome:
            break

    # Documento
    while True:
        cpf = input('Digite seu CPF: ')
        cpf = cpf_validacao(cpf)

        if cpf is None:
            continue

        if verificar_duplicidade_documento(cpf, alunos, funcionarios):
            print("CPF já cadastrado.")
            continue

        break

    # Cadastro Status
    status = True

    return{
    "id": id_aluno,
    "nome": nome,
    "documento": cpf,
    "ativo": status
}

# Cadastrar aluno - Parte 2: Dados pessoais
def dados_pessoais(dados_cadastrais, alunos, funcionarios):
    # Data de nascimento e Idade
    data_nascimento, idade = validar_data_nascimento()

    # Sexo Masculino / Feminino
    while True:
        sexo = input("Digite o Sexo: [M/F/Outros] ")
        sexo = validar_opção_sexual(sexo)

        if sexo:
            break

    # Telefone
    while True:
        telefone = input('Digite seu telefone com DDD: ')
        telefone = validar_telefone(telefone, alunos, funcionarios)

        if telefone:
            break

    # Email
    while True:
        email = input('E-mail: ')
        email = validar_email(email, alunos, funcionarios)

        if email:
            break

    # Endereço
    while True:
            cidade = input("Cidade: ")
            logradouro = input("Logradouro: ")
            numero = input("Número: ")
            cep = input("CEP: ")

            endereço = validar_endereço(cidade, logradouro, numero, cep)
            if endereço:
                break

    return{
    "data_nascimento": str(data_nascimento),
    "idade": idade,
    "sexo": sexo,
    "telefone": telefone,
    "email": email,
    "endereço": endereço
}

# Cadastrar aluno - Parte 3: Plano e pagamento
def dados_plano_pagamento():
    # Plano do aluno
    while True:
        plano = input('Plano: [Mensal/Trimestral/Anual] ')
        plano = validar_plano(plano)

        if plano:
            break

    # Data de início
    data_inicio = date.today()

    # Data de vencimento
    if plano == "mensal":
        data_vencimento = data_inicio + relativedelta(months=1)

    elif plano == "trimestral":
        data_vencimento = data_inicio + relativedelta(months=3)

    elif plano == "anual":
        data_vencimento = data_inicio + relativedelta(years=1)

    # Método de pagamento
    while True:
        pagamento = input('Pagamento: [Pix/Dinheiro/Cartão de crédito/Cartão de débito] ')
        pagamento = validar_metodo_pagamento(pagamento)

        if pagamento:
            break

    # Status inicial do pagamento
    status_pagamento = "pago" 

    return {
    "plano": {
        "tipo": plano,
        "data_inicio": str(data_inicio),
        "data_vencimento": str(data_vencimento),
        "metodo_pagamento": pagamento,
        "status_pagamento": status_pagamento
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
    dados_pessoais_aluno = dados_pessoais(dados_cadastrais, alunos, funcionarios)
    dados_plano = dados_plano_pagamento()

    dados_cadastrais.update(dados_pessoais_aluno)
    dados_cadastrais.update(dados_plano)

    salvar_cadastro_aluno(id_aluno, dados_cadastrais)

    return dados_cadastrais