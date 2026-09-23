---
title: "Funções em Python"
date: 2026-09-23
draft: false
tags:
  - python
  - funcoes
  - programacao
description: "Guia sobre como definir, usar e documentar funções em Python, incluindo tipos de parâmetros e escopo."
---

Entender como definir e usar funções em Python é fundamental para escrever código claro, eficiente e reutilizável. As funções permitem a modularização do seu programa, facilitando a manutenção, organização e a expansão do código. Elas recebem dados através dos parâmetros, processam e retornam a informação.

## Tabela de parâmetros de funções

Tabela organizada com as diferentes formas de passagem de parâmetros em funções Python:

| **Tipo de Passagem de Parâmetros**        | **Descrição**                                   | **Exemplo**                                                                                                                                                                                                                            | **Saída**                                                                   |
| ----------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Parâmetros Posicionais**                | Passados na ordem definida.                     | `def exibir_informacoes(nome, idade):`<br>  `print(f"Nome: {nome}, Idade: {idade}")`<br>`exibir_informacoes("Maria", 30)`                                                                                                              | Nome: Maria, Idade: 30                                                      |
| **Parâmetros Nomeados**                   | Especificados pelo nome, independente da ordem. | `def exibir_informacoes(nome, idade):`<br>    `print(f"Nome: {nome}, Idade: {idade}")`<br>`exibir_informacoes(idade=30, nome="Maria")`                                                                                    | Nome: Maria, Idade: 30                                                      |
| **Parâmetros com Valores Padrão**         | Parâmetros com valores definidos por padrão.    | `def exibir_informacoes(nome, idade=25):`<br>    `print(f"Nome: {nome}, Idade: {idade}")`<br>`exibir_informacoes("Carlos")`<br>`exibir_informacoes("Ana", 22)`                                                          | Nome: Carlos, Idade: 25`<br>Nome: Ana, Idade: 22                            |
| **Parâmetros Arbitrários \(*args\)**      | Aceita múltiplos argumentos posicionais.        | `def listar_nomes(*nomes):`<br>    `for nome in nomes:`<br>        `print(nome)`<br>`listar_nomes("Ana", "Carlos", "Beatriz")`                                                                                                  | Ana`<br>Carlos`<br>Beatriz                                                  |
| **Parâmetros Arbitrários \(**kwargs\)**   | Aceita múltiplos argumentos nomeados.           | `def exibir_detalhes(**detalhes):`<br>    `for chave, valor in detalhes.items():`<br>        `print(f"{chave}: {valor}")`<br>`exibir_detalhes(nome="Ana", idade=25, cidade="Fortaleza")`                                          | nome: Ana`<br>idade: 25`<br>cidade: Fortaleza                               |
| **Passagem por Referência (Mutáveis)**    | Objetos mutáveis são passados por referência.   | `def adicionar_elemento(lista):`<br>    `lista.append(4)`<br>    `print(f"Lista dentro da função: {lista}")`<br>`minha_lista = [1, 2, 3]`<br>`adicionar_elemento(minha_lista)`<br>`print(f"Lista fora da função: {minha_lista}")` | Lista dentro da função: [1, 2, 3, 4]`<br>Lista fora da função: [1, 2, 3, 4] |
| **Passagem por Valor (Imutáveis)**        | Objetos imutáveis são passados por valor.       | `def incrementar_numero(numero):`<br>    `numero += 1`<br>    `print(f"Número dentro da função: {numero}")`<br>`meu_numero = 10`<br>`incrementar_numero(meu_numero)`<br>`print(f"Número fora da função: {meu_numero}")`           | Número dentro da função: 11`<br>Número fora da função: 10                   |
| **Desempacotamento de Argumentos \(*\)**  | Desempacota argumentos posicionais.             | `def exibir_informacoes(nome, idade):`<br>    `print(f"Nome: {nome}, Idade: {idade}")`<br>`dados = ("João", 28)`<br>`exibir_informacoes(*dados)`                                                                              | Nome: João, Idade: 28                                                       |
| **Desempacotamento de Argumentos \(**\)** | Desempacota argumentos nomeados.                | `def exibir_informacoes(nome, idade):`<br>    `print(f"Nome: {nome}, Idade: {idade}")`<br>`detalhes = {"nome": "Maria", "idade": 30}`<br>`exibir_informacoes(**detalhes)`                                                        | Nome: Maria, Idade: 30                                                      |


A tabela acima resume as diversas maneiras de passar parâmetros em funções Python, destacando a flexibilidade e a versatilidade oferecidas por essa linguagem para manipular dados dentro de funções. Compreender essas técnicas é crucial para escrever código eficiente e reutilizável.

## Como usar funções em Python

As funções são blocos de código reutilizáveis que permitem estruturar seu programa de forma modular e eficiente. Em Python, as funções são definidas usando a palavra-chave `def`, seguidas por um nome de função, parênteses que podem conter parâmetros e dois pontos. Vamos explorar como criar e usar funções em Python através dos seguintes tópicos:

### 1. Definição de Funções

Para definir uma função, você usa a estrutura básica a seguir:

```python
def nome_da_funcao(parametros):
    # Bloco de código
    return valor_de_retorno
```

**Exemplo:**

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

### 2. Chamando Funções

Depois de definir uma função, você pode chamá-la em qualquer lugar do seu código utilizando o nome da função seguido por parênteses contendo argumentos, se houver.

**Exemplo:**

```python
mensagem = saudacao("Maria")
print(mensagem)  # Saída: Olá, Maria!
```

### 3. Funções com Parâmetros Padrão

Você pode definir valores padrão para os parâmetros de uma função. Isso permite que a função seja chamada com menos argumentos do que os parâmetros definidos.

**Exemplo:**

```python
def saudacao(nome="Visitante"):
    return f"Olá, {nome}!"

print(saudacao())         # Saída: Olá, Visitante!
print(saudacao("João"))   # Saída: Olá, João!
```

### 4. Funções com Vários Parâmetros

Uma função pode ter múltiplos parâmetros, separados por vírgulas.

**Exemplo:**

```python
def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  # Saída: 7
```

### 5. Funções com Número Variável de Argumentos

Para aceitar um número variável de argumentos, use `*args` para argumentos posicionais e `**kwargs` para argumentos nomeados.

**Exemplo:**

```python
def listar_nomes(*nomes):
    for nome in nomes:
        print(nome)

listar_nomes("Ana", "Carlos", "Beatriz")  # Saída: Ana\nCarlos\nBeatriz

def exibir_detalhes(**detalhes):
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")

exibir_detalhes(nome="Ana", idade=25, cidade="Fortaleza")  # Saída: nome: Ana\nidade: 25\ncidade: Fortaleza
```

### 6. Funções Lambda

As funções lambda são funções anônimas, usadas para operações simples e rápidas. Elas são definidas usando a palavra-chave `lambda`.

**Exemplo:**

```python
soma = lambda a, b: a + b
print(soma(5, 3))  # Saída: 8
```

### 7. Documentando Funções

É uma boa prática documentar suas funções para descrever o que elas fazem, os parâmetros que aceitam e o valor de retorno. Isso é feito usando strings de documentação (docstrings).

**Exemplo:**

```python
def saudacao(nome):
    """
    Retorna uma mensagem de saudação para o nome fornecido.

    Parâmetros:
    nome (str): O nome da pessoa a ser saudada.

    Retorna:
    str: Uma mensagem de saudação.
    """
    return f"Olá, {nome}!"
```

### 8. Escopo de Variáveis em Funções

As variáveis definidas dentro de uma função têm escopo local, ou seja, só existem dentro da função.

**Exemplo:**

```python
def teste_escopo():
    variavel_local = "Eu existo apenas dentro desta função"
    print(variavel_local)

teste_escopo()
# print(variavel_local)  # Isso causará um erro, pois a variável não é acessível fora da função
```

> [!NOTE] 
> Pratique criando suas próprias funções e explorando diferentes tipos de parâmetros para se familiarizar com essas ferramentas poderosas.

## Como são as Passagens de Parâmetros nas Funções em Python

As passagens de parâmetros nas funções em Python podem ser realizadas de várias maneiras, oferecendo flexibilidade para que suas funções sejam tão simples ou complexas quanto necessário. Vamos explorar os diferentes métodos de passagem de parâmetros e suas nuances.

### 1. Parâmetros Posicionais

Os parâmetros posicionais são passados para a função na ordem em que são definidos.

**Exemplo:**

```python
def exibir_informacoes(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exibir_informacoes("Maria", 30)  # Saída: Nome: Maria, Idade: 30
```

### 2. Parâmetros Nomeados

Os parâmetros nomeados permitem especificar os argumentos por nome, independentemente da ordem.

**Exemplo:**

```python
def exibir_informacoes(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

exibir_informacoes(idade=30, nome="Maria")  # Saída: Nome: Maria, Idade: 30
```

### 3. Parâmetros com Valores Padrão

Parâmetros com valores padrão são usados quando um valor padrão é desejado caso nenhum argumento seja fornecido.

**Exemplo:**

```python
def exibir_informacoes(nome, idade=25):
    print(f"Nome: {nome}, Idade: {idade}")

exibir_informacoes("Carlos")  # Saída: Nome: Carlos, Idade: 25
exibir_informacoes("Ana", 22)  # Saída: Nome: Ana, Idade: 22
```

### 4. Parâmetros Arbitrários: *args e **kwargs

Para permitir que uma função aceite um número variável de argumentos, usamos `*args` e `**kwargs`.

**Exemplo com *args:**

```python
def listar_nomes(*nomes):
    for nome in nomes:
        print(nome)

listar_nomes("Ana", "Carlos", "Beatriz")  # Saída: Ana\nCarlos\nBeatriz
```

**Exemplo com **kwargs:**

```python
def exibir_detalhes(**detalhes):
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")

exibir_detalhes(nome="Ana", idade=25, cidade="Fortaleza")  # Saída: nome: Ana\nidade: 25\ncidade: Fortaleza
```

### 5. Passagem por Referência vs. Passagem por Valor

Em Python, a passagem de argumentos funciona por referência para objetos mutáveis (como listas e dicionários) e por valor para objetos imutáveis (como inteiros e strings).

**Exemplo com objetos mutáveis:**

```python
def adicionar_elemento(lista):
    lista.append(4)
    print(f"Lista dentro da função: {lista}")

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista)
print(f"Lista fora da função: {minha_lista}")  # Saída: Lista fora da função: [1, 2, 3, 4]
```

**Exemplo com objetos imutáveis:**

```python
def incrementar_numero(numero):
    numero += 1
    print(f"Número dentro da função: {numero}")

meu_numero = 10
incrementar_numero(meu_numero)
print(f"Número fora da função: {meu_numero}")  # Saída: Número fora da função: 10
```

### 6. Desempacotamento de Argumentos

Você pode usar o operador de desempacotamento `*` para argumentos posicionais e `**` para argumentos nomeados ao chamar uma função.

**Exemplo:**

```python
def exibir_informacoes(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

dados = ("João", 28)
exibir_informacoes(*dados)  # Saída: Nome: João, Idade: 28

detalhes = {"nome": "Maria", "idade": 30}
exibir_informacoes(**detalhes)  # Saída: Nome: Maria, Idade: 30
```

> [!NOTE] 
> A passagem de parâmetros em funções Python é versátil, permitindo uma grande flexibilidade na forma como as funções são chamadas e como os dados são manipulados dentro delas. Compreender as diferentes maneiras de passar parâmetros permitirá que você escreva funções mais robustas e reutilizáveis, aprimorando a qualidade e a eficiência do seu código.
