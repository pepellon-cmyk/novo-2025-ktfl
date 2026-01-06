# Kite for Life — Deploy

## Descrição
Aplicação Kite for Life desenvolvida com Python e Flask.

## Pré-requisitos
- Python >= 3.9
- pip
- Conta no Heroku (para deploy)

## Instalação

### 1. Criar ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2. Instalar dependências:
```bash
pip install -r requirements.txt
```

### 3. Rodar local:
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:3000`

### 4. Criar repositório GitHub e push:
```bash
git remote add origin <URL_DO_REPO>
git push -u origin main
```

### 5. Configurar GitHub Actions:

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

### 6. Deploy automático:

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
├── app.py                   # Aplicação Flask
├── requirements.txt         # Dependências Python
├── Procfile                 # Configuração do Heroku
└── README.md                # Documentação
```

## Scripts disponíveis

- `python app.py` - Inicia o servidor em modo desenvolvimento
- No Heroku: `gunicorn app:app` - Inicia o servidor em produção

## Tecnologias

- **Python** - Linguagem de programação
- **Flask** - Framework web minimalista
- **Gunicorn** - Servidor WSGI para produção
- **Heroku** - Plataforma de deploy
- **GitHub Actions** - CI/CD
