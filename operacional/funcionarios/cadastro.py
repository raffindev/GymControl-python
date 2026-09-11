# ====================================
#  Funções de cadastro de funcionario.
# ====================================

from datetime import date
from utils.arquivos import salvar_json
from utils.validações import (
    validar_nome,
    cpf_validacao,
    validar_data_nascimento,
    validar_opção_sexual,
    validar_telefone,
    validar_email,
    validar_endereço,
    validar_opcao,
    verificar_duplicidade_documento,
)

# Dados pessoais
def dados_pessoais_funcionario(alunos, funcionarios):
    # Cadastro Nome
    while True:
        nome = input('Nome do Funcionario: ')
        nome = validar_nome(nome, funcionarios)

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

    # Data de nascimento e Idade
    data_nascimento, idade = validar_data_nascimento()
    if idade < 18:
        print("Cadastro Recusado")
        print("Funcionários devem ter 18 anos ou mais.")
        return None
        

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

    # Codigo Acesso
    codigo = gerar_codigo_funcionario(funcionarios, nome, cpf)

    return{
    "codigo": codigo,
    "nome": nome,
    "documento": cpf,
    "data_nascimento": str(data_nascimento),
    "idade": idade,
    "sexo": sexo,
    "telefone": telefone,
    "email": email,
    "endereço": endereço
}

    # Gerar codigo

# Gerar codigo funcionario
def gerar_codigo_funcionario(funcionarios, nome, cpf):
    sequencial = 1

    while True:
        if any(sequencial == int(funcionario["codigo"][-3:]) for funcionario in funcionarios):
            sequencial += 1
            continue

        break

    sequencial_formatado = f"{sequencial:03}"
    codigo = f"{nome[:3].upper()}{cpf[-3:]}{sequencial_formatado}"

    return codigo

    # Cargo

# Cargo
def cargo_funcionario():
    cargos = {
        1: "Recepcionista",
        2: "Limpeza",
        3: "Instrutor",
        4: "Personal Trainer",
        5: "Financeiro",
        6: "Gerente"
    }

    print(
        """1 - Recepcionista
2 - Limpeza
3 - Instrutor
4 - Personal Trainer
5 - Financeiro
6 - Gerente"""
    )

    cargo = validar_opcao(cargos, "Escolha o cargo do funcionário: ")
    return cargo

# Turno
def turno_funcionario():
    turnos = {
        1: "06:00 às 12:00",
        2: "09:00 às 15:00",
        3: "12:00 às 18:00",
        4: "15:00 às 23:00",
    }

    print(
        """1 - 06:00 às 12:00
2 - 09:00 às 15:00
3 - 12:00 às 18:00
4 - 15:00 às 23:00"""
        )

    turno = validar_opcao(turnos, "Escolha o turno do funcionário: ")
    return turno

# Vinculo
def tipo_vinculo_funcionario():
    vinculos = {
        1: "CLT",
        2: "Estagiário",
        3: "Freelancer"
    }

    print(
        """1 - CLT
2 - Estagiário
3 - Freelancer"""
        )

    vinculo = validar_opcao(vinculos, "Escolha o vínculo do funcionário: ")
    return vinculo

# Cref
def validar_cref(cargo):
    while True:
        if cargo not in ("Instrutor", "Personal Trainer"):
            return None

        else:
            cref = input("Digite o CREF: ")

            if len(cref) != 6 or not cref.isnumeric():
                print("CREF inválido.")
                continue
            
            else:
                return cref

# Dados Profissionais
def dados_profissionais_funcionario():
    
    cargo = cargo_funcionario()
    turno = turno_funcionario()
    data_admissao = date.today()
    vinculo = tipo_vinculo_funcionario()
    cref = validar_cref(cargo)

    return{
    "cargo": cargo,
    "turno": turno,
    "data_admissao": str(data_admissao),
    "data_desligamento": None,
    "tipo_vinculo": vinculo,
    "cref": cref
}

# Cadastro funcionario
def cadastrar_funcionario(alunos, funcionarios):
    
    funcionario = dados_pessoais_funcionario(alunos, funcionarios)
    if funcionario is None:
        return 'Erro ao cadastrar esse funcionario.'
    else:
        dados_profissionais = dados_profissionais_funcionario()

        funcionario.update(dados_profissionais)
        funcionarios.append(funcionario)

        salvar_json("dados/empresa/funcionarios.json", funcionarios)

        print("Funcionario cadastrado com sucesso!")
        return funcionario