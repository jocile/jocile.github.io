---
description: "Exemplo prático de um cadastro com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
  - programacao
---

Para continuar a  **Prática CRUD Python SQLite com Bottle**, vamos expandir o sistema criando o módulo de **Cadastro de Produtos** integrado ao cadastro de **Clientes**.

Para manter o código organizado e com navegação entre as duas entidades no navegador, utilizaremos:

1. **Estrutura de Banco Relacional (DDL)** com uma nova tabela `produtos` contendo campos como `nome`, `preco` e `estoque`.
2. **Rotas dedicadas no Bottle** (`/produtos`, `/produtos/cadastrar`, `/produtos/editar/<id>` e `/produtos/deletar/<id>`).
3. **Navegação no Template Base** para alternar facilmente entre a gestão de **Clientes** e **Produtos**.

---

### **1. Atualização do Esquema do Banco de Dados (DDL)**

No banco de dados SQLite (`meu_banco_de_dados.db`), a nova tabela `produtos` utilizará os tipos `REAL` para valores monetários e `INTEGER` para o controle do estoque físico:

```sql
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
);
```

*(Modelagem da tabela de produtos com restrições de validação de preço e estoque).*

---

### **2. Estrutura das Pastas e Templates**

A organização recomendada para o projeto expandido é:

```text
meu_projeto/
│
├── app.py
├── meu_banco_de_dados.db
└── views/
    ├── base.tpl          # Layout base com menu de navegação
    ├── clientes.tpl      # Listagem e formulário de clientes
    ├── cliente_editar.tpl# Edição de cliente
    ├── produtos.tpl      # Listagem e formulário de produtos
    └── produto_editar.tpl# Edição de produto
```

---

### **3. Código dos Templates HTML (`.tpl`)**

#### **Layout Base (`views/base.tpl`)**

Adicionamos uma barra de navegação no topo para alternar entre as telas do sistema:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ get('titulo', 'Sistema de Gestão') }}</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: #f8f9fa; }
        nav { background: #0d6efd; padding: 1rem 2rem; }
        nav a { color: white; text-decoration: none; margin-right: 20px; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        main { max-width: 900px; margin: 30px auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .alerta { background: #f8d7da; color: #842029; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
        form.card { background: #f1f3f5; padding: 15px; border-radius: 6px; margin-bottom: 25px; }
        form.card input { display: block; margin-bottom: 10px; padding: 8px; width: 100%; box-sizing: border-box; }
        form.card input[type="submit"] { background: #198754; color: white; border: none; cursor: pointer; font-weight: bold; width: auto; padding: 10px 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #dee2e6; padding: 10px; text-align: left; }
        th { background: #e9ecef; }
        .btn-edit { color: #0d6efd; text-decoration: none; font-weight: bold; margin-right: 10px; }
        .btn-del { color: #dc3545; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <nav>
        <a href="/">👤 Clientes</a>
        <a href="/produtos">📦 Produtos</a>
    </nav>
    <main>
        {{!base}}
    </main>
</body>
</html>
```

#### **Tela de Produtos (`views/produtos.tpl`)**

```html
% rebase('base.tpl', titulo='Gestão de Produtos')

<h2>Cadastro de Produtos</h2>

% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end

<form class="card" action="/produtos/cadastrar" method="post">
    <label>Nome do Produto:</label>
    <input type="text" name="nome" required placeholder="Ex: Notebook, Mouse...">

    <label>Preço (R$):</label>
    <input type="number" step="0.01" name="preco" required placeholder="0.00">

    <label>Estoque Inicial:</label>
    <input type="number" name="estoque" required placeholder="0" value="0">

    <input type="submit" value="Cadastrar Produto">
</form>

<hr>

<h2>Produtos em Estoque</h2>
% if not lista_produtos:
    <p>Nenhum produto cadastrado até o momento.</p>
% else:
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Preço</th>
                <th>Estoque</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for p in lista_produtos:
            <tr>
                <td>{{ p['id'] }}</td>
                <td>{{ p['nome'] }}</td>
                <td>R$ {{ "%.2f" % p['preco'] }}</td>
                <td>{{ p['estoque'] }} unid.</td>
                <td>
                    <a class="btn-edit" href="/produtos/editar/{{ p['id'] }}">Editar</a>
                    <a class="btn-del" href="/produtos/deletar/{{ p['id'] }}" onclick="return confirm('Deseja excluir este produto?');">Excluir</a>
                </td>
            </tr>
            % end
        </tbody>
    </table>
% end
```

#### **Tela de Edição de Produto (`views/produto_editar.tpl`)**

```html
% rebase('base.tpl', titulo='Editar Produto')

<h2>Editar Produto #{{ produto['id'] }}</h2>

<form class="card" action="/produtos/editar/{{ produto['id'] }}" method="post">
    <label>Nome do Produto:</label>
    <input type="text" name="nome" value="{{ produto['nome'] }}" required>

    <label>Preço (R$):</label>
    <input type="number" step="0.01" name="preco" value="{{ produto['preco'] }}" required>

    <label>Estoque:</label>
    <input type="number" name="estoque" value="{{ produto['estoque'] }}" required>

    <input type="submit" value="Salvar Alterações">
    <a href="/produtos" style="margin-left: 10px; color: #6c757d; text-decoration: none;">Cancelar</a>
</form>
```

---

### **4. Código do Servidor HTTP em Python (`app.py`)**

Abaixo está o código em Python unificando o controle de **Clientes** e **Produtos** com manipulação segura de transações, validação e tratamento de exceções com `rollback()`:

```python
import sqlite3
from pathlib import Path
from bottle import get, post, request, redirect, template, run, abort

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")

def get_connection():
    """Abre a conexão com o banco de dados configurada para acesso por nome de coluna."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    """Cria as tabelas 'clientes' e 'produtos' no banco SQLite."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Tabela de Clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        
        # Tabela de Produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco >= 0.0),
                estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
            );
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# ==========================================
# ROTAS DE CLIENTES
# ==========================================

@get('/')
def listar_clientes():
    msg_erro = request.query.get('erro', '')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes ORDER BY id DESC;")
    clientes = cursor.fetchall()
    conn.close()
    return template('clientes', lista_clientes=clientes, msg_erro=msg_erro)

@post('/cadastrar')
def cadastrar_cliente():
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()

    if not nome or not email:
        redirect('/?erro=Preencha+todos+os+campos')

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        conn.rollback()
        redirect('/?erro=O+e-mail+já+está+cadastrado.')
    finally:
        conn.close()

@get('/editar/<id:int>')
def exibir_edicao_cliente(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        redirect('/?erro=Cliente+não+encontrado.')

    return template('cliente_editar', cliente=cliente)

@post('/editar/<id:int>')
def salvar_edicao_cliente(id):
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", (nome, email, id))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        conn.rollback()
        redirect('/?erro=O+e-mail+pertence+a+outro+cliente.')
    finally:
        conn.close()

@get('/deletar/<id:int>')
def deletar_cliente(id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()
    redirect('/')

# ==========================================
# ROTAS DE PRODUTOS (NOVO MÓDULO)
# ==========================================

@get('/produtos')
def listar_produtos():
    msg_erro = request.query.get('erro', '')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos ORDER BY id DESC;")
    produtos = cursor.fetchall()
    conn.close()
    return template('produtos', lista_produtos=produtos, msg_erro=msg_erro)

@post('/produtos/cadastrar')
def cadastrar_produto():
    nome = (request.forms.getunicode('nome') or '').strip()
    
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
    except ValueError:
        redirect('/produtos?erro=Preço+ou+estoque+inválidos.')

    if not nome or preco < 0 or estoque < 0:
        redirect('/produtos?erro=Informe+dados+válidos+para+o+produto.')

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?);", (nome, preco, estoque))
        conn.commit()
        redirect('/produtos')
    except sqlite3.Error as e:
        conn.rollback()
        redirect(f'/produtos?erro=Erro+ao+cadastrar+produto:+{e}')
    finally:
        conn.close()

@get('/produtos/editar/<id:int>')
def exibir_edicao_produto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE id = ?;", (id,))
    produto = cursor.fetchone()
    conn.close()

    if not produto:
        redirect('/produtos?erro=Produto+não+encontrado.')

    return template('produto_editar', produto=produto)

@post('/produtos/editar/<id:int>')
def salvar_edicao_produto(id):
    nome = (request.forms.getunicode('nome') or '').strip()
    
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
    except ValueError:
        redirect('/produtos?erro=Preço+ou+estoque+inválidos.')

    if not nome or preco < 0 or estoque < 0:
        redirect('/produtos?erro=Valores+inválidos+para+atualização.')

    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?;", (nome, preco, estoque, id))
        conn.commit()
        redirect('/produtos')
    except sqlite3.Error as e:
        conn.rollback()
        redirect(f'/produtos?erro=Erro+ao+atualizar+produto:+{e}')
    finally:
        conn.close()

@get('/produtos/deletar/<id:int>')
def deletar_produto(id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?;", (id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()
    redirect('/produtos')

if __name__ == '__main__':
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Como Executar e Testar**

1. Verifique se a estrutura de pastas e arquivos `.tpl` na pasta `views/` foi criada corretamente.
2. Execute o servidor no terminal:

   ```bash
   python app.py
   ```

3. Acesse **`http://localhost:8080`** no navegador:
   * Clique em **👤 Clientes** para gerenciar os clientes.
   * Clique em **📦 Produtos** para cadastrar, editar, listar e excluir produtos com controle de estoque e preços formatados.

---

>[!tip] ⬅️ [[Pratica CRUD Python Sqlite Quarta fase - tratamento de erros]]

>[!important] 🛒 Próximo passo: avançar um passo além criando uma tabela de **Pedidos** relacionando **Clientes** e **Produtos** com chave estrangeira (`FOREIGN KEY`) e cálculo automático de valor total do pedido
> [[Pratica CRUD Python Sqlite cadastro de pedidos]]
