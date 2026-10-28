---
title: Gestão de Produtos e Categorias
draft: true
description: "Exemplo prático de manipulação de tabelas CSV com Python e Pandas."
tags:
  - banco-de-dados
  - Python/bd
  - Pandas
---

Esta é uma **atividade prática guiada em Python e SQLite**, projetada para ensinar o ciclo completo do **CRUD** (Create, Read, Update, Delete) e integrar técnicas de **análise de dados** com SQL e Pandas. 

>[!note] Use o [Google Colab](https://colab.research.google.com/) como editor.

## Atividade guiada

---

### 🎯 **Objetivo da Atividade**

Desenvolver um script em Python que cria um banco de dados relacional de **Gestão de Produtos e Categorias**, executa todas as operações de escrita e manipulação de dados de forma segura e responde a perguntas de análise sobre o estoque.

---

### 📋 **Pré-requisitos**

- Python 3 instalado (o módulo `sqlite3` já faz parte da biblioteca padrão).
- Biblioteca Pandas instalada para a etapa de análise (`pip install pandas`).

---

### 🚀 **Passo a Passo da Atividade**

#### **Passo 1: Conexão e Inicialização do Banco de Dados**

Importe as bibliotecas necessárias e estabeleça a conexão com o arquivo do banco `.db`. Se o arquivo não existir, o SQLite criará a base automaticamente.

```python
import sqlite3
import pandas as pd

# 1. Abre a conexão com o banco de dados local
conn = sqlite3.connect('gestao_produtos.db')

# 2. Cria o cursor para enviar comandos SQL
cursor = conn.cursor()

print("Conexão estabelecida com sucesso!")
```

---

#### **Passo 2: Criar as Tabelas (DDL - Data Definition Language)**

Defina a estrutura relacional com duas tabelas (`Categoria` e `Produto`) utilizando restrições de **Chave Primária**, **Chave Estrangeira** e validações `CHECK`.

```python
# Ativa a verificação de chaves estrangeiras no SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Criação das estruturas das tabelas
cursor.executescript('''
CREATE TABLE IF NOT EXISTS Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL CHECK(estoque >= 0),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);
''')

conn.commit()
print("Tabelas 'Categoria' e 'Produto' criadas com sucesso!")
```

---

#### **Passo 3: Inserir Registros (DML - Create)**

Para evitar riscos como **SQL Injection**, insira os dados em lote utilizando **marcadores de posição (`?`)** com `cursor.executemany()`.

```python
# 1. Dados fictícios para categorias
categorias = [
    ('Eletrônicos',),
    ('Móveis',),
    ('Vestuário',)
]

# 2. Dados fictícios para produtos (nome, preço, estoque, id_categoria)
produtos = [
    ('Smartphone', 1500.00, 10, 1),
    ('Notebook', 3500.00, 5, 1),
    ('Sofá', 800.00, 3, 2),
    ('Cadeira de Escritório', 350.00, 12, 2),
    ('Camisa Polo', 80.00, 25, 3),
    ('Calça Jeans', 120.00, 15, 3)
]

cursor.executemany("INSERT INTO Categoria (nome_categoria) VALUES (?);", categorias)
cursor.executemany("INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);", produtos)

conn.commit()
print(f"Registros inseridos com sucesso!")
```

---

#### **Passo 4: Consultar os Dados (DQL - Read)**

Execute o comando `SELECT` para recuperar e exibir as linhas cadastradas utilizando o método `fetchall()`.

```python
cursor.execute("SELECT id_produto, nome, preco, estoque FROM Produto;")
produtos = cursor.fetchall()

print("\n--- Lista de Produtos Cadastrados ---")
for id_p, nome, preco, estoque in produtos:
    print(f"ID: {id_p} | Produto: {nome} | Preço: R$ {preco:.2f} | Estoque: {estoque}")
```

---

#### **Passo 5: Atualizar e Excluir Registros (Update / Delete)**

Realize edições e remoções pontuais utilizando os comandos `UPDATE` e `DELETE` combinados com a cláusula `WHERE`.

```python
# 1. Atualizar o preço de um produto específico
cursor.execute("UPDATE Produto SET preco = ? WHERE nome = ?;", (1600.00, 'Smartphone'))

# 2. Deletar um produto específico do banco
cursor.execute("DELETE FROM Produto WHERE nome = ?;", ('Calça Jeans',))

conn.commit()
print("\nAlterações de atualização e exclusão aplicadas!")
```

---

#### **Passo 6: Análise de Dados e Relatórios**

Nesta etapa, aplique consultas para **responder a perguntas estratégicas** de análise de dados cruzando tabelas com `JOIN` e agregações.

##### **Pergunta 1 (Via SQL Agregado): Qual é o valor total investido em estoque por categoria?**

```python
query_estoque_categoria = """
SELECT 
    c.nome_categoria,
    COUNT(p.id_produto) AS total_produtos,
    SUM(p.preco * p.estoque) AS valor_total_estoque
FROM Categoria c
JOIN Produto p ON c.id_categoria = p.id_categoria
GROUP BY c.nome_categoria
ORDER BY valor_total_estoque DESC;
"""

cursor.execute(query_estoque_categoria)
print("\n--- Valor Total de Estoque por Categoria ---")
for cat, qtd, valor in cursor.fetchall():
    print(f"Categoria: {cat} | Variedade: {qtd} item(ns) | Valor em Estoque: R$ {valor:.2f}")
```

##### **Pergunta 2 (Via Pandas): Qual é o resumo estatístico geral e a média de preços dos produtos?**

Carregue a consulta direta em um DataFrame do Pandas com `pd.read_sql_query()`:

```python
# Carrega os dados unificados no Pandas
df_produtos = pd.read_sql_query("""
    SELECT p.nome, p.preco, p.estoque, c.nome_categoria 
    FROM Produto p 
    JOIN Categoria c ON p.id_categoria = c.id_categoria
""", conn)

print("\n--- Visão Geral do DataFrame Pandas ---")
print(df_produtos.head())

print("\n--- Resumo Estatístico dos Preços e Estoques ---")
print(df_produtos.describe())
```

---

#### **Passo 7: Fechamento Seguro da Conexão**

Finalize a prática garantindo que o cursor e a conexão sejam devidamente encerrados para liberar os recursos do sistema.

```python
cursor.close()
conn.close()
print("\nConexão com o banco de dados encerrada com segurança.")
```

---

## Adicionando tabela de vendas

💡 **Sugestão de Desafio:** Tente adicionar uma tabela de `Vendas` que registre a data da transação e a quantidade vendida, e em seguida descubra qual é o produto mais vendido do sistema.

Aqui está a solução completa do **Desafio de Vendas e Estoque**.

Nesta solução, adicionamos a tabela `Vendas` com chave estrangeira apontando para a tabela `Produto`, registramos transações simulando a baixa no estoque e executamos a consulta de agregação (`SUM`, `GROUP BY`, `ORDER BY`, `LIMIT`) via SQL e Pandas para identificar o **produto campeão de vendas** [cite: 2, 10, 231, 239, 244].

---

### 1. Atualização do Esquema (DDL - Criando a Tabela `Vendas`)

A tabela `Vendas` conecta cada venda a um produto cadastrado através de uma **Chave Estrangeira (`FOREIGN KEY`)** [cite: 2, 10].

```python
import sqlite3
import pandas as pd

# Conexão com o banco de dados
conn = sqlite3.connect('gestao_produtos.db')
cursor = conn.cursor()

# Ativação obrigatória de Foreign Keys no SQLite
cursor.execute("PRAGMA foreign_keys = ON;")

# Criação da tabela Vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
    data_venda TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);
''')

conn.commit()
print("Tabela 'Vendas' criada com sucesso!")
```

---

### 2. Registrar Vendas e Dar Baixa no Estoque (DML + Transação)

Para garantir a integridade dos dados, inserimos os registros de venda e atualizamos o saldo da coluna `estoque` na tabela `Produto` [cite: 2, 14]:

```python
# Dados de teste para registrar vendas: (id_produto, quantidade_vendida)
novas_vendas = [
    (1, 3),  # 3 Smartphones vendidos
    (2, 2),  # 2 Notebooks vendidos
    (1, 4),  # Mais 4 Smartphones vendidos (Total = 7)
    (3, 1),  # 1 Sofá vendido
    (4, 5),  # 5 Cadeiras de Escritório vendidas
    (5, 10)  # 10 Camisas Polo vendidas
]

try:
    # Registrar as vendas na tabela
    cursor.executemany(
        "INSERT INTO Vendas (id_produto, quantidade) VALUES (?, ?);", 
        novas_vendas
    )

    # Dar baixa automática no estoque de cada produto vendido
    for id_p, qtd in novas_vendas:
        cursor.execute(
            "UPDATE Produto SET estoque = estoque - ? WHERE id_produto = ?;", 
            (qtd, id_p)
        )

    # Confirmação atômica da transação
    conn.commit()
    print("Vendas registradas e estoque atualizado com sucesso!")
except sqlite3.Error as e:
    conn.rollback()
    print(f"Erro ao processar vendas: {e}")
```

---

### 3. Consulta SQL: Descobrindo o Produto Mais Vendido (DQL)

Para encontrar o produto mais vendido, usamos um **`INNER JOIN`** para unir as tabelas `Produto` e `Vendas`, aplicamos a agregação **`SUM(v.quantidade)`**, agrupamos por produto (`GROUP BY`) e ordenamos de forma decrescente (`ORDER BY ... DESC`), limitando ao primeiro resultado (`LIMIT 1`) [cite: 2, 10, 120, 239, 244]:

```python
query_campeao = """
SELECT 
    p.id_produto,
    p.nome AS produto,
    c.nome_categoria AS categoria,
    SUM(v.quantidade) AS total_unidades_vendidas,
    SUM(v.quantidade * p.preco) AS faturamento_total
FROM Vendas v
INNER JOIN Produto p ON v.id_produto = p.id_produto
INNER JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, c.nome_categoria
ORDER BY total_unidades_vendidas DESC
LIMIT 1;
"""

cursor.execute(query_campeao)
resultado = cursor.fetchone()

if resultado:
    id_p, nome, categoria, total_qtd, faturamento = resultado
    print("\n🏆 --- PRODUTO MAIS VENDIDO ---")
    print(f"Produto: {nome} (ID: {id_p})")
    print(f"Categoria: {categoria}")
    print(f"Total de Unidades Vendidas: {total_qtd} unidades")
    print(f"Faturamento Gerado: R$ {faturamento:.2f}")
```

---

### 4. Relatório Geral de Vendas por Produto com Pandas

Para gerar uma visão analítica completa de todos os produtos comercializados, carregamos a consulta agregada diretamente em um DataFrame do Pandas :

```python
query_ranking = """
SELECT 
    p.nome AS Produto,
    c.nome_categoria AS Categoria,
    p.preco AS Preco_Unitario,
    SUM(v.quantidade) AS Qtd_Vendida,
    SUM(v.quantidade * p.preco) AS Faturamento_Total,
    p.estoque AS Estoque_Restante
FROM Produto p
LEFT JOIN Vendas v ON p.id_produto = v.id_produto
LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, c.nome_categoria
ORDER BY Qtd_Vendida DESC;
"""

df_vendas = pd.read_sql_query(query_ranking, conn)

# Preenche com 0 os produtos que ainda não tiveram vendas registradas
df_vendas['Qtd_Vendida'] = df_vendas['Qtd_Vendida'].fillna(0).astype(int)
df_vendas['Faturamento_Total'] = df_vendas['Faturamento_Total'].fillna(0.0)

print("\n📊 --- RANKING COMPLETO DE VENDAS POR PRODUTO ---")
print(df_vendas.to_string(index=False))

# Fechamento seguro da conexão
conn.close()
```

---

### 📌 Resumo dos Aprendizados Aplicados

1. **Relacionamento\\(1:N\\)**: Cada venda está vinculada a um único produto via `FOREIGN KEY`
2. **Consistência de Estoque**: A transação atualiza o histórico de vendas e reduz o estoque de forma atômica (`commit()` / `rollback()`).
3. **Cruzamento & Agregação**: A consulta utiliza `INNER JOIN` / `LEFT JOIN` e `SUM()` agrupando com `GROUP BY` para responder diretamente à pergunta de negócio.

---

## Gerando gráficos

📈 Quer ver como gerar um gráfico de barras desse ranking de vendas usando Matplotlib/Seaborn?

Para criar um gráfico de barras horizontal a partir do DataFrame `df_vendas` gerado na etapa anterior, você pode utilizar o **Seaborn** combinado com o **Matplotlib**. 

Gráficos de barras horizontais são ideais para rankings de produtos, pois facilitam a leitura dos rótulos e a comparação visual das quantidades vendidas.

---

### **Código Python com Seaborn e Matplotlib**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuração de estilo visual limpo e profissional
sns.set_theme(style='whitegrid', palette='colorblind')

# 2. Criação da figura e eixos
fig, ax = plt.subplots(figsize=(10, 5))

# 3. Desenha o gráfico de barras horizontal (ordenado do maior para o menor)
bars = sns.barplot(
    data=df_vendas,
    x='Qtd_Vendida',
    y='Produto',
    hue='Produto',
    palette='Blues_r',
    legend=False,
    ax=ax
)

# 4. Título focado no destaque principal e rótulos dos eixos
ax.set_title('Camisa Polo Lidera em Volume com 10 Unidades Vendidas', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Quantidade de Unidades Vendidas', fontsize=11)
ax.set_ylabel('Produto', fontsize=11)

# 5. Adiciona os rótulos de dados numéricos no topo de cada barra
for p in ax.patches:
    largura = p.get_width()
    if largura > 0:
        ax.annotate(
            f'{int(largura)} un.',
            (largura, p.get_y() + p.get_height() / 2.),
            ha='left', va='center',
            xytext=(6, 0), textcoords='offset points',
            fontsize=10, fontweight='bold'
        )

# 6. Remove bordas desnecessárias (topo e direita)
sns.despine(top=True, right=True)

# 7. Ajusta o espaçamento interno
plt.tight_layout(pad=1.5)

# Exibe o gráfico (ou salva em arquivo)
plt.show()
```

---

### **Destaques do Gráfico Gerado (`ranking_vendas.png`)**

1. **Leitura Direta**: A visualização destaca a **Camisa Polo** no topo com 10 unidades vendidas, seguida pelo **Smartphone** (7 unidades) e **Cadeira de Escritório** (5 unidades).
2. **Paleta Sequencial (`Blues_r`)**: A gradação de cores enfatiza visualmente os produtos mais vendidos com tons mais escuros.
3. **Rótulos de Dados Integrados**: Exibe a quantidade exata ao lado de cada barra, eliminando a necessidade de adivinhar valores pela escala do eixo X.

---

## Integrando em um Web App Bottle

💡 Quer ver como disponibilizar essa consulta de faturamento e ranking em uma **API REST em formato JSON** utilizando o framework **Bottle**?

Para integrar a consulta e a análise do ranking de vendas com o micro-framework **Bottle**, você pode adotar duas rotas principais:

1. **Endpoint de API REST (JSON)**: Retorna os dados agrupados diretamente em formato JSON, ideal para dashboards, sistemas externos ou requisições assíncronas (`fetch`).
2. **Página Web Interativa (HTML)**: Renderiza uma tabela dinâmica com o relatório de faturamento e insere a imagem do gráfico gerado (`ranking_vendas.png`) diretamente na página.

---

### **Código Completo de Integração (`app.py`)**

```python
import sqlite3
import pandas as pd
from pathlib import Path
from bottle import Bottle, get, template, run, static_file

app = Bottle()
DB_PATH = Path(__file__).with_name("gestao_produtos.db")

def get_connection():
    """Abre a conexão com o banco SQLite e ativa Foreign Keys."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

# ==========================================
# 1. ROTA DE API REST (Retorna JSON)
# ==========================================
@app.get('/api/ranking-vendas')
def api_ranking_vendas():
    """
    Executa a consulta SQL agregada e retorna um dicionário.
    O Bottle converte automaticamente dicionários Python em respostas JSON.
    """
    conn = get_connection()
    query = """
        SELECT 
            p.nome AS produto,
            c.nome_categoria AS categoria,
            p.preco AS preco_unitario,
            COALESCE(SUM(v.quantidade), 0) AS total_vendido,
            COALESCE(SUM(v.quantidade * p.preco), 0.0) AS faturamento_total
        FROM Produto p
        LEFT JOIN Vendas v ON p.id_produto = v.id_produto
        LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
        GROUP BY p.id_produto, p.nome, c.nome_categoria
        ORDER BY total_vendido DESC;
    """
    cursor = conn.cursor()
    cursor.execute(query)
    registros = cursor.fetchall()
    conn.close()

    # Formata os registros em uma estrutura de dicionários
    ranking = [
        {
            "produto": r["produto"],
            "categoria": r["categoria"],
            "preco_unitario": r["preco_unitario"],
            "total_vendido": r["total_vendido"],
            "faturamento_total": r["faturamento_total"]
        }
        for r in registros
    ]

    # O Bottle configura automaticamente o Content-Type: application/json
    return {"status": "sucesso", "dados": ranking}

# ==========================================
# 2. ROTA DE PÁGINA WEB (HTML + Imagem do Gráfico)
# ==========================================
@app.get('/relatorio/ranking')
def exibir_pagina_ranking():
    """
    Consulta o banco de dados via Pandas e renderiza a view com a tabela e o gráfico.
    """
    conn = get_connection()
    df_ranking = pd.read_sql_query("""
        SELECT 
            p.nome AS produto,
            c.nome_categoria AS categoria,
            COALESCE(SUM(v.quantidade), 0) AS qtd_vendida,
            COALESCE(SUM(v.quantidade * p.preco), 0.0) AS faturamento
        FROM Produto p
        LEFT JOIN Vendas v ON p.id_produto = v.id_produto
        LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
        GROUP BY p.id_produto, p.nome, c.nome_categoria
        ORDER BY qtd_vendida DESC;
    """, conn)
    conn.close()

    html_template = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Ranking de Vendas</title>
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; margin: 30px; background-color: #f8f9fa; }
            h1 { color: #0d6efd; }
            .card-grafico { text-align: center; margin-bottom: 25px; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            .card-grafico img { max-width: 100%; border-radius: 4px; }
            table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
            th, td { border: 1px solid #dee2e6; padding: 12px; text-align: left; }
            th { background-color: #0d6efd; color: white; }
            tr:nth-child(even) { background-color: #f1f3f5; }
        </style>
    </head>
    <body>
        <h1>📊 Painel e Ranking de Vendas</h1>

        <!-- Exibição da Imagem do Gráfico Gerado pelo Matplotlib/Seaborn -->
        <div class="card-grafico">
            <img src="/static/ranking_vendas.png" alt="Gráfico do Ranking de Vendas">
        </div>

        <h2>Tabela Detalhada de Desempenho</h2>
        <table>
            <tr>
                <th>Produto</th>
                <th>Categoria</th>
                <th>Qtd. Vendida</th>
                <th>Faturamento Total</th>
            </tr>
            % for _, row in ranking.iterrows():
            <tr>
                <td><strong>{{ row['produto'] }}</strong></td>
                <td>{{ row['categoria'] }}</td>
                <td>{{ int(row['qtd_vendida']) }} unid.</td>
                <td>R$ {{ "%.2f" % row['faturamento'] }}</td>
            </tr>
            % end
        </table>
    </body>
    </html>
    '''
    return template(html_template, ranking=df_ranking)

# ==========================================
# 3. ROTA PARA SERVIR O GRÁFICO (Arquivos Estáticos)
# ==========================================
@app.get('/static/<filepath:path>')
def servir_estatico(filepath):
    """Serve a imagem ranking_vendas.png presente no diretório out/ ou scratch/."""
    return static_file(filepath, root='./scratch')

if __name__ == '__main__':
    print("Servidor rodando em http://localhost:8080 ...")
    run(app, host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Destaques da Arquitetura**

* **Transformação Automática em JSON**: Quando o *callback* de uma rota do Bottle retorna um dicionário Python (`dict`), o Bottle serializa o conteúdo automaticamente em JSON e configura o cabeçalho `Content-Type: application/json`.
* **Combinação com Pandas**: A função `pd.read_sql_query()` lê o resultado das junções (`JOIN`) e agregações (`SUM`, `GROUP BY`) do SQLite e injeta o DataFrame no motor de templates `SimpleTemplate` do Bottle.
* **Entrega de Ativos Visuais**: A função `static_file()` disponibiliza a imagem `.png` gerada pelo script de visualização do Seaborn para que o navegador a renderize no painel web.

---

## Adicionando uma camada de proteção para acesso com autenticação

💡 Gostaria de ver como adicionar uma camada de **proteção com autenticação via Cookies / Sessão** para restringir o acesso a essa rota de relatórios corporativos?

Para adicionar uma camada de proteção com autenticação via **Cookies / Sessão** em uma aplicação **Bottle**, utiliza-se a funcionalidade nativa de **cookies assinados criptograficamente** (`secret`) combinada a um **decorator** customizado em Python.

---

### **Como Funciona a Proteção**

1. **Cookies Assinados (`secret='sua_chave_secreta'`)**: O Bottle gera uma assinatura digital para o valor armazenado. Se um usuário malicioso tentar alterar o valor do cookie diretamente no navegador, a verificação falhará no servidor e retornará `None`.
2. **Atributo `httponly=True`**: Impede que scripts do lado do cliente (Ataques XSS) leiam ou roubem o cookie de autenticação.
3. **Decorator `@requer_autenticacao`**: Um interceptador que verifica se o cookie assinado existe antes de permitir a execução da rota restrita de relatórios. Se a sessão for inválida ou inexistente, o usuário é redirecionado para a tela de login.

---

### **1. Código de Autenticação e Proteção de Rotas (`app.py`)**

```python
import functools
import sqlite3
from bottle import Bottle, get, post, request, response, redirect, template, run

app = Bottle()

# Chave secreta usada para assinar digitalmente os cookies de sessão [cite: 307]
CHAVE_SECRETA = "sua_chave_secreta_super_segura_12345"

# ------------------------------------------------------------------
# 1. DECORATOR DE AUTENTICAÇÃO (RESTRIÇÃO DE ROTAS)
# ------------------------------------------------------------------
def requer_autenticacao(funcao_rota):
    """
    Decorator que intercepta as requisições e valida o cookie assinado de sessão [cite: 307].
    """
    @functools.wraps(funcao_rota)
    def wrapper(*args, **kwargs):
        # Tenta ler e validar a assinatura digital do cookie de sessão [cite: 307]
        usuario_logado = request.get_cookie("usuario_sessao", secret=CHAVE_SECRETA)
        
        if not usuario_logado:
            # Se o cookie estiver ausente ou foi alterado pelo usuário, bloqueia e envia para o login [cite: 304, 307]
            redirect("/login?erro=Acesso+restrito.+Faça+login+para+continuar.")
            
        return funcao_rota(*args, **kwargs)
    return wrapper

# ------------------------------------------------------------------
# 2. ROTAS DE LOGIN E LOGOUT
# ------------------------------------------------------------------
@app.get('/login')
def exibir_login():
    msg_erro = request.query.get('erro', '')
    return template('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Login - Acesso Corporativo</title>
            <style>
                body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f8f9fa; }
                .card-login { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 320px; }
                input { width: 100%; padding: 10px; margin: 8px 0 15px; box-sizing: border-box; }
                input[type="submit"] { background: #0d6efd; color: white; border: none; font-weight: bold; cursor: pointer; border-radius: 4px; }
                .alerta { color: #dc3545; font-size: 0.9em; margin-bottom: 10px; }
            </style>
        </head>
        <body>
            <div class="card-login">
                <h2>🔐 Acesso Restrito</h2>
                % if msg_erro:
                    <div class="alerta">⚠️ {{ msg_erro }}</div>
                % end
                <form action="/login" method="post">
                    <label>Usuário:</label>
                    <input type="text" name="usuario" required placeholder="Digite seu usuário">
                    
                    <label>Senha:</label>
                    <input type="password" name="senha" required placeholder="Digite sua senha">
                    
                    <input type="submit" value="Entrar no Sistema">
                </form>
            </div>
        </body>
        </html>
    ''', msg_erro=msg_erro)

@app.post('/login')
def processar_login():
    usuario = (request.forms.getunicode('usuario') or '').strip()
    senha = (request.forms.getunicode('senha') or '').strip()

    # Em uma aplicação real, consulte a tabela 'usuarios' no SQLite usando hash seguro [cite: 44]
    if usuario == "admin" and senha == "senha123":
        # Cria o cookie assinado criptograficamente [cite: 307]
        response.set_cookie(
            "usuario_sessao", 
            usuario, 
            secret=CHAVE_SECRETA, 
            httponly=True,   # Impede que o cookie seja lido via JS no cliente (Proteção XSS) [cite: 305, 306]
            max_age=3600     # Define o tempo de expiração da sessão para 1 hora [cite: 305]
        )
        redirect('/relatorio/ranking')
    else:
        redirect('/login?erro=Usuário+ou+senha+inválidos.')

@app.get('/logout')
def logout():
    # Remove/expira a sessão gravada no navegador [cite: 304, 305]
    response.delete_cookie("usuario_sessao")
    redirect('/login?erro=Sessão+encerrada+com+sucesso.')

# ------------------------------------------------------------------
# 3. ROTA PROTEGIDA DE RELATÓRIO
# ------------------------------------------------------------------
@app.get('/relatorio/ranking')
@requer_autenticacao  # Aplica a verificação de autenticação nesta rota [cite: 300, 307]
def exibir_relatorio_protegido():
    # Recupera o identificador do usuário autenticado no cookie [cite: 307]
    usuario_atual = request.get_cookie("usuario_sessao", secret=CHAVE_SECRETA)
    
    return f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head><meta charset="UTF-8"><title>Relatório Restrito</title></head>
        <body style="font-family: Arial, sans-serif; margin: 30px;">
            <h1>📊 Relatório Corporativo Restrito</h1>
            <p>Sessão ativa para o usuário: <strong>{usuario_atual}</strong> | <a href="/logout">Sair</a></p>
            <hr>
            <p>✅ Acesso concedido. Este conteúdo é visível apenas para usuários autenticados.</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Fluxo de Navegação e Segurança:**

1. **Acesso Não Autorizado**: Se o usuário tentar acessar a URL `/relatorio/ranking` diretamente, o decorator `@requer_autenticacao` intercepta o acesso e redireciona para a tela de login `/login`.
2. **Validação de Credenciais**: Ao submeter o formulário de login via método `POST`, o servidor verifica o usuário e senha e armazena a sessão assinada com `response.set_cookie(..., secret=CHAVE_SECRETA, httponly=True)`.
3. **Navegação Segura**: Nas requisições subsequentes, o navegador envia o cookie assinado. O método `request.get_cookie(..., secret=CHAVE_SECRETA)` valida a integridade do valor e concede o acesso.
4. **Encerramento de Sessão**: Ao clicar no link de logout `/logout`, a chamada `response.delete_cookie("usuario_sessao")` expira o cookie no navegador.

---

## Integrando autenticação em uma tabela de usuários

🔐 Quer ver como integrar essa autenticação com uma tabela de **Usuários** no SQLite salvando senhas criptografadas com **`hashlib`** ou **`bcrypt`**?

Para integrar a autenticação com uma tabela de **Usuários** no **SQLite** e armazenar senhas com **hashing seguro** (em vez de texto puro), vamos aplicar as seguintes práticas de segurança:

1. **Nunca salvar senhas em texto puro**: Armazenamos apenas um *hash* da senha [cite: 255].
2. **Uso de Salt (Sal)**: Adiciona-se um valor aleatório único antes do hash para evitar ataques de tabelas de comparação (*rainbow tables*).
3. **Algoritmo de Hash Seguro**: Utilizaremos **PBKDF2 / SHA-256** (nativo do módulo `hashlib`) ou a biblioteca **`bcrypt`**.

---

### **1. Estrutura da Tabela no SQLite (DDL)**

No SQLite, criamos a tabela `usuarios` com colunas para o login, a senha criptografada e o salt gerado [cite: 87]:

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    salt TEXT NOT NULL
);
```

---

### **2. Abordagem A: Usando a Biblioteca Padrão (`hashlib` com PBKDF2)**

O módulo `hashlib` faz parte da biblioteca padrão do Python (não precisa instalar nada) e fornece o algoritmo **`pbkdf2_hmac`**, recomendado para derivação segura de senhas.

#### **Funções Auxiliares de Hashing (`seguranca.py`)**

```python
import hashlib
import os

def gerar_hash_senha(senha_plana: str) -> tuple[str, str]:
    """
    Gera um salt aleatório e calcula o hash da senha usando PBKDF2-HMAC-SHA256.
    Retorna a tupla (senha_hash_hex, salt_hex).
    """
    # 1. Gera um salt aleatório de 16 bytes
    salt = os.urandom(16)
    
    # 2. Gera o hash com 100.000 iterações de PBKDF2
    hash_bytes = hashlib.pbkdf2_hmac(
        'sha256', 
        senha_plana.encode('utf-8'), 
        salt, 
        100000
    )
    
    return hash_bytes.hex(), salt.hex()

def verificar_senha(senha_digitada: str, senha_hash_salva: str, salt_salvo: str) -> bool:
    """
    Recalcula o hash da senha digitada usando o salt armazenado e compara com o hash salvo.
    """
    salt_bytes = bytes.fromhex(salt_salvo)
    
    hash_calculado = hashlib.pbkdf2_hmac(
        'sha256', 
        senha_digitada.encode('utf-8'), 
        salt_bytes, 
        100000
    )
    
    # hmac.compare_digest evita ataques de tempo (timing attacks)
    return hashlib.compare_digest(hash_calculado.hex(), senha_hash_salva)
```

---

### **3. Abordagem B: Usando a Biblioteca `bcrypt`**

Se você puder instalar a biblioteca `bcrypt` (`pip install bcrypt`), a verificação e geração de salt ficam ainda mais simples:

```python
import bcrypt

def gerar_hash_bcrypt(senha_plana: str) -> str:
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(senha_plana.encode('utf-8'), salt)
    return hash_bytes.decode('utf-8')

def verificar_senha_bcrypt(senha_digitada: str, hash_salvo: str) -> bool:
    return bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_salvo.encode('utf-8'))
```

---

### **4. Aplicação Completa no Bottle + SQLite (`app.py`)**

Abaixo está a integração completa utilizando o **`hashlib` nativo**, onde a tabela é inicializada, o usuário `admin` padrão é cadastrado com senha criptografada (caso não exista), e o login valida os dados diretamente no SQLite:

```python
import functools
import hashlib
import os
import sqlite3
from pathlib import Path
from bottle import Bottle, get, post, request, response, redirect, template, run

app = Bottle()

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")
CHAVE_SECRETA = "sua_chave_secreta_super_segura_12345"

# ------------------------------------------------------------------
# FUNCIONALIDADES DE SEGURANÇA E HASHING
# ------------------------------------------------------------------
def gerar_hash_senha(senha_plana: str) -> tuple[str, str]:
    salt = os.urandom(16)
    hash_bytes = hashlib.pbkdf2_hmac('sha256', senha_plana.encode('utf-8'), salt, 100000)
    return hash_bytes.hex(), salt.hex()

def verificar_senha(senha_digitada: str, senha_hash_salva: str, salt_salvo: str) -> bool:
    salt_bytes = bytes.fromhex(salt_salvo)
    hash_calculado = hashlib.pbkdf2_hmac('sha256', senha_digitada.encode('utf-8'), salt_bytes, 100000)
    return hashlib.compare_digest(hash_calculado.hex(), senha_hash_salva)

# ------------------------------------------------------------------
# INICIALIZAÇÃO DO BANCO DE DADOS
# ------------------------------------------------------------------
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def inicializar_banco():
    """Cria a tabela de usuários e cadastra o usuário 'admin' padrão."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                senha_hash TEXT NOT NULL,
                salt TEXT NOT NULL
            );
        ''')
        
        # Cadastra o admin caso o banco esteja vazio
        cursor.execute("SELECT id FROM usuarios WHERE usuario = 'admin';")
        if not cursor.fetchone():
            senha_hash, salt = gerar_hash_senha("senha123")
            cursor.execute(
                "INSERT INTO usuarios (usuario, senha_hash, salt) VALUES (?, ?, ?);",
                ('admin', senha_hash, salt)
            )
            print("👤 Usuário 'admin' padrão criado com sucesso!")

# ------------------------------------------------------------------
# DECORATOR DE AUTENTICAÇÃO DE ROTA
# ------------------------------------------------------------------
def requer_autenticacao(funcao_rota):
    @functools.wraps(funcao_rota)
    def wrapper(*args, **kwargs):
        usuario_logado = request.get_cookie("usuario_sessao", secret=CHAVE_SECRETA)
        if not usuario_logado:
            redirect("/login?erro=Acesso+restrito.+Faça+login.")
        return funcao_rota(*args, **kwargs)
    return wrapper

# ------------------------------------------------------------------
# ROTAS DE LOGIN E LOGOUT
# ------------------------------------------------------------------
@app.get('/login')
def exibir_login():
    msg_erro = request.query.get('erro', '')
    return template('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8"><title>Login de Acesso</title>
            <style>
                body { font-family: Arial; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f8f9fa; }
                .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 300px; }
                input { width: 100%; padding: 8px; margin: 8px 0 12px; box-sizing: border-box; }
                input[type="submit"] { background: #0d6efd; color: white; border: none; font-weight: bold; cursor: pointer; }
                .erro { color: red; font-size: 0.9em; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🔐 Login no Sistema</h2>
                % if msg_erro:
                    <p class="erro">⚠️ {{ msg_erro }}</p>
                % end
                <form action="/login" method="post">
                    <label>Usuário:</label>
                    <input type="text" name="usuario" required placeholder="admin">
                    
                    <label>Senha:</label>
                    <input type="password" name="senha" required placeholder="senha123">
                    
                    <input type="submit" value="Entrar">
                </form>
            </div>
        </body>
        </html>
    ''', msg_erro=msg_erro)

@app.post('/login')
def processar_login():
    usuario_input = (request.forms.getunicode('usuario') or '').strip()
    senha_input = (request.forms.getunicode('senha') or '').strip()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT usuario, senha_hash, salt FROM usuarios WHERE usuario = ?;", (usuario_input,))
    usuario_bd = cursor.fetchone()
    conn.close()

    # Se o usuário existe e a senha bate com o hash armazenado
    if usuario_bd and verificar_senha(senha_input, usuario_bd['senha_hash'], usuario_bd['salt']):
        response.set_cookie(
            "usuario_sessao", 
            usuario_bd['usuario'], 
            secret=CHAVE_SECRETA, 
            httponly=True, 
            max_age=3600
        )
        redirect('/relatorio/ranking')
    else:
        redirect('/login?erro=Usuário+ou+senha+incorretos.')

@app.get('/logout')
def logout():
    response.delete_cookie("usuario_sessao")
    redirect('/login?erro=Sessão+encerrada.')

# ------------------------------------------------------------------
# ROTA PROTEGIDA
# ------------------------------------------------------------------
@app.get('/relatorio/ranking')
@requer_autenticacao
def exibir_relatorio():
    usuario_atual = request.get_cookie("usuario_sessao", secret=CHAVE_SECRETA)
    return f'''
        <h1>📊 Painel Corporativo Protegido</h1>
        <p>Bem-vindo, <strong>{usuario_atual}</strong>! | <a href="/logout">Sair</a></p>
        <p>Esta página consulta os dados sensíveis após validar o hash de senha no banco SQLite.</p>
    '''

if __name__ == '__main__':
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    run(app, host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Resumo dos Componentes Integrados**

1. **Tabela `usuarios`**: Armazena `usuario`, `senha_hash` e `salt` [cite: 87, 255].
2. **PBKDF2-HMAC-SHA256**: O algoritmo de hash realiza 100.000 iterações com um salt exclusivo de 16 bytes.
3. **Validação no Login**: A Rota `POST /login` consulta a linha do usuário no SQLite, recupera o `salt` salvo para recomputar o hash e utiliza `compare_digest` para garantir uma validação segura imune a *timing attacks*.
4. **Cookie Assinado**: Em caso de sucesso, o Bottle assina digitalmente o cookie de sessão com a `CHAVE_SECRETA` [cite: 246].
