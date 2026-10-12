---
title: Prática com Python e SQLite
description: Nesta prática, vamos desenvolver um aplicativo em Python que se conecta
  a um banco de dados SQLite, realiza operações CRUD (Create, Read, Update, Delete)
  e…
date: '2026-10-12'
draft: false
tags:
  - banco-de-dados
  - Python
---

Nesta prática, vamos desenvolver um aplicativo em Python que se conecta a um banco de dados SQLite, realiza operações CRUD (Create, Read, Update, Delete) e manipula dados. Este exercício é ideal para estudantes de programação que desejam aprender a manipular bancos de dados com Python.

## Pré-requisitos

- Conhecimento básico de Python.
- Bibliotecas Python: `sqlite3`, `pandas`.

### Passo a Passo

### 1. Configuração do Ambiente

Instale as bibliotecas necessárias utilizando o comando abaixo:

```bash
pip install pandas
```

### 2. Conectando-se ao Banco de Dados SQLite

Crie um script Python para conectar-se ao banco de dados SQLite e executar consultas.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('meu_banco_de_dados.db')

# Criando um cursor
cursor = conn.cursor()

# Testando a conexão
cursor.execute("SELECT sqlite_version();")
print(f"Versão do SQLite: {cursor.fetchone()[0]}")
```

### 3. Criando as Tabelas no Banco de Dados

Crie as tabelas `Produto` e `Categoria` no banco de dados SQLite.

```python
create_table_query = """
CREATE TABLE IF NOT EXISTS Categoria (
    ID_Categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_Categoria TEXT NOT NULL,
    Descricao TEXT
);

CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Descricao TEXT,
    Preco REAL,
    ID_Categoria INTEGER,
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);
"""

cursor.executescript(create_table_query)
conn.commit()
```

### 4. Operações CRUD

#### 4.1 Inserir Dados (Create)

```python
# Dados para inserir
categorias = [
    ('Eletrônicos', 'Dispositivos eletrônicos'),
    ('Móveis', 'Móveis de diversos tipos'),
    ('Vestuário', 'Roupas e acessórios')
]

produtos = [
    ('Smartphone', 'Telefone com funcionalidades avançadas', 1500.00, 1),
    ('Sofá', 'Sofá de três lugares', 800.00, 2),
    ('Camisa', 'Camisa de algodão', 50.00, 3)
]

# Inserindo dados nas tabelas
cursor.executemany("INSERT INTO Categoria (Nome_Categoria, Descricao) VALUES (?, ?);", categorias)
cursor.executemany("INSERT INTO Produto (Nome, Descricao, Preco, ID_Categoria) VALUES (?, ?, ?, ?);", produtos)
conn.commit()
```

#### 4.2 Ler Dados (Read)

```python
# Ler dados das tabelas
cursor.execute("SELECT * FROM Produto")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)
```

#### 4.3 Atualizar Dados (Update)

```python
# Atualizar um produto
update_query = """
UPDATE Produto
SET Preco = 1600.00
WHERE Nome = 'Smartphone';
"""
cursor.execute(update_query)
conn.commit()
```

#### 4.4 Deletar Dados (Delete)

```python
# Deletar um produto
delete_query = """
DELETE FROM Produto
WHERE Nome = 'Camisa';
"""
cursor.execute(delete_query)
conn.commit()
```

### 5. Análise de Dados

Utilize a biblioteca `pandas` para analisar os dados.

```python
# Ler dados e carregar em um DataFrame
df_produtos = pd.read_sql_query("SELECT * FROM Produto", conn)
print(df_produtos)

# Análise simples
print(df_produtos.describe())
```

### 6. Conclusão

Nesta prática, você aprendeu a desenvolver um aplicativo em Python que se conecta a um banco de dados SQLite, realiza operações CRUD e manipula dados para análise. O uso de ferramentas como o SQLite, que é leve e de fácil configuração, facilita bastante o gerenciamento e a manipulação de bancos de dados, especialmente para iniciantes e em ambientes de desenvolvimento ágeis.

**Dica**: Sempre feche a conexão com o banco de dados ao final do seu script para garantir que todos os recursos sejam liberados corretamente.

```python
conn.close()
```
