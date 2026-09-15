---
title: 2023 04 13 Intoducao A Funcoes
description: Conhecidas pelo nome de sub-rotina, as funções possuem um nome e, como
  sua própria denominação sugere, realizam uma função específica. No entanto, uma
  função…
date: '2026-09-14'
draft: false
tags:
- exercícios
- lógica
- programador
- programação
- python
- senac
---

Conhecidas pelo nome de sub-rotina, as funções possuem um nome e, como sua própria denominação sugere, realizam uma função específica. No entanto, uma função pode ser comparada a um programa completo. Como vimos anteriormente, um programa contém entrada, processamento e saída, e o mesmo pode ocorrer com uma função. Por exemplo, uma função pode receber uma frase, realizar um processamento interno para a contagem de vogais e retornar a quantidade de vogais existentes nessa frase.

## Funcionamento

Em Python, uma função é definida usando a palavra-chave "def" seguida do nome da função e seus parâmetros. A definição da função é seguida por um bloco de código indentado que define as instruções que a função executará.

Por exemplo, vamos criar uma função simples que adiciona dois números e retorna o resultado:

```python
def add_numbers(a, b):
    result = a + b
    return result
```

Neste exemplo, a função **`add_numbers`** recebe dois parâmetros **`a`** e **`b`**. O bloco de código da função adiciona esses dois parâmetros e armazena o resultado na variável **`result`**, que é então retornada pela função.

Podemos chamar a função **`add_numbers`** passando dois argumentos:

```python
x = add_numbers(3, 5)
print(x)
```

Neste exemplo, estamos passando os valores **`3`** e **`5`** para a função **`add_numbers`**. A função executa a operação de adição e retorna o resultado **`8`**, que é armazenado na variável **`x`**. Em seguida, usamos a função **`print()`** para exibir o valor armazenado em **`x`**.

Além de receber parâmetros e retornar valores, as funções em Python também podem ter variáveis locais e globais. Variáveis locais são definidas dentro do escopo da função e só podem ser acessadas dentro da função, enquanto as variáveis globais são definidas fora da função e podem ser acessadas de qualquer lugar no código.

Por exemplo, vamos modificar nossa função **`add_numbers`** para usar uma variável global:

```python
global_var = 10

def add_numbers(a, b):
    local_var = 5
    result = a + b + global_var + local_var
    return result
```

Neste exemplo, estamos definindo uma variável global **`global_var`** fora da função **`add_numbers`**. Dentro da função, também estamos definindo uma variável local **`local_var`**. O bloco de código da função adiciona os parâmetros **`a`** e **`b`**, a variável global **`global_var`** e a variável local **`local_var`** e retorna o resultado.

Podemos chamar a função **`add_numbers`** da mesma forma que fizemos anteriormente:

```python
x = add_numbers(3, 5)
print(x)
```

Neste exemplo, a função **`add_numbers`** adiciona os valores **`3`** e **`5`** aos valores das variáveis global e local (**`10`** e **`5`**, respectivamente) e retorna o resultado **`23`**, que é armazenado na variável **`x`** e, em seguida, exibido com a função **`print()`**.

Em resumo, funções em Python permitem encapsular blocos de código em unidades reutilizáveis que recebem parâmetros e retornam valores. Essa funcionalidade é muito útil para reduzir a complexidade do código, tornando-o mais modular e fácil de ler e manter.

## Exercícios

1. Criar uma função que calcule o fatorial de um número inteiro.
2. Criar uma função que receba uma lista de números e retorne a soma de todos os números pares.
3. Criar uma função que receba uma string e retorne a mesma string invertida.
4. Criar uma função que receba uma lista de números e retorne o maior e o menor número da lista.
5. Criar uma função que receba uma lista de strings e retorne uma nova lista com todas as strings maiúsculas.
6. Cria um menu de opções para acessar cada função anterior.

## Resolução

### 1. fatorial de um número inteiro

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
```

### 2. soma de todos os números pares

```python
def soma_pares(lista):
    total = 0
    for numero in lista:
        if numero % 2 == 0:
            total += numero
    return total
```

### 3. texto invertido

```python
def inverte_string(string):
    return string[::-1]
```

### 4. maior e o menor número

```python
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor
```

### 5. retornar texto em maiúsculo

```python
def maiusculas(lista):
    nova_lista = []
    for string in lista:
        nova_lista.append(string.upper())
    return nova_lista
```

### 6. menu de opções para as funções

```python
while True:
    print("Selecione uma opção:")
    print("1. Calcular o fatorial de um número")
    print("2. Calcular a soma de números pares em uma lista")
    print("3. Inverter uma string")
    print("4. Encontrar o maior e o menor número em uma lista")
    print("5. Transformar uma lista de strings em maiúsculas")
    print("0. Sair")

    opcao = int(input("Opção selecionada: "))

    if opcao == 1:
        numero = int(input("Digite um número: "))
        resultado = fatorial(numero)
        print("O fatorial de {} é {}".format(numero, resultado))
    elif opcao == 2:
        lista = input("Digite uma lista de números separados por vírgula: ").split(",")
        lista = [int(numero) for numero in lista]
        resultado = soma_pares(lista)
        print("A soma dos números pares na lista é {}".format(resultado))
    elif opcao == 3:
        string = input("Digite uma string: ")
        resultado = inverte_string(string)
        print("A string invertida é: {}".format(resultado))
    elif opcao == 4:
        lista = input("Digite uma lista de números separados por vírgula: ").split(",")
        lista = [int(numero) for numero in lista]
        maior, menor = maior_menor(lista)
        print("O maior número na lista é {} e o menor é {}".format(maior, menor))
    elif opcao == 5:
        lista = input("Digite uma lista de strings separadas por vírgula: ").split(",")
        resultado = maiusculas(lista)
        print("A lista de strings em maiúsculas é: {}".format(resultado))
    elif opcao == 0:
        break
    else:
        print("Opção inválida. Tente novamente.")
```

## Referência

Furgeri, Sérgio
Introdução à programação em Python - cap. 6
E-book. Disponível em: [https://bibliotecadigitalsenac.com.br/?from=%3FcontentInfo%3D3011#/legacy/epub/3011](https://bibliotecadigitalsenac.com.br/?from=%3FcontentInfo%3D3011#/legacy/epub/3011)
Acesso em 14/04/2023
