# 🧪 Sistema de Avaliações de Produtos - Teste Técnico

Um sistema completo **Backend + Frontend** desenvolvido para testes técnicos, com **falhas propositais** para serem identificadas e corrigidas pelos candidatos.

## 📁 Estrutura do Projeto

```
hu-test/
├── product-review/           # 🐍 API Flask (Backend)
│   ├── main.py              # API REST
│   ├── models.py            # Modelos SQLAlchemy
│   ├── crud.py              # Operações CRUD
│   ├── schemas.py           # Validação de dados
│   ├── database.py          # Config DB + dados pré-populados
│   └── docker-compose.yml   # Container da API
│
└── product-review-frontend/  # ⚛️ Frontend React
    ├── src/App.jsx          # Interface para visualizar avaliações
    ├── docker-compose.yml   # 🐳 Container do frontend
    └── README.md            # Instruções do frontend
```

## 🚀 Execução Simples

### 🎯 **Executar em 2 passos separados:**

#### 1. **Backend (API Flask):**
```bash
cd product-review
docker compose up --build
```
**API disponível em:** `http://localhost:8000`

#### 2. **Frontend (React) - Nova aba do terminal:**
```bash
cd product-review-frontend
docker compose up --build
# OU: npm install && npm run dev
```
**Frontend disponível em:** `http://localhost:5173`

### 🔥 **Resultado:**
- 🐍 **API Flask:** `http://localhost:8000`
- ⚛️ **Frontend React:** `http://localhost:5173`

## 🎯 Objetivo do Teste

O candidato deve **identificar e corrigir falhas propositais** na API:


## 🛠 Tecnologias

### Backend
- **Python 3.11** + **Flask**
- **SQLAlchemy** + **SQLite**
- **Docker**

### Frontend  
- **React 18** + **Vite**
- **Tailwind CSS**
- **Material UI**
- **Docker**
