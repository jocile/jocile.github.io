---
title: Manipulação de Banco de Dados
description: "criar e manipular um banco de dados utilizando o MySQL Workbench e acessar um servidor MySQL na rede local"
date: '2026-09-17'
draft: false
tags:
  - banco-de-dados
  - Python
---

>[!summary] Nesta prática, vamos criar e manipular um banco de dados utilizando o MySQL Workbench e acessar um servidor MySQL na rede local. Vamos aprender e praticar os principais comandos SQL.

## Pré-requisitos

- MySQL Server instalado e acessível na rede local.
- MySQL Workbench instalado para gerenciar o banco de dados.
- Conhecimento básico de SQL e Python.
- Biblioteca Python: `mysql-connector-python`.

### Passo a Passo

### 1. Configurando o MySQL Server e MySQL Workbench

1. **Instalar o MySQL Server**: Siga as instruções específicas para a sua plataforma (Windows, macOS, Linux) para instalar o MySQL Server.
2. **Configurar Usuário e Permissões**: Crie um usuário e conceda as permissões necessárias para acessar e manipular o banco de dados.
3. **Instalar o MySQL Workbench**: Baixe e instale o MySQL Workbench para gerenciar o banco de dados.

### 2. Conectando-se ao Servidor MySQL com MySQL Workbench

1. Abra o MySQL Workbench.
2. Clique em `+` para criar uma nova conexão.
3. Insira as informações da conexão, como nome, endereço do host (IP do servidor na rede local), nome de usuário e senha.
4. Teste a conexão e salve-a se estiver funcionando corretamente.

### 3. Criando o Banco de Dados e Tabelas com MySQL Workbench

Abra uma nova aba de query e execute os seguintes comandos SQL para criar o banco de dados e as tabelas:

```sql
-- Criando o banco de dados
CREATE DATABASE IF NOT EXISTS meu_banco_de_dados;

-- Usando o banco de dados criado
USE meu_banco_de_dados;

-- Criando a tabela Categoria
CREATE TABLE IF NOT EXISTS Categoria (
    ID_Categoria INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Categoria VARCHAR(45) NOT NULL,
    Descricao VARCHAR(120)
);

-- Criando a tabela Produto
CREATE TABLE IF NOT EXISTS Produto (
    ID_Produto INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    Descricao VARCHAR(120),
    Preco DOUBLE,
    ID_Categoria INT,
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);
```

### 4. Inserindo Dados nas Tabelas

Execute os comandos SQL abaixo para inserir dados nas tabelas `Categoria` e `Produto`:

```sql
-- Inserindo dados na tabela Categoria
INSERT INTO Categoria (Nome_Categoria, Descricao) VALUES ('Eletrônicos', 'Dispositivos eletrônicos');
INSERT INTO Categoria (Nome_Categoria, Descricao) VALUES ('Móveis', 'Móveis de diversos tipos');
INSERT INTO Categoria (Nome_Categoria, Descricao) VALUES ('Vestuário', 'Roupas e acessórios');

-- Inserindo dados na tabela Produto
INSERT INTO Produto (Nome, Descricao, Preco, ID_Categoria) VALUES ('Smartphone', 'Telefone com funcionalidades avançadas', 1500.00, 1);
INSERT INTO Produto (Nome, Descricao, Preco, ID_Categoria) VALUES ('Sofá', 'Sofá de três lugares', 800.00, 2);
INSERT INTO Produto (Nome, Descricao, Preco, ID_Categoria) VALUES ('Camisa', 'Camisa de algodão', 50.00, 3);
```

### 5. Manipulando Dados com Comandos SQL

#### 5.1 Ler Dados (SELECT)

```sql
-- Selecionando todos os dados da tabela Produto
SELECT * FROM Produto;

-- Selecionando produtos com preço acima de 100
SELECT * FROM Produto WHERE Preco > 100;
```

#### 5.2 Atualizar Dados (UPDATE)

```sql
-- Atualizando o preço de um produto
UPDATE Produto SET Preco = 1600.00 WHERE Nome = 'Smartphone';
```

#### 5.3 Deletar Dados (DELETE)

```sql
-- Deletando um produto
DELETE FROM Produto WHERE Nome = 'Camisa';
```

### 6. Conectando ao Banco de Dados MySQL com Python

Vamos agora criar um script Python para conectar-se ao banco de dados MySQL e executar consultas.

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

### 7. Executando Operações CRUD com Python

#### 7.1 Inserir Dados (Create)

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

#### 7.2 Ler Dados (Read)

```python
# Ler dados das tabelas
cursor.execute("SELECT * FROM Produto")
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)
```

#### 7.3 Atualizar Dados (Update)

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

#### 7.4 Deletar Dados (Delete)

```python
# Deletar um produto
delete_query = """
DELETE FROM Produto
WHERE Nome = 'Camisa';
"""
cursor.execute(delete_query)
conn.commit()
```

### 8. Análise de Dados com Pandas

Utilize a biblioteca `pandas` para analisar os dados.

```python
# Ler dados e carregar em um DataFrame
df_produtos = pd.read_sql("SELECT * FROM Produto", con=conn)
print(df_produtos)

# Análise simples
print(df_produtos.describe())
```

### 9. Conclusão

Nesta prática, você aprendeu a criar e manipular um banco de dados utilizando o MySQL Workbench e a executar operações CRUD usando Python. O MySQL Workbench é uma ferramenta poderosa para gerenciar bancos de dados MySQL, e a integração com Python permite criar aplicativos robustos e eficientes para manipulação de dados.

>[!tip] **Dica**: Sempre feche a conexão com o banco de dados ao final do seu script para garantir que todos os recursos sejam liberados corretamente.

```python
cursor.close()
conn.close()
```

### Considerações Finais

O conhecimento de comandos SQL e a habilidade de integrar bancos de dados com aplicações Python são essenciais para desenvolvedores que desejam trabalhar com gerenciamento de dados e desenvolvimento de aplicações baseadas em banco de dados. Praticar operações CRUD e manipulação de dados com ferramentas como o MySQL Workbench e `pandas` proporciona uma base sólida para projetos mais complexos e escaláveis.
