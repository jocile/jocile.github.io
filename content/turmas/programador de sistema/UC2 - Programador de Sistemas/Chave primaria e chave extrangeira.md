---
description: "relacionar tabelas em um banco de dados relacional"
tags:
  - banco-de-dados
  - Python/bd
---

## Relacionando tabelas

Para relacionar tabelas em um banco de dados relacional, utiliza-se a combinação de **Chave Primária (`PRIMARY KEY`)** e **Chave Estrangeira (`FOREIGN KEY`)**:

---

### **1. Conceitos Fundamentais**

* **Chave Primária (`PRIMARY KEY`)**: É uma coluna (ou conjunto de colunas) que identifica de maneira única cada registro em uma tabela. Ela não aceita valores duplicados.
* **Chave Estrangeira (`FOREIGN KEY`)**: É um campo em uma tabela que faz referência direta à Chave Primária de outra tabela (ou da mesma tabela em um auto-relacionamento). É ela quem garante a **integridade referencial**, impedindo a criação de registros "órfãos" que apontem para dados inexistentes na tabela pai.

---

### **2. Sintaxe de Criação em SQL (DDL)**

Ao criar as tabelas com o comando `CREATE TABLE`, define-se a chave primária na tabela pai e, em seguida, declara-se a chave estrangeira na tabela filho indicando qual coluna e tabela ela referencia:

```sql
-- 1. Tabela Pai (Contém a Chave Primária)
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 2. Tabela Filho (Contém a Chave Estrangeira)
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data_pedido TEXT DEFAULT (datetime('now', 'localtime')),
    -- Definição da Chave Estrangeira:
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT ON UPDATE CASCADE
);
```

*(Exemplo de criação estrutural de tabelas relacionadas).*

#### **Regras da Chave Estrangeira:**

* **`REFERENCES clientes(id)`**: Estabelece que a coluna `cliente_id` da tabela `pedidos` aponta diretamente para a coluna `id` da tabela `clientes`.
* **`ON DELETE RESTRICT`**: Impede que um cliente seja excluído caso existam pedidos vinculados a ele.
* **`ON UPDATE CASCADE`**: Se o `id` do cliente for alterado, o valor atualiza automaticamente na tabela de pedidos.

---

### **3. Regra Específica do SQLite**

Por padrão, a verificação de integridade de Chaves Estrangeiras vem desabilitada em conexões SQLite. Para garantir que o banco de dados bloqueie inserções inválidas, deve-se emitir obrigatoriamente o seguinte comando ao abrir a conexão:

```sql
PRAGMA foreign_keys = ON;
```

*(Ativação do controle de integridade referencial no SQLite).*

No Python, você pode executá-lo logo após conectar:

```python
import sqlite3

conn = sqlite3.connect('meu_banco.db')
conn.execute("PRAGMA foreign_keys = ON;")  # Ativa o controle de FK
```

---

### **4. Consultando Dados Relacionados (DQL / `JOIN`)**

Para reunir e visualizar os dados espalhados entre as tabelas relacionadas, utiliza-se a cláusula `JOIN` combinando a Chave Estrangeira da tabela filho com a Chave Primária da tabela pai:

```sql
SELECT 
    clientes.nome AS cliente,
    pedidos.id AS num_pedido,
    pedidos.data_pedido
FROM pedidos
INNER JOIN clientes ON pedidos.cliente_id = clientes.id;
```

*(Consulta de dados cruzados via `INNER JOIN`).*

---

💡 Gostaria de ver como mapear e criar a tabela associativa para relacionamentos **Muitos-para-Muitos (\\(N:M\\))**, como no caso de um pedido contendo múltiplos produtos?

## Tabela associativa para relacionamentos

Em modelagem relacional, um relacionamento **Muitos-para-Muitos (\\(N:M\\))** ocorre quando uma entidade pode estar associada a múltiplos registros de outra entidade e vice-versa [cite: 87, 235]. No caso de vendas:

* Um **Pedido** pode conter **múltiplos Produtos** [cite: 87, 235].
* Um **Produto** pode estar presente em **múltiplos Pedidos** [cite: 87, 235].

Como os bancos de dados relacionais exigem valores atômicos e não permitem armazenar listas ou arrays diretamente em uma única coluna (conforme as regras da Primeira e Segunda Formas Normais - 1FN e 2FN) [cite: 87, 89], é necessário criar uma **Tabela Associativa** (também conhecida como tabela de junção ou *junction table*) [cite: 87].

---

### **1. Como Funciona a Tabela Associativa**

A tabela associativa (frequentemente chamada de `itens_pedido` ou `pedido_produtos`) decompõe a relação \\(N:M\\) em dois relacionamentos \\(1:N\\) encadeados [cite: 87]:

1. **Chave Primária Composta**: A chave primária da tabela associativa é formada pela junção das duas chaves estrangeiras advindas das tabelas principais (`pedido_id` e `produto_id`) [cite: 87, 88].
2. **Atributos Próprios do Relacionamento**: Além das chaves, a tabela associativa armazena dados específicos daquela interseção, como a **quantidade** comprada e o **preço unitário congelado** no ato da compra (o que garante a integridade temporal do histórico financeiro caso o preço do produto mude no futuro) [cite: 6, 88].

---

### **2. Scripts SQL de Definição (DDL)**

Abaixo está o script completo para criar as tabelas `pedidos`, `produtos` e a tabela associativa `itens_pedido` no SQLite [cite: 92]:

```sql
-- 1. Ativação do controle de integridade referencial no SQLite
PRAGMA foreign_keys = ON;

-- 2. Tabela de Pedidos (Tabela Pai 1)
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data_pedido TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    status TEXT NOT NULL DEFAULT 'Pendente' CHECK(status IN ('Pendente', 'Pago', 'Cancelado')),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 3. Tabela de Produtos (Tabela Pai 2)
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
);

-- 4. Tabela Associativa com Chave Primária Composta (Itens do Pedido)
CREATE TABLE IF NOT EXISTS itens_pedido (
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    preco_unitario REAL NOT NULL CHECK(preco_unitario >= 0.0),
    -- Define a Chave Primária Composta por duas colunas
    PRIMARY KEY (pedido_id, produto_id),
    -- Garante que se um pedido for excluído, seus itens também serão removidos (CASCADE)
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE ON UPDATE CASCADE,
    -- Impede a exclusão de um produto que já esteja associado a um pedido histórico (RESTRICT)
    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT ON UPDATE CASCADE
);
```

*(Modelagem e restrições DDL da tabela associativa baseadas nos materiais) [cite: 88, 92].*

---

### **3. Inserindo e Consultando Dados (DML e DQL)**

#### **a) Inserindo um Pedido com Múltiplos Produtos**

Quando um cliente realiza uma compra contendo mais de um item, gera-se um registro na tabela `pedidos` e múltiplos registros na tabela associativa `itens_pedido` [cite: 93]:

```sql
-- 1. Registra o Pedido para o cliente ID 1
INSERT INTO pedidos (cliente_id, status) VALUES (1, 'Pendente');

-- 2. Insere múltiplos produtos no mesmo pedido (Pedido ID = 1)
-- Produto 101 (Notebook): 1 unidade a R$ 4500.00
-- Produto 202 (Mouse): 2 unidades a R$ 120.00 cada
INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES 
    (1, 101, 1, 4500.00),
    (1, 202, 2, 120.00);
```

*(Exemplo de inserção de itens com preço congelado) [cite: 93].*

#### **b) Consultando o Pedido Completo com `INNER JOIN`**

Para cruzar as três tabelas e obter a lista detalhada do pedido, realiza-se um encadeamento de `INNER JOIN` entre `pedidos`, `itens_pedido` e `produtos` [cite: 8, 93]:

```sql
SELECT 
    p.id AS num_pedido,
    p.data_pedido,
    prod.nome AS nome_produto,
    ip.quantidade,
    ip.preco_unitario,
    (ip.quantidade * ip.preco_unitario) AS subtotal
FROM pedidos p
INNER JOIN itens_pedido ip ON p.id = ip.pedido_id
INNER JOIN produtos prod ON ip.produto_id = prod.id
WHERE p.id = 1;
```

*(Consulta de junção tripla baseada nos materiais) [cite: 8, 93].*

---

### **4. Exemplo Prático em Python com SQLite**

Abaixo está o código em Python demonstrando a criação da estrutura e a gravação atômica de um pedido com múltiplos itens dentro de uma transação gerenciada [cite: 93, 98]:

```python
import sqlite3

def criar_pedido_com_itens(caminho_db, cliente_id, itens_compra):
    """
    Cadastra um pedido e insere múltiplos produtos na tabela associativa.
    itens_compra é uma lista de tuplas: [(produto_id, quantidade, preco_unitario), ...]
    """
    conn = sqlite3.connect(caminho_db)
    conn.execute("PRAGMA foreign_keys = ON;")  # Ativa Foreign Keys no SQLite
    cursor = conn.cursor()
    
    try:
        # Abertura explícita de transação
        cursor.execute("BEGIN IMMEDIATE;")
        
        # 1. Cria a ordem de compra na tabela pedidos
        cursor.execute("INSERT INTO pedidos (cliente_id, status) VALUES (?, 'Pendente');", (cliente_id,))
        pedido_id = cursor.lastrowid  # Captura o ID do pedido recém-criado
        
        # 2. Prepara a lista de itens vinculando ao pedido_id
        dados_itens = [
            (pedido_id, prod_id, qtd, preco) 
            for prod_id, qtd, preco in itens_compra
        ]
        
        # 3. Insere todos os produtos associados em lote na tabela itens_pedido
        cursor.executemany('''
            INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario)
            VALUES (?, ?, ?, ?);
        ''', dados_itens)
        
        # 4. Confirma todas as operações de forma atômica
        conn.commit()
        print(f"Pedido #{pedido_id} criado com {len(itens_compra)} item(ns) associado(s)!")
        
    except sqlite3.Error as e:
        conn.rollback()  # Cancela o pedido se houver falha em algum item
        print(f"Erro ao registrar o pedido: {e}")
    finally:
        conn.close()

# Exemplo de Uso:
# Cliente 1 comprando o Produto ID 1 (1 un. a R$ 1500) e o Produto ID 2 (3 un. a R$ 50)
itens = [
    (1, 1, 1500.00),
    (2, 3, 50.00)
]
criar_pedido_com_itens('meu_banco_de_dados.db', cliente_id=1, itens_compra=itens)
```

*(Gravação atômica transacional em Python baseada nos materiais) [cite: 93, 98].*

---

💡 Quer ver como adaptar o formulário do **Bottle** no navegador para permitir que o usuário adicione dinamicamente múltiplos produtos ao mesmo pedido antes de enviar?

## Exemplo prático

Para permitir que o usuário adicione dinamicamente **múltiplos produtos** a um mesmo pedido diretamente no navegador, combina-se o seguinte fluxo [cite: 1, 93]:

1. **Frontend (HTML + JavaScript)**: Um botão de "+ Adicionar Produto" duplica os campos de seleção (`<select name="produto_id">`) e quantidade (`<input name="quantidade">`) dinamicamente no DOM.
2. **Recebimento no Bottle (`request.forms.getall`)**: Quando o formulário envia múltiplos campos com o mesmo atributo `name`, o Bottle captura todas as entradas como listas através do método `request.forms.getall('nome_do_campo')` [cite: 261].
3. **Persistência Atômica no SQLite**: O servidor insere a ordem de compra principal na tabela `pedidos`, recupera o ID recém-gerado com `cursor.lastrowid` [cite: 86] e grava todos os itens em lote na tabela associativa `itens_pedido` com `cursor.executemany()` dentro de uma transação protegida por `commit()` e `rollback()` [cite: 37, 72, 81].

---

### **Passo 1: Formulário Dinâmico HTML + JavaScript (`views/novo_pedido.tpl`)**

No template de criação do pedido, utiliza-se JavaScript para adicionar ou remover linhas de produtos antes do envio:

```html
% rebase('base.tpl', titulo='Novo Pedido Multi-Itens')

<h2>🛒 Criar Novo Pedido</h2>

% if get('msg_erro', ''):
    <div class="alerta" style="background: #f8d7da; color: #721c24; padding: 10px; margin-bottom: 15px;">
        ⚠️ {{ msg_erro }}
    </div>
% end

<form action="/pedidos/cadastrar-multiplo" method="post" class="card">
    <div style="margin-bottom: 20px;">
        <label><strong>Cliente:</strong></label>
        <select name="cliente_id" required style="width: 100%; padding: 8px;">
            <option value="">-- Selecione o Cliente --</option>
            % for c in lista_clientes:
                <option value="{{ c['id'] }}">{{ c['nome'] }} ({{ c['email'] }})</option>
            % end
        </select>
    </div>

    <h3>Itens do Pedido</h3>
    <!-- Container onde as linhas de produtos serão adicionadas dinamicamente -->
    <div id="itens-container">
        <div class="item-linha" style="display: flex; gap: 10px; margin-bottom: 10px; align-items: center;">
            <select name="produto_id" required style="flex: 2; padding: 8px;">
                <option value="">-- Selecione o Produto --</option>
                % for p in lista_produtos:
                    <option value="{{ p['id'] }}">{{ p['nome'] }} - R$ {{ "%.2f" % p['preco'] }} (Estoque: {{ p['estoque'] }})</option>
                % end
            </select>

            <input type="number" name="quantidade" value="1" min="1" required placeholder="Qtd" style="flex: 1; padding: 8px;">

            <button type="button" onclick="removerLinha(this)" style="background: #dc3545; color: white; border: none; padding: 8px 12px; cursor: pointer; border-radius: 4px;">X</button>
        </div>
    </div>

    <button type="button" onclick="adicionarLinha()" style="background: #0d6efd; color: white; border: none; padding: 8px 15px; cursor: pointer; border-radius: 4px; margin-bottom: 20px;">
        ➕ Adicionar Outro Produto
    </button>

    <br>
    <input type="submit" value="Finalizar Pedido Completo" style="background: #198754; color: white; border: none; padding: 12px 20px; font-weight: bold; cursor: pointer; border-radius: 4px;">
</form>

<!-- Script JS para manipulação do DOM -->
<script>
function adicionarLinha() {
    const container = document.getElementById('itens-container');
    const primeiraLinha = container.querySelector('.item-linha');
    
    # Clona a primeira linha de produtos
    const novaLinha = primeiraLinha.cloneNode(true);
    
    # Reseta os valores selecionados
    novaLinha.querySelector('select').value = '';
    novaLinha.querySelector('input[type="number"]').value = '1';
    
    container.appendChild(novaLinha);
}

function removerLinha(botao) {
    const container = document.getElementById('itens-container');
    # Mantém ao menos uma linha visível
    if (container.querySelectorAll('.item-linha').length > 1) {
        botao.closest('.item-linha').remove();
    } else {
        alert('O pedido deve conter pelo menos um produto!');
    }
}
</script>
```

---

### **Passo 2: Processamento no Python (`app.py`)**

No backend Python, resgatam-se as listas de produtos e quantidades enviadas usando `request.forms.getall()`. Toda a gravação é executada dentro de um bloco transacional atômico [cite: 37, 261]:

```python
import sqlite3
from pathlib import Path
from bottle import get, post, request, redirect, template, run

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")  # Garante integridade das FKs [cite: 98]
    return conn

@post('/pedidos/cadastrar-multiplo')
def cadastrar_pedido_multiplo():
    cliente_id = request.forms.get('cliente_id')
    
    # Captura todas as ocorrências repetidas dos inputs 'produto_id' e 'quantidade' [cite: 261]
    produtos_ids = request.forms.getall('produto_id')
    quantidades = request.forms.getall('quantidade')

    if not cliente_id or not produtos_ids or not quantidades:
        redirect('/pedidos?erro=Selecione+um+cliente+e+pelo+menos+um+produto.')

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Abertura explícita de transação [cite: 10, 102]
        cursor.execute("BEGIN IMMEDIATE;")

        # 1. Cria a ordem de compra principal na tabela 'pedidos' [cite: 99]
        cursor.execute(
            "INSERT INTO pedidos (cliente_id, status) VALUES (?, 'Pendente');", 
            (cliente_id,)
        )
        # Recupera o ID gerado para o pedido [cite: 86]
        pedido_id = cursor.lastrowid

        itens_para_inserir = []

        # 2. Processa e valida cada produto selecionado
        for prod_id_str, qtd_str in zip(produtos_ids, quantidades):
            if not prod_id_str:
                continue
                
            prod_id = int(prod_id_str)
            qtd = int(qtd_str)

            # Consulta o preço atual e verifica o saldo no estoque [cite: 99]
            cursor.execute("SELECT preco, estoque FROM produtos WHERE id = ?;", (prod_id,))
            produto = cursor.fetchone()

            if not produto:
                raise ValueError(f"Produto ID {prod_id} não encontrado.")

            if produto['estoque'] < qtd:
                raise ValueError(f"Estoque insuficiente para o produto ID {prod_id}. Disponível: {produto['estoque']}")

            # Congela o preço unitário do momento da venda [cite: 5, 96, 99]
            preco_unitario = produto['preco']
            
            # Prepara a tupla para o executemany [cite: 81, 99]
            itens_para_inserir.append((pedido_id, prod_id, qtd, preco_unitario))

            # Atualiza e dá baixa no estoque do produto [cite: 6, 99]
            cursor.execute(
                "UPDATE produtos SET estoque = estoque - ? WHERE id = ?;", 
                (qtd, prod_id)
            )

        if not itens_para_inserir:
            raise ValueError("Nenhum produto válido foi selecionado.")

        # 3. Insere todos os itens em lote na tabela associativa [cite: 81, 96, 99]
        cursor.executemany('''
            INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario)
            VALUES (?, ?, ?, ?);
        ''', itens_para_inserir)

        # Confirma a transação inteira no banco de dados [cite: 37, 71]
        conn.commit()
        redirect('/pedidos')

    except (ValueError, sqlite3.Error) as e:
        # Em caso de qualquer erro ou falha de estoque, reverte tudo [cite: 37, 72]
        conn.rollback()
        redirect(f'/pedidos?erro={str(e)}')
    finally:
        conn.close()
```

---

### **Por que essa Abordagem é Segura?**

1. **Atomicidade Garantida**: Se o estoque de apenas um dos 5 produtos selecionados for insuficiente, a chamada de `conn.rollback()` cancela **todo o pedido**, impedindo a gravação de um pedido incompleto ou órfão.
2. **Preço Histórico Inalterável**: O preço unitário de cada item é gravado na tabela `itens_pedido` no momento do processamento.
3. **Escalonamento em Lote (`executemany`)**: A inserção dos itens em lote garante melhor desempenho ao enviar todas as tuplas em uma única instrução SQL para o banco.

---

>[!tip] ⬅️ [[Pratica CRUD Python Sqlite criando relatorios]]
