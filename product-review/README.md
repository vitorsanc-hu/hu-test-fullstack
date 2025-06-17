# Sistema de Avaliações de Produtos

Um sistema backend simples para gerenciar produtos e suas avaliações, desenvolvido com Flask e SQLite.

## 🚀 Como executar

### 🐳 **Opção 1: Docker Compose (RECOMENDADO)**
**Sem instalar Python ou dependências!**

1. **Pré-requisito:** Apenas [Docker](https://www.docker.com/products/docker-desktop/)

2. **Executar:**
   ```bash
   git clone <repo-url>
   cd product-review
   docker compose up --build
   ```

   **🔥 Hot Reload:** Edite qualquer arquivo Python e veja as mudanças automaticamente!

### 🐍 **Opção 2: Python Local (Alternativa)**

1. **Pré-requisitos:** Python 3.10+

2. **Executar:**
   ```bash
   git clone <repo-url>
   cd product-review
   python3 -m pip install -r requirements.txt
   python3 main.py
   ```

---

**🌐 API disponível em:** `http://localhost:8000`

**📝 Nota:** A API já vem pré-populada com dados de exemplo para facilitar os testes!

## 📋 Funcionalidades

### Produtos
- `GET /produtos` - Listar todos os produtos
- `POST /produtos` - Criar um novo produto
- `GET /produtos/{produto_id}` - Ver um produto e suas avaliações
- `DELETE /produtos/{produto_id}` - Deletar um produto

### Avaliações
- `POST /produtos/{produto_id}/avaliacoes` - Adicionar avaliação ao produto
- `GET /avaliacoes` - Listar todas as avaliações
- `GET /produtos/{produto_id}/media` - Mostrar média de notas do produto

## 🗃️ Estrutura do Banco

### Produto
- `id`: Identificador único
- `nome`: Nome do produto
- `descricao`: Descrição opcional do produto

### Avaliacao
- `id`: Identificador único
- `produto_id`: ID do produto avaliado
- `nota`: Nota de 1 a 5
- `comentario`: Comentário opcional

## 📝 Exemplos de Uso

### Criar um produto:
```json
POST /produtos
{
  "nome": "Smartphone XYZ",
  "descricao": "Um excelente smartphone"
}
```

### Adicionar avaliação:
```json
POST /produtos/1/avaliacoes
{
  "nota": 5,
  "comentario": "Produto excelente!"
}
```

### Ver média de um produto:
```
GET /produtos/1/media
```