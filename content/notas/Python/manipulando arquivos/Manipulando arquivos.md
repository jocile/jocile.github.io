---
title: Manipulação de Arquivos em Python
description: Este documento sintetiza o conteúdo sobre manipulação de arquivos em
  Python, baseado na apresentação de referência.
date: 2026-10-03
draft: false
tags:
- programadorpythonarquivos
---

Este documento sintetiza o conteúdo sobre manipulação de arquivos em Python, baseado na apresentação de referência.

## Visão Geral

Vamos aprender a importância dos arquivos, como abrir, ler, escrever e gerenciar arquivos em Python, focando nos formatos `.txt` e `.csv`.

## Pré-requisitos
*Liste aqui os pré-requisitos para o tema, desde configurações do ambiente até as noções básicas necessárias para uma melhor assimilação do conteúdo.*

## 1. Introdução

Arquivos são essenciais para persistir dados além da vida útil de um programa.
- **Conceito:** Container para armazenamento de informações em formato digital.
- **Tipos em Python:** Texto e binários.

## 2. Abrindo e Fechando Arquivos

- **Função `open()`:** Necessária para abrir arquivos.
- **Função `close()`:** Necessária para liberar recursos após o uso.
- **Modos de Abertura:**
  - `'r'`: Somente leitura.
  - `'w'`: Gravação.
  - `'a'`: Anexar.

```python
# Abrindo e fechando manualmente
arquivo = open('exemplo.txt', 'w')
arquivo.write('Olá, mundo!')
arquivo.close()
```

## 3. Lendo Arquivos

Métodos disponíveis:
- `read()`: Lê todo o conteúdo.
- `readline()`: Lê uma linha por vez.
- `readlines()`: Retorna uma lista com todas as linhas.

```python
with open('exemplo.txt', 'r') as f:
    conteudo = f.read()
    print(conteudo)
```

## 4. Escrevendo em Arquivos

- Métodos: `write()` ou `writelines()`.
- **Nota:** Certifique-se de abrir o arquivo no modo correto.

```python
with open('exemplo.txt', 'w') as f:
    f.write('Nova linha de texto.\n')
    f.writelines(['Linha 1\n', 'Linha 2\n'])
```

## 5. Gerenciando Arquivos e Diretórios

Utilização dos módulos `os` e `shutil` para criar, renomear e excluir arquivos e diretórios.

```python
import os

# Renomeando um arquivo
os.rename('antigo.txt', 'novo.txt')

# Removendo um arquivo
os.remove('arquivo_para_deletar.txt')
```

## 6. Tratamento de Exceções

Importante para lidar com erros comuns.

```python
try:
    with open('arquivo_inexistente.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('Erro: O arquivo não foi encontrado.')
except PermissionError:
    print('Erro: Permissão negada.')
```

## 7. Boas Práticas

- **Use gerenciamento de contexto (`with`):** Garante que arquivos sejam fechados automaticamente.
- **Verificação:** Verifique se o arquivo foi aberto com sucesso.
- **Codificação:** Sempre especifique o argumento `encoding` no `open()` para garantir a leitura/escrita correta.

```python
# Boa prática: usando 'with' e especificando encoding
with open('dados.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

## 8. Trabalhando com arquivos CSV

Formato amplamente utilizado para dados tabulares.

```python
import csv

# Escrevendo em CSV
with open('dados.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nome', 'Idade'])
    writer.writerow(['Alice', 30])

# Lendo CSV
with open('dados.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for linha in reader:
        print(linha)
```

## Referências

[Apresentação sobre Manipulação de arquivos com Python](https://drive.google.com/file/d/1QIGu_-z1LTd3CY-BDemBxW7sPo_AOTwN/view?usp=sharing)
