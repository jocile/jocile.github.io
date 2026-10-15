---
description: "Exemplo prático de um tratamento de erros com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
date: 2026-10-15
draft: false
---
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
@get('/')
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
@post('/cadastrar')
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
@get('/editar/<id:int>')
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
@post('/editar/<id:int>')
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
@get('/deletar/<id:int>')
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

💡 Próximos passos: como automatizar **backups seguros** do arquivo `.db` via Python sem interromper o funcionamento da sua aplicação web.
