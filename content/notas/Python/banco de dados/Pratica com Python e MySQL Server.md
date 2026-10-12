---
title: Prática com Python e MySQL Server
description: Nesta prática, vamos desenvolver um aplicativo em Python que se conecta
  a um banco de dados MySQL Server, realiza operações CRUD (Create, Read, Update,…
date: '2026-09-17'
draft: false
tags:
  - banco-de-dados
  - Python
---

Nesta prática, vamos desenvolver um aplicativo em Python que se conecta a um banco de dados MySQL Server, realiza operações CRUD (Create, Read, Update, Delete) e manipula dados. Utilizaremos o MySQL Workbench para criar e gerenciar o banco de dados.

## Pré-requisitos

- Conta no MySQL Server com acesso ao MySQL Workbench.
- Conhecimento básico de Python.
- Bibliotecas Python: `mysql-connector-python`, `pandas`.

### Passo a Passo

### 1. Configuração do Ambiente

Instale as bibliotecas necessárias utilizando o comando abaixo:

```bash
pip install mysql-connector-python pandas
```

### 2. Configurando o MySQL Server e MySQL Workbench

1. **Instalar o MySQL Server**: Siga as instruções específicas para a sua plataforma (Windows, macOS, Linux) para instalar o MySQL Server.
2. **Configurar Usuário e Permissões**: Crie um usuário e conceda as permissões necessárias para acessar e manipular o banco de dados.
3. **Criar Banco de Dados no MySQL Workbench**:
   - Abra o MySQL Workbench e conecte-se ao servidor.
   - Crie um novo banco de dados chamado `meu_banco_de_dados`.

### 3. Conectando-se ao Banco de Dados MySQL

Crie um script Python para conectar-se ao banco de dados MySQL e executar consultas.

```python
import mysql.connector
import pandas as pd

db_host = 'seu_host_do_mysql'  # exemplo: 'localhost' ou '192.168.1.100'
db_user = 'seu_usuario'
db_password = 'sua_senha'
db_name = 'meu_banco_de_dados'

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# Criando um cursor
cursor = conn.cursor()

# Testando a conexão
cursor.execute("SELECT VERSION();")
print(f"Versão do MySQL: {cursor.fetchone()[0]}")
```

### 4. Criando as Tabelas no Banco de Dados

Crie as tabelas `Produto` e `Categoria` no banco de dados MySQL.

```python
create_table_query = """
CREATE TABLE IF NOT EXISTS Categoria (
    ID_Categoria INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Categoria VARCHAR(45) NOT NULL,
    Descricao VARCHAR(120)
);

CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Descricao VARCHAR(120),
    Preco DOUBLE,
    ID_Categoria INT,
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);
"""

cursor.execute(create_table_query, multi=True)
conn.commit()
```

### 5. Operações CRUD

#### 5.1 Inserir Dados (Create)

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
insert_categoria_query = "INSERT INTO Categoria (Nome_Categoria, Descricao) VALUES (%s, %s)"
insert_produto_query = "INSERT INTO Produto (Nome, Descricao, Preco, ID_Categoria) VALUES (%s, %s, %s, %s)"

cursor.executemany(insert_categoria_query, categorias)
cursor.executemany(insert_produto_query, produtos)
conn.commit()
```

#### 5.2 Ler Dados (Read)

```python
# Ler dados das tabelas
cursor.execute("SELECT * FROM Produto")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)
```

#### 5.3 Atualizar Dados (Update)

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

#### 5.4 Deletar Dados (Delete)

```python
# Deletar um produto
delete_query = """
DELETE FROM Produto
WHERE Nome = 'Camisa';
"""
cursor.execute(delete_query)
conn.commit()
```

### 6. Análise de Dados

Utilize a biblioteca `pandas` para analisar os dados.

```python
# Ler dados e carregar em um DataFrame
df_produtos = pd.read_sql("SELECT * FROM Produto", con=conn)
print(df_produtos)

# Análise simples
print(df_produtos.describe())
```

### 7. Conclusão

Nesta prática, você aprendeu a desenvolver um aplicativo em Python que se conecta a um banco de dados MySQL Server, realiza operações CRUD e manipula dados para análise usando a biblioteca `pandas`. O MySQL Server é uma solução robusta e amplamente utilizada para gerenciamento de bancos de dados, e o uso do MySQL Workbench facilita a administração e manipulação dos dados.

**Dica**: Sempre feche a conexão com o banco de dados ao final do seu script para garantir que todos os recursos sejam liberados corretamente.

```python
cursor.close()
conn.close()
```

### Considerações Finais

Trabalhar com MySQL e Python é uma habilidade valiosa para qualquer desenvolvedor, pois muitas aplicações web e corporativas utilizam essa combinação para gerenciar grandes volumes de dados. O conhecimento de operações CRUD e a capacidade de analisar dados com `pandas` proporcionam uma base sólida para avançar em projetos mais complexos e escaláveis.
