# ============================================
#  Funções relacionadas a validações de dados
# ============================================

from datetime import date
from alunos.consultas import verificar_duplicidade_cadastral

# Validar Nome
def validar_nome(nome, alunos):
    nome = nome.strip().title()
    palavras = nome.split()

    if len(palavras) < 2:
        print("Digite seu nome e sobrenome!")

    elif not all(palavra.isalpha() for palavra in palavras):
        print("O nome não pode conter caracteres especiais.")

    elif any(nome == aluno["nome"] for aluno in alunos):
        print("Nome já cadastrado. Digite outro nome.")

    else:
        return nome

# Validar Cpf
def cpf_validacao(cpf):
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11 or not cpf.isnumeric():
        print("CPF inválido")
        return None

    return cpf

# Data de nascimento e Idade
def validar_data_nascimento():
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

            return data_nascimento, idade

        except ValueError:
            print("Somente números válidos devem ser informados.")

# Validar Sexo
def validar_opção_sexual(sexo):
    sexo = sexo.capitalize()
    if sexo not in ("M", "F", "Outros"):
        print("Sexo inválido")
    else:
        return sexo

# Validar Telefone
def validar_telefone(telefone, alunos):
    telefone = telefone.replace('.', '').replace('-', '')

    if len(telefone) != 11 or not telefone.isnumeric():
        print("Telefone inválido")
        return None

    if verificar_duplicidade_cadastral(telefone, "telefone", alunos):
        print("Telefone já cadastrado.")
        return None

    return telefone

# Validar Email
def validar_email(email, alunos):
    email = email.lower().strip()

    if email.count('@') != 1:
        print('E-mail inválido.')
        return None

    elif not email.split('@')[0]:
        print('E-mail inválido.')
        return None

    else:
        apos_arroba = email.split('@')[1]

        if '.' not in apos_arroba:
            print('E-mail inválido.')
            return None

        elif verificar_duplicidade_cadastral(email, "email", alunos):
            print('E-mail já cadastrado.')
            return None

    return email

# Validar Endereço
def validar_endereço(cidade, logradouro, numero, cep):
    cidade = cidade.strip().title()
    logradouro = logradouro.strip().title()
    numero = numero.strip()
    cep = cep.replace(".", "").replace("-", "").strip()

    if not cidade:
        print("Cidade inválida.")
        return None

    if not logradouro:
        print("Logradouro inválido.")
        return None

    if len(cep) != 8 or not cep.isnumeric():
        print("CEP inválido.")
        return None

    return {
        "cidade": cidade,
        "logradouro": logradouro,
        "numero": numero,
        "cep": cep
    }

# Validar Plano
def validar_plano(plano):
    plano = plano.lower().strip()

    if plano not in ("mensal", "trimestral", "anual"):
        print("Escolha um plano válido.")
        return None

    return plano

def validar_metodo_pagamento(pagamento):
    pagamento = pagamento.lower().strip().replace(' ','-')

    if pagamento not in ("pix", "cartão-de-crédito", "cartão-de-credito", "cartão-de-debito", "cartão-de-débito", "dinheiro"):
        print("Método de pagamento inválido.")
        return None

    return pagamento