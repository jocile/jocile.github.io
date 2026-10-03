---
title: Diagrama de tuplas em Python
description: diagrama Mermaid com as descrições das principais funções de tuplas em Python
tags:
  - diagrama
  - programador/Python/estruturas
---

```mermaid
graph LR
A[Tupla] --> B(acessar elemento por índice)
B --> B1(Retorna o elemento na posição especificada)
B --> B2("ex. `elemento = minha_tupla[indice]`")
A --> C(acessar elementos por fatiamento)
C --> C1(Retorna uma nova tupla com base em um intervalo)
C --> C2("ex. `nova_tupla = minha_tupla[inicio:fim:passo]`")
A --> D(concatenar)
D --> D1(Cria uma nova tupla combinando duas tuplas)
D --> D2("ex. `nova_tupla = minha_tupla1 + minha_tupla2`")
A --> E(repetir)
E --> E1(Cria uma nova tupla com um elemento repetido n vezes)
E --> E2("ex. `nova_tupla = (elemento, ) * n`")
A --> F(tamanho)
F --> F1(Retorna o número de elementos da tupla)
F --> F2("ex. `tamanho = len(minha_tupla)`")
A --> G(verificar se é imutável)
G --> G1(Retorna `True` se a tupla for imutável)
G --> G2("ex. `imutavel = isinstance(minha_tupla, tuple)`")
```

## **Explicação do diagrama:**

O diagrama Mermaid acima ilustra as principais operações de tuplas em Python. Cada operação é representada por um nó no diagrama, e as setas indicam a relação entre as operações.

**Operações:**

- **Acessar elemento por índice:** Retorna o elemento na posição especificada da tupla.
- **Acessar elementos por fatiamento:** Retorna uma nova tupla com base em um intervalo de índices.
- **Concatenar:** Cria uma nova tupla combinando duas tuplas.
- **Repetir:** Cria uma nova tupla com um elemento repetido um número específico de vezes.
- **Tamanho:** Retorna o número de elementos da tupla.
- **Verificar se é imutável:** Retorna `True` se a tupla for imutável.

**Exemplos:**

O diagrama também inclui exemplos de como usar cada operação. Por exemplo, o exemplo para a operação "Acessar elemento por índice" mostra como obter o elemento na posição `0` da tupla `minha_tupla`.

**Observações:**

- Este diagrama é apenas uma visão geral das principais operações de tuplas em Python. Existem outras operações disponíveis, e cada operação tem suas próprias nuances e detalhes.
