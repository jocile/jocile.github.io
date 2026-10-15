---
description: "Exemplo prático de um cadastro com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
  - programacao
date: 2026-10-15
draft: false
---
Esta é uma **prática passo a passo** para quem está iniciando a integração de **Python com o banco de dados SQLite**. O SQLite é um banco de dados SQL leve, portátil e *serverless* (sem servidor). Além disso, o módulo `sqlite3` já vem pré-instalado na biblioteca padrão do Python.

## Fase inicial - criando o Banco de Dados

---

### **Objetivo da Prática**

Criar um banco de dados local, construir uma tabela de **clientes**, executar todas as operações fundamentais do ciclo **CRUD** (Criar, Ler, Atualizar e Deletar) e fechar a conexão de forma segura.

---

### **Passo 1: Conectar ao Banco de Dados**

Importe o módulo `sqlite3` e abra uma conexão chamando `sqlite3.connect()`. Se o arquivo `.db` ainda não existir no diretório, o SQLite irá criá-lo automaticamente. Em seguida, crie o objeto **cursor**, que é responsável por executar os comandos SQL na base.

```python
import sqlite3

# 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
conn = sqlite3.connect('meu_banco_de_dados.db')

# 2. Cria o objeto cursor para enviar comandos SQL
cursor = conn.cursor()

print("Conexão estabelecida com sucesso!")
```

*(Conceitos de conexão e cursor baseados nos materiais).*

---

### **Passo 2: Criar uma Tabela (DDL)**

Defina a estrutura da tabela utilizando o comando DDL (**Data Definition Language**) `CREATE TABLE IF NOT EXISTS`. A tabela `clientes` terá uma chave primária autoincrementada (`id`), além de colunas para `nome`, `email` e `telefone`.

```python
# Executa a criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    );
''')

# Confirma a alteração estrutural no banco
conn.commit()
print("Tabela 'clientes' pronta para uso!")
```

*(Comando de criação estrutural e confirmação baseados nos materiais).*

---

### **Passo 3: Inserir Registros (DML - Create)**

Para evitar falhas de segurança como **SQL Injection**, nunca concatene variáveis diretamente no texto da query; utilize **marcadores de posição** (`?`). Você pode inserir múltiplos registros em lote usando o método `cursor.executemany()` e depois confirmar as alterações com `conn.commit()`.

```python
# Lista de tuplas com os dados de exemplo
novos_clientes = [
    ("Ana Silva", "ana.silva@example.com", "11 99999-0001"),
    ("Bruno Souza", "bruno.souza@example.com", "11 99999-0002"),
    ("Carla Pereira", "carla.pereira@example.com", "11 99999-0003")
]

# Inserção em lote usando placeholders (?)
cursor.executemany(
    "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
    novos_clientes
)

# Salva permanentemente a inserção no arquivo do banco
conn.commit()
print(f"{cursor.rowcount} registros inseridos com sucesso!")
```

*(Inserção segura com marcadores de posição baseada nos materiais).*

---

### **Passo 4: Consultar os Dados (DQL - Read)**

Para consultar as informações salvas, execute uma instrução `SELECT`. Utilize o método `fetchall()` para obter todas as linhas retornadas.

```python
# Executa a consulta
cursor.execute("SELECT id, nome, email, telefone FROM clientes;")

# Recupera todas as linhas encontradas
resultados = cursor.fetchall()

print("\n--- Lista de Clientes ---")
for id_, nome, email, telefone in resultados:
    print(f"ID: {id_} | Nome: {nome} | E-mail: {email} | Telefone: {telefone}")
```

*(Consulta de dados e varredura de resultados baseadas nos materiais).*

---

### **Passo 5: Atualizar e Excluir Registros (Update / Delete)**

Para alterar dados existentes ou remover um registro, utilize os comandos `UPDATE` e `DELETE` acompanhados da cláusula `WHERE` e dos marcadores `?`.

```python
# 1. Atualizar e-mail de um cliente específico pelo ID
cursor.execute(
    "UPDATE clientes SET email = ? WHERE id = ?;",
    ("ana.nova@example.com", 1)
)

# 2. Deletar um cliente específico pelo ID
cursor.execute(
    "DELETE FROM clientes WHERE id = ?;",
    (3,)
)

# Confirma as alterações no banco de dados
conn.commit()
print("\nAlterações de atualização e exclusão aplicadas!")
```

*(Comandos DML de atualização e exclusão baseados nos materiais).*

---

### **Passo 6: Fechar a Conexão**

Após concluir todas as operações, feche o cursor e a conexão para garantir a liberação de recursos do sistema e a consistência do arquivo.

```python
cursor.close()
conn.close()
print("Conexão fechada com segurança.")
```

*(Fechamento e boas práticas baseados nos materiais).*

---

### **Passo Bônus: Leitura Avançada com Pandas**

Você também pode integrar o banco SQLite à biblioteca **Pandas** para carregar os dados diretamente em um DataFrame usando `pd.read_sql_query()`.

```python
import pandas as pd

conn = sqlite3.connect('meu_banco_de_dados.db')

# Carrega a consulta direto em um DataFrame do Pandas
df_clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
print("\n--- DataFrame do Pandas ---")
print(df_clientes)

conn.close()
```

💡 Agora que tal expandir essa prática, vamos conectar esses comandos a uma interface web simples utilizando o micro-framework **Bottle** para criar um sistema com formulários no navegador.

[[Pratica CRUD Python Sqlite Segunda fase - Front End Web]]
