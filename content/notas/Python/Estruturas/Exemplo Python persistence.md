---
title: Exemplo Python persistence
description: "Modelo de função simples e direta em Python para salvar uma lista em vários formatos de arquivo"
tags:
  - Python
  - banco-de-dados
  - estruturas-de-dados
---

## Modelo de Função salvar

- Modelo de função simples e direta em Python para salvar a lista de bicicletas em um arquivo de texto.
- A função utiliza o gerenciador de contexto with (que garante que o arquivo seja fechado corretamente) e formata os dados em colunas para facilitar a leitura.

```python
def salvar_cadastro_bicicletas(lista_bicicletas, nome_arquivo="bicicletas.txt"):
    """
    Salva uma lista de dicionários contendo o cadastro de bicicletas em um arquivo .txt.
    
    Cada bicicleta deve ser um dicionário com as chaves: 'cor', 'modelo' e 'ano'.
    """
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            # Escreve o cabeçalho do arquivo
            arquivo.write(f"{'MODELO':<20} | {'COR':<15} | {'ANO':<5}\n")
            arquivo.write("-" * 46 + "\n")
            
            # Escreve os dados de cada bicicleta
            for bike in lista_bicicletas:
                modelo = bike.get('modelo', 'N/A')
                cor = bike.get('cor', 'N/A')
                ano = bike.get('ano', 'N/A')
                
                arquivo.write(f"{modelo:<20} | {cor:<15} | {ano:<5}\n")
                
        print(f"Cadastro salvo com sucesso em '{nome_arquivo}'!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Lista de exemplo com o cadastro das bicicletas
    minhas_bikes = [
        {"modelo": "Mountain Bike X", "cor": "Preto", "ano": 2024},
        {"modelo": "Speed Pro", "cor": "Vermelho", "ano": 2025},
        {"modelo": "Urbana Vintage", "cor": "Verde Oliva", "ano": 2023}
    ]

    # Chamada da função
    salvar_cadastro_bicicletas(minhas_bikes)
```

## Como o arquivo final vai ficar:

```text
MODELO               | COR             | ANO  
----------------------------------------------
Mountain Bike X      | Preto           | 2024 
Speed Pro            | Vermelho        | 2025 
Urbana Vintage       | Verde Oliva     | 2023 
```

## Para evoluir o código

- Salvar em formato CSV ou JSON (que são melhores para carregar os dados de volta para o Python depois).
- Adicionar uma função para ler o arquivo e exibir as bicicletas na tela.
- Criar um menu interativo no terminal para cadastrar novas bicicletas antes de salvar.

## Salvar no formato CSV

- Salvar no formato CSV (Comma-Separated Values) é uma escolha excelente, pois o arquivo gerado pode ser aberto diretamente no Excel, Google Sheets ou reimportado facilmente para o Python.
- A forma mais eficiente e segura de fazer isso é utilizando o módulo nativo csv do Python.

```python
import csv

def salvar_cadastro_csv(lista_bicicletas, nome_arquivo="bicicletas.csv"):
    """
    Salva uma lista de dicionários contendo o cadastro de bicicletas em um arquivo .csv.
    """
    # Define os nomes das colunas (cabeçalho) com base nas chaves do dicionário
    campos = ['modelo', 'cor', 'ano']
    
    try:
        # 'newline=""' impede linhas em branco extras no Windows
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
            # Cria o gravador de dicionários do módulo csv
            escritor = csv.DictWriter(arquivo, fieldnames=campos, delimiter=';')
            
            # Escreve o cabeçalho (modelo;cor;ano)
            escritor.writeheader()
            
            # Escreve todas as linhas da lista de uma vez
            escritor.writerows(lista_bicicletas)
            
        print(f"Cadastro salvo com sucesso em '{nome_arquivo}'!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    minhas_bikes = [
        {"modelo": "Mountain Bike X", "cor": "Preto", "ano": 2024},
        {"modelo": "Speed Pro", "cor": "Vermelho", "ano": 2025},
        {"modelo": "Urbana Vintage", "cor": "Verde Oliva", "ano": 2023}
    ]

    salvar_cadastro_csv(minhas_bikes)
```

>[!info] 💡 Por que usamos o ponto e vírgula (;) como delimitador?
> Por padrão, o CSV usa a vírgula ( , ). Porém, em sistemas operacionais configurados em português (como o Windows no Brasil), o Excel usa a vírgula como separador decimal (ex: R$ 10,50). Usar o ponto e vírgula (;) garante que o Excel abra o arquivo dividindo as colunas corretamente de primeira, sem desconfigurar o texto.

## Salvar no formato JSON

Salvar no formato JSON (JavaScript Object Notation) é a melhor opção se você pretende ler esses dados de volta no Python mais tarde ou usá-los em uma aplicação web, pois ele preserva a estrutura de dados (lista de dicionários) perfeitamente.
Para isso, usamos o módulo nativo json do Python.

```python
import json

def salvar_cadastro_json(lista_bicicletas, nome_arquivo="bicicletas.json"):
    """
    Salva uma lista de dicionários contendo o cadastro de bicicletas em um arquivo .json.
    """
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            # indent=4 deixa o arquivo visualmente organizado (com quebras de linha e recuos)
            # ensure_ascii=False garante que acentos (como em 'Vermelho') sejam salvos corretamente
            json.dump(lista_bicicletas, arquivo, indent=4, ensure_ascii=False)
            
        print(f"Cadastro salvo com sucesso em '{nome_arquivo}'!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    minhas_bikes = [
        {"modelo": "Mountain Bike X", "cor": "Preto", "ano": 2024},
        {"modelo": "Speed Pro", "cor": "Vermelho", "ano": 2025},
        {"modelo": "Urbana Vintage", "cor": "Verde Oliva", "ano": 2023}
    ]

    salvar_cadastro_json(minhas_bikes)
```

### Como o arquivo final vai ficar

O arquivo bicicletas.json será gerado exatamente assim, mantendo o formato original do seu código:

```json
[
    {
        "modelo": "Mountain Bike X",
        "cor": "Preto",
        "ano": 2024
    },
    {
        "modelo": "Speed Pro",
        "cor": "Vermelho",
        "ano": 2025
    },
    {
        "modelo": "Urbana Vintage",
        "cor": "Verde Oliva",
        "ano": 2023
    }
]
```

Agora que vimos TXT, CSV e JSON, o que fazer a seguir?

- Criar a função para ler o arquivo JSON de volta para o Python?
- Desenvolver um menu interativo no terminal para cadastrar as bicicletas antes de salvar?
- Adicionar validações (como não permitir anos futuros ou campos vazios)?

## Salvando em um banco de dados SqLite

- Para salvar os dados em um banco de dados SQLite, utilizamos o módulo nativo sqlite3 do Python. Ao contrário dos arquivos de texto, CSV ou JSON, o banco de dados armazena as informações de forma estruturada em uma tabela, permitindo buscas e atualizações muito mais rápidas.
- A abordagem ideal é criar uma função que garanta a existência da tabela antes de inserir os dados, evitando erros caso o banco seja novo.

```python
import sqlite3

def salvar_cadastro_sqlite(lista_bicicletas, nome_banco="bicicletas.db"):
    """
    Salva uma lista de dicionários contendo o cadastro de bicicletas em um banco de dados SQLite.
    """
    conexao = None
    try:
        # Conecta ao arquivo do banco de dados (será criado se não existir)
        conexao = sqlite3.connect(nome_banco)
        cursor = conexao.cursor()
        
        # 1. Cria a tabela caso ela ainda não exista
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bicicletas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                cor TEXT NOT NULL,
                ano INTEGER NOT NULL
            )
        """)
        
        # 2. Prepara o comando SQL de inserção
        # Usamos '?' (placeholders) para evitar vulnerabilidades de SQL Injection
        comando_inserir = "INSERT INTO bicicletas (modelo, cor, ano) VALUES (?, ?, ?)"
        
        # 3. Transforma a lista de dicionários em uma lista de tuplas para inserção em lote
        dados_tuplas = [
            (bike.get('modelo'), bike.get('cor'), bike.get('ano')) 
            for bike in lista_bicicletas
        ]
        
        # Executa a inserção de todas as bicicletas de uma vez só
        cursor.executemany(comando_inserir, dados_tuplas)
        
        # Salva (confirma) as alterações no banco de dados
        conexao.commit()
        print(f"Cadastro de {len(lista_bicicletas)} bicicleta(s) salvo com sucesso no banco '{nome_banco}'!")
        
    except sqlite3.Error as e:
        print(f"Erro no banco de dados SQLite: {e}")
        if conexao:
            conexao.rollback() # Cancela as alterações em caso de erro
            
    finally:
        # Garante que a conexão com o banco será fechada
        if conexao:
            conexao.close()

# --- Exemplo de Uso ---
if __name__ == "__main__":
    minhas_bikes = [
        {"modelo": "Mountain Bike X", "cor": "Preto", "ano": 2024},
        {"modelo": "Speed Pro", "cor": "Vermelho", "ano": 2025},
        {"modelo": "Urbana Vintage", "cor": "Verde Oliva", "ano": 2023}
    ]

    salvar_cadastro_sqlite(minhas_bikes)
```

### 🔍 Vantagens desta abordagem:

- `IF NOT EXISTS`: Você pode rodar o script dezenas de vezes; ele só criará a tabela na primeira execução.
- `executemany`: Insere centenas de registros de uma só vez, o que é infinitamente mais rápido do que fazer um execute dentro de um laço for.
- `commit` e `rollback`: Se ocorrer um erro no meio do salvamento, o rollback garante que o banco não fique com dados corrompidos ou incompletos.

## Para avançar no uso do banco de dados,

- Criar uma função para buscar e listar as bicicletas salvas no SQLite?
- Aprender a fazer filtros (como buscar apenas bicicletas de uma cor específica)?
- Criar uma função para deletar ou atualizar uma bicicleta pelo ID?
