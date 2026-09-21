---
title: Diagrama de listas em Python
description: diagrama Mermaid com as descrições das principais listas em Python
tags:
  - diagrama
  - programador/Python/estruturas
---

```mermaid
graph LR
A[Lista] --> B(append)
B --> B1(Adiciona um elemento ao final)
B --> B2("ex. `minha_lista.append(novo_elemento)`")
A --> C(clear)
C --> C1(Remove todos os elementos)
C --> C2("ex. `minha_lista.clear()`")
A --> D(copy)
D --> D1(Retorna uma cópia)
D --> D2("ex. `nova_lista = minha_lista.copy()`")
A --> E(count)
E --> E1(Conta o número de ocorrências de um elemento)
E --> E2("ex. `numero_ocorrencias = minha_lista.count(elemento)`")
A --> F(extend)
F --> F1(Adiciona elementos de outra lista ao final)
F --> F2("ex. `minha_lista.extend(outra_lista)`")
A --> G(index)
G --> G1(Retorna o índice do primeiro elemento encontrado)
G --> G2("ex. `indice = minha_lista.index(elemento)`")
A --> H(insert)
H --> H1(Insere um elemento em uma posição específica)
H --> H2("ex. `minha_lista.insert(indice, novo_elemento)`")
A --> I(pop)
I --> I1(Remove o elemento em uma posição específica)
I --> I2("ex. `elemento_removido = minha_lista.pop(indice)`")
A --> J(remove)
J --> J1(Remove a primeira ocorrência de um elemento)
J --> J2("ex. `minha_lista.remove(elemento)`")
A --> K(reverse)
K --> K1(Inverte a ordem dos elementos)
K --> K2("ex. `minha_lista.reverse()`")
A --> L(sort)
L --> L1(Ordena os elementos)
L --> L2("ex. `minha_lista.sort()`")
A --> M(copy)
M --> M1(Retorna uma cópia da lista)
M --> M2("ex. `nova_lista = minha_lista.copy()`")
```

**Explicação do diagrama:**

O diagrama Mermaid acima ilustra as principais funções das listas em Python. Cada função é representada por um nó no diagrama, e as setas indicam a relação entre as funções.

**Funções:**

- **append:** Adiciona um elemento ao final da lista.
- **clear:** Remove todos os elementos da lista.
- **copy:** Retorna uma cópia da lista.
- **count:** Conta o número de ocorrências de um elemento na lista.
- **extend:** Adiciona elementos de outra lista ao final da lista.
- **index:** Retorna o índice do primeiro elemento encontrado na lista.
- **insert:** Insere um elemento em uma posição específica da lista.
- **pop:** Remove o elemento em uma posição específica da lista.
- **remove:** Remove a primeira ocorrência de um elemento da lista.
- **reverse:** Inverte a ordem dos elementos da lista.
- **sort:** Ordena os elementos da lista.

**Exemplos:**

O diagrama também inclui exemplos de como usar cada função. Por exemplo, o exemplo para a função `append` mostra como adicionar o elemento `novo_elemento` ao final da lista `minha_lista`.

#programador/projetos/diagramas #programador/Python/estruturas
