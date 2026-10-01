# GymControl

Sistema de gerenciamento para academias desenvolvido em Python, com foco em organização de dados, regras de negócio, validações e arquitetura modular.

> 🚧 Projeto em desenvolvimento

## 📌 Sobre o projeto

O GymControl tem como objetivo simular um sistema utilizado no gerenciamento de uma academia, permitindo controlar alunos, funcionários, planos, pagamentos, treinos, avaliações físicas e processos operacionais.

O projeto está sendo desenvolvido de forma incremental, priorizando código funcional, organização, validação, separação de responsabilidades e refatoração contínua.

## 🎯 Objetivos

- Praticar Python em um projeto de maior escala
- Aplicar funções, estruturas de dados e manipulação de arquivos
- Trabalhar com dados persistidos em JSON
- Desenvolver regras de negócio e validações
- Aplicar organização modular e separação de responsabilidades
- Evoluir gradualmente a arquitetura do sistema
- Utilizar Git e branches durante o processo de desenvolvimento
- Construir um projeto para portfólio

## 🧩 Funcionalidades

### 👤 Alunos

Atualmente implementado:

- Cadastro de alunos
- Geração automática de ID
- Dados pessoais e cadastrais
- Validação de CPF, telefone, e-mail e endereço
- Consulta por ID
- Listagem de alunos
- Planos e informações de pagamento
- Estrutura individual de dados
- Autenticação por CPF com limite de tentativas

Planejado:

- Busca por nome
- Alteração de cadastro
- Ativação e inativação
- Gerenciamento de planos e pagamentos
- Controle de acesso

### 👔 Funcionários

Atualmente implementado:

- Cadastro de funcionários
- Geração de código de funcionário
- Dados pessoais e profissionais
- Cargos
- Turnos
- Tipos de vínculo
- Data de admissão
- Validação de CREF para cargos específicos

Planejado:

- Consultas de funcionários
- Autenticação
- Autorização por cargo
- Controle de permissões
- Registro de presença
- Controle financeiro

### 🏋️ Treinos

Estrutura inicial em desenvolvimento:

- Estrutura para treino atual
- Estrutura para histórico de treinos
- Consulta e exibição de treinos
- Preparação do histórico para novos treinos

Planejado:

- Cadastro de exercícios
- Criação de treinos
- Organização por treino A/B/C
- Séries e repetições
- Alteração de treinos
- Histórico e evolução

### 📊 Avaliações

Planejado:

- Cadastro de avaliação física
- Avaliação atual
- Histórico de avaliações
- Comparação de avaliações
- Acompanhamento da evolução do aluno

### 💰 Financeiro

Planejado:

- Controle de caixa
- Entradas e saídas
- Mensalidades
- Despesas
- Pagamentos
- Financeiro dos funcionários
- Relatórios

> O módulo financeiro será desenvolvido em uma etapa posterior.

## 🗂️ Estrutura de dados

O projeto utiliza arquivos **JSON** para persistência dos dados nesta primeira versão.

Cada aluno possui uma pasta própria identificada por um **ID de três dígitos**. O arquivo `indice_alunos.json` funciona como índice geral, enquanto os dados completos ficam organizados dentro da pasta individual de cada aluno.

```text
dados/
├── indice_alunos.json
│
├── alunos/
│   ├── 001/
│   │   ├── cadastro/
│   │   │   └── dados_cadastrais.json
│   │   │
│   │   ├── treinos/
│   │   │   ├── treino_atual.json
│   │   │   └── historico_treinos.json
│   │   │
│   │   └── avaliações/
│   │       ├── avaliacao_atual.json
│   │       └── historico_avaliacoes.json
│   │
│   └── ...
│
└── empresa/
    └── funcionarios.json
```

### `indice_alunos.json`

O arquivo `indice_alunos.json` funciona como **índice principal dos alunos**, contendo somente as informações necessárias para identificar e localizar rapidamente cada cadastro.

Exemplo:

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

Dessa forma, operações básicas como listagem, busca por ID e verificação de status podem ser realizadas sem carregar o cadastro completo de cada aluno.

### Cadastro

Cada aluno possui um arquivo `dados_cadastrais.json`, responsável por armazenar seus dados completos.

Entre eles estão:

- dados básicos;
- data de nascimento e idade;
- sexo;
- documento;
- telefone e e-mail;
- endereço;
- plano;
- informações de pagamento.

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

A aplicação está organizada por responsabilidades:

```text
GymControl/
│
├── alunos/
│   ├── cadastro.py
│   ├── consultas.py
│   └── estrutura_aluno.py
│
├── treinos/
│
├── avaliacoes/
│
├── menus/
│
├── operacional/
│   ├── acesso/
│   ├── financeiro/
│   └── funcionarios/
│
├── utils/
│
├── dados/
│
├── main.py
├── README.md
└── ROADMAP.md
```

As principais responsabilidades são separadas entre cadastro, consultas, validações, persistência, menus e regras operacionais.

A arquitetura continua sendo construída gradualmente conforme novas funcionalidades são implementadas, evitando abstrações prematuras e mantendo a primeira versão do sistema simples.

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

As funcionalidades são desenvolvidas e revisadas de forma incremental antes de serem integradas à versão principal do projeto.

Ao final do desenvolvimento será realizada uma nova etapa de refatoração geral, incluindo limpeza, organização, padronização, revisão de responsabilidades e documentação.

## 🛠️ Tecnologias

- Python
- JSON
- Git
- GitHub

Bibliotecas e módulos utilizados durante o desenvolvimento incluem:

- `pathlib`
- `datetime`
- `dateutil.relativedelta`

## 🚀 Evolução planejada

O desenvolvimento segue uma evolução gradual:

1. Fundação e arquitetura
2. Cadastro e consultas de alunos
3. Funcionários
4. Treinos
5. Avaliações
6. Autenticação e autorização
7. Controle de acesso
8. Registro de presença
9. Sistema financeiro
10. Relatórios
11. Testes e revalidação geral
12. Evolução técnica da aplicação

Tecnologias como **POO, PostgreSQL, testes automatizados e API** poderão ser incorporadas posteriormente conforme a evolução do projeto e a necessidade de novas soluções.

O planejamento detalhado das próximas etapas está disponível no `ROADMAP.md`.

## 📚 Status

**Em desenvolvimento**

O projeto está passando por desenvolvimento e refatoração incremental, com novas funcionalidades sendo adicionadas e revisadas antes da integração à versão principal.
