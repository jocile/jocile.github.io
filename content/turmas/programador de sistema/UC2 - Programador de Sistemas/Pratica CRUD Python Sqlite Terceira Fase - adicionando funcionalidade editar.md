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
draft: false
---
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

⬅️ [[Pratica CRUD Python Sqlite Segunda fase - Front End Web]] | ➡️ [[Pratica CRUD Python Sqlite Quarta fase - tratamento de erros]]
