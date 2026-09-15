---
title: 2023 03 29 Expressoes Com Literais
description: São expressões com constantes e/ou variáveis literais que têm como resultado
  valores literais. Diferentemente das expressões aritméticas, as expressões…
date: '2026-09-14'
draft: false
tags:
- exercícios
- lógica
- portugol
- programador
- programação
- senac
---

São expressões com constantes e/ou variáveis literais que têm como resultado valores literais. Diferentemente das expressões aritméticas, as expressões literais aceitam somente o operador de concatenação.

Resolver expressões literais obtendo um caractere ou um conjunto de caracteres.

```plaintext
		Problema
		Sendo X, Y e Z as variáveis literais, qual o resultado de cada variável no final do algoritmo?
		início
		X,  Z, Y: literal
		X ← " Banana"
		Z ← X + "da"
		Y ← "A " + Z + " é feita de " + X + "."
		fim
		Solucionando o problema
			1.	Separe as expressões do algoritmo.
		X ← "  Banana"
		Z ← X + "da"
		Y ← "A" + Z + " é feita de" + X + "."
			2.	O resultado da variável X é o valor Banan...

```

Resolução em Portugol:

```plaintext
programa {
/*
início
			X,  Z, Y: literal
			X ← “ Banana”
			Z ← X + “da”
			Y ← “A “ + Z + “ é feita de “ + X + “.”
			fim
  */
  cadeia x, y, z
  funcao inicio() {
    x = "Banana"
    z = x + "da"
    y = "A " + z + " é feita de " + x + "."
    escreva("x = " + x + "\n")
    escreva("z = " + z + "\n")
    escreva("y = " + y)
  }
}
```

## Expressões relacionais

Resolvendo expressões relacionais:

```plaintext
		Aprender a resolver expressões relacionais.

		Tarefa:

		Resolver expressões aritméticas e relacionais obtendo resultados lógicos.

		Problema
		Sendo X, Y, Z variáveis numéricas e W, T variáveis lógicas, qual o valor de cada variável no final do algoritmo?
		início

		X, Z, Y: numérico
		W, T: lógico
		X ←	 5
		Z ←	 (X + 4) / 3
		Y ←	 ((X + 4) ^ (1/2))
		W ←	 (X >= Z)
		T ←	 (Z <> Y)

		fim...

```

## Expressões lógicas

São expressões compostas por expressões relacionais com operadores lógicos. As expressões lógicas retornam valores lógicos.

Exemplo:

Sendo X e Y variáveis numéricas, Z e W variáveis literais e T e K variáveis lógicas, qual o resultado de cada variável no final do algoritmo?
início

```plaintext
		X, Y: numérico
		Z, W: literal
		T, K: lógico
		X ← 3
Y ← X ↑ 2
			Z ← "Abaca"
			W ← Z + "xi"
			T ← (X <= Y) e (não (Z + "te" <> W))
			K ← não (T e  ("Abaca" = Z))
			
			fim...

```

Resolução em Portugol:

```plaintext
programa {
  /* Sendo X e Y variáveis numéricas, Z e W variáveis literais e T e K variá­veis lógicas,
     qual o resultado de cada variável no final do algoritmo?
			X, Y: numérico
			Z, W: literal
			T, K: lógico
			X ← 3
			Y ← X ↑ 2
			Z ← “Abaca”
			W ← Z + “xi”
			T ← (X <= Y) e (não (Z + “te” <> W))
			K ← não (T e  (“Abaca” = Z))
      */

  funcao inicio() {
    real X, Y
		cadeia Z, W
		logico T, K
			X = 3
			Y = X * X
			Z = "Abaca"
			W = Z + "xi"
			T = (X <= Y) e (nao (Z + "te" <> W))
			K = nao (T e  ("Abaca" == Z))
      escreva("X = " + X + ", Y = " + Y + ", Z = " + Z + ", W = " + W + ", T = " + T + ", K = " + K)
  }
}
```

## Referências

[IDE do Portugol Studio online](https://dgadelha.github.io/Portugol-Webstudio/)

Xavier, Gley Fabiano Cardoso
Lógica de programação
E-book. Disponível em: [https://bibliotecadigitalsenac.com.br/?from=%3FcontentInfo%3D1306#/legacy/epub/1306](https://bibliotecadigitalsenac.com.br/?from=%3FcontentInfo%3D1306#/legacy/epub/1306)
Acesso em 30/03/2023
