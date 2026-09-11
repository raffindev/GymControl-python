# ================
#  Arquivos JSON
# ================

import json

# Leitura de JSON
def ler_json(diretorio):
    try:
        with open(diretorio, "r", encoding="utf-8") as arquivo_json:
            return json.load(arquivo_json)
        
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []

    except json.JSONDecodeError:
        print("Arquivo JSON inválido ou vazio.")
        return []

# Salvando dados em JSON
def salvar_json(diretorio, dados):
    with open(diretorio, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    alunos = ler_json("dados/indice_alunos.json")
    funcionarios = ler_json("dados/empresa/funcionarios.json")

    return alunos, funcionarios