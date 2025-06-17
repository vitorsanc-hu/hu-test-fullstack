FROM node:18-alpine

# Instalar dependências do sistema
RUN apk add --no-cache git

# Configurar diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY package*.json ./

# Instalar dependências
RUN npm install

# Copiar código da aplicação
COPY . .

# Expor porta do Vite
EXPOSE 5173

# Comando para executar em desenvolvimento
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"] 