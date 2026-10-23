---
description: "Exemplo prático de um cadastro com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
  - programacao
date: 2026-10-15
draft: true
---
Esta é uma **prática passo a passo** para quem está iniciando a integração de **Python com o banco de dados SQLite**. O SQLite é um banco de dados SQL leve, portátil e *serverless* (sem servidor). Além disso, o módulo `sqlite3` já vem pré-instalado na biblioteca padrão do Python.

## Fase inicial - criando o Banco de Dados

---

### **Objetivo da Prática**

Criar um banco de dados local, construir uma tabela de **clientes**, executar todas as operações fundamentais do ciclo **CRUD** (Criar, Ler, Atualizar e Deletar) e fechar a conexão de forma segura.

---

### **Passo 1: Conectar ao Banco de Dados**

Importe o módulo `sqlite3` e abra uma conexão chamando `sqlite3.connect()`. Se o arquivo `.db` ainda não existir no diretório, o SQLite irá criá-lo automaticamente. Em seguida, crie o objeto **cursor**, que é responsável por executar os comandos SQL na base.

```python
import sqlite3

# 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')

# 2. Cria o objeto cursor para enviar comandos SQL
cursor = conn.cursor()

print("Conexão estabelecida com sucesso!")
```

*(Conceitos de conexão e cursor baseados nos materiais).*

---

### **Passo 2: Criar uma Tabela (DDL)**

Defina a estrutura da tabela utilizando o comando DDL (**Data Definition Language**) `CREATE TABLE IF NOT EXISTS`. A tabela `clientes` terá uma chave primária autoincrementada (`id`), além de colunas para `nome`, `email` e `telefone`.

```python
# Executa a criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    );
''')

# Confirma a alteração estrutural no banco
conn.commit()
print("Tabela 'clientes' pronta para uso!")
```

*(Comando de criação estrutural e confirmação baseados nos materiais).*

---

### **Passo 3: Inserir Registros (DML - Create)**

Para evitar falhas de segurança como **SQL Injection**, nunca concatene variáveis diretamente no texto da query; utilize **marcadores de posição** (`?`). Você pode inserir múltiplos registros em lote usando o método `cursor.executemany()` e depois confirmar as alterações com `conn.commit()`.

```python
# Lista de tuplas com os dados de exemplo
novos_clientes = [
    ("Ana Silva", "ana.silva@example.com", "11 99999-0001"),
    ("Bruno Souza", "bruno.souza@example.com", "11 99999-0002"),
    ("Carla Pereira", "carla.pereira@example.com", "11 99999-0003")
]

# Inserção em lote usando placeholders (?)
cursor.executemany(
    "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
    novos_clientes
)

# Salva permanentemente a inserção no arquivo do banco
conn.commit()
print(f"{cursor.rowcount} registros inseridos com sucesso!")
```

*(Inserção segura com marcadores de posição baseada nos materiais).*

---

### **Passo 4: Consultar os Dados (DQL - Read)**

Para consultar as informações salvas, execute uma instrução `SELECT`. Utilize o método `fetchall()` para obter todas as linhas retornadas.

```python
# Executa a consulta
cursor.execute("SELECT id, nome, email, telefone FROM clientes;")

# Recupera todas as linhas encontradas
resultados = cursor.fetchall()

print("\n--- Lista de Clientes ---")
for id_, nome, email, telefone in resultados:
    print(f"ID: {id_} | Nome: {nome} | E-mail: {email} | Telefone: {telefone}")
```

*(Consulta de dados e varredura de resultados baseadas nos materiais).*

---

### **Passo 5: Atualizar e Excluir Registros (Update / Delete)**

Para alterar dados existentes ou remover um registro, utilize os comandos `UPDATE` e `DELETE` acompanhados da cláusula `WHERE` e dos marcadores `?`.

```python
# 1. Atualizar e-mail de um cliente específico pelo ID
cursor.execute(
    "UPDATE clientes SET email = ? WHERE id = ?;",
    ("ana.nova@example.com", 1)
)

# 2. Deletar um cliente específico pelo ID
cursor.execute(
    "DELETE FROM clientes WHERE id = ?;",
    (3,)
)

# Confirma as alterações no banco de dados
conn.commit()
print("\nAlterações de atualização e exclusão aplicadas!")
```

*(Comandos DML de atualização e exclusão baseados nos materiais).*

---

### **Passo 6: Fechar a Conexão**

Após concluir todas as operações, feche o cursor e a conexão para garantir a liberação de recursos do sistema e a consistência do arquivo.

```python
cursor.close()
conn.close()
print("Conexão fechada com segurança.")
```

*(Fechamento e boas práticas baseados nos materiais).*

>[!done]  Veja o código completo em:
> [GitHub - profjocile/cadastro-de-clientes: Exercício de um CRUD com banco de dados SQLite e front end Bottle · GitHub](https://github.com/profjocile/cadastro-de-clientes)

---

### **Passo Bônus: Leitura Avançada com Pandas**

Você também pode integrar o banco SQLite à biblioteca **Pandas** para carregar os dados diretamente em um DataFrame usando `pd.read_sql_query()`.

```python
import pandas as pd

conn = sqlite3.connect('meu_banco_de_dados.db')

# Carrega a consulta direto em um DataFrame do Pandas
df_clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
print("\n--- DataFrame do Pandas ---")
print(df_clientes)

conn.close()
```

💡 Agora que tal expandir essa prática, vamos conectar esses comandos a uma interface web simples utilizando o micro-framework **Bottle** para criar um sistema com formulários no navegador.

## Segunda fase - Front End Web

Para expandir a prática anterior e integrar o banco de dados **SQLite** a uma interface web no navegador, utiliza-se o **Bottle**, um micro-framework WSGI para Python leve, rápido e distribuído em arquivo único, que não possui dependências de terceiros além da biblioteca padrão.

Nesta etapa, você criará uma aplicação web em um único arquivo Python que permite **cadastrar**, **listar** e **excluir** clientes diretamente por meio de formulários HTML no navegador.

---

### **Pré-requisito: Instalação do Bottle**

Antes de iniciar o script, instale o micro-framework Bottle, copiando o [arquivo do Bottle](https://github.com/bottlepy/bottle) para seu projeto ou executando o comando no terminal:

```bash
pip install bottle
```

---

### **Passo a Passo da Aplicação Web**

#### **1. Configuração do Servidor e Banco de Dados**

Importe os módulos do Bottle (`route`, `get`, `post`, `request`, `redirect`, `template`, `run`) e o módulo `sqlite3`. Em seguida, crie uma função para garantir que a tabela `clientes` exista no banco de dados SQLite antes de iniciar o servidor web.

#### **2. Rota Principal (`GET /`): Exibir Formulário e Listagem**

Crie uma rota para a raiz da aplicação (`/`). Esta rota se conecta ao SQLite, busca todos os registros gravados com `SELECT` e renderiza na tela tanto o formulário HTML para novos cadastros quanto a tabela com os clientes existentes.

#### **3. Rota de Cadastro (`POST /cadastrar`): Processar o Formulário**

Crie uma rota `POST` que recebe os dados digitados no formulário utilizando `request.forms.get('nome')` e `request.forms.get('email')`. Insira esses dados de forma segura no SQLite utilizando marcadores de posição (`?`), confirme a gravação com `commit()` e redirecione o usuário de volta para a página principal com `redirect('/')`.

#### **4. Rota de Exclusão (`GET /deletar/<id:int>`): Remover Registros**

Utilize um filtro dinâmico de URL `<id:int>` para capturar o ID do cliente que deve ser removido. Execute o comando `DELETE FROM clientes WHERE id = ?`, confirme as alterações e redirecione o navegador.

#### **5. Execução do Servidor HTTP Local**

Inicie o servidor HTTP embutido utilizando o método `run(host='localhost', port=8080)`.

---

### **Código Completo do Sistema Web (`app.py`)**

```python
import sqlite3
from bottle import route, get, post, request, redirect, template, run

DB_NAME = 'meu_banco_de_dados.db'

def inicializar_banco():
    """Garante que a tabela 'clientes' esteja criada no banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# 1. ROTA PRINCIPAL: Lista os clientes e exibe o formulário de cadastro
@route('/', method=['GET','POST'])
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()

    # Layout HTML com SimpleTemplate incorporado
    html_template = '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Gestão de Clientes - Bottle + SQLite</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                h1, h2 { color: #333; }
                form { margin-bottom: 20px; background: #f4f4f4; padding: 15px; border-radius: 5px; }
                input { margin-bottom: 10px; padding: 8px; width: 250px; display: block; }
                input[type="submit"] { background: #28a745; color: white; border: none; cursor: pointer; width: 120px; }
                table { width: 100%; border-collapse: collapse; margin-top: 10px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #007bff; color: white; }
                .btn-del { color: red; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Cadastro de Clientes</h1>
            
            <form action="/cadastrar" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" required placeholder="Digite o nome completo">
                
                <label>E-mail:</label>
                <input type="email" name="email" required placeholder="exemplo@email.com">
                
                <input type="submit" value="Cadastrar">
            </form>

            <h2>Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
                % for id_, nome, email in lista_clientes:
                <tr>
                    <td>{{id_}}</td>
                    <td>{{nome}}</td>
                    <td>{{email}}</td>
                    <td><a class="btn-del" href="/deletar/{{id_}}">Excluir</a></td>
                </tr>
                % end
            </table>
        </body>
        </html>
    '''
    return template(html_template, lista_clientes=clientes)

# 2. ROTA DE CADASTRO: Recebe os dados do formulário via POST
@route('/cadastrar', method=['GET','POST'])
def cadastrar():
    nome = request.forms.get('nome')
    email = request.forms.get('email')

    if nome and email:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        conn.commit()
        conn.close()

    redirect('/')

# 3. ROTA DE EXCLUSÃO: Remove o registro do banco pelo ID
@route('/deletar/<id:int>', method=['GET','POST'])
def deletar(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
    
    redirect('/')

if __name__ == '__main__':
    # Inicializa a estrutura da tabela
    inicializar_banco()
    
    print("Iniciando o servidor Bottle em http://localhost:8080 ...")
    # Inicia o servidor HTTP embutido
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Como Executar o Projeto**

1. Salve o código acima em um arquivo chamado `app.py`.
2. Abra o terminal na pasta do arquivo e execute:

   ```bash
   python app.py
   ```

3. Abra o seu navegador e acesse: **`http://localhost:8080`**.
4. Teste preencher o formulário para adicionar novos clientes e clique em **Excluir** para remover um cliente cadastrado do banco de dados.

---

>[!done]  Veja o código completo em:
> [GitHub - profjocile/cadastro-de-clientes: Exercício de um CRUD com banco de dados SQLite e front end Bottle · GitHub](https://github.com/profjocile/cadastro-de-clientes)

🌐 Próximos passos: adicionar uma funcionalidade para **editar/atualizar** os dados de um cliente existente diretamente pelo navegador

## Terceira Fase - adicionando funcionalidade editar

Para integrar a funcionalidade de **Edição/Atualização (UPDATE)** no navegador com **Bottle** e **SQLite**, implementa-se o padrão web tradicional composto por duas etapas:

1. **Rota `GET /editar/<id:int>`**: Busca os dados atuais do cliente no SQLite pelo seu ID e renderiza um formulário preenchido com as informações existentes.
2. **Rota `POST /editar/<id:int>`**: Recebe os novos dados enviados pelo formulário e executa o comando SQL `UPDATE` de forma segura com marcadores de posição `?`.

---

### **Como Funciona a Lógica de Edição**

* **Captura do ID na URL**: Utiliza-se o filtro dinâmico de rota `<id:int>` do Bottle para capturar o ID do cliente que será alterado
* **Busca do Registro**: Executa-se `SELECT id, nome, email FROM clientes WHERE id = ?` e recupera-se o registro individual usando `cursor.fetchone()`
* **Atualização no Banco**: No envio do formulário, os dados capturados com `request.forms.get()` são passados para a instrução `UPDATE clientes SET nome = ?, email = ? WHERE id = ?`. A transação é gravada com `conn.commit()` e o usuário é redirecionado de volta à página principal com `redirect('/')`.

---

### **Código Completo Atualizado (`app.py`)**

Abaixo está a versão completa do script, com a listagem, cadastro, exclusão e a **nova rota de edição completa**:

```python
import sqlite3
from bottle import route, get, post, request, redirect, template, run

DB_NAME = 'meu_banco_de_dados.db'

def inicializar_banco():
    """Garante a existência da tabela 'clientes' no banco SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# 1. ROTA PRINCIPAL: Listagem de Clientes e Formulário de Cadastro
@route('/', method=['GET','POST'])
def index():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()

    html_template = '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Gestão de Clientes - Bottle + SQLite</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                h1, h2 { color: #333; }
                form { margin-bottom: 20px; background: #f4f4f4; padding: 15px; border-radius: 5px; }
                input { margin-bottom: 10px; padding: 8px; width: 250px; display: block; }
                input[type="submit"] { background: #28a745; color: white; border: none; cursor: pointer; width: 120px; }
                table { width: 100%; border-collapse: collapse; margin-top: 10px; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #007bff; color: white; }
                .btn-edit { color: #007bff; text-decoration: none; font-weight: bold; margin-right: 10px; }
                .btn-del { color: red; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Cadastro de Clientes</h1>
            
            <form action="/cadastrar" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" required placeholder="Digite o nome completo">
                
                <label>E-mail:</label>
                <input type="email" name="email" required placeholder="exemplo@email.com">
                
                <input type="submit" value="Cadastrar">
            </form>

            <h2>Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
                % for id_, nome, email in lista_clientes:
                <tr>
                    <td>{{id_}}</td>
                    <td>{{nome}}</td>
                    <td>{{email}}</td>
                    <td>
                        <a class="btn-edit" href="/editar/{{id_}}">Editar</a>
                        <a class="btn-del" href="/deletar/{{id_}}">Excluir</a>
                    </td>
                </tr>
                % end
            </table>
        </body>
        </html>
    '''
    return template(html_template, lista_clientes=clientes)

# 2. ROTA DE CADASTRO (Novo Cliente)
@route('/cadastrar', method=['GET','POST'])
def cadastrar():
    nome = request.forms.get('nome')
    email = request.forms.get('email')

    if nome and email:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        conn.commit()
        conn.close()

    redirect('/')

# 3. ROTA DE EDIÇÃO - EXIBIR FORMULÁRIO (GET)
@route('/editar/<id:int>', method=['GET','POST'])
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        redirect('/')

    html_editar = '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Editar Cliente</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                h1 { color: #333; }
                form { background: #f4f4f4; padding: 15px; border-radius: 5px; width: 300px; }
                input { margin-bottom: 10px; padding: 8px; width: 90%; display: block; }
                input[type="submit"] { background: #007bff; color: white; border: none; cursor: pointer; width: 100px; }
                a { color: #6c757d; text-decoration: none; display: inline-block; margin-top: 10px; }
            </style>
        </head>
        <body>
            <h1>Editar Cliente #{{cliente}}</h1>
            
            <form action="/editar/{{cliente}}" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" value="{{cliente}}" required>
                
                <label>E-mail:</label>
                <input type="email" name="email" value="{{cliente}}" required>
                
                <input type="submit" value="Salvar">
            </form>

            <a href="/">← Cancelar e Voltar</a>
        </body>
        </html>
    '''
    return template(html_editar, cliente=cliente)

# 4. ROTA DE EDIÇÃO - SALVAR ALTERAÇÕES (POST)
@route('/editar/<id:int>', method=['GET','POST'])
def salvar_edicao(id):
    nome = request.forms.get('nome')
    email = request.forms.get('email')

    if nome and email:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Atualiza os dados com a instrução SQL UPDATE usando parâmetros seguros
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ? WHERE id = ?;",
            (nome, email, id)
        )
        conn.commit()
        conn.close()

    redirect('/')

# 5. ROTA DE EXCLUSÃO
@route('/deletar/<id:int>', method=['GET','POST'])
def deletar(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
    
    redirect('/')

if __name__ == '__main__':
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Testando no Navegador**

1. Salve o código e inicie o aplicativo no terminal:

   ```bash
   python app.py
   ```

2. Acesse **`http://localhost:8080`**.
3. Na tabela de clientes cadastrados, clique no link **Editar**.
4. O navegador abrirá a tela com os campos preenchidos com o nome e e-mail atuais.
5. Modifique os valores e clique em **Salvar**. Os dados atualizados serão salvos no SQLite com `UPDATE` e exibidos na tabela principal.

### 🔍 Análise do Código

#### ✅ O que está bom

* Consultas parametrizadas (?) em todos os comandos SQL. Isso protege contra SQL injection.
* Padrão `Post/Redirect/Get`: depois de cadastrar, editar ou excluir, você redireciona para /. Isso evita reenvio do formulário ao atualizar a página.
* Escape automático: o `{{ }}` do Bottle escapa HTML por padrão, então o código não tem XSS ao exibir nome e e-mail.
* `Conversor <id:int>` na rota, que valida o parâmetro antes de a função rodar.
* `CREATE TABLE IF NOT EXISTS` deixa a inicialização idempotente, o que também ajuda com o `reloader=True`.

#### 🐛 Bugs / Erros

* A tela de edição renderiza a tupla inteira. Em exibir_formulario_edicao, cliente é `(id, nome, email)`, e o template usa {{cliente}} em todo lugar. O título, o action e os value recebem (`1, 'Ana', 'ana@x.com'`). O formulário envia para uma URL inválida `(/editar/(1, 'Ana', ...))` e dá 404. O correto é cliente[0], cliente[1] e cliente[2].
* A rota `/editar/<id:int>` está registrada duas vezes com os mesmos métodos. Testei: o Bottle mantém só a última definição. Por isso salvar_edicao responde também ao GET, e o formulário de edição nunca é exibido. O GET cai no redirect('/'). É para isso que servem os get e post que você importou e não usou.
* Acentos podem ser gravados quebrados. No Python 3, request.forms.get() devolve o texto decodificado como latin-1. Um nome como “João” pode virar “JoÃ£o”. O correto é request.forms.getunicode('nome').
* A validação falha em silêncio. Se nome ou email vier vazio, o código faz redirect('/') sem avisar ninguém. Também passa um nome só com espaços, e o e-mail não é validado no servidor. Só o HTML valida, e isso é fácil de burlar.

#### ⚠️ Melhorias de Qualidade

* Use os métodos certos. method=['GET','POST'] em todas as rotas é frouxo demais. /cadastrar, /deletar e a gravação da edição deveriam aceitar só POST. Use @get e @post.
* Abrir e fechar conexão repetido seis vezes. Se der erro entre connect e close, a conexão vaza. Um context manager com try/finally resolve isso e elimina a repetição.
* Registro inexistente vira redirect. Para ID inexistente o certo é abort(404). No `UPDATE`, `cursor.rowcount == 0` indica que nada foi alterado.
* O caminho do banco é relativo. `DB_NAME` depende do diretório de onde você roda o script. Prefira `Path(__file__).with_name(...)`.
* HTML e CSS dentro do .py, e o CSS repetido nos dois templates. O ideal é a pasta views/ com arquivos .tpl.
* id sombreia a função embutida `id()`. Use `cliente_id`.
* Falta type hint e docstring. Também há imports sem uso (get, post).
* Não há mensagem para lista vazia. A tabela aparece só com o cabeçalho.

#### ⚡ Oportunidades de Performance

Para um CRUD pequeno não há problema. Se a tabela crescer, adicione `ORDER BY` e paginação (LIMIT/OFFSET) na listagem.

#### 🔒 Segurança

Exclusão por link GET (`<a href="/deletar/1">`). Qualquer pré-carregamento do navegador, extensão ou página externa pode apagar registros com um simples acesso a essa URL. Use um `<form method="post">` com confirm() no navegador. No código corrigido, testei que o GET passou a retornar 405.
Não há token CSRF. Num projeto local não é crítico. Se algum dia o app for publicado, vale incluir.
`debug=True` e `reloader=True` expõem `tracebacks` completos no navegador. Desligue os dois em produção.

### Versão refatorada

Ests versão corrigida aplica tudo isso, usando `@get/@post`, `getunicode`, context manager de conexão, `sqlite3.Row` para acessar colunas por nome, exclusão via `POST` e 404 para ID inexistente.

```python
"""CRUD de clientes com Bottle + SQLite.

Requisitos: Python 3.12+ e `bottle`.
Executar: python app_clientes.py  ->  http://localhost:8080
"""

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from bottle import abort, get, post, redirect, request, run, template

# Caminho absoluto: não depende do diretório de onde o script é executado.
DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")

STYLE = """
body { font-family: Arial, sans-serif; margin: 30px; }
h1, h2 { color: #333; }
form.card { margin-bottom: 20px; background: #f4f4f4; padding: 15px;
            border-radius: 5px; width: 300px; }
form.card input { margin-bottom: 10px; padding: 8px; width: 90%; display: block; }
form.card input[type="submit"] { background: #28a745; color: white; border: none;
                                 cursor: pointer; width: 120px; }
form.inline { display: inline; }
table { width: 100%; border-collapse: collapse; margin-top: 10px; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #007bff; color: white; }
.btn-edit { color: #007bff; text-decoration: none; font-weight: bold;
            margin-right: 10px; }
.btn-del { color: red; font-weight: bold; background: none; border: none;
           cursor: pointer; padding: 0; font-size: 1em; }
a.voltar { color: #6c757d; text-decoration: none; }
"""

INDEX_TPL = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Gestão de Clientes - Bottle + SQLite</title>
    <style>{{!estilo}}</style>
</head>
<body>
    <h1>Cadastro de Clientes</h1>

    <form class="card" action="/cadastrar" method="post">
        <label>Nome:</label>
        <input type="text" name="nome" required placeholder="Digite o nome completo">
        <label>E-mail:</label>
        <input type="email" name="email" required placeholder="exemplo@email.com">
        <input type="submit" value="Cadastrar">
    </form>

    <h2>Clientes Cadastrados</h2>
    % if not clientes:
    <p>Nenhum cliente cadastrado ainda.</p>
    % else:
    <table>
        <tr><th>ID</th><th>Nome</th><th>E-mail</th><th>Ações</th></tr>
        % for c in clientes:
        <tr>
            <td>{{c['id']}}</td>
            <td>{{c['nome']}}</td>
            <td>{{c['email']}}</td>
            <td>
                <a class="btn-edit" href="/editar/{{c['id']}}">Editar</a>
                <form class="inline" action="/deletar/{{c['id']}}" method="post"
                      onsubmit="return confirm('Excluir este cliente?');">
                    <button class="btn-del" type="submit">Excluir</button>
                </form>
            </td>
        </tr>
        % end
    </table>
    % end
</body>
</html>
"""

EDIT_TPL = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Editar Cliente</title>
    <style>{{!estilo}}</style>
</head>
<body>
    <h1>Editar Cliente #{{cliente['id']}}</h1>

    <form class="card" action="/editar/{{cliente['id']}}" method="post">
        <label>Nome:</label>
        <input type="text" name="nome" value="{{cliente['nome']}}" required>
        <label>E-mail:</label>
        <input type="email" name="email" value="{{cliente['email']}}" required>
        <input type="submit" value="Salvar">
    </form>

    <a class="voltar" href="/">← Cancelar e Voltar</a>
</body>
</html>
"""


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    """Abre uma conexão SQLite, confirma ao final e sempre a fecha.

    Yields:
        Conexão com `row_factory` configurada para acesso por nome de coluna.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def inicializar_banco() -> None:
    """Garante a existência da tabela 'clientes'."""
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """
        )


def ler_formulario() -> tuple[str, str]:
    """Lê e valida nome/e-mail do formulário enviado.

    Returns:
        Tupla (nome, email) já sem espaços nas pontas.

    Raises:
        HTTPError: 400 se algum campo estiver vazio ou o e-mail for inválido.
    """
    # getunicode() corrige a decodificação (latin-1) que o Bottle faz no Python 3,
    # evitando "JoÃ£o" no banco quando há acentos.
    nome = (request.forms.getunicode("nome") or "").strip()
    email = (request.forms.getunicode("email") or "").strip()
    if not nome or "@" not in email:
        abort(400, "Informe um nome e um e-mail válidos.")
    return nome, email


@get("/")
def index() -> str:
    """Lista os clientes e exibe o formulário de cadastro."""
    with get_connection() as conn:
        clientes = conn.execute(
            "SELECT id, nome, email FROM clientes ORDER BY id;"
        ).fetchall()
    return template(INDEX_TPL, clientes=clientes, estilo=STYLE)


@post("/cadastrar")
def cadastrar() -> None:
    """Cria um novo cliente e volta para a listagem (Post/Redirect/Get)."""
    nome, email = ler_formulario()
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email)
        )
    redirect("/")


@get("/editar/<cliente_id:int>")
def exibir_formulario_edicao(cliente_id: int) -> str:
    """Exibe o formulário de edição preenchido com os dados do cliente."""
    with get_connection() as conn:
        cliente = conn.execute(
            "SELECT id, nome, email FROM clientes WHERE id = ?;", (cliente_id,)
        ).fetchone()
    if cliente is None:
        abort(404, "Cliente não encontrado.")
    return template(EDIT_TPL, cliente=cliente, estilo=STYLE)


@post("/editar/<cliente_id:int>")
def salvar_edicao(cliente_id: int) -> None:
    """Atualiza nome e e-mail do cliente."""
    nome, email = ler_formulario()
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE clientes SET nome = ?, email = ? WHERE id = ?;",
            (nome, email, cliente_id),
        )
    if cursor.rowcount == 0:
        abort(404, "Cliente não encontrado.")
    redirect("/")


@post("/deletar/<cliente_id:int>")
def deletar(cliente_id: int) -> None:
    """Remove o cliente. Só aceita POST, para evitar exclusão por simples link."""
    with get_connection() as conn:
        conn.execute("DELETE FROM clientes WHERE id = ?;", (cliente_id,))
    redirect("/")


if __name__ == "__main__":
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    # Em produção: debug=False e reloader=False.
    run(host="localhost", port=8080, debug=True, reloader=True)
```

>[!done]  Veja o código completo em:
> [GitHub - profjocile/cadastro-de-clientes: Exercício de um CRUD com banco de dados SQLite e front end Bottle · GitHub](https://github.com/profjocile/cadastro-de-clientes)

💡 Próximos passos: como tratar erros de banco de dados (usando `try/except` com `rollback()`) para evitar que a aplicação caia em caso de falha de conexão.

## Quarta fase - tratamento de erros

O tratamento de erros em operações de banco de dados baseia-se no princípio de **atomicidade** das transações. A atomicidade garante a regra do "tudo ou nada": todas as instruções da transação devem ser executadas com sucesso ou nenhuma delas será mantida no banco.

Se ocorrer alguma falha no meio de uma operação de escrita (`INSERT`, `UPDATE`, `DELETE`), o método `rollback()` desfaz todas as alterações pendentes daquela transação, restaurando o banco ao seu estado consistente anterior. Caso a transação ocorra totalmente sem falhas, executa-se o `commit()` para gravar as alterações permanentemente no arquivo.

---

### **1. Principais Exceções do Módulo `sqlite3`**

Ao manipular o SQLite em Python, as exceções tratadas herdam da classe base `sqlite3.Error`:

* **`sqlite3.IntegrityError`**: Lançada quando ocorre uma violação de integridade relacional, como tentar cadastrar um e-mail duplicado em uma coluna com restrição `UNIQUE` ou utilizar uma chave estrangeira inválida.
* **`sqlite3.OperationalError`**: Lançada em erros operacionais do banco, como tentar acessar uma tabela que não existe ou quando a base está bloqueada por outro processo (*database locked*).
* **`sqlite3.Error`**: Captura qualquer exceção genérica da biblioteca `sqlite3`.

---

### **2. Padrão Estrutural com `try / except / else / finally`**

Em scripts Python, a boa prática exige envolver a execução dos comandos SQL dentro de um bloco de tratamento de exceções.

```python
import sqlite3

def cadastrar_cliente_seguro(nome, email):
    conn = None
    try:
        conn = sqlite3.connect('meu_banco_de_dados.db')
        cursor = conn.cursor()
        
        # Executa o comando de inserção
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        
        # Se nenhuma exceção ocorreu, confirma as alterações no banco
        conn.commit()
        print("Cliente cadastrado com sucesso!")
        
    except sqlite3.IntegrityError as e:
        # Reverte as alterações pendentes da transação
        if conn:
            conn.rollback()
        print(f"Erro de integridade (ex: e-mail duplicado): {e}")
        
    except sqlite3.Error as e:
        # Reverte qualquer outra falha no banco de dados
        if conn:
            conn.rollback()
        print(f"Erro operacional no banco de dados: {e}")
        
    finally:
        # Garante a liberação dos recursos e o fechamento da conexão
        if conn:
            conn.close()
            print("Conexão fechada com segurança.")
```

*(Estrutura de controle transacional e tratamento de falhas baseada nos materiais).*

---

### **3. Protegendo a Aplicação Web Bottle Contra Quedas**

Em uma aplicação web, se uma rota tentar inserir dados inválidos sem tratamento de exceção, o Python lançará uma falha não capturada que derrubará a requisição HTTP com um erro desformatado no navegador.

Abaixo está o código completo do servidor **Bottle + SQLite** atualizado, onde as rotas contêm blocos `try/except/finally` com `rollback()` e redirecionam o usuário exibindo mensagens amigáveis na tela:

```python
import sqlite3
from bottle import get, post, request, redirect, template, run

DB_NAME = 'meu_banco_de_dados.db'

def inicializar_banco():
    """Cria a tabela de clientes garantindo a restrição UNIQUE na coluna email."""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inicializar tabela: {e}")
    finally:
        if conn:
            conn.close()

# 1. ROTA PRINCIPAL: Exibe alertas de erro e listagem de clientes
@route('/', method=['GET','POST'])
def index():
    msg_erro = request.query.get('erro', '')
    clientes = []
    
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM clientes;")
        clientes = cursor.fetchall()
    except sqlite3.Error as e:
        msg_erro = f"Falha ao carregar clientes: {e}"
    finally:
        if conn:
            conn.close()

    html_template = '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Gestão de Clientes - Bottle + SQLite</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                .alerta { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; padding: 10px; border-radius: 5px; margin-bottom: 15px; }
                form { background: #f4f4f4; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
                input { margin-bottom: 10px; padding: 8px; width: 250px; display: block; }
                input[type="submit"] { background: #28a745; color: white; border: none; cursor: pointer; width: 120px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #007bff; color: white; }
                .btn-edit { color: #007bff; text-decoration: none; margin-right: 10px; font-weight: bold; }
                .btn-del { color: red; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Cadastro de Clientes</h1>
            
            % if msg_erro:
                <div class="alerta">⚠️ <strong>Erro:</strong> {{msg_erro}}</div>
            % end

            <form action="/cadastrar" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" required placeholder="Digite o nome completo">
                
                <label>E-mail:</label>
                <input type="email" name="email" required placeholder="exemplo@email.com">
                
                <input type="submit" value="Cadastrar">
            </form>

            <h2>Clientes Cadastrados</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
                % for id_, nome, email in lista_clientes:
                <tr>
                    <td>{{id_}}</td>
                    <td>{{nome}}</td>
                    <td>{{email}}</td>
                    <td>
                        <a class="btn-edit" href="/editar/{{id_}}">Editar</a>
                        <a class="btn-del" href="/deletar/{{id_}}">Excluir</a>
                    </td>
                </tr>
                % end
            </table>
        </body>
        </html>
    '''
    return template(html_template, lista_clientes=clientes, msg_erro=msg_erro)

# 2. ROTA DE CADASTRO COM TRATAMENTO DE ERROS E ROLLBACK
@route('/cadastrar', method=['GET','POST'])
def cadastrar():
    nome = request.forms.get('nome')
    email = request.forms.get('email')

    if not nome or not email:
        redirect('/?erro=Preencha+todos+os+campos')

    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        if conn:
            conn.rollback()
        redirect('/?erro=O+e-mail+informado+já+está+cadastrado.')
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        redirect(f'/?erro=Erro+no+banco+de+dados:+{e}')
    finally:
        if conn:
            conn.close()

# 3. ROTA DE EDIÇÃO (EXIBIR FORMULÁRIO)
@route('/editar/<id:int>', method=['GET','POST'])
def exibir_formulario_edicao(id):
    conn = None
    cliente = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
        cliente = cursor.fetchone()
    except sqlite3.Error as e:
        redirect(f'/?erro=Erro+ao+buscar+cliente:+{e}')
    finally:
        if conn:
            conn.close()

    if not cliente:
        redirect('/?erro=Cliente+não+encontrado')

    html_editar = '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Editar Cliente</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 30px; }
                form { background: #f4f4f4; padding: 15px; border-radius: 5px; width: 300px; }
                input { margin-bottom: 10px; padding: 8px; width: 90%; display: block; }
                input[type="submit"] { background: #007bff; color: white; border: none; cursor: pointer; width: 100px; }
                a { color: #6c757d; text-decoration: none; display: inline-block; margin-top: 10px; }
            </style>
        </head>
        <body>
            <h1>Editar Cliente #{{cliente}}</h1>
            
            <form action="/editar/{{cliente}}" method="post">
                <label>Nome:</label>
                <input type="text" name="nome" value="{{cliente}}" required>
                
                <label>E-mail:</label>
                <input type="email" name="email" value="{{cliente}}" required>
                
                <input type="submit" value="Salvar">
            </form>

            <a href="/">← Cancelar e Voltar</a>
        </body>
        </html>
    '''
    return template(html_editar, cliente=cliente)

# 4. ROTA DE EDIÇÃO (SALVAR ALTERAÇÕES COM ROLLBACK)
@route('/editar/<id:int>', method=['GET','POST'])
def salvar_edicao(id):
    nome = request.forms.get('nome')
    email = request.forms.get('email')

    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", (nome, email, id))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        if conn:
            conn.rollback()
        redirect('/?erro=O+e-mail+informado+já+pertence+a+outro+cliente.')
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        redirect(f'/?erro=Erro+ao+atualizar:+{e}')
    finally:
        if conn:
            conn.close()

# 5. ROTA DE EXCLUSÃO
@route('/deletar/<id:int>', method=['GET','POST'])
def deletar(id):
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        redirect(f'/?erro=Erro+ao+excluir:+{e}')
    finally:
        if conn:
            conn.close()
            
    redirect('/')

if __name__ == '__main__':
    inicializar_banco()
    print("Iniciando servidor robusto em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Vantagens Práticas Desta Abordagem**

1. **Prevenção de Quedas na Aplicação**: Ao tentar cadastrar um e-mail repetido, a exceção `sqlite3.IntegrityError` é capturada, o `rollback()` cancela a instrução com falha e o sistema avisa o usuário na tela sem travar a aplicação web.
2. **Consistência do Banco de Dados**: A base de dados permanece livre de registros parciais ou transações abertas pendentes.
3. **Gerenciamento Seguro de Recursos**: O bloco `finally` garante que `conn.close()` seja executado obrigatoriamente, evitando vazamento de conexões ou travamentos no arquivo do SQLite.

>[!done]  Veja o código completo em:
> [GitHub - profjocile/cadastro-de-clientes: Exercício de um CRUD com banco de dados SQLite e front end Bottle · GitHub](https://github.com/profjocile/cadastro-de-clientes)
