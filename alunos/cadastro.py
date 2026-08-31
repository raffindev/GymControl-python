# =================================
#  Funções de cadastro de aluno.
# =================================

from datetime import datetime

# Cadastrar aluno - parte 1 - base.
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
            print('Nome não pode ter caracters especiais.')

        elif any(nome == aluno["nome"] for aluno in alunos):
            print('Nome já cadastrado. Digite outro nome.')

        else:
            break

    # Cadastro Status
    status = True

    return{
    "id": id_aluno,
    "nome": nome,
    "ativo": status
}

# Cadastrar aluno - parte 2 - dados pessoais
def dados_pessoais(lista_cadastro):
    while True:
        try:
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))

            hoje = datetime.date.today()

            data_nascimento = datetime.date(ano, mes, dia)
            if data_nascimento > hoje:
                print("A data de nascimento não pode ser futura.")
                continue

            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            break

        except ValueError:
            print("Somente números válidos devem ser informados.")

    while True:
        sexo = input("Digite o Sexo: [M/F] ").upper()
        if sexo not in ("M", "F"):
            print("Sexo inválido")
        else:
            break

    while True:
        cpf = input('Digite seu CPF: ').replace('.','').replace('-','')

        if len(cpf) != 11 or not cpf.isnumeric():
            print("CPF inválido")

        elif any(cpf == aluno["documento"] for aluno in lista_cadastro):
            print('CPF já cadastrado.')
            
        else:
            break

    while True:
        telefone = input('Digite seu telefone com DDD: ').replace('.','').replace('-','')

        if len(telefone) != 11 or not telefone.isnumeric():
            print("telefone inválido")

        elif any(telefone == aluno["telefone"] for aluno in lista_cadastro):
            print('telefone já cadastrado.')
            
        else:
            break

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