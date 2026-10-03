---
title: Manipulação de Arquivos de Texto com Python
description: Este documento contém os conceitos fundamentais sobre leitura e escrita
  de arquivos de texto em Python, estruturado para facilitar a consulta.
date: '2026-10-03'
draft: false
tags:
- arquivos
- automacao
- python
---

Este documento contém os conceitos fundamentais sobre leitura e escrita de arquivos de texto em Python, estruturado para facilitar a consulta.

## Lendo e Escrevendo Arquivos de Texto

O tipo de arquivo mais simples são os arquivos de texto e por isso começaremos com eles.

Antes, precisamos falar de algumas particularidades que podem gerar alguns problemas para nós.

### Quebra de Linhas

Primeiro, as quebras de linha são interpretadas diferentemente entre Windows e Linux/mac. Por exemplo, esse arquivo criado em Windows:

```text
Pug\r\n
Jack Russell Terrier\r\n
English Springer Spaniel\r\n
German Shepherd\r\n
Staffordshire Bull Terrier\r\n
Cavalier King Charles Spaniel\r\n
Golden Retriever\r\n
West Highland White Terrier\r\n
Boxer\r\n
Border Terrier\r\n
```

Será interpretado de forma diferente pelo Linux:

```text
Pug\r
\n
Jack Russell Terrier\r
\n
English Springer Spaniel\r
\n
German Shepherd\r
\n
Staffordshire Bull Terrier\r
\n
Cavalier King Charles Spaniel
Golden Retriever\r
\n
West Highland White Terrier\r
\n
Boxer\r
\n
Border Terrier\r
```

Isso ocorre porque a quebra de linha é indicada de forma diferente entre os dois sistemas.

### Codificação (encoding) de Caracteres

Outro problema comum que você pode enfrentar é a codificação dos dados do byte. Uma codificação é uma tradução de dados de byte para caracteres legíveis por humanos. Isso geralmente é feito atribuindo um valor numérico para representar um caractere. As duas codificações mais comuns são os formatos ASCII e UNICODE. O ASCII pode armazenar apenas 128 caracteres, enquanto o Unicode pode conter até 1.114.112 caracteres.

ASCII é, na verdade, um subconjunto de Unicode (UTF-8), o que significa que ASCII e Unicode compartilham os mesmos valores numéricos para caracteres. É importante observar que a análise de um arquivo com a codificação de caracteres incorreta pode levar a falhas ou deturpação do caractere.

Por exemplo, se um arquivo foi criado usando a codificação UTF-8 e você tentar analisá-lo usando a codificação ASCII, se houver um caractere fora desses 128 valores, um erro será gerado.

Mais sobre: [Unicode (IME-USP)](https://www.ime.usp.br/~pf/algoritmos/apend/unicode.html)

### Abrindo um Arquivo

O Python fornece uma função built-in para a leitura de arquivos, a função `open`:

```python
lista_compras = open('lista_de_compras.txt')
```

É importante lembrar que, sempre que abrimos um arquivo é como se tivéssemos aberto uma planilha no computador. Temos que explicitamente pedir para o Python fechá-lo. Caso contrário, ele ficará aberto e consumindo memória ram do seu programa. É um erro comum esquecer de fechar o arquivo, o que acarreta em diversos problemas no script.

Então vamos aprender a fechar um arquivo:

```python
lista_compras.close()
```

Outra forma mais utilizada (e mais recomendada) é utilizar o `with`.

```python
with open('lista_de_compras.txt') as lista_compras:
    # processamentos do arquivo aqui
```

Nesse caso, ocorre que o objeto criado pela função `open` é armazenado na variável `lista_compras`. A diferença é que quando saímos da indentação do `with`, automaticamente o arquivo é fechado e o objeto deixa de existir. Isso faz com que a variável só exista então dentro do escopo do `with`, e não precisamos portanto utilizar o `close`, garantindo que nosso arquivo esteja aberto apenas quando estamos utilizando ele.

### Modos de abertura de um arquivo

Existem diversos modos nos quais os arquivos podem ser abertos, e fica a cargo do usuário decidir qual se adéqua mais às necessidades do seu código. Por exemplo, utilizando o parâmetro ‘r’, abriremos um arquivo no modo de leitura, não sendo permitido realizar modificações nele.

```python
with open('lista_de_compras.txt', 'r') as lista_compras:
    # processamentos do arquivo aqui
```

Segue uma tabela dos principais modos:

| Caracteres | Significado |
| :--- | :--- |
| 'r' | Modo apenas leitura (padrão) |
| 'r+' | Modo de leitura e escrita |
| 'w' | Modo de escrita, reescreve arquivo caso já exista com o mesmo nome |
| 'a' | Acrescenta a um arquivo sem reescrever conteúdo preexistente |
| 'rb' | Faz a leitura do arquivo em binário |

Para esclarecer melhor:

| Permissão | r | r+ | w | w+ | a | a+ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| leitura | + | + | | + | | + |
| escrita | | + | + | + | + | + |
| cria | | | + | + | + | + |
| sobrescreve | | | + | + | | |
| posição no início | + | + | + | + | | |
| posição no final | | | | | + | + |

- **leitura**: permite a leitura do arquivo
- **escrita**: permite a escrita no arquivo
- **cria**: cria um arquivo novo caso ele não exista
- **sobrescreve**: sobrescreve o arquivo caso ele exista
- **posição no início**: após aberto, a posição inicial da leitura do arquivo é colocada no início
- **posição no final**: após aberto, a posição inicial da leitura do arquivo é colocada no final

### Lendo um arquivo

Existe três métodos principais de se ler um arquivo:

| Método | Uso |
| :--- | :--- |
| `.read()` | Ele lê todo o arquivo de uma só vez |
| `.readline()` | Ele uma linha completa do arquivo |
| `.readlines()` | Lê as linhas remanescentes e retorna como uma lista de linhas |

Utilizando os métodos:

```python
from pathlib import Path
pasta_atual = Path( __file__ ).parent.absolute()

# Exemplo com .read()
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    print(lista_compras.read())

# Exemplo com .readline()
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end='')
        linha = lista_compras.readline()

# Exemplo com .readlines()
with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    print(lista_compras.readlines())
```

### Escrevendo em um arquivo

Existe dois métodos principais de se escrever em um arquivo:

| Método | Uso |
| :--- | :--- |
| `.write(texto)` | Escreve a variável texto (que deve ser uma string) ao arquivo |
| `.writelines(linhas)` | Escreve uma sequência de linhas ao arquivo. Recebe uma lista de valores strings como argumento |

No exemplo a seguir, atualizamos a lista de compras retirando itens que já foram comprados. Primeiro utilizamos o método `write`, que recebe uma string completa como argumento.

```python
itens_ja_comprados = ['ovos', 'leite']

with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    itens_lista_compras = lista_compras.readlines()

with open('lista_de_compras_atualizada.txt', 'w') as lista_atualizada:
    for item in itens_lista_compras:
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)
```

Já no segundo exemplo, utilizamos o método `writelines`, que recebe uma lista de strings como argumento.

```python
itens_ja_comprados = ['ovos', 'leite']

with open(pasta_atual / 'lista_de_compras.txt', 'r') as lista_compras:
    itens_lista_compras = [item for item in lista_compras.readlines() \
    if not item.replace('\n', '') in itens_ja_comprados]

with open('lista_de_compras_atualizada.txt', 'w') as lista_atualizada:
    lista_atualizada.writelines(itens_lista_compras)
```

### Adicionando valores a um arquivo

Por fim, vamos utilizar o método `write` com o arquivo aberto no modo 'a' para fazer uma adição a uma lista. Lembrando, que quando utilizamos o modo 'w', o arquivo original com o mesmo nome é sobrescrito. Já com o modo 'a' (o a vem de *append*, acrescentar do inglês), o arquivo não é sobrescrito e permite que escrevamos mais dados ao arquivo selecionado.

```python
itens_para_adicionar = ['farinha', 'fermento']

with open(pasta_atual / 'lista_de_compras.txt', 'a') as lista_compras:
    for item in itens_para_adicionar:
        lista_compras.write(f'\n{item}')
```

Note que temos que adicionar o `‘\n’` para garantir a quebra de linha!
