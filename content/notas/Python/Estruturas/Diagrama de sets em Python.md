---
title: Diagrama de sets em Python
description: diagrama Mermaid com os principais conjuntos em Python
tags:
  - diagrama
  - programador/Python/estruturas
---

```mermaid
graph LR
A[Set] --> B(add)
B --> B1(Adiciona um elemento ao set)
B --> B2("ex. `meu_set.add(elemento)`")
A --> C(clear)
C --> C1(Remove todos os elementos do set)
C --> C2("ex. `meu_set.clear()`")
A --> D(copy)
D --> D1(Retorna uma cópia do set)
D --> D2("ex. `novo_set = meu_set.copy()`")
A --> E(difference)
E --> E1(Retorna um novo set com a diferença entre dois sets)
E --> E2("ex. `diferenca = meu_set1.difference(meu_set2)`")
A --> F(discard)
F --> F1(Remove um elemento do set se existir)
F --> F2("ex. `meu_set.discard(elemento)`")
A --> G(intersection)
G --> G1(Retorna um novo set com a intersecção entre dois sets)
G --> G2("ex. `intersecao = meu_set1.intersection(meu_set2)`")
A --> H(isdisjoint)
H --> H1(Verifica se dois sets não possuem elementos em comum)
H --> H2("ex. `disjuntos = meu_set1.isdisjoint(meu_set2)`")
A --> I(issubset)
I --> I1(Verifica se um set está contido em outro)
I --> I2("ex. `subconjunto = meu_set1.issubset(meu_set2)`")
A --> J(issuperset)
J --> J1(Verifica se um set contém outro)
J --> J2("ex. `superconjunto = meu_set1.issuperset(meu_set2)`")
A --> K(pop)
K --> K1(Remove e retorna um elemento aleatório do set)
K --> K2("ex. `elemento_removido = meu_set.pop()`")
A --> L(remove)
L --> L1(Remove um elemento do set se existir)
L --> L2("ex. `meu_set.remove(elemento)`")
A --> M(union)
M --> M1(Retorna um novo set com a união entre dois sets)
M --> M2("ex. `uniao = meu_set1.union(meu_set2)`")
```

## **Explicação do diagrama:**

O diagrama Mermaid acima ilustra as principais funções dos sets em Python. Cada função é representada por um nó no diagrama, e as setas indicam a relação entre as funções.

**Funções:**

- **add:** Adiciona um elemento ao set.
- **clear:** Remove todos os elementos do set.
- **copy:** Retorna uma cópia do set.
- **difference:** Retorna um novo set com a diferença entre dois sets.
- **discard:** Remove um elemento do set se existir.
- **intersection:** Retorna um novo set com a intersecção entre dois sets.
- **isdisjoint:** Verifica se dois sets não possuem elementos em comum.
- **issubset:** Verifica se um set está contido em outro.
- **issuperset:** Verifica se um set contém outro.
- **pop:** Remove e retorna um elemento aleatório do set.
- **remove:** Remove um elemento do set se existir.
- **union:** Retorna um novo set com a união entre dois sets.

## **Exemplos:**

O diagrama também inclui exemplos de como usar cada função. Por exemplo, o exemplo para a função `add` mostra como adicionar o elemento `elemento` ao set `meu_set`.

**Observações:**

- Este diagrama é apenas uma visão geral das principais funções dos sets em Python. Existem muitas outras funções disponíveis, e cada função tem suas próprias nuances e detalhes.
- Para mais informações sobre as funções de set em Python, consulte a documentação oficial do Python: [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
