# 🏗️ Arquitetura – My Budget Project

## 🎯 Princípios norteadores

- Separação clara de responsabilidades (SoC)
    
- Baixo acoplamento, alta coesão
    
- Facilidade para testes unitários e integração
    
- Escalabilidade da lógica sem dependência de framework
    

## 🧱 Camadas

### 1. Core

- `models/`: entidades de domínio (ex: Transaction, Budget)
    
- `services/`: regras de negócio e lógica de aplicação
    

### 2. Infraestrutura

- `repositories/`: acesso a dados e persistência (ex: SQLite, JSON)
    

### 3. Interface

- `views/`: interação com usuário (CLI/Web/API)
    
- `templates/`: HTML (se necessário)
    

## 📁 Estrutura de pastas sugerida

```
finance_app/
├── core/
│   ├── models/
│   └── services/
│
├── infrastructure/
│   └── repositories/
│
├── interfaces/
│   ├── views/
│   └── templates/
│
├── tests/
└── main.py
```

## 🔄 Repositórios

- Cada entidade de domínio possui um repositório correspondente
    
- Abstração de persistência permite troca entre SQLite, PostgreSQL ou arquivos
    

## 🔍 Design Patterns usados

- Repository Pattern
    
- Service Layer
    
- Dependency Inversion (futuramente)
    
- Separation of Concerns
    

## 🛠️ Padrões de codificação

- Pythonic (PEP8)
    
- Métodos pequenos, com nomes claros
    
- Preferência por composição ao invés de herança
    

## 🧪 Testes

- Testes unitários por módulo (`tests/`)
    
- Futuramente: testes de integração (ex: cadastro + leitura de transações)
    

## 📦 Extensibilidade futura

- Plugável para APIs externas (Open Finance)
    
- Facilidade para mover lógica para backend web ou app mobile
    
- Pronto para Dockerização e deploy futuro