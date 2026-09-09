# GymControl

Sistema de gerenciamento para academias desenvolvido em Python, com foco em organização de dados, regras de negócio, validações e arquitetura modular.

> 🚧 Projeto em desenvolvimento

## 📌 Sobre o projeto

O GymControl tem como objetivo simular um sistema utilizado no gerenciamento de uma academia, permitindo controlar alunos, planos, pagamentos, treinos e avaliações físicas.

O projeto está sendo desenvolvido de forma incremental, priorizando código funcional, organização, validação e refatoração contínua.

## 🎯 Objetivos

* Praticar Python em um projeto de maior escala
* Aplicar funções, estruturas de dados e manipulação de arquivos
* Trabalhar com dados persistidos em JSON
* Desenvolver regras de negócio e validações
* Aplicar organização modular
* Evoluir gradualmente a arquitetura do sistema
* Construir um projeto para portfólio

## 🧩 Funcionalidades planejadas

### 👤 Alunos

* Cadastro de alunos
* Geração automática de ID
* Busca por nome
* Consulta por ID
* Alteração de cadastro
* Ativação e inativação
* Dados cadastrais
* Planos e pagamentos

### 🏋️ Treinos

* Cadastro de exercícios
* Criação de treinos
* Organização por treino A/B/C
* Séries e repetições
* Alteração de treinos
* Histórico e evolução

### 📊 Avaliações

* Cadastro de avaliação física
* Avaliação atual
* Histórico de avaliações
* Comparação de avaliações
* Acompanhamento da evolução do aluno

### 💰 Financeiro

* Controle de caixa
* Entradas e saídas
* Mensalidades
* Despesas
* Pagamentos
* Relatórios

> O módulo financeiro do estabelecimento será desenvolvido em uma etapa posterior.

## ## 🗂️ Estrutura de dados

O projeto utiliza arquivos **JSON** para persistência dos dados nesta primeira versão.

Cada aluno possui uma pasta própria identificada por um **ID de três dígitos**. O arquivo `alunos.json` funciona como um índice geral, enquanto os dados completos ficam organizados dentro da pasta individual de cada aluno.

```text
dados/
├── alunos.json
│
└── alunos/
    ├── 001/
    │   ├── cadastro/
    │   │   └── dados_cadastrais.json
    │   │
    │   ├── treinos/
    │   │   ├── treino_atual.json
    │   │   └── historico_treinos.json
    │   │
    │   └── avaliações/
    │       ├── avaliacao_atual.json
    │       └── historico_avaliacoes.json
    │
    └── ...
```

### `alunos.json`

O arquivo `alunos.json` funciona como **índice principal do sistema**, contendo somente as informações necessárias para localizar e identificar rapidamente cada aluno:

```json
[
    {
        "id": 1,
        "nome": "obi wan kenobi",
        "ativo": true
    },
    {
        "id": 2,
        "nome": "darth vader",
        "ativo": true
    },
    {
        "id": 3,
        "nome": "indiana jones",
        "ativo": true
    }
]
```

Dessa forma, consultas básicas, como listagem, busca por ID e verificação de status, podem ser realizadas sem carregar todo o cadastro do aluno.

### Cadastro

Cada aluno possui um arquivo `dados_cadastrais.json`, responsável por armazenar seus dados completos.

Entre eles estão:

* dados básicos;
* data de nascimento e idade;
* sexo;
* documento;
* telefone e e-mail;
* endereço;
* plano e informações de pagamento.

### Treinos

A pasta `treinos/` separa o treino atualmente utilizado pelo aluno de seu histórico:

```text
treinos/
├── treino_atual.json
└── historico_treinos.json
```

O `treino_atual.json` começa como um objeto vazio (`{}`), enquanto o `historico_treinos.json` começa como uma lista vazia (`[]`) para permitir o armazenamento de múltiplos registros.

### Avaliações

A pasta `avaliações/` segue a mesma lógica:

```text
avaliações/
├── avaliacao_atual.json
└── historico_avaliacoes.json
```

O `avaliacao_atual.json` começa como um objeto vazio (`{}`), enquanto o `historico_avaliacoes.json` começa como uma lista vazia (`[]`) para armazenar avaliações anteriores.

Essa organização mantém os dados de cada aluno separados e facilita a evolução futura do sistema.


## 🏗️ Arquitetura

```text
GymControl
│
├── alunos/
├── treinos/
├── avaliacoes/
├── financeiro/
├── menus/
├── utils/
├── dados/
└── main.py
```

A arquitetura será construída gradualmente conforme novas funcionalidades forem implementadas.

## 🔄 Processo de desenvolvimento

Cada funcionalidade segue um ciclo de desenvolvimento:

```text
Planejamento
     ↓
Implementação
     ↓
Testes
     ↓
Validação
     ↓
Revisão
     ↓
Refatoração
     ↓
Commit
```

Ao final do projeto será realizada uma segunda etapa de refatoração geral, incluindo limpeza, organização, padronização e documentação.

## 🛠️ Tecnologias

* Python
* JSON
* Git
* GitHub

## 🚀 Evolução planejada

1. Fundação
2. Consultas e gerenciamento de alunos
3. Planos e pagamentos
4. Treinos
5. Avaliações
6. Evolução dos alunos
7. Sistema financeiro
8. Evolução técnica da aplicação

Tecnologias como POO, PostgreSQL, testes automatizados e API poderão ser incorporadas posteriormente conforme a evolução do projeto.

## 📚 Status

**Em desenvolvimento**