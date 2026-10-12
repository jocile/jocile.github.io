---
title: Introdução ao SQL e Bottle para construir Apps em Python
date: 2026-10-12
description: "guia completo sobre como utilizar SQLite - banco de dados SQL em combinação com Python e Bottle."
tags:
  - python
  - programação
  - banco-de-dados
---

## 📝 Resumo Executivo

Este documento apresenta um guia completo sobre como utilizar **SQLite** (banco de dados SQL) em combinação com **Python**, **Bottle** (framework web), e integração com **Olama** (LLM local). O conteúdo original é uma transcrição de uma aula prática do Silicon Dojo.

---

## 🎯 Objetivo da Aula

Combinar os componentes anteriores (Python, SQL, APIs) em aplicações web reais que podem ser:
- Implantadas na nuvem
- Utilizadas internamente na empresa
- Integradas com serviços externos (como AI/LLMs)

---

## 🗄️ Módulo 1: SQLite e Banco de Dados Relacional

### O Que é SQLite?

> ⚠️ **Importante** - "SQLite é o que chamamos de sistema de gerenciamento de banco de dados relacional. Vários nomes diferentes para servidores de banco de dados: MySQL, MariaDB, PostgreSQL, MSSQL. SQL Light (SQLite) é usado por sua simplicidade."

| Característica | Descrição |
|----------------|-----------|
| **Tipo** | Sistema de gerenciamento de banco de dados relacional |
| **Linguagem** | SQL (Structured Query Language) |
| **Segurança** | Não há "segurança" tradicional - você pode abrir o arquivo com editor de texto |
| **Ideal para** | Ambientes laboratoriais, projetos internos |

### Principais Conceitos de SQL

#### 1. ACID vs BASE

>[!info] ⚖️Transações Relacionais (ACID)
> 
> - **Atomicidade**: Ou tudo funciona ou tudo falha
> - **Consistência**: As regras permanecem válidas após a transação
> - **Isolamento**: Transações não se sobrepõem
> - **Durabilidade**: Mudanças são realmente salvas
> 
> 🔑 O problema: é um "nightmare arquitetônico" para sistemas de grande escala. Por isso temos NoSQL.

#### 2. ACID vs BASE (NoSQL)

| Sistema | Padrão | Escalabilidade | Consistência |
|---------|--------|----------------|--------------|
| **Relacional** (SQL) | ACID | Dificulta | Imediata |
| **NoSQL** | BASE | Alta | Possivelmente 30 min |

>[!info] 📊 Exemplo prático: "Se você perde uma transação a cada mil para o Facebook, quem se importa? Você vai chorar se pagar $1.000 ao proprietário e isso some."

### Comandos Internos do SQLite Shell

```sql
-- Navegação e comandos úteis
.tables          -- Lista todas as tabelas
.schema table    -- Exibe estrutura da tabela
.mode column      -- Melhor legibilidade que mode list
.headers on       -- Mostra cabeçalhos nas resultados
.backup db.new    -- Copia dados para novo banco
.exit             -- Sai do shell SQLite3
```

#### Dicas de Shell

>[!tip] 🛠️ **Dica** - Use `up` (seta acima) para revisar comandos anteriores quando houver erro. O SQLite mantém histórico simples em muitos casos.

### Criando Tabelas

```python
# SQLite não precisa definir tipos de dados rigorosamente
CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Row ID é automático
    name TEXT,
    age INTEGER,
    size TEXT,
    allergy TEXT
)
```

| Coluna | Tipo Recomendado | Observação |
|--------|------------------|------------|
| `id` | INTEGER AUTOINCR | Primary key automático (reutilizável ao excluir) |
| `name` | TEXT | Pode conter texto longo (até blog post inteiro!) |
| `age` | INTEGER | Use com cuidado em sistemas críticos |
| `size` | TEXT ou INT | Evite strings inconsistentes |

>[!warning] ⚠️ **Cuidado** - O SQLite reutiliza IDs automaticamente ao excluir registros. Para CRM e sistemas financeiros, crie um primary key manual (randomizado).

### Operações SQL Básicas

#### SELECT com Clause WHERE

```sql
-- Wildcards para busca parcial
SELECT * FROM student WHERE name LIKE '%M%'           -- Qualquer nome com M
SELECT * FROM student WHERE name LIKE 'M%'            -- Começa com M
SELECT * FROM student WHERE name LIKE _%_             -- M em qualquer lugar (1 char)
SELECT * FROM student WHERE name LIKE '__m__'         -- M específico em posição fixa

-- Condições múltiplas
SELECT * FROM student WHERE size = 'small' AND age <= 13
```

#### Funções Agregadas SQL

```sql
COUNT(name)           -- Conta registros únicos de nome
MAX(age)              -- Maior idade (111 anos!)
MIN(age)              -- Menor idade (8 anos)
AVG(age)              -- Média de idade (24.11)
SUM(age)              -- Soma total de idades
```

### INSERT, UPDATE e DELETE em SQL

```sql
-- Insert com ou sem valores completos
INSERT INTO student3 (name, size) VALUES ('Timmy', 'small')
INSERT INTO student3 (id, name, age, size, allergy) 
VALUES (50, 'Alice', 15, 'large', 'peanut')

-- Update seguro (SEMPRE use WHERE com ID único!)
UPDATE student3 SET name = 'Bill' WHERE name = 'William' AND row_id = 2

-- O erro comum: update sem WHERE específico
-- UPDATE student3 SET allergy = 'peanut' WHERE name = 'Timmy'
-- Isso atualiza TODOS os 'Timmy' no sistema!

DELETE FROM student3 WHERE row_id = 2
```

### Joins em SQL SQLite

```sql
-- INNER JOIN: apenas coincidências
SELECT * FROM student3 INNER JOIN allergy 
ON student3.allergy.name = allergy.name

-- LEFT JOIN: mantém registros da tabela esquerda (mesma coisa para SQLite)
SELECT s.*, a.condition, a.treatment 
FROM student3 s LEFT JOIN allergy a ON s.allergy.name = a.name

-- SQLite NÃO suporta RIGHT JOIN!
```

>[!tip] 📌 **Dica de Arquitetura** - Cada tabela deve focar em dados específicos. Use joins quando você precisa relacionar informações entre entidades.

---

## 🐍 Módulo 2: Python e Integração com Banco de Dados

### Instalando Dependências Essenciais

```bash
# Instale módulos via pip (Windows requer essa opção)
pip install bottle olama sqlalchemy
# ou para múltiplos:
pip3 install -r requirements.txt
```

| Ferramenta | Propósito | Importar em Python |
|------------|-----------|-------------------|
| **Bottle** | Web framework simples | `from bottle import run, route` |
| **Olama** | LLM local (Granite 350M) | `import lama.chat` |
| **SQLAlchemy** | ORM (não usado neste guia) | `import sqlalchemy` |

### Conectando Python ao SQLite

```python
import sqlite3

# Conectar ao banco de dados existente ou criar novo se não existir
conn = sqlite3.connect('class.db')
cursor = conn.cursor()

# Executar SQL sem semicolão (Python adiciona automaticamente)
sql = """
    SELECT * FROM student
"""
result = cursor.execute(sql)

# Pega todos os resultados como lista de tuplas
results = result.fetchall()

# Fechamento obrigatório em ambientes de produção
conn.close()
```

#### Parâmetros e Prevenção de SQL Injection

```python
# ❌ RISCIDO - Concatenação direta com f-string
sql = f"SELECT * FROM student WHERE age = {age}"

# ✅ SEGURO - Usando placeholders (???)
sql = "SELECT * FROM student WHERE age = ?"
cursor.execute(sql, (age_value,))  # Parâmetro como tupla!
```

>[!info] 🔒 **Porque é seguro**: Os placeholders são tratados como dados, não como código SQL executável. O SQLite insere o valor literalmente no resultado.

---

## 🤖 Módulo 3: OLama e Cache de Respostas AI

### Setup do Environment para LLM Local

```bash
# Instale o modelo local antes
pip install olama
ollama run granite:350m    # Modelo gratuito, roda localmente
```

#### Arquitetura de Cache de Respostas AI

```python
import sqlite3
from llama import chat_response

def find_query(query):
    conn = sqlite3.connect('cache.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT query, response FROM cache WHERE query_response LIKE ?", (%query%))
    return result.fetchone()

def send_query_to_ai(query):
    # Chama o modelo local
    model = ollama.chat("granite:350m")
    response = model.query(query)
    return response.message.content

# Lógica de cache simples
query = "como posso te ajudar?"
memory = find_query(query)

if memory is not None:
    # Resposta já está no banco (rápido!)
    return f"Query: {memory[0]}, Response: {memory[1]}"
else:
    # Gerar novo via AI
    ai_response = send_query_to_ai(query)
    # Salvar na cache para futuras consultas
    insert_into_cache(query, ai_response)
```

| Benefício | Descrição |
|-----------|-----------|
| **Performance** | Cache reduz tempo de resposta de 15s para <100ms |
| **Custo** | Evita chamadas API externas (Grátis com cache!) |
| **Consistência** | Respostas uniformes através do sistema |

>[!important] 💡 **Por que usar o cache?** - "Se um AI der a resposta errada uma vez, é OK. Mil vezes? É problema sua, não da AI!"

---

## 🌐 Módulo 4: Bottle Web Framework

### Estrutura de Arquivos para Projeto Bottle

```
/projeto/
├── web_app.py          # Código principal do aplicativo
├── static/             # Arquivos estáticos (imagens, CSS, JS)
│   └── robot.png
└── views/              # Templates HTML
    └── index.tpl
```

### Rotas Estáticas e Dinâmicas em Bottle

```python
from bottle import run, route, request, response

@route('/')  
def index():
    return "Hello World"

# Route com variáveis dinâmicas do URL
@route('/<name>')
def hello(name):
    # name é automaticamente extraído da URL
    return f"Hello {name}, welcome!"

# Route com tipos específicos
@route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    total = int(num1) + int(num2)
    return f"{num1} + {num2} = {total}"

@route('/mult/<float:n1>/<float:n2>')
def multiply(n1, n2):
    result = float(n1) * float(n2)
    return f"{n1} × {n2} = {result:.2f}"
```

#### Método POST vs GET em Bottle

```python
@route('/submit', method=['GET', 'POST'])  
def submit():
    # Para POST (form data)
    query = request.forms.get('query')
    
    # Para GET (url parameters)
    color = request.query.get('color', 'white')
    
    return f"Query received: {query or '*'}"
```

>[!hint] 🎯 **Dica de segurança**: Usar POST para dados sensíveis - os usuários não podem injetar valores via URL sem autenticação.

### Template Variables em Bottle

```python
# Criar template (views/index.tpl)
{% for name in roster %}
    {{name}}<br>
{% endfor %}

<!-- ❌ Sem escape = risco de XSS -->
<a href="https://cnn.com">{{tim}}</a>

<!-- ✅ Com escape padrão do Bottle -->
<a href="https://example.com">Tim</a>
```

---

## 🔧 Módulo 5: Deploy em Digital Ocean e EngineX

### Arquitetura de Produção Recomendada

```
┌───────────────────┐
│   Cloudflare DNS │ ← HTTPS (flexible SSL)
└──────┬────────────┘
       ↓
┌───────────────────┐
│     Engine X      │ ← Reverse proxy
│  (config file)    │
└──────┬────────────┘
       ↓
┌───────────────────┐
│   Gunicorn +      │ ← WSGI HTTP server
│ Bottle Web App    │
└───────────────────┘
```

### Comandos de Deploy em Linux Ubuntu/VPS

```bash
# 1. Atualize o sistema e repositórios
sudo apt update
sudo apt upgrade

# 2. Instale EngineX (reverse proxy)
sudo pip3 install engine-x

# 3. Crie virtual environment para isolamento
python3 -m venv my_env
source my_env/bin/activate

# 4. Instale dependências
pip install bottle olama

# 5. Crie arquivo de serviço systemd (.service file)
sudo nano /etc/systemd/system/my-app.service

# Conteúdo do .service (exemplo simplificado):
[Unit]
Description=My App Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/my_env/bin/gunicorn -w 4 -b 127.0.0.1:8000 web_app:app

# 6. Carregue e inicie o serviço
sudo systemctl daemon-reload
sudo systemctl start my-app
sudo systemctl enable my-app

# 7. Configure EngineX (reverse proxy)
sudo nano /etc/engine-x/site-config.yml

# Adicione pass through para Gunicorn
pass to gunicorn://127.0.0.1:8000

# 8. Teste acessando IP + port 8000 ou domain name
curl http://seu-ip-localhost:8000
```

#### Considerações de Segurança no Deploy

| Camada | Vulnerabilidade Comum | Mitigação Recomendada |
|--------|----------------------|----------------------|
| **VPS** | Excesso de privilégios de root | Use usuário www-data, não root |
| **Bottle** | Falhas em parâmetros (,) | Valide entradas rigorosamente |
| **Gunicorn** | Amplificação web | Limite workers, rate limit |
| **EngineX** | Configuração errada | Teste via `engine-x check` antes de produção |
| **DNS** | Tempo de propagacao lento | Configure TTL baixo (1 min) + edita se necessário |

>[!important] ⚠️ **Dica de Erro Comum**: "Nunca use 127.0.0.1 em VPS - é loopback local! Use 0.0.0.0 ou IP específico."

### Custo e Escala em Digital Ocean

| Tamanho | RAM | CPU | LLM Suportado | Preço/Mês |
|---------|-----|-----|----------------|-----------|
| **$4** | 1GB | 2 vCPU | SM-LLM (135M) | $4 |
| **$6** | 2GB | 2 vCPU | SM-LLM + modelos básicos | $6 |
| **$12** | 2GB | 2 vCPU | Granite 350M, 7B | $12 |

>[!info] 💰 **Estratégia de Custo**: Se usar por horas/dias → Desligue e destrole o droplet para zero custo.

---

## 🧪 Laboratórios Práticos da Aula

### Lab 1: Bottle + Olama (API Simple)

```bash
# Instale módulo
pip install bottle olama

# Código web_app.py básico
from bottle import run, route, request
import llama.chat as chat_module

@route('/chat', method=['POST'])
def ai_chat():
    query = request.forms.get('query')
    
    # Envia para AI se não for POST
    response = None
    if request.method != 'POST':
        response = "*"
    else:
        try:
            response = chat_module.send_to_ai(query, "granite:350m")
        except:
            response = "Erro na chamada API"
    
    return f"Query: {query}, AI Response: {response}"

# Inicie
python web_app.py --port 8080
```

### Lab 2: Bottle + Olama + Template (Segurança)

```python
# views/ai_app.tpl (template seguro)
<html>
    <body>
        <form method="post" action="/submit">
            <input type="text" name="query" placeholder="Pergunta...">
            <button type="submit">Enviar</button>
        </form>
        {% if response %}
            <h3>{{response}}</h3>
        {% endif %}
    </body>
</html>
```

### Lab 3: Bottle + Olama + SQL Cache (Performance)

```python
import sqlite3
from bottle import run, route, request
from llama.chat import send_to_ai

# Conectar e criar tabelas se não existir
conn = sqlite3.connect('cache.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cache(query TEXT PRIMARY KEY, response TEXT)")
conn.commit()

def get_cached_response(query):
    cursor.execute("SELECT * FROM cache WHERE query=?", (query,))
    return cursor.fetchone()[1]

def save_to_cache(query, response):
    cursor.execute("INSERT OR REPLACE INTO cache VALUES(?, ?)", (query, response))
    conn.commit()

@route('/api/ask', method=['POST'])
def ask_ai():
    query = request.forms.get('query')
    
    # Tente buscar no cache primeiro
    cached = get_cached_response(query)
    if cached:
        return cached
    
    # Se não existir, chama AI e salva
    ai_resp = send_to_ai(query)
    save_to_cache(query, ai_resp)
    
    return ai_resp

# Executar
python web_app.py --port 8080
```

>[!note] 📈 **Resultado**: Segunda pergunta ao banco de dados (cache) vs primeira (API AI) = ~15x mais rápido!

---

## 🎯 Resumo dos Pontos-Chave

### Principais Tomadas da Aula

1. **Biblioteca vs Projeto**: "Python, SQL e Bottle são todos pequenos - juntam-se para formar grandes sistemas."
2. **Commas Matam Tudo**: "Você vai aprender tecnologia por osmose? Não. Se você esquecer a vírgula, todo dia é uma luta para debugar."
3. **Cache = Performance**: LLMs são caros e lentos. Cacheia 90% das consultas repetidas.
4. **Segurança First**: Templates sanitizam inputs; POST > GET para dados sensíveis; Use parâmetros sempre.
5. **Deploy Não é Mágica**: 8-12 passos, mas todos testáveis. Verifique EngineX, Gunicorn antes de DNS final.
6. **Custo Real vs Preço**: Digital Ocean permite pagar por horas (destrole e pague $0).

---

## 📚 Glossário de Termos Técnicos

| Termo | Definição |
|-------|-----------|
| **VPS** | Virtual Private Server (servidor em nuvem acessível via SSH) |
| **Gunicorn** | WSGI HTTP server para Bottle (multithreaded, melhor que built-in) |
| **EngineX** | Reverse proxy que enrute para Gunicorn baseado em regras |
| **ORM** | Object Relational Mapper (SQLAlchemy - não usado neste guia simplificado) |
| **LLM** | Large Language Model (Granite 350M, rodando localmente via Olama) |
| **Cache** | Armazenamento temporário de respostas para performance e custo |
| **SSL Flexible** | Modo Cloudflare onde tráfico browser→Cloudflare é HTTPS, mas Cloudflare→VPS não |

---

## 📖 Recursos Referenciados

- [Intro to SQL and Bottle for Building AI Apps in Python (Full Day) - YouTube](https://www.youtube.com/watch?v=AJ1qw8xYuxM)
- [GitHub - SiliconDojo/In-Person-Classes: Dump of Code and Material for Silicon Dojo · GitHub](https://github.com/SiliconDojo/In-Person-Classes/)
- [GitHub - SiliconDojo/Online-Classes: Notes, Slides and Code for Online Classes · GitHub](https://github.com/SiliconDojo/Online-Classes/)
- **Silicon Dojo Website**: silicon-dojo.com (documentação oficial)
- **Digital Ocean Droplet Pricing**: docs.digitalocean.com/pricing/
- **Bottle Framework Docs**: bottle.krafft.de/en/stable/
- **SQL Cheat Sheet**: https://www.w3resource.com/sql/index.php

---

>[!tip] 🎓 **Aula Final**: "Não aprendemos tecnologia por osmose - somos pessoas, não máquinas. Se esquecer a vírgula, todo dia é uma luta." (Trânsito original 2026-10-12)
