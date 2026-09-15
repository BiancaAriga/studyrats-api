# StudyRats API

API REST desenvolvida para o **StudyRats**, uma aplicação de acompanhamento de estudos.

O backend é responsável pelo gerenciamento de usuários, autenticação, sessões de estudo e integração com uma API externa de frases motivacionais.

---

## 🛠️ Tecnologias

* **Python 3.12**
* **FastAPI**
* **SQLModel**
* **SQLite**
* **JWT**
* **pwdlib**
* **Pydantic**
* **ZenQuotes API**
* **Docker**

---

## 🏗️ Arquitetura

O StudyRats é composto por uma interface frontend, uma API backend e uma API externa.

```text
                    STUDYRATS

┌───────────────────────┐
│       Angular         │
│       Interface       │
└───────────┬───────────┘
            │ HTTP / REST
            ▼
┌───────────────────────┐
│       FastAPI         │
│       Backend         │
│                       │
│ Users                 │
│ Auth / JWT            │
│ Study Sessions        │
│ SQLite                │
└───────────┬───────────┘
            │ HTTP
            ▼
┌───────────────────────┐
│   ZenQuotes API       │
│    External API       │
└───────────────────────┘
```

A comunicação entre os componentes ocorre por meio de requisições HTTP.

O Angular se comunica com a API FastAPI, enquanto o backend realiza a integração com a API externa ZenQuotes.

---

## 💡 Integração com API Externa — ZenQuotes

O sistema utiliza a [ZenQuotes API](https://zenquotes.io/) para buscar frases de incentivo em formato JSON.

* **Licença e Condições de Uso:** A API é gratuita, mas exige **atribuição obrigatória**. Aplicações que a consomem devem exibir a mensagem *"Inspirational quotes provided by ZenQuotes API"* vinculada ao site oficial (`https://zenquotes.io/`).

* **Cadastro e Autenticação:** **Não é necessário** realizar cadastro ou enviar uma chave de autenticação (API Key) para o endpoint utilizado.

* **Rotas Utilizadas:**

  * `GET https://zenquotes.io/api/quotes`: Retorna um lote com várias citações aleatórias.

  > **Nota:** O backend do StudyRats faz a requisição para esta rota e salva o resultado em cache de memória. Isso evita que o limite de uso gratuito do ZenQuotes — **5 requisições a cada 30 segundos por IP** — seja estourado.

---

## 🚀 Instalação e Execução

### Pré-requisitos

Para executar o projeto localmente, é necessário ter instalado:

* Python 3.12 ou superior
* Git

Para executar utilizando Docker:

* Docker Desktop

---

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd studyrats-api
```

---

### 2. Configurar as variáveis de ambiente

Na raiz do projeto, crie um arquivo `.env`:

```env
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
```

> O arquivo `.env` não deve ser versionado no Git.

---

### 3. Escolher a forma de execução

O projeto pode ser executado diretamente com Python ou utilizando Docker.

---

### ▶️ Execução local

#### Criar o ambiente virtual

```bash
python -m venv .venv
```

#### Ativar o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

#### Instalar as dependências

```bash
pip install -r requirements.txt
```

#### Executar a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://localhost:8000
```

---

### 🐳 Execução com Docker

#### Criar a imagem

```bash
docker build -t studyrats-api .
```

#### Executar o container

```bash
docker run --env-file .env -p 8000:8000 studyrats-api
```

A API estará disponível em:

```text
http://localhost:8000
```

---

## 📖 Swagger / Documentação da API

O FastAPI disponibiliza automaticamente uma interface interativa para testar e consultar os endpoints.

Com a aplicação em execução, acesse:

```text
http://localhost:8000/docs
```

A documentação permite:

* Visualizar os endpoints disponíveis.
* Consultar os parâmetros das requisições.
* Visualizar os modelos de entrada e saída.
* Realizar requisições diretamente pelo navegador.
* Autenticar utilizando o token JWT através do botão **Authorize**.

Para endpoints protegidos, utilize o formato:

```text
Bearer <token>
```

O Swagger também permite visualizar os códigos de resposta HTTP e os possíveis erros retornados pela API.
