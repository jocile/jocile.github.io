---
title: Arquivos txt com Python
description: A manipulação de arquivos é crucial para a programação, pois permite armazenar e recuperar dados, tornando-os persistentes além da vida útil de um programa…
date: '2026-09-17'
draft: false
tags:
  - programador/Python/arquivos
---

A manipulação de arquivos é crucial para a programação, pois permite armazenar e recuperar dados, tornando-os persistentes além da vida útil de um programa específico.

## 1. Introdução à Manipulação de Arquivos

Os arquivos são containers no computador onde as informações são armazenadas em formato digital. Podemos manipular dois tipos principais de arquivos em Python: arquivos de texto e arquivos binários.

## 2. Abrindo e Fechando Arquivos

Para manipular arquivos em Python, primeiro precisamos abri-los usando a função `open()`. Ao terminar, usamos a função `close()` para liberar recursos.

### Modos de Abertura de Arquivo

- `r`: Somente leitura.
- `w`: Gravação (sobrescreve o arquivo).
- `a`: Anexar (adiciona ao final do arquivo).

**Exemplo de Código:**

```python
arquivo = open('exemplo.txt', 'r')
# Fechando o arquivo
arquivo.close()
```

## 3. Lendo de um Arquivo

Python fornece várias maneiras de ler um arquivo:

- `read()`: Lê o conteúdo inteiro.

```py
# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "/home/usuario/Projetos/estudando-python/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()
```

- `readline()`: Lê uma linha por vez.

```py
arquivo = open(
    "/home/usuario/Projetos/estudando-python/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

```

- `readlines()`: Retorna uma lista onde cada elemento é uma linha do arquivo.

```python
arquivo = open(
    "/home/usuario/Projetos/estudando-python/05 - Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()
```

Usando loop:

```py
arquivo = open(
    "/home/usuario/Projetos/estudando-python/05 - Manipulação de arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
```

## 4. Escrevendo em um Arquivo

Para escrever em um arquivo, utilizamos `write()` ou `writelines()`, lembrando de abrir o arquivo no modo correto.

**Exemplo de Código:**

```python
arquivo = open(
    "/home/usuario/Projetos/estudando-python/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
```

## Exemplo

Vamos criar um exemplo completo que envolve a criação de um arquivo `txt`, a escrita de uma lista de itens nele, e a leitura dos itens posteriormente.

### Passo 1: Criando e Escrevendo em um Arquivo TXT

Primeiro, vamos criar uma lista de itens e escrever cada item em um novo arquivo `lista_compras.txt`.

**Exemplo de Código:**

```python
# Lista de itens
lista_compras = ["Maçã", "Banana", "Leite", "Pão", "Ovos"]

# Abrindo o arquivo no modo de escrita
with open('lista_compras.txt', 'w') as arquivo:
    # Escrevendo cada item da lista em uma nova linha do arquivo
    for item in lista_compras:
        arquivo.write(item + '\n')

print("Lista de compras salva com sucesso em 'lista_compras.txt'.")
```

### Passo 2: Lendo de um Arquivo TXT

Agora, vamos ler o conteúdo do arquivo `lista_compras.txt` e exibir cada item.

**Exemplo de Código:**

```python
# Abrindo o arquivo no modo de leitura
with open('lista_compras.txt', 'r') as arquivo:
    # Lendo todas as linhas do arquivo
    linhas = arquivo.readlines()

# Exibindo cada item da lista de compras
print("Itens da lista de compras:")
for linha in linhas:
    print(linha.strip())
```

### Explicação do Código

1. **Escrita no Arquivo TXT:**
   - Criamos uma lista chamada `lista_compras` com alguns itens.
   - Abrimos o arquivo `lista_compras.txt` no modo de escrita (`'w'`). Se o arquivo não existir, ele será criado. Se já existir, seu conteúdo será sobrescrito.
   - Usamos um loop `for` para iterar sobre cada item da lista e escrevê-los no arquivo, adicionando um caractere de nova linha (`'\n'`) após cada item.
   - O bloco `with` garante que o arquivo será fechado corretamente após a escrita.

2. **Leitura do Arquivo TXT:**
   - Abrimos o arquivo `lista_compras.txt` no modo de leitura (`'r'`).
   - Utilizamos o método `readlines()` para ler todas as linhas do arquivo e armazená-las em uma lista chamada `linhas`.
   - Iteramos sobre a lista `linhas` e usamos `strip()` para remover o caractere de nova linha (`'\n'`) ao exibir cada item.

### Conclusão

Este exemplo ilustra como podemos criar e manipular arquivos de texto em Python para armazenar e recuperar dados. Essa técnica é fundamental para diversas aplicações, desde a simples persistência de dados até a manipulação de grandes volumes de informações em projetos mais complexos. Experimente adaptar este exemplo às suas necessidades específicas e explore outras funcionalidades da manipulação de arquivos em Python.

#programador/Python/arquivos
