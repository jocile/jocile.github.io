---
title: uc1.02 - Variáveis, constantes e primeiros programas em Python
date: 2026-11-27
draft: false
tags:
  - logica/aulas/uc1
  - python/variaveis
  - senac
description: Variáveis, constantes e tipos de dados, e os primeiros programas em Python no Google Colab com input, atribuição e print, usando o caixa de uma cantina.
uc: 1
aula: 2
---

> [!abstract] Resumo da aula
> Nesta aula, a turma descobre que um programa precisa **guardar informações** para trabalhar com elas. Partimos do caixa de uma cantina, aprendemos o que são variáveis, constantes e tipos de dados e escrevemos os primeiros programas em Python no Google Colab, com entrada, atribuição e saída.

Na [[uc1.01 - Introducao a logica e algoritmos|Aula 1]], vimos que um algoritmo é uma sequência de passos e executamos um script que criava pastas e arquivos. Agora o programa passa a **guardar e usar valores**.

## O caso da cantina: o que o caixa precisa saber?

A cantina da escola quer informatizar o caixa. Antes de programar, calculamos em papel o **total** e o **troco** de três pedidos e listamos que informações o caixa precisa guardar para fazer a conta.

| Pedido | Itens | Valor pago |
|---|---|---|
| A | 2 salgados a R\$ 6,50 e 1 suco a R\$ 5,00 | R\$ 20,00 |
| B | 3 pães de queijo a R\$ 4,00 e 1 café a R\$ 3,50 | R\$ 15,00 |
| C | 2 almoços a R\$ 18,90 | R\$ 40,00 |

> [!success]- Respostas
> - **A**: total R\$ 18,00 e troco R$ 2,00.
> - **B**: total R\$ 15,50, e o valor pago não é suficiente (faltam R\$ 0,50).
> - **C**: total R\$ 37,80 e troco R\$ 2,20.

Algumas informações mudam de um pedido para outro (itens, quantidades, valor pago) e outras não. O programa precisa de um lugar para guardar cada uma. Esse lugar é a **variável**.

## Variáveis

> [!info] Variável
> Uma **variável** é um espaço da memória com um **nome** que guarda um **valor**. O valor pode mudar durante a execução do programa. Assim como uma pasta tem um nome, uma variável também tem.

Em Python, usamos o sinal `=` para **atribuir** um valor a uma variável. Lê-se "recebe": `preco = 6.50` significa "preco recebe 6,50".

```python
nome = "Ana"
idade = 17
preco = 6.50
pagou = False
print(nome, idade, preco, pagou)
```

Saída: `Ana 17 6.5 False`

### Cuidado: variável guarda uma cópia do valor

Antes de executar, tente prever o que o programa mostra:

```python
x = 3
y = x
x = 10
print(x, y)
```

> [!success]- Resposta
> Mostra `10 3`. O comando `y = x` copia o valor de `x` naquele momento. Depois, mudar `x` não altera `y`.

## Constantes

> [!info] Constante
> Uma **constante** é um valor que não deve mudar durante o programa, como a taxa de serviço de uma cantina.

Em Python, a constante é uma **convenção**: escrevemos o nome em maiúsculas. A linguagem não impede a alteração, mas quem lê o código entende que aquele valor não deve mudar.

```python
TAXA_SERVICO = 0.10
```

## Tipos de dados

Todo valor tem um **tipo**, que diz o que ele representa e o que se pode fazer com ele. Na aula 1, a extensão (`.txt`, `.bat`) dizia o tipo de um arquivo. Com os valores é parecido.

| Tipo | Nome em Python | Exemplo | Uso |
|---|---|---|---|
| Inteiro | `int` | `17` | Quantidades, idades |
| Real | `float` | `6.50` | Preços, médias |
| Texto | `str` | `"Ana"` | Nomes, mensagens |
| Lógico | `bool` | `True` ou `False` | Verdadeiro ou falso |

Para ver o tipo de um valor, use `type()`:

```python
print(type(6.50))
```

Saída: `<class 'float'>`

> [!warning] Número decimal usa ponto
> Em Python, escrevemos `6.50` e não `6,50`.

## Nomes de variáveis

- Escolha nomes que expliquem o conteúdo: `preco_salgado` é melhor que `x`.
- Não use espaços. Use o sublinhado: `valor_pago`.
- Não comece o nome com número: `1nome` dá erro.
- Maiúsculas e minúsculas fazem diferença: `nome` e `Nome` são variáveis diferentes.

## Entrada, atribuição e saída

Um programa útil recebe dados, guarda em variáveis e mostra um resultado.

- `input()` lê o que o usuário digita (**entrada**).
- `=` guarda o valor em uma variável (**atribuição**).
- `print()` mostra um valor na tela (**saída**).

```python
nome = input("Qual o seu nome? ")
print("Olá,", nome)
```

### O `input()` sempre devolve texto

Se o usuário digitar `17`, o `input()` devolve o **texto** `"17"`, e não o número. Por isso o código abaixo dá erro:

```python
idade = input("Idade: ")
print(idade + 1)
```

```
TypeError: can only concatenate str (not "int") to str
```

Para usar o valor como número, **converta** com `int()` (inteiro) ou `float()` (real):

```python
idade = int(input("Idade: "))
print(idade + 1)
```

## Teste de mesa

O **teste de mesa** é acompanhar, no papel, o valor de cada variável depois de cada linha, como se você fosse o computador. Veja o exemplo de `x` e `y`:

| Linha executada | x | y |
|---|---|---|
| `x = 3` | 3 | |
| `y = x` | 3 | 3 |
| `x = 10` | 10 | 3 |

Com o teste de mesa, descobrimos o valor das variáveis sem precisar executar o programa.

## Pratique no Colab

Use o notebook da aula no Google Colab ([[Python com Colab]]). Comece pelo nível que preferir e avance quando concluir.

> [!todo] Nível 1: completar o código
> ```python
> nome = input("Nome: ")
> idade = ______(input("Idade: "))
> print("Olá,", ______)
> print("Você tem", ______, "anos")
> ```

> [!todo] Nível 2: total do pedido
> Escreva um programa que receba o **preço** e a **quantidade** de um item e mostre o **total** do pedido.

> [!success]- Possível solução do nível 2
> ```python
> preco = float(input("Preço do item: "))
> quantidade = int(input("Quantidade: "))
> total = preco * quantidade
> print("Total:", total)
> ```

> [!todo] Nível 3: pedido com dois itens
> Peça o **nome do cliente** e o preço e a quantidade de **dois itens**. Mostre uma linha com o nome do cliente e o total. Use nomes claros e uma constante para um valor que não muda.

Depois, troque de programa com um colega: **preveja a saída** do programa dele para o pedido A (preço 6.50 e quantidade 2), execute e compare com o cálculo que você fez em papel.

## Erros comuns

- Usar vírgula como separador decimal (`6,50`). Em Python é ponto, e `float("6,50")` dá `ValueError`.
- Esquecer as aspas no texto (`nome = Ana`) ou os parênteses do `input()`.
- Calcular com o valor do `input()` sem converter para número.
- Escolher nomes com espaço (`preco total`).
- Achar que `y = x` faz `y` acompanhar as mudanças de `x`.

> [!tip] Erro é pista
> Leia a mensagem de erro do Python: ela diz o tipo do problema e em que linha ele aconteceu. Ler a mensagem é a primeira técnica de quem programa.

## Para revisar

> [!question] Perguntas
> 1. Qual a diferença entre variável e constante?
> 2. Quais são os quatro tipos básicos vistos na aula? Dê um exemplo de cada.
> 3. Que tipo de valor o `input()` devolve? Como transformá-lo em número inteiro?
> 4. Depois de `x = 3`, `y = x` e `x = 10`, qual é o valor de `y`?
>
> > [!success]- Respostas
> > 1. A variável pode mudar de valor. A constante não deve mudar (em Python, é uma convenção com nome em maiúsculas).
> > 2. `int` (17), `float` (6.50), `str` ("Ana") e `bool` (`True`).
> > 3. Texto (`str`). Para inteiro, usa-se `int(input(...))`.
> > 4. `y` vale 3.

## Próxima aula

Na próxima aula, vamos **calcular** com o que foi guardado: expressões aritméticas e lógicas, para descobrir o total e o troco do pedido e se o cliente pagou o suficiente.
