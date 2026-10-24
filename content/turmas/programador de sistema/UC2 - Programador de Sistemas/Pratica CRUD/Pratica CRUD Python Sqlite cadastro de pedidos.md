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

Para avançar no projeto **CRUD Python + SQLite com Bottle**, estruturamos a camada de persistência com um relacionamento relacional completo.

Criaremos a tabela de **Pedidos** relacionando **Clientes** e **Produtos** por meio de **Chaves Estrangeiras (`FOREIGN KEY`)**. Além disso, implementaremos o **congelamento do preço unitário** no momento da venda para preservar a integridade temporal do histórico financeiro e o **cálculo automático do valor total** usando `JOIN` no SQL.

---

### **1. Princípios de Modelação e Chaves Estrangeiras no SQLite**

* **Ativação do PRAGMA**: No SQLite, o suporte a chaves estrangeiras vem desabilitado por padrão. Portanto, ao abrir qualquer conexão com o banco de dados, é obrigatório executar `PRAGMA foreign_keys = ON;` antes de realizar transações.
* **Integridade Histórica de Preço**: O valor de um produto pode mudar com o tempo. Ao realizar um pedido, copiamos o `preco` atual do produto para a coluna `preco_unitario` do pedido, garantindo que alterações futuras no cadastro do produto não alterem retroativamente o valor de vendas passadas.
* **Cálculo Automático**: O valor total de cada item do pedido é calculado dinamicamente no comando SQL `SELECT` através da expressão `(quantidade * preco_unitario)`.

---

### **2. Estrutura do Banco de Dados (DDL)**

As tabelas conectadas via `FOREIGN KEY` com regras de integridade `ON DELETE RESTRICT`:

```sql
-- 1. Ativa a verificação de chaves estrangeiras no SQLite
PRAGMA foreign_keys = ON;

-- 2. Tabela de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 3. Tabela de Produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
);

-- 4. Tabela de Pedidos relacionando Clientes e Produtos
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    preco_unitario REAL NOT NULL CHECK(preco_unitario >= 0.0),
    data_pedido TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
);
```

*(Modelagem relacional e ativamento de chaves estrangeiras).*

---

### **3. Atualização do Layout Base e Novos Templates**

#### **Menu de Navegação (`views/base.tpl`)**

Atualize o menu de navegação no arquivo `views/base.tpl` para incluir o link de Pedidos:

```html
<nav>
    <a href="/">👤 Clientes</a>
    <a href="/produtos">📦 Produtos</a>
    <a href="/pedidos">🛒 Pedidos</a>
</nav>
```

#### **Tela de Pedidos (`views/pedidos.tpl`)**

Crie o arquivo `views/pedidos.tpl` que exibirá seletores dinâmicos `<select>` carregados com os clientes e produtos do banco de dados, além de listar os pedidos já efetuados com o cálculo do valor total:

```html
% rebase('base.tpl', titulo='Gestão de Pedidos')

<h2>Realizar Novo Pedido</h2>

% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end

<form class="card" action="/pedidos/cadastrar" method="post">
    <label>Selecione o Cliente:</label>
    <select name="cliente_id" required style="display:block; width:100%; padding:8px; margin-bottom:10px;">
        <option value="">-- Escolha um Cliente --</option>
        % for c in lista_clientes:
            <option value="{{ c['id'] }}">{{ c['nome'] }} ({{ c['email'] }})</option>
        % end
    </select>

    <label>Selecione o Produto:</label>
    <select name="produto_id" required style="display:block; width:100%; padding:8px; margin-bottom:10px;">
        <option value="">-- Escolha um Produto --</option>
        % for p in lista_produtos:
            <option value="{{ p['id'] }}">{{ p['nome'] }} - R$ {{ "%.2f" % p['preco'] }} (Estoque: {{ p['estoque'] }})</option>
        % end
    </select>

    <label>Quantidade:</label>
    <input type="number" name="quantidade" value="1" min="1" required style="display:block; width:100%; padding:8px; margin-bottom:10px;">

    <input type="submit" value="Finalizar Pedido" style="background: #198754; color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px; font-weight: bold;">
</form>

<hr>

<h2>Histórico de Pedidos</h2>
% if not lista_pedidos:
    <p>Nenhum pedido realizado até o momento.</p>
% else:
    <table>
        <thead>
            <tr>
                <th>Nº Pedido</th>
                <th>Data / Hora</th>
                <th>Cliente</th>
                <th>Produto</th>
                <th>Qtd.</th>
                <th>Preço Unit.</th>
                <th>Valor Total</th>
            </tr>
        </thead>
        <tbody>
            % for ped in lista_pedidos:
            <tr>
                <td>#{{ ped['id'] }}</td>
                <td>{{ ped['data_pedido'] }}</td>
                <td>{{ ped['cliente_nome'] }}</td>
                <td>{{ ped['produto_nome'] }}</td>
                <td>{{ ped['quantidade'] }}</td>
                <td>R$ {{ "%.2f" % ped['preco_unitario'] }}</td>
                <td><strong>R$ {{ "%.2f" % ped['valor_total'] }}</strong></td>
            </tr>
            % end
        </tbody>
    </table>
% end
```

---

### **4. Implementação do Servidor HTTP (`app.py`)**

Abaixo está o código contendo a função de conexão com suporte ao `PRAGMA foreign_keys = ON;`, consulta utilizando `INNER JOIN` para cálculo do valor total (`quantidade * preco_unitario`) e baixa automática no estoque do produto:

```python
import sqlite3
from pathlib import Path
from bottle import get, post, request, redirect, template, run

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")

def get_connection():
    """Abre a conexão com o SQLite, ativa Foreign Keys e ativa Row Factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    # Ativação fundamental para garantir a integridade referencial de chaves estrangeiras
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_banco():
    """Garante que a estrutura das tabelas esteja pronta no banco de dados."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco >= 0.0),
                estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
            );
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL CHECK(quantidade > 0),
                preco_unitario REAL NOT NULL CHECK(preco_unitario >= 0.0),
                data_pedido TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
                FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
            );
        ''')
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Erro na inicialização do banco: {e}")
    finally:
        if conn:
            conn.close()

# ==========================================
# ROTAS DE PEDIDOS (NOVO MÓDULO)
# ==========================================

@get('/pedidos')
def listar_pedidos():
    msg_erro = request.query.get('erro', '')
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Carrega opções para os seletores (<select>) no formulário
    cursor.execute("SELECT id, nome, email FROM clientes ORDER BY nome;")
    clientes = cursor.fetchall()
    
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE estoque > 0 ORDER BY nome;")
    produtos = cursor.fetchall()
    
    # 2. Busca o histórico de pedidos fazendo JOINs e calculando o Valor Total dinamicamente
    query_pedidos = """
        SELECT 
            p.id,
            p.data_pedido,
            c.nome AS cliente_nome,
            prod.nome AS produto_nome,
            p.quantidade,
            p.preco_unitario,
            (p.quantidade * p.preco_unitario) AS valor_total
        FROM pedidos p
        INNER JOIN clientes c ON p.cliente_id = c.id
        INNER JOIN produtos prod ON p.produto_id = prod.id
        ORDER BY p.id DESC;
    """
    cursor.execute(query_pedidos)
    pedidos = cursor.fetchall()
    
    conn.close()
    
    return template(
        'pedidos', 
        lista_clientes=clientes, 
        lista_produtos=produtos, 
        lista_pedidos=pedidos, 
        msg_erro=msg_erro
    )

@post('/pedidos/cadastrar')
def cadastrar_pedido():
    try:
        cliente_id = int(request.forms.get('cliente_id'))
        produto_id = int(request.forms.get('produto_id'))
        quantidade = int(request.forms.get('quantidade', 1))
    except (TypeError, ValueError):
        redirect('/pedidos?erro=Selecione+um+cliente,+produto+e+quantidade+válida.')

    if quantidade <= 0:
        redirect('/pedidos?erro=A+quantidade+deve+ser+maior+que+zero.')

    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        # 1. Consulta o preço atual e verifica o saldo no estoque
        cursor.execute("SELECT preco, estoque FROM produtos WHERE id = ?;", (produto_id,))
        produto = cursor.fetchone()
        
        if not produto:
            redirect('/pedidos?erro=Produto+não+encontrado.')
            
        if produto['estoque'] < quantidade:
            redirect(f"/pedidos?erro=Estoque+insuficiente.+(Disponível:+{produto['estoque']})")
            
        preco_unitario = produto['preco']
        
        # 2. Insere o pedido congelando o preço unitário do produto
        cursor.execute('''
            INSERT INTO pedidos (cliente_id, produto_id, quantidade, preco_unitario)
            VALUES (?, ?, ?, ?);
        ''', (cliente_id, produto_id, quantidade, preco_unitario))
        
        # 3. Baixa automática no estoque do produto
        cursor.execute('''
            UPDATE produtos 
            SET estoque = estoque - ? 
            WHERE id = ?;
        ''', (quantidade, produto_id))
        
        # Confirma a transação atômica completa
        conn.commit()
        redirect('/pedidos')
        
    except sqlite3.IntegrityError as e:
        conn.rollback()
        redirect(f'/pedidos?erro=Falha+de+integridade+referencial:+(FK)+{e}')
    except sqlite3.Error as e:
        conn.rollback()
        redirect(f'/pedidos?erro=Erro+ao+processar+pedido:+{e}')
    finally:
        conn.close()

if __name__ == '__main__':
    inicializar_banco()
    print("Servidor ativo em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **5. Como Funciona a Execução na Prática**

1. Cadastre previamente um **Cliente** na rota `/` e um **Produto** na rota `/produtos`.
2. Navegue até **`http://localhost:8080/pedidos`**:
   * O formulário exibirá os seletores populados a partir do banco de dados.
   * Ao selecionar o cliente, produto e quantidade, a rota `/pedidos/cadastrar` busca o preço atual do produto e verifica se há estoque suficiente.
   * Se o estoque for suficiente, o pedido é gravado com o preço congelado, o estoque do produto é debitado e a transação é confirmada com `commit()`.
   * O histórico de pedidos renderizará a junção `INNER JOIN` trazendo o nome do cliente, nome do produto e a coluna calculada `valor_total`.

---

>[!tip] ⬅️ [[Pratica CRUD Python Sqlite cadastro de produtos]]

>[!important] 📊 Quer ver como gerar um **relatório consolidado de vendas por cliente** usando a cláusula de agregação `GROUP BY` e `SUM()` no SQL?
> [[Pratica CRUD Python Sqlite criando relatorios]]
