---
title: Templates no Bottle
description: "projetado para ser leve, rápido e fácil de aprender, permitindo que você escreva código HTML dinâmico"
tags:
  - Python/Bottle
  - webdesign
  - Template
---
O motor de templates padrão e nativo do Bottle é o **SimpleTemplate** (também conhecido como `stpl`). Ele foi projetado para ser leve, rápido e fácil de aprender, permitindo que você escreva código HTML dinâmico utilizando a sintaxe do próprio Python. Internamente, o Bottle compila esses arquivos em bytecode Python para garantir alta eficiência na renderização.

---

## Como funciona o Template

### **1. Interpolação de Variáveis e Expressões (`{{ ... }}`)**

Para exibir valores e variáveis Python diretamente no meio do HTML, utiliza-se a sintaxe de chaves duplas:

- **Com Escape Automático (Padrão):** `{{ expressao }}`  
    Avalia a expressão Python e converte os caracteres especiais de HTML em entidades seguras (ex: `<` vira `&lt;`), o que **previne ataques de Injeção de Script (XSS)**.

    ```html
    <h1>Bem-vindo, {{ nome }}!</h1>
    <p>Total do pedido: R$ {{ "%.2f" % preco_total }}</p>
    ```

- **Sem Escape (HTML Bruto):** `{{! expressao }}`  
    O ponto de exclamação `!` desativa a proteção de escape, renderizando o HTML exatamente como ele for retornado.

    ```html
    <div>{{! html_confiavel }}</div>
    ```

---

### **2. Estruturas de Controle e Código Python (`%`)**

Você pode inserir estruturas de repetição (`for`), condicionais (`if/elif/else`) e atribuições diretas de variáveis dentro do próprio template:

- **Linhas de Código (`%`):** Qualquer linha iniciada com o caractere `%` na primeira posição é tratada como código Python.
- **Fechamento Explícito (`% end`):** Como a indentação tradicional do Python é ignorada pelo compilador do template, **todos os blocos lógicos (`if`, `for`, `while`) precisam ser encerrados obrigatoriamente com a palavra-chave `% end`**.

```html
<ul>
% for cliente in lista_clientes:
    % if cliente['ativo']:
        <li><strong>{{ cliente['nome'] }}</strong> - {{ cliente['email'] }}</li>
    % else:
        <li style="color: gray;">{{ cliente['nome'] }} (Inativo)</li>
    % end
% end
</ul>
```

---

### **3. Herança e Reutilização de Layouts (`rebase` e `include`)**

O SimpleTemplate oferece funções nativas pré-carregadas para evitar repetição de código no HTML:

- **`rebase()` (Herança/Layout Base):** Permite reutilizar uma estrutura padrão (como um `base.tpl` contendo `<html>`, `<head>` e navegação) O conteúdo do arquivo filho é inserido na variável `{{!base}}` do arquivo pai.

    ```html
    <!-- Arquivo: views/pagina.tpl -->
    % rebase('base.tpl', titulo='Painel do Cliente')
    
    <h2>Conteúdo Principal</h2>
    <p>Aqui entra o corpo da página.</p>
    ```

- **`include()` (Inclusão de Componentes):** Renderiza um sub-template inline em uma posição específica da página (ex: cabeçalhos ou rodapés compartilhados).

    ```html
    % include('header.tpl', usuario=usuario_atual)
    ```

---

### **4. Integração com o Código Python no Bottle**

Para conectar a rota do Bottle ao arquivo de template:

1. Por padrão, o Bottle procura os arquivos de template com extensão **`.tpl`** na pasta **`./views/`** do projeto [cite: 145, 331].
2. Na função manipuladora da rota, utiliza-se a função `template()` passando o nome do template e as variáveis como argumentos nomeados (ou via dicionário) [cite: 41, 277, 331].

```python
from bottle import route, run, template

@route('/clientes')
def listar_clientes():
    dados_clientes = [
        {"nome": "Ana Silva", "email": "ana@email.com", "ativo": True},
        {"nome": "Bruno Souza", "email": "bruno@email.com", "ativo": False}
    ]
    # Carrega o arquivo views/clientes.tpl e injeta a variável lista_clientes
    return template('clientes', lista_clientes=dados_clientes)

if __name__ == '__main__':
    run(host='localhost', port=8080)
```

---

💡 Quer ver um exemplo de como estruturar um **layout base (`base.tpl`)** completo utilizando CSS moderno para aplicar um visual padronizado em todas as telas da sua aplicação?

## Estruturando um layout

Para criar um layout padronizado para todas as telas da sua aplicação Bottle, a prática recomendada é utilizar a técnica de **herança de templates** do motor **SimpleTemplate** através da função `rebase()`.

Dessa forma, o cabeçalho (`<head>`), os estilos CSS, a barra de navegação e o rodapé ficam centralizados em um único arquivo base (ex: `base.tpl`), enquanto as páginas específicas apenas "injetam" seu conteúdo dentro desse layout central através da variável especial `{{!base}}`.

---

### 1. Estrutura de Pastas Recomendada

Por padrão, o Bottle procura os templates com extensão `.tpl` dentro da pasta **`views/`** localizada na raiz do seu projeto.

```txt
meu_projeto/
│
├── app.py
├── meu_banco_de_dados.db
└── views/
    ├── base.tpl       # Layout base compartilhado (CSS, Header, Footer)
    ├── index.tpl      # Tela de listagem e cadastro
    └── editar.tpl     # Tela de edição de cliente
```

---

### **2. Criando o Layout Base (`views/base.tpl`)**

Este arquivo define a casca de todas as páginas da aplicação, contendo o HTML5 principal e uma estilização em CSS moderno. A instrução **`{{!base}}`** renderiza o conteúdo que vier do template filho sem aplicar o escape do HTML:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get('titulo', 'Sistema de Clientes') }}</title>
    <style>
        :root {
            --primary-color: #0d6efd;
            --success-color: #198754;
            --danger-color: #dc3545;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #212529;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
        }

        header {
            background-color: var(--primary-color);
            color: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        header h1 { margin: 0; font-size: 1.5rem; }

        main {
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .alerta {
            background-color: #f8d7da;
            color: #842029;
            border: 1px solid #f5c2c7;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 20px;
        }

        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.85rem;
            color: #6c757d;
        }
    </style>
</head>
<body>

    <header>
        <h1>⚡ Painel de Controle - Gestão de Clientes</h1>
    </header>

    <main>
        <!-- Injeção dinâmica das páginas filhas -->
        {{!base}}
    </main>

    <footer>
        <p>Desenvolvido com Python 3, Bottle e SQLite</p>
    </footer>

</body>
</html>
```

---

### **3. Criando a Tela Principal (`views/index.tpl`)**

No topo do arquivo, adiciona-se a linha **`% rebase('base.tpl', titulo='...')`** para indicar que esta página herdará o layout de `base.tpl`:

```html
% rebase('base.tpl', titulo='Listagem de Clientes')

<h2>Cadastrar Novo Cliente</h2>

% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end

<form action="/cadastrar" method="post" style="margin-bottom: 30px;">
    <div style="margin-bottom: 10px;">
        <label style="display:block;">Nome:</label>
        <input type="text" name="nome" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>

    <div style="margin-bottom: 10px;">
        <label style="display:block;">E-mail:</label>
        <input type="email" name="email" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>

    <input type="submit" value="Salvar Cliente" style="background: var(--success-color); color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px;">
</form>

<hr>

<h2>Clientes Cadastrados</h2>
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background: #e9ecef; text-align: left;">
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">ID</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Nome</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">E-mail</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for id_, nome, email in lista_clientes:
        <tr style="border-bottom: 1px solid #dee2e6;">
            <td style="padding: 10px;">{{ id_ }}</td>
            <td style="padding: 10px;">{{ nome }}</td>
            <td style="padding: 10px;">{{ email }}</td>
            <td style="padding: 10px;">
                <a href="/editar/{{ id_ }}" style="color: var(--primary-color); font-weight: bold; margin-right: 10px; text-decoration: none;">Editar</a>
                <a href="/deletar/{{ id_ }}" style="color: var(--danger-color); font-weight: bold; text-decoration: none;">Excluir</a>
            </td>
        </tr>
        % end
    </tbody>
</table>
```

---

### **4. Criando a Tela de Edição (`views/editar.tpl`)**

Esta tela reutiliza exatamente o mesmo `base.tpl`, garantindo identidade visual em todo o sistema:

```html
% rebase('base.tpl', titulo=f'Editar Cliente #{cliente}')

<h2>Editar Cliente</h2>

<form action="/editar/{{ cliente }}" method="post" style="max-width: 400px;">
    <div style="margin-bottom: 10px;">
        <label style="display:block;">Nome:</label>
        <input type="text" name="nome" value="{{ cliente }}" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>

    <div style="margin-bottom: 10px;">
        <label style="display:block;">E-mail:</label>
        <input type="email" name="email" value="{{ cliente }}" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>

    <input type="submit" value="Atualizar" style="background: var(--primary-color); color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px;">
    <a href="/" style="margin-left: 10px; color: #6c757d; text-decoration: none;">Cancelar</a>
</form>
```

---

### **5. Atualizando as Rotas no Python (`app.py`)**

No script Python, basta retornar a chamada da função `template('nome_do_arquivo')` passando os dados necessários, sem precisar embutir código HTML dentro de strings:

```python
import sqlite3
from bottle import get, post, request, redirect, template, run

DB_NAME = 'meu_banco_de_dados.db'

@get('/')
def index():
    msg_erro = request.query.get('erro', '')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()

    # Chama o arquivo views/index.tpl enviando os parâmetros
    return template('index', lista_clientes=clientes, msg_erro=msg_erro)

@get('/editar/<id:int>')
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        redirect('/?erro=Cliente+não+encontrado')

    # Chama o arquivo views/editar.tpl
    return template('editar', cliente=cliente)

# (Demais rotas de cadastrar, salvar_edicao e deletar mantêm a lógica do banco de dados)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

🎨 Agora vamos separar o estilo, servindo um arquivo CSS externo (`style.css`) estático usando a rota `static_file()` do Bottle.

## Separando o estilo CSS

No Bottle, arquivos estáticos (como CSS, imagens e scripts JavaScript) **não são servidos automaticamente** por motivos de segurança e controle de acesso. Para que o navegador consiga carregar um arquivo como `style.css`, você deve criar uma rota dedicada usando a função helper **`static_file()`**.

O `static_file()` também inclui proteção nativa contra ataques de navegação de diretório (_path traversal_), garantindo que o usuário só consiga acessar arquivos que estejam explicitamente dentro da pasta autorizada.

---

### **1. Estrutura do Projeto**

Crie uma pasta chamada **`static/`** na raiz do seu projeto para armazenar o CSS e outros arquivos públicos:

```plaintext
meu_projeto/
│
├── app.py
├── meu_banco_de_dados.db
├── static/
│   └── style.css       # Seu arquivo CSS externo
└── views/
    ├── base.tpl
    └── index.tpl
```

---

### **2. Configurando a Rota no Python (`app.py`)**

Importe a função `static_file` do Bottle e crie uma rota dinâmica com o filtro **`<filepath:path>`**. O filtro `:path` permite que a rota aceite subdiretórios e barras no caminho do arquivo.

```python
from bottle import get, static_file, template, run

DB_NAME = 'meu_banco_de_dados.db'

# ROTA PARA SERVIR ARQUIVOS ESTÁTICOS (CSS, Imagens, JS)
@get('/static/<filepath:path>')
def servir_estatico(filepath):
    # O parâmetro root define a pasta raiz autorizada onde o Bottle buscará os arquivos
    return static_file(filepath, root='./static')

@get('/')
def index():
    return template('index', lista_clientes=[])

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
```

_(Uso do filtro `:path` e da função `static_file` com a raiz configurada)._

---

### **3. Criando o Arquivo CSS (`static/style.css`)**

Coloque todas as suas regras de estilo dentro do arquivo `static/style.css`:

```css
/* static/style.css */
body {
    font-family: 'Segoe UI', Arial, sans-serif;
    background-color: #f4f6f9;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: #ffffff;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #007bff;
}

.btn-salvar {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
```

---

### **4. Vinculando o CSS nos Templates HTML (`base.tpl`)**

No elemento `<head>` do seu arquivo de layout ou template, inclua a tag `<link>` apontando para a rota `/static/style.css`:

```html
<!-- views/base.tpl -->
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ get('titulo', 'Sistema de Clientes') }}</title>
    <!-- Vincula o arquivo CSS externo através da rota estática -->
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        {{!base}}
    </div>
</body>
</html>
```

---

### **💡 Boas Práticas e Recursos Adicionais**

1. **Subpastas organizadas**: Como utilizou-se o filtro `<filepath:path>`, você pode organizar arquivos estáticos em subpastas como `static/css/style.css` ou `static/js/app.js` sem precisar alterar a rota Python.
2. **Download Forçado**: Se em alguma rota você precisar que o arquivo seja baixado diretamente em vez de exibido no navegador, pode passar o parâmetro `download=True` para o `static_file()`:

    ```python
    return static_file('relatorio.pdf', root='./docs', download=True)
    ```

## Adicionando um filtro search

Para implementar um **filtro de pesquisa (Search)** dinâmico na aplicação Bottle com SQLite, combina-se a captura de parâmetros da requisição HTTP no Bottle com o operador `LIKE` e marcadores de posição do SQL.

---

### **Como Funciona a Lógica de Pesquisa**

1. **Parâmetros GET no Bottle**: Quando um formulário de busca é enviado usando o método `GET`, os valores pesquisados são anexados à URL como parâmetros de busca (por exemplo: `/?q=Ana`). No script Python, esse valor é capturado utilizando `request.query.get('q')`.
2. **Operador SQL `LIKE` e Coringas (`%`)**: O operador `LIKE` realiza correspondências parciais em colunas de texto. O símbolo `%` funciona como um caractere coringa que representa zero, um ou múltiplos caracteres. Ao utilizar a estrutura `%termo%`, a consulta localiza o texto em qualquer posição do campo.
3. **Prevenção de SQL Injection**: Para manter a aplicação segura contra injeções de código SQL, a string contendo os coringas `f"%{busca}%"` é repassada como argumento dentro de uma tupla utilizando o marcador de posição `?` no método `execute()`.

---

### **1. Atualização do Template (`views/index.tpl`)**

Adiciona-se um formulário de pesquisa acima da tabela de clientes com um campo de texto (`name="q"`) e o botão para filtrar:

```html
% rebase('base.tpl', titulo='Listagem de Clientes')

<h2>Buscar Clientes</h2>

<!-- Formulário de busca via GET -->
<form action="/" method="get" style="display: flex; gap: 10px; margin-bottom: 25px;">
    <input type="text" name="q" value="{{ get('termo_busca', '') }}" placeholder="Digite o nome ou e-mail..." style="flex: 1; padding: 8px;">
    <input type="submit" value="Pesquisar" style="background: var(--primary-color); color: white; border: none; padding: 8px 15px; cursor: pointer; border-radius: 4px;">
    % if get('termo_busca', ''):
        <a href="/" style="padding: 8px 12px; background: #6c757d; color: white; text-decoration: none; border-radius: 4px;">Limpar</a>
    % end
</form>

<h2>Clientes Cadastrados</h2>

% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end

<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background: #e9ecef; text-align: left;">
            <th style="padding: 10px;">ID</th>
            <th style="padding: 10px;">Nome</th>
            <th style="padding: 10px;">E-mail</th>
            <th style="padding: 10px;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for id_, nome, email in lista_clientes:
        <tr style="border-bottom: 1px solid #dee2e6;">
            <td style="padding: 10px;">{{ id_ }}</td>
            <td style="padding: 10px;">{{ nome }}</td>
            <td style="padding: 10px;">{{ email }}</td>
            <td style="padding: 10px;">
                <a href="/editar/{{ id_ }}" style="color: var(--primary-color); font-weight: bold; margin-right: 10px; text-decoration: none;">Editar</a>
                <a href="/deletar/{{ id_ }}" style="color: var(--danger-color); font-weight: bold; text-decoration: none;">Excluir</a>
            </td>
        </tr>
        % end
    </tbody>
</table>
```

---

### **2. Atualização da Rota no Python (`app.py`)**

A rota principal `GET /` captura o parâmetro de busca `q` enviado na URL. Se houver algum termo preenchido, a instrução SQL é montada filtrando por `nome` ou `email` com o comando `LIKE`. Caso contrário, executa o `SELECT` padrão para listar todos os registros.

```python
import sqlite3
from bottle import get, post, request, redirect, template, run

DB_NAME = 'meu_banco_de_dados.db'

@get('/')
def index():
    # 1. Captura o termo de busca enviado via parâmetro GET na URL (?q=termo)
    termo_busca = request.query.get('q', '').strip()
    msg_erro = request.query.get('erro', '')
    clientes = []

    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        if termo_busca:
            # 2. Executa a consulta filtrando por nome ou e-mail usando LIKE e marcadores seguros (?)
            query = """
                SELECT id, nome, email
                FROM clientes
                WHERE nome LIKE ? OR email LIKE ?;
            """
            padrao = f"%{termo_busca}%"
            cursor.execute(query, (padrao, padrao))
        else:
            # 3. Executa a busca geral sem filtros
            cursor.execute("SELECT id, nome, email FROM clientes;")

        clientes = cursor.fetchall()
    except sqlite3.Error as e:
        msg_erro = f"Erro na consulta: {e}"
    finally:
        if conn:
            conn.close()

    # Passa o termo de busca de volta ao template para mantê-lo preenchido no campo de texto
    return template('index', lista_clientes=clientes, termo_busca=termo_busca, msg_erro=msg_erro)
```

---

### **Resumo do Fluxo**

- Ao digitar **"Silva"** e clicar em **Pesquisar**, a URL se altera para `/?q=Silva`.
- O Python processa a busca com `WHERE nome LIKE '%Silva%' OR email LIKE '%Silva%'` e retorna somente os registros correspondentes.
- O botão **Limpar** direciona para a raiz `/`, redefinindo a lista e exibindo todos os clientes novamente.

---

📊 Sugestão para próximos passos: adicionar uma funcionalidade de **paginação** (utilizando as cláusulas `LIMIT` e `OFFSET` do SQLite) para dividir a listagem quando o banco de dados tiver muitos registros.

## Referências

- [Bottle SimpleTemplate](https://bottlepy.org/docs/dev/stpl.htm)
