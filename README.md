# Kite for Life — Deploy

## Descrição
Aplicação Kite for Life desenvolvida com Node.js e Express.

## Pré-requisitos
- Node.js >= 14.0.0
- npm >= 6.0.0
- Conta no Heroku (para deploy)

## Instalação

### 1. Instalar dependências:
```bash
npm install
```

### 2. Rodar local:
```bash
npm run dev
```

A aplicação estará disponível em `http://localhost:3000`

### 3. Criar repositório GitHub e push:
```bash
git remote add origin <URL_DO_REPO>
git push -u origin main
```

### 4. Configurar GitHub Actions:

Para fazer o deploy automático no Heroku via GitHub Actions, você precisa configurar os seguintes secrets no seu repositório:

1. Acesse seu repositório no GitHub
2. Vá em **Settings** > **Secrets and variables** > **Actions**
3. Clique em **New repository secret**
4. Adicione os seguintes secrets:

   - **HEROKU_API_KEY**: Sua chave de API do Heroku
     - Obtenha em: https://dashboard.heroku.com/account
     - Vá em **Account Settings** > **API Key** > **Reveal**
   
   - **HEROKU_APP_NAME**: Nome da sua aplicação no Heroku
     - Exemplo: `minha-app-kite-for-life`
   
   - **HEROKU_EMAIL**: Email da sua conta Heroku
     - O email que você usa para fazer login no Heroku

### 5. Deploy automático:

Após configurar os secrets, basta fazer push para a branch `main`:

```bash
git push origin main
```

O GitHub Actions irá automaticamente:
- Instalar as dependências
- Fazer o deploy no Heroku

Você pode acompanhar o progresso na aba **Actions** do seu repositório.

## Endpoints

- `GET /` - Página inicial com informações do app
- `GET /health` - Health check do servidor

## Estrutura do Projeto

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions workflow
├── .gitignore               # Arquivos ignorados pelo Git
├── index.js                 # Servidor Express
├── package.json             # Dependências e scripts
├── Procfile                 # Configuração do Heroku
└── README.md                # Documentação
```

## Scripts disponíveis

- `npm start` - Inicia o servidor em produção
- `npm run dev` - Inicia o servidor em modo desenvolvimento com hot-reload

## Tecnologias

- **Node.js** - Runtime JavaScript
- **Express** - Framework web
- **Nodemon** - Hot-reload em desenvolvimento
- **Heroku** - Plataforma de deploy
- **GitHub Actions** - CI/CD
