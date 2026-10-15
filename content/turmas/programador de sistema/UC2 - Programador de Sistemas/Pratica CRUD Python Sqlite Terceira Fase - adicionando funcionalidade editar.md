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
@get('/')
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
@post('/cadastrar')
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
@get('/editar/<id:int>')
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
@post('/editar/<id:int>')
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
@get('/deletar/<id:int>')
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

💡 Próximos passos: como tratar erros de banco de dados (usando `try/except` com `rollback()`) para evitar que a aplicação caia em caso de falha de conexão.

[[Pratica CRUD Python Sqlite Quarta fase - tratamento de erros]]
