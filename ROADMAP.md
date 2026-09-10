# 🏋️ GymControl

> Sistema de gerenciamento de academia desenvolvido em Python com foco em prática de arquitetura, organização de código, persistência de dados e desenvolvimento incremental.

---

# 🗺️ Roadmap

## 1. 🧱 Estrutura e arquitetura

* [x] Separar responsabilidades do projeto
* [x] Criar estrutura de `utils`
* [x] Separar validações do cadastro
* [x] Organizar módulos de alunos
* [x] Organizar menus
* [x] Criar estrutura `operacional`
* [x] Separar autenticação e autorização
* [x] Definir estrutura inicial dos dados
* [x] Definir `indice_alunos.json`
* [ ] Definir estrutura definitiva de funcionários
* [ ] Definir estrutura definitiva da empresa
* [ ] Revisar todos os caminhos dos arquivos
* [ ] Revisar imports
* [ ] Revisão geral da arquitetura

---

# 👨‍🎓 2. Alunos

## Cadastro

* [x] Cadastro inicial
* [x] Geração automática de ID
* [x] Nome
* [x] CPF
* [x] Data de nascimento
* [x] Idade
* [x] Sexo
* [x] Telefone
* [x] E-mail
* [x] Endereço
* [x] Plano
* [x] Método de pagamento
* [x] Status do pagamento
* [x] Data de início
* [x] Data de vencimento
* [x] Status ativo/inativo
* [x] Validações separadas do cadastro
* [x] Consultas separadas do cadastro

## Estrutura dos dados

```text
dados/
├── indice_alunos.json
│
└── alunos/
    └── 001/
        ├── cadastro/
        │   └── dados_cadastrais.json
        │
        ├── treinos/
        │   ├── treino_atual.json
        │   └── historico_treinos.json
        │
        └── avaliações/
            ├── avaliacao_atual.json
            └── historico_avaliacoes.json
```

## Treinos

* [ ] Criar treino
* [ ] Exercícios
* [ ] Séries
* [ ] Repetições
* [ ] Treino atual
* [ ] Histórico
* [ ] Atualização do treino
* [ ] Comparação entre treinos
* [ ] Histórico periódico

## Avaliações

* [ ] Criar avaliação
* [ ] Objetivo
* [ ] Peso
* [ ] Altura
* [ ] Percentual de gordura
* [ ] Problemas de saúde
* [ ] Observações
* [ ] Avaliação atual
* [ ] Histórico
* [ ] Comparação entre avaliações

---

# 👔 3. Funcionários

## Cadastro

### Definir antes de implementar

* [ ] Estrutura definitiva de `funcionarios.json`
* [ ] Campos obrigatórios
* [ ] Código do funcionário
* [ ] Cargos
* [ ] Turnos
* [ ] Status ativo/inativo
* [ ] Regras específicas por cargo
* [ ] Regra do CREF para instrutores

### Dados planejados

* [ ] Nome
* [ ] Data de nascimento
* [ ] CPF
* [ ] Telefone
* [ ] E-mail
* [ ] Código
* [ ] Cargo
* [ ] Turno
* [ ] Data de admissão
* [ ] Ativo/inativo
* [ ] CREF quando necessário

## Consultas

* [ ] Buscar funcionário por código
* [ ] Buscar por nome
* [ ] Listar funcionários
* [ ] Consultar funcionário ativo/inativo
* [ ] Verificar duplicidades

---

# 🔐 4. Autenticação

## Alunos

* [x] Autenticação por CPF
* [x] Limite de tentativas
* [x] Bloqueio após tentativas

## Funcionários

* [ ] Definir método de autenticação
* [ ] Autenticação por código
* [ ] Definir segundo dado de autenticação
* [ ] Limite de tentativas
* [ ] Bloqueio
* [ ] Retornar funcionário autenticado

---

# 🛡️ 5. Autorização

## Cargos e permissões

### Recepcionista

* [ ] Alunos
* [ ] Controle de acesso

### Instrutor

* [ ] Alunos
* [ ] Treinos
* [ ] Avaliações
* [ ] Controle de acesso

### Gerente

* [ ] Acesso completo

## Implementação

* [ ] Estrutura de permissões
* [ ] Verificação de permissão
* [ ] Integração com menus
* [ ] Bloqueio de áreas não autorizadas

---

# 🚪 6. Controle de acesso

* [ ] Consultar aluno
* [ ] Verificar se aluno está ativo
* [ ] Verificar situação do plano
* [ ] Verificar vencimento
* [ ] Liberar acesso
* [ ] Bloquear acesso
* [ ] Registrar entrada
* [ ] Criar histórico de acessos
* [ ] Integrar com funcionário responsável

---

# 📅 7. Registro de presença

Arquivo planejado:

```text
dados/
└── empresa/
    └── registro_presença.json
```

## Definir estrutura

* [ ] Presença
* [ ] Falta
* [ ] Folga
* [ ] Férias
* [ ] Datas
* [ ] Funcionário relacionado
* [ ] Regras de jornada

## Calendário

* [ ] Gerar calendário mensal com Python
* [ ] Utilizar `datetime` / `date`
* [ ] Mostrar dias da semana
* [ ] Identificar domingos
* [ ] Identificar folgas
* [ ] Identificar férias
* [ ] Identificar faltas
* [ ] Mostrar funcionário relacionado
* [ ] Permitir consulta por mês

> O calendário será **gerado pelo Python**. Não será necessário salvar um calendário mensal em JSON.

### Regra da academia

* [ ] Domingo = academia fechada

> Domingo fechado é uma regra da empresa, não uma folga individual do funcionário.

---

# 💰 8. Financeiro dos funcionários

Arquivo:

```text
dados/empresa/financeiro_funcionarios.json
```

* [ ] Definir estrutura
* [ ] Salário
* [ ] Dados bancários
* [ ] Agência
* [ ] Conta
* [ ] Data de pagamento
* [ ] Histórico de pagamentos
* [ ] Faltas
* [ ] Descontos
* [ ] Horas extras
* [ ] Cálculo de salário
* [ ] Registro de pagamento
* [ ] Histórico financeiro

---

# 🏢 9. Financeiro da empresa

Arquivo:

```text
dados/empresa/financeiro_empresa.json
```

* [ ] Definir estrutura
* [ ] Receitas
* [ ] Despesas
* [ ] Pagamentos de alunos
* [ ] Outras entradas
* [ ] Despesas operacionais
* [ ] Pagamentos de funcionários
* [ ] Movimentações
* [ ] Saldo
* [ ] Histórico
* [ ] Relatórios financeiros

---

# 📊 10. Relatórios

* [ ] Relatório de alunos
* [ ] Alunos ativos/inativos
* [ ] Relatório de funcionários
* [ ] Funcionários ativos/inativos
* [ ] Relatório de presença
* [ ] Relatório de faltas
* [ ] Relatório de folgas
* [ ] Relatório de férias
* [ ] Relatório financeiro da empresa
* [ ] Relatório financeiro dos funcionários
* [ ] Relatórios integrados

---

# 🖥️ 11. Menus

* [x] Menu principal
* [x] Estrutura de menus
* [ ] Menu do aluno
* [ ] Menu administrativo
* [ ] Menu de funcionários
* [ ] Menu financeiro
* [ ] Menu de controle de acesso
* [ ] Menu de relatórios
* [ ] Aplicar permissões aos menus

---

# 🧪 12. Testes

Cada funcionalidade deve ser testada antes de avançarmos.

## Testes individuais

* [ ] Fluxo normal
* [ ] Entrada inválida
* [ ] Dados duplicados
* [ ] Dados vazios
* [ ] Arquivo inexistente
* [ ] JSON inválido
* [ ] Casos extremos
* [ ] Retorno das funções

## Testes integrados

* [ ] Cadastro → consulta
* [ ] Cadastro → atualização
* [ ] Aluno → pagamento → acesso
* [ ] Funcionário → autenticação → autorização
* [ ] Funcionário → presença → financeiro
* [ ] Folga/férias → calendário
* [ ] Sistema completo

---

# 🧹 13. Refatoração

Depois que cada módulo estiver funcionando:

* [ ] Revisar nomes
* [ ] Revisar funções
* [ ] Revisar parâmetros
* [ ] Revisar imports
* [ ] Remover duplicação
* [ ] Avaliar abstrações
* [ ] Simplificar código
* [ ] Melhorar mensagens
* [ ] Revisar responsabilidades
* [ ] Verificar arquitetura

## Segunda grande refatoração

Depois que o sistema estiver funcional:

* [ ] Revisar projeto inteiro
* [ ] Procurar responsabilidades mal posicionadas
* [ ] Procurar funções grandes
* [ ] Procurar código repetido
* [ ] Revisar estrutura de pastas
* [ ] Revisar persistência
* [ ] Revisar regras de negócio
* [ ] Melhorar documentação

---

# 📚 14. Python aplicado ao projeto

Durante o desenvolvimento, utilizar e consolidar:

* [x] `json`
* [x] `pathlib`
* [x] funções
* [x] dicionários
* [x] listas
* [x] validações
* [x] tratamento de exceções
* [x] `datetime.date`
* [ ] `datetime.datetime`
* [ ] `timedelta`
* [ ] `relativedelta`
* [ ] manipulação de datas
* [ ] comparação de datas
* [ ] geração de calendários
* [ ] outras ferramentas conforme necessidade

> O projeto também serve como laboratório para consolidar ferramentas Python que aparecem naturalmente em situações reais.

---

# 🌱 15. Git

## Estratégia

Desenvolver funcionalidades em branches independentes e realizar os merges somente quando a etapa estiver validada.

Estrutura atual:

```text
main
│
├── feature/menus
│
└── feature/operacional
```

## Processo

```text
Criar branch
    ↓
Desenvolver
    ↓
Testar
    ↓
Revisar
    ↓
Refatorar
    ↓
Commit
    ↓
Push
    ↓
Merge somente quando a etapa estiver concluída
```

## Etapas

* [x] `feature/menus`
* [ ] `feature/operacional`
* [ ] Revalidação final
* [ ] Merge final na `main`

---

# 📝 16. Decisões de arquitetura

Registrar aqui decisões importantes para evitar voltar às mesmas discussões posteriormente.

### Dados

```text
dados/
├── indice_alunos.json
│
├── alunos/
│   └── 001/
│       ├── cadastro/
│       ├── treinos/
│       └── avaliações/
│
└── empresa/
    ├── funcionarios.json
    ├── financeiro_funcionarios.json
    ├── registro_presença.json
    └── financeiro_empresa.json
```

### Princípios

* [x] Separar validação de cadastro
* [x] Separar consulta de cadastro
* [x] Separar autenticação de autorização
* [x] Manter regras de negócio fora dos menus
* [x] Menus responsáveis por navegação
* [x] Dados persistentes separados da lógica
* [x] Evitar abstrações prematuras
* [x] Preferir simplicidade na V1
* [ ] Revisar arquitetura antes da versão final

---

# 📌 17. Próxima sequência de desenvolvimento

## Etapa atual — Funcionários

### 1.

* [ ] Fechar estrutura de `funcionarios.json`

### 2.

* [ ] Criar cadastro de funcionário

### 3.

* [ ] Criar consultas de funcionários

### 4.

* [ ] Testar e refatorar

### 5.

* [ ] Criar autenticação de funcionários

### 6.

* [ ] Criar autorização por cargo

### 7.

* [ ] Criar registro de presença

### 8.

* [ ] Criar financeiro dos funcionários

### 9.

* [ ] Criar calendário

### 10.

* [ ] Criar financeiro da empresa

### 11.

* [ ] Criar relatórios

### 12.

* [ ] Revalidação geral

---

# 🧠 Regra de desenvolvimento do GymControl

> **Não implementar apenas para fazer funcionar.**
>
> Entender por que a função existe, onde ela pertence, quais dados recebe, o que retorna e como ela se relaciona com o restante do sistema.

Cada nova funcionalidade deve passar por:

```text
IDEIA
  ↓
ARQUITETURA
  ↓
IMPLEMENTAÇÃO
  ↓
TESTE
  ↓
REVISÃO
  ↓
REFATORAÇÃO
  ↓
COMMIT
```

---

## 🚧 Observação

Este documento é um **roadmap vivo**.

Novas necessidades podem aparecer durante o desenvolvimento. Quando isso acontecer, a arquitetura deve ser reavaliada antes de simplesmente adicionar código.

O objetivo não é terminar o projeto o mais rápido possível.

**O objetivo é construir um sistema cada vez melhor enquanto se aprende Python e desenvolvimento de software na prática.**
