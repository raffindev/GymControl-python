# =================================
#  Funções de cadastro de aluno.
# =================================

from datetime import date
from dateutil.relativedelta import relativedelta

# Cadastrar aluno - Parte 1: Dados básicos
def dados_iniciais_aluno(alunos):
    # Cadastro ID
    maior_id = 0
    alunos.sort(key=lambda aluno: aluno["id"])

    for aluno in alunos:
        if aluno["id"] >= maior_id:
            maior_id = aluno["id"]

    id_aluno = maior_id + 1

    # Cadastro Nome
    while True:
        nome = input('Nome do Aluno: ').strip().lower()
        palavras = nome.split()

        if len(palavras) < 2:
            print('Digite seu nome e sobrenome!')

        elif not all(palavra.isalpha() for palavra in palavras):
            print("O nome não pode conter caracteres especiais.")

        elif any(nome == aluno["nome"] for aluno in alunos):
            print("Nome já cadastrado. Digite outro nome.")

        else:
            break

    # Cadastro Status
    status = True

    return{
    "id": id_aluno,
    "nome": nome,
    "ativo": status
}

# Cadastrar aluno - Parte 2: Dados pessoais
def dados_pessoais(lista_cadastro):
    # Data de nascimento e Idade
    while True:
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))

            hoje = date.today()

            data_nascimento = date(ano, mes, dia)
            if data_nascimento > hoje:
                print("A data de nascimento não pode ser futura.")
                continue

            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            break

        except ValueError:
            print("Somente números válidos devem ser informados.")

    # Sexo Masculino / Feminino
    while True:
        sexo = input("Digite o Sexo: [M/F] ").upper()
        if sexo not in ("M", "F"):
            print("Sexo inválido")
        else:
            break

    # Documento
    while True:
        cpf = input('Digite seu CPF: ').replace('.','').replace('-','')

        if len(cpf) != 11 or not cpf.isnumeric():
            print("CPF inválido")

        elif any(cpf == aluno["documento"] for aluno in lista_cadastro):
            print('CPF já cadastrado.')
            
        else:
            break

    # Telefone
    while True:
        telefone = input('Digite seu telefone com DDD: ').replace('.','').replace('-','')

        if len(telefone) != 11 or not telefone.isnumeric():
            print("telefone inválido")

        elif any(telefone == aluno["telefone"] for aluno in lista_cadastro):
            print('telefone já cadastrado.')
            
        else:
            break

    # Email
    while True:
        email = input('E-mail: ').lower().strip()

        if email.count('@') != 1:
            print('E-mail inválido.')

        elif not email.split('@')[0]:
            print('E-mail inválido.')

        else:
            apos_arroba = email.split('@')[1]

            if '.' not in apos_arroba:
                print('E-mail inválido.')

            elif any(email == aluno["email"] for aluno in lista_cadastro):
                print('E-mail já cadastrado.')

            else:
                break

    # Endereço
    endereço = {}
    while True:

        endereço["cidade"] = input("Cidade: ").strip()
        if not endereço["cidade"]:
            print("Cidade não pode ficar vazia")
            continue

        endereço["rua"] = input("Rua e número: ").strip()

        endereço["cep"] = input("CEP: ").replace("-", "").strip()

        if len(endereço["cep"]) != 8 or not endereço["cep"].isnumeric():
            print("CEP inválido")
            continue

        break

    return{
    "data_nascimento": str(data_nascimento),
    "idade": idade,
    "sexo": sexo,
    "documento": cpf,
    "telefone": telefone,
    "email": email,
    "endereço": endereço
}

# Cadastrar aluno - Parte 3: Plano e pagamento
def dados_plano_pagamento():
    # Plano do aluno
    while True:
        plano = input('Plano: [Mensal/Trimestral/Anual] ').lower().strip()
        if plano not in ("mensal", "trimestral", "anual"):
            print("Escolha um plano válido.")
        else:
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
        pagamento = input(
            'Pagamento: [Pix/Dinheiro/Cartão de credito/Cartão de debito] '
        ).lower().strip().replace(' ','-')

        if pagamento not in ("pix", "cartão-de-credito", "cartão-de-debito", "dinheiro"):
            print("Método de pagamento inválido.")
            
        else:
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

# Gera a versão resumida do cadastro
def base_aluno(cadastro):
    return {
    "id": cadastro["id"],
    "nome": cadastro["nome"],
    "ativo": cadastro["ativo"]
}

# Junta todas as partes do cadastro
def cadastrar_aluno(alunos, lista_cadastro):

    dados_iniciais = dados_iniciais_aluno(alunos)
    dados_pessoais_aluno = dados_pessoais(lista_cadastro)
    dados_plano = dados_plano_pagamento()

    cadastro = {
        **dados_iniciais,
        **dados_pessoais_aluno,
        **dados_plano
    }

    return cadastro