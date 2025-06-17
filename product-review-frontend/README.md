# Frontend - Sistema de Avaliações de Produtos

Frontend React simples para visualizar as avaliações de produtos da API Flask.

## 🚀 Como executar

### 🎯 **Opção 1: Docker (RECOMENDADO)**

```bash
# Certifique-se que a API está rodando em localhost:8000
docker compose up --build
```

### 🐍 **Opção 2: Node.js Local**

```bash
# Certifique-se que a API está rodando em localhost:8000
npm install
npm run dev
```

**Frontend disponível em:** `http://localhost:5173`

### ⚠️ **Pré-requisito Importante**
A API Flask deve estar rodando em `localhost:8000` primeiro:
```bash
cd ../product-review
docker compose up --build
```

## 🎯 Funcionalidades

- ✅ Lista todas as avaliações cadastradas
- ✅ Exibe nome do produto para cada avaliação
- ✅ Mostra nota com sistema de estrelas
- ✅ Exibe comentários das avaliações
- ✅ Design responsivo com Tailwind CSS

## 🛠 Tecnologias

- **React 18** - Framework frontend
- **Vite** - Build tool moderna e rápida
- **Tailwind CSS** - Estilização utility-first
- **Fetch API** - Consumo da API REST

## 📋 Estrutura

```
src/
├── App.jsx          # Componente principal
├── index.css        # Estilos Tailwind
└── main.jsx         # Entry point
```

## 🔗 Integração com API

O frontend consome os seguintes endpoints:
- `GET /produtos` - Lista produtos
- `GET /avaliacoes` - Lista avaliações

O proxy está configurado no `vite.config.js` para redirecionar as chamadas para `localhost:8000`.

---

**💡 Dica:** Execute primeiro a API Flask (`docker compose up`) e depois o frontend (`npm run dev`) para ver todas as avaliações pré-populadas!
