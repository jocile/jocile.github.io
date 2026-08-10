---
title: Exercicio De Normalizacao De Banco De Dados
description: Para consolidar o entendimento sobre a normalização de dados, vamos realizar um exercício prático. Neste exercício, você terá que aplicar as formas normais…
date: '2026-08-09'
draft: false
tags:
- Markdown
- banco-de-dados
---

### Exercício de Normalização de Dados

Para consolidar o entendimento sobre a normalização de dados, vamos realizar um exercício prático. Neste exercício, você terá que aplicar as formas normais (1FN, 2FN, e 3FN) para normalizar um conjunto de tabelas.

#### Contexto do Exercício

Você foi contratado para organizar o banco de dados de uma pequena loja de música. Atualmente, a loja mantém todas as informações em uma única tabela desnormalizada chamada `MUSICA`. Aqui estão os dados da tabela:

| ID | Titulo           | Artista         | Album          | AnoAlbum | Genero      | Duração | DataCompra   | PrecoCompra | NomeComprador | EmailComprador     |
|----|------------------|-----------------|----------------|----------|-------------|---------|--------------|-------------|---------------|--------------------|
| 1  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    | 2024-01-15   | 1.99        | Alice         | alice@mail.com     |
| 2  | Song B           | Artist 2        | Album Y        | 2021     | Pop         | 4:12    | 2024-01-16   | 2.49        | Bob           | bob@mail.com       |
| 3  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    | 2024-02-01   | 1.99        | Charlie       | charlie@mail.com   |
| 4  | Song C           | Artist 3        | Album Z        | 2019     | Jazz        | 5:00    | 2024-02-01   | 3.00        | Alice         | alice@mail.com     |

#### Tarefas

1. **Primeira Forma Normal (1FN):**
    - Remova grupos repetitivos.
    - Garanta que cada coluna contenha valores atômicos.

2. **Segunda Forma Normal (2FN):**
    - Certifique-se de que a tabela esteja em 1FN.
    - Elimine dependências parciais (dependências de parte da chave primária).

3. **Terceira Forma Normal (3FN):**
    - Certifique-se de que a tabela esteja em 2FN.
    - Remova dependências transitivas (dependências de atributos não chave com outros atributos não chave).

### Passos Detalhados

#### Passo 1: Aplicar a 1FN

**Tabela original:**

| ID | Titulo           | Artista         | Album          | AnoAlbum | Genero      | Duração | DataCompra   | PrecoCompra | NomeComprador | EmailComprador     |
|----|------------------|-----------------|----------------|----------|-------------|---------|--------------|-------------|---------------|--------------------|

**Após 1FN:**

| ID | Titulo           | Artista         | Album          | AnoAlbum | Genero      | Duração | DataCompra   | PrecoCompra | CompradorID |
|----|------------------|-----------------|----------------|----------|-------------|---------|--------------|-------------|-------------|
| 1  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    | 2024-01-15   | 1.99        | 1           |
| 2  | Song B           | Artist 2        | Album Y        | 2021     | Pop         | 4:12    | 2024-01-16   | 2.49        | 2           |
| 3  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    | 2024-02-01   | 1.99        | 3           |
| 4  | Song C           | Artist 3        | Album Z        | 2019     | Jazz        | 5:00    | 2024-02-01   | 3.00        | 1           |

| CompradorID | NomeComprador | EmailComprador      |
|-------------|---------------|---------------------|
| 1           | Alice         | alice@mail.com      |
| 2           | Bob           | bob@mail.com        |
| 3           | Charlie       | charlie@mail.com    |

#### Passo 2: Aplicar a 2FN

**Tabela `MUSICA`**

| ID | Titulo           | Artista         | Album          | AnoAlbum | Genero      | Duração |
|----|------------------|-----------------|----------------|----------|-------------|---------|
| 1  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    |
| 2  | Song B           | Artist 2        | Album Y        | 2021     | Pop         | 4:12    |
| 3  | Song A           | Artist 1        | Album X        | 2020     | Rock        | 3:45    |
| 4  | Song C           | Artist 3        | Album Z        | 2019     | Jazz        | 5:00    |

**Tabela `COMPRA`**

| CompraID | MusicaID | DataCompra   | PrecoCompra | CompradorID |
|----------|----------|--------------|-------------|-------------|
| 1        | 1        | 2024-01-15   | 1.99        | 1           |
| 2        | 2        | 2024-01-16   | 2.49        | 2           |
| 3        | 1        | 2024-02-01   | 1.99        | 3           |
| 4        | 3        | 2024-02-01   | 3.00        | 1           |

#### Passo 3: Aplicar a 3FN

**Tabela `MUSICA`**

| ID | Titulo           | Artista         | AlbumID |
|----|------------------|-----------------|---------|
| 1  | Song A           | Artist 1        | 1       |
| 2  | Song B           | Artist 2        | 2       |
| 3  | Song A           | Artist 1        | 1       |
| 4  | Song C           | Artist 3        | 3       |

**Tabela `ALBUM`**

| AlbumID | NomeAlbum | AnoAlbum | Genero |
|---------|-----------|----------|--------|
| 1       | Album X   | 2020     | Rock   |
| 2       | Album Y   | 2021     | Pop    |
| 3       | Album Z   | 2019     | Jazz   |

**Tabela `COMPRA`**

| CompraID | MusicaID | DataCompra   | PrecoCompra | CompradorID |
|----------|----------|--------------|-------------|-------------|
| 1        | 1        | 2024-01-15   | 1.99        | 1           |
| 2        | 2        | 2024-01-16   | 2.49        | 2           |
| 3        | 1        | 2024-02-01   | 1.99        | 3           |
| 4        | 3        | 2024-02-01   | 3.00        | 1           |

**Tabela `COMPRADOR`**

| CompradorID | NomeComprador | EmailComprador      |
|-------------|---------------|---------------------|
| 1           | Alice         | alice@mail.com      |
| 2           | Bob           | bob@mail.com        |
| 3           | Charlie       | charlie@mail.com    |

### Tarefas para os Alunos

1. **Primeira Forma Normal (1FN):**
    - Analise a tabela `MUSICA` original e identifique grupos repetitivos.
    - Reestruture a tabela para que cada coluna contenha valores atômicos.

2. **Segunda Forma Normal (2FN):**
    - Garanta que a tabela `MUSICA` esteja em 1FN.
    - Crie tabelas separadas para eliminar dependências parciais.
    - Relacione as tabelas adequadamente com chaves estrangeiras.

3. **Terceira Forma Normal (3FN):**
    - Garanta que as tabelas estejam em 2FN.
    - Identifique e elimine dependências transitivas.
    - Crie novas tabelas se necessário para armazenar informações dependentes.

### Solução Esperada

No final do exercício, os alunos devem ter produzido um conjunto de tabelas normalizadas similar ao exemplo fornecido nos passos detalhados. Isso deve incluir tabelas separadas para músicas, álbuns, compras e compradores, todas inter-relacionadas por chaves primárias e estrangeiras.

Boa sorte, e lembrem-se: a prática leva à perfeição!
