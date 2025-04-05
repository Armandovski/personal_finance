# 🗓️ Planejamento – My Budget Project

## Épico 1: Gestão de Transações

### 🔧 Core: Preparar base da aplicação para operações CRUD com transações

- Criar classe `Transaction`
    
- Criar repositório `TransactionRepository`
    
- Criar estrutura de visualização `CashflowView`
    
- Criar camada de persistência `MasterRepository`
    
- Definir estrutura de dados base (SQLite ou JSON)
    
- Criar esquema de pastas e módulos
    
- Escrever testes unitários para `Transaction`
    

### ✅ User Stories

#### Story 1: Ver lista de transações por mês

> Como usuário, quero ver a lista de transações de um determinado mês, para acompanhar meus gastos.

- Criar view `CashflowView`
    

#### Story 2: Cadastrar nova transação

> Como usuário, quero cadastrar uma nova transação manualmente, para registrar meus gastos.

- Criar view `AddTransaction`
    

#### Story 3: Editar uma transação existente

> Como usuário, quero editar uma transação cadastrada, para corrigir erros ou atualizar informações.

- Criar view `EditTransaction`
    

#### Story 4: Deletar transação

> Como usuário, quero deletar uma transação, para corrigir qualquer imputação de dados incorreta.

- Criar view `DeleteTransaction`
    

#### Story 5: Marcar transação como paga

> Como usuário, quero marcar uma transação como paga, para controlar meus boletos.

- Criar view `PayTransaction`
    
- Criar service para somar o total por mês
    

### ⏳ Backlog Técnico Futuro

- Criar camada de validação de domínio (validação de datas, categorias e contas)
    
- Criar testes de integração view ↔ service ↔ repository
    
- Agregações por categoria e tipo (despesa/receita)
    
- Visualização CLI ou HTML
    

---

## 📌 Organização de sprints (sugestão)

### Sprint 1 – Base técnica

- Criar estrutura de pastas
    
- Criar entidade `Transaction`
    
- Criar `TransactionRepository`
    
- Escrever primeiros testes unitários
    

### Sprint 2 – CRUD de transações via CLI

- Criar interface de inserção
    
- Criar listagem filtrada por mês
    
- Permitir edição e exclusão
    
- Marcar como paga
    

### Sprint 3 – Orçamento e relatório

- Início do módulo de orçamento
    
- Comparação orçado vs. realizado
    
- Exibição de faturas e boletos
    

---

> Todo esse planejamento será iterado conforme surgirem novas necessidades ou aprendizados durante o desenvolvimento.