---
title: Arquivos e pastas com Python
description: Python oferece funções para criar, renomear e excluir arquivos e diretórios usando os módulos os e shutil.
date: '2026-09-17'
draft: false
tags:
  - programador/Python/arquivos
---

Python oferece funções para criar, renomear e excluir arquivos e diretórios usando os módulos `os` e `shutil`.

**Exemplo de Código:**

```python
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
```

## Tratamento de Exceções em Manipulação de Arquivos

Lidar com erros é essencial ao manipular arquivos. Python oferece diversas exceções para tratar erros comuns:

- `FileNotFoundError`: Arquivo não encontrado.
- `PermissionError`: Permissão insuficiente.
- `IOError`: Erro de E/S geral.
- `UnicodeDecodeError`: Erro de decodificação.
- `UnicodeEncodeError`: Erro de codificação.
- `IsADirectoryError`: Tentativa de abrir um diretório.

**Exemplo de Código:**

```python
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
```

## Boas Práticas na Manipulação de Arquivos

- **Gerenciamento de Contexto:** Use `with` para garantir que os arquivos sejam fechados corretamente, mesmo em caso de exceções.

**Exemplo de Código:**

```python
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
```

- **Verificação de Abertura de Arquivo:** Certifique-se de que o arquivo foi aberto corretamente antes de realizar operações de leitura ou gravação.
- **Uso da Codificação Correta:** Especifique a codificação ao abrir arquivos de texto.

## Exemplo

Vamos ampliar nosso exemplo para incluir a criação de pastas e arquivos. Neste exemplo, criaremos uma estrutura de diretórios para organizar nossos arquivos de lista de compras. Vamos criar uma pasta chamada `listas` e dentro dela, criaremos o arquivo `lista_compras.txt`.

### Passo 1: Criando Pastas e Arquivos

Primeiro, vamos criar uma pasta e depois criar um arquivo dentro dela, escrevendo nossa lista de compras nesse arquivo.

**Exemplo de Código:**

```python
import os

# Diretório onde queremos salvar o arquivo
diretorio = 'listas'

# Verificando se o diretório já existe, caso contrário, criando-o
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Caminho completo do arquivo dentro do diretório criado
caminho_arquivo = os.path.join(diretorio, 'lista_compras.txt')

# Lista de itens
lista_compras = ["Maçã", "Banana", "Leite", "Pão", "Ovos"]

# Abrindo o arquivo no modo de escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrevendo cada item da lista em uma nova linha do arquivo
    for item in lista_compras:
        arquivo.write(item + '\n')

print(f"Lista de compras salva com sucesso em '{caminho_arquivo}'.")
```

### Passo 2: Lendo de um Arquivo Dentro de uma Pasta

Agora, vamos ler o conteúdo do arquivo `lista_compras.txt` dentro da pasta `listas` e exibir cada item.

**Exemplo de Código:**

```python
# Caminho completo do arquivo dentro do diretório
caminho_arquivo = os.path.join(diretorio, 'lista_compras.txt')

# Abrindo o arquivo no modo de leitura
with open(caminho_arquivo, 'r') as arquivo:
    # Lendo todas as linhas do arquivo
    linhas = arquivo.readlines()

# Exibindo cada item da lista de compras
print("Itens da lista de compras:")
for linha in linhas:
    print(linha.strip())
```

### Explicação do Código

1. **Criação do Diretório:**
   - Importamos o módulo `os` que contém funções para interagir com o sistema operacional.
   - Definimos o nome do diretório onde queremos salvar nosso arquivo (`'listas'`).
   - Usamos `os.path.exists()` para verificar se o diretório já existe. Se não existir, `os.makedirs()` é usado para criá-lo.

2. **Criação do Arquivo Dentro do Diretório:**
   - Criamos o caminho completo do arquivo combinando o nome do diretório e o nome do arquivo usando `os.path.join()`.
   - Criamos uma lista de itens chamada `lista_compras`.
   - Abrimos o arquivo no modo de escrita (`'w'`) e escrevemos cada item da lista no arquivo, adicionando um caractere de nova linha (`'\n'`) após cada item.

3. **Leitura do Arquivo Dentro do Diretório:**
   - Reutilizamos o caminho completo do arquivo criado anteriormente.
   - Abrimos o arquivo no modo de leitura (`'r'`).
   - Usamos `readlines()` para ler todas as linhas do arquivo e armazená-las em uma lista chamada `linhas`.
   - Iteramos sobre a lista `linhas` e usamos `strip()` para remover o caractere de nova linha (`'\n'`) ao exibir cada item.

### Conclusão

Este exemplo demonstra como criar e organizar arquivos dentro de diretórios utilizando Python. A criação de pastas e a manipulação de arquivos dentro dessas pastas é uma técnica essencial para organizar dados e manter uma estrutura de armazenamento limpa e eficiente. Experimente adaptar este exemplo para criar estruturas de diretórios mais complexas e manipular diferentes tipos de arquivos conforme suas necessidades.

#programador/Python/arquivos
