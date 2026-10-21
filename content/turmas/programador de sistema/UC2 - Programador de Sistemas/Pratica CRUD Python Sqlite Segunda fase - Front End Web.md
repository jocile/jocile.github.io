---
description: "Exemplo prático de uma interface web no navegador, utilizando o Bottle."
tags:
  - pratica
  - Python/Bottle
  - sqlite
  - crud
  - didatica
date: 2026-10-15
draft: false
---
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

🌐 Próximos passos: adicionar uma funcionalidade para **editar/atualizar** os dados de um cliente existente diretamente pelo navegador

[[Pratica CRUD Python Sqlite Terceira Fase - adicionando funcionalidade editar]]
