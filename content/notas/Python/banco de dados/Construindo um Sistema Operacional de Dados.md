---
title: "Construindo um Sistema Operacional de Dados"
date: 2026-10-12
draft: false
tags:
  - python
  - banco-de-dados
  - sqlite
  - quartz
  - sql
description: "Tutorial prático sobre desenvolvimento com SQLite em Python, cobrindo conexões seguras, DDL, proteção contra SQL Injection e recuperação de dados."
---

Este tutorial apresenta passo a passo para desenvolver uma aplicação completa em Python que gerencia a camada relacional de um sistema de vendas. O script aplica validações de esquema, restrições de integridade, proteção contra injeção de SQL e otimização do mapeamento de resultados.

## Pré-requisitos

- Python 3.12+ 
- SQLite (incluído com o Python)
- Conhecimento básico de DB-API 2.0

## Passo 1: Conexão Segura e Configuração de Infraestrutura

O primeiro passo é inicializar a conexão com a base de dados em disco (`vendas.db`) ou em memória RAM (`:memory:`), aplicando as instruções de infraestrutura em modo `autocommit=True` e depois ativando a gestão manual da transação.

```python
import sqlite3

def criar_conexao_segura(caminho_banco: str = "vendas.db") -> sqlite3.Connection:
    """
    Abre a conexão com o SQLite aplicando boas práticas de infraestrutura
    conforme as especificações modernas do Python 3.12+.
    
    Para bancos temporários em memória RAM, utilize caminho_banco=\":memory:\".
    """
    # 1. Abre a conexão com autocommit=True para emitir comandos PRAGMA com segurança
    conn = sqlite3.connect(caminho_banco, autocommit=True)
    
    # Exemplo alternativo para banco em memória RAM:
    # conn_ram = sqlite3.connect(":memory:", autocommit=True)
    
    # 2. Configurações essenciais de infraestrutura e integridade
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    
    # 3. Alterna para o gerenciamento de transação manual (PEP 249)
    conn.autocommit = False
    return conn

# Teste de inicialização da conexão
conexao = criar_conexao_segura("vendas.db")
print("Conexão estabelecida e infraestrutura configurada com sucesso.")
```

## Passo 2: Definição do Esquema Relacional (DDL)

Com a infraestrutura pronta, criaremos o cursor (`conn.cursor()`) para definir as tabelas relacionais (`produtos` e `pedidos`) com restrições operacionais explicitadas (`PRIMARY KEY AUTOINCREMENT`, `NOT NULL`, `UNIQUE`, `CHECK` e `FOREIGN KEY`). Utilizaremos o gerenciador de contexto `with conn:` que, quando `autocommit=False`, gerencia automaticamente os limites da transação, efetuando o `commit()` em caso de sucesso ou `rollback()` na ocorrência de exceções.

```python
def criar_tabelas(conn: sqlite3.Connection):
    """
    Cria as tabelas do sistema de vendas aplicando restrições de integridade.
    """
    # O gerenciador de contexto na conexão lida com commit/rollback da transação DDL
    with conn:
        cursor = conn.cursor()
        
        # Tabela de Produtos (incluindo atributo 'categoria' para agregações)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL CHECK(preco >= 0.0),
            estoque INTEGER NOT NULL CHECK(estoque >= 0)
        );
        """)
        
        # Tabela de Pedidos
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL CHECK(quantidade > 0),
            data_pedido TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
        );
        """)

criar_tabelas(conexao)
print("Tabelas criadas com sucesso.")
```

## Passo 3: Manipulação de Dados (DML) e Proteção contra SQL Injection

A montagem de consultas SQL por meio de concatenação direta de strings expõe o sistema a vulnerabilidades graves de Injeção de SQL (SQL Injection). Ao concatenar dados inseridos pelos usuários diretamente na instrução SQL, invasores podem adulterar a sintaxe da consulta e executar comandos arbitrários no banco de dados.

Para prevenir falhas de segurança, deve-se obrigatoriamente utilizar a substituição de parâmetros da DB-API. O driver `sqlite3` suporta dois estilos seguros:

- **Estilo Posicional (qmark)**: Utiliza marcadores de interrogação `?` no SQL e passa uma tupla com os valores na chamada.
- **Estilo Nomeado (named)**: Utiliza chaves precedidas por dois-pontos (`ex: :nome`) no SQL e passa um dicionário de valores.

Abaixo, vemos a inserção simples com `cursor.execute()` e a inserção em massa com `cursor.executemany()`:

```python
def popular_dados_iniciais(conn: sqlite3.Connection):
    """
    Insere dados na tabela de produtos utilizando substituição de parâmetros segura.
    """
    cursor = conn.cursor()
    
    # Inserção única utilizando o estilo posicional (qmark) com tupla
    produto_unico = ("Teclado Mecânico", "Periféricos", 250.00, 15)
    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, estoque) 
        VALUES (?, ?, ?, ?);
    """, produto_unico)
    
    # Inserções em massa utilizando executemany com uma lista de tuplas
    lista_produtos = [
        ("Mouse Óptico", "Periféricos", 80.00, 30),
        ("Monitor 24 Polegadas", "Monitores", 900.00, 8),
        ("Headset Gamer", "Periféricos", 350.00, 20),
        ("Monitor 27 Curvo", "Monitores", 1400.00, 5)
    ]
    cursor.executemany("""
        INSERT INTO produtos (nome, categoria, preco, estoque) 
        VALUES (?, ?, ?, ?);
    """, lista_produtos)
    
    # Exemplo utilizando o estilo nomeado com dicionário
    pedido_nomeado = {"p_id": 1, "qtd": 2}
    cursor.execute("""
        INSERT INTO pedidos (produto_id, quantidade) 
        VALUES (:p_id, :qtd);
    """, pedido_nomeado)
    
    # Efetivação explícita da transação DML
    conn.commit()

try:
    popular_dados_iniciais(conexao)
    print("Dados operacionais inseridos com segurança.")
except sqlite3.IntegrityError as e:
    print(f"Erro de integridade ao inserir dados: {e}")
    conexao.rollback()
```

## Passo 4: Consultas Avançadas e Mapeamento de Resultados

Para recuperar dados de consultas, a DB-API 2.0 disponibiliza os métodos `fetchone()`, `fetchmany(size)` e `fetchall()`, além de permitir a iteração direta sobre o cursor. Por padrão, os resultados são retornados como tuplas simples. Atribuir o objeto de alto desempenho `sqlite3.Row` à propriedade `conn.row_factory` habilita o acesso às colunas por índice numérico e por nome de campo (de forma insensível a maiúsculas/minúsculas).

Abaixo, demonstramos explicitamente todas as quatro formas de recuperação de dados:

```python
def demonstrar_formas_de_busca(conn: sqlite3.Connection):
    """
    Demonstra fetchone(), fetchmany(), fetchall() e iteração direta sobre o cursor
    utilizando a fábrica de linhas sqlite3.Row.
    """
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("\n--- 1. Exemplo com fetchone() ---")
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE preco > ?", (500.0,))
    linha_unica = cursor.fetchone()
    if linha_unica:
        print(f"Produto Caro (Nome): {linha_unica['nome']} | Preço (Índice): R$ {linha_unica[2]}")
        
    print("\n--- 2. Exemplo com fetchmany(size=2) ---")
    cursor.execute("SELECT id, nome, categoria FROM produtos ORDER BY id;")
    lote = cursor.fetchmany(2)
    for prod in lote:
        print(f"ID: {prod['id']} | Nome: {prod['nome']} | Categoria: {prod['categoria']}")
        
    print("\n--- 3. Exemplo com fetchall() ---")
    cursor.execute("SELECT nome, estoque FROM produtos WHERE categoria = ?", ("Periféricos",))
    todos_perifericos = cursor.fetchall()
    print(f"Total de periféricos encontrados: {len(todos_perifericos)}")
    for item in todos_perifericos:
        print(f"Item: {item['nome']} | Estoque: {item['estoque']}")
        
    print("\n--- 4. Exemplo com Iteração Direta sobre o Cursor ---")
    cursor.execute("SELECT * FROM produtos;")
    for linha in cursor:
        print(f"ID: {linha['id']} | Nome: {linha['NOME']} | Categoria: {linha['categoria']}")

demonstrar_formas_de_busca(conexao)
conexao.close()
```

Concluído o ciclo essencial de manipulação e consulta estruturada (CRUD), o SQLite oferece recursos avançados para integração analítica e rotinas de manutenção corporativa.
