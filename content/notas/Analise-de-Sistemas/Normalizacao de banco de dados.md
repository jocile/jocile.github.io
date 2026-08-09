---
title: Normalizacao De Banco De Dados
description: A normalização é um processo essencial no design de banco de dados que
  envolve a organização dos dados para reduzir redundâncias e dependências. Este processo…
date: '2026-08-09'
draft: false
tags:
- banco-de-dados
---

### 3. Normalização de Dados

A normalização é um processo essencial no design de banco de dados que envolve a organização dos dados para reduzir redundâncias e dependências. Este processo é dividido em várias formas normais (normal forms), onde cada uma tem regras específicas que ajudam a garantir a integridade dos dados.

#### 3.1 Primeira Forma Normal (1FN)

A Primeira Forma Normal exige que os dados em cada coluna sejam atômicos, ou seja, indivisíveis. Além disso, todas as entradas em uma coluna devem ser do mesmo tipo de dado.

**Exemplo:**

Suponha que temos uma tabela `LIVROS` com os seguintes dados:

| ID  | Titulo             | Autores            |
|-----|--------------------|--------------------|
| 1   | Banco de Dados     | João, Maria        |
| 2   | Redes de Computadores | Pedro, Ana     |

Para estar em 1FN, precisamos dividir os autores em linhas separadas:

| ID  | Titulo               | Autor   |
|-----|----------------------|---------|
| 1   | Banco de Dados       | João    |
| 1   | Banco de Dados       | Maria   |
| 2   | Redes de Computadores| Pedro   |
| 2   | Redes de Computadores| Ana     |

#### 3.2 Segunda Forma Normal (2FN)

A Segunda Forma Normal requer que a tabela esteja primeiro na 1FN e que todos os atributos não chave dependam totalmente da chave primária. Isso significa que não deve haver dependências parciais de chave (ou seja, dependências de parte da chave primária).

**Exemplo:**

Considerando a tabela `LIVROS` com atributos `ID`, `Titulo`, e `AnoPublicacao` e uma tabela `AUTORES_LIVROS` com `IDLivro` e `IDAutor`.

| IDLivro | IDAutor |
|---------|---------|
| 1       | 1       |
| 1       | 2       |
| 2       | 3       |
| 2       | 4       |

Aqui, temos duas tabelas, `LIVROS` e `AUTORES_LIVROS`, eliminando a dependência parcial dos autores.

#### 3.3 Terceira Forma Normal (3FN)

A Terceira Forma Normal requer que a tabela esteja na 2FN e que não haja dependências transitivas. Isso significa que atributos não chave não devem depender de outros atributos não chave.

**Exemplo:**

Considere uma tabela `ESTUDANTES`:

| Matricula | Nome      | Curso    | Coordenador |
|-----------|-----------|----------|-------------|
| 123       | João      | Informática | Prof. Silva |
| 124       | Maria     | Matemática | Prof. Oliveira |

Aqui, `Coordenador` depende de `Curso`, e `Curso` depende da `Matricula`. Para estar na 3FN, criamos uma nova tabela `CURSOS`:

Tabela `ESTUDANTES`:

| Matricula | Nome      | CursoID |
|-----------|-----------|---------|
| 123       | João      | 1       |
| 124       | Maria     | 2       |

Tabela `CURSOS`:

| CursoID | Curso       | Coordenador     |
|---------|-------------|-----------------|
| 1       | Informática | Prof. Silva     |
| 2       | Matemática  | Prof. Oliveira  |

### Exemplos Práticos de Normalização

#### Exemplo 1: Sistema de Biblioteca

**Tabela original:**

| LivroID | Titulo           | Autor           | Categoria        |
|---------|------------------|-----------------|------------------|
| 1       | Banco de Dados   | João            | Tecnologia       |
| 2       | Redes de Computadores | Ana      | Tecnologia       |
| 3       | Dom Casmurro     | Machado de Assis| Literatura       |

**Após 1FN:**

| LivroID | Titulo               | Autor            | Categoria       |
|---------|----------------------|------------------|-----------------|
| 1       | Banco de Dados       | João             | Tecnologia      |
| 2       | Redes de Computadores| Ana              | Tecnologia      |
| 3       | Dom Casmurro         | Machado de Assis | Literatura      |

**Após 2FN:**

| LivroID | Titulo               | CategoriaID |
|---------|----------------------|-------------|
| 1       | Banco de Dados       | 1           |
| 2       | Redes de Computadores| 1           |
| 3       | Dom Casmurro         | 2           |

| CategoriaID | Categoria     |
|-------------|---------------|
| 1           | Tecnologia    |
| 2           | Literatura    |

**Após 3FN:**

| LivroID | Titulo               | CategoriaID |
|---------|----------------------|-------------|
| 1       | Banco de Dados       | 1           |
| 2       | Redes de Computadores| 1           |
| 3       | Dom Casmurro         | 2           |

| CategoriaID | Categoria   |
|-------------|-------------|
| 1           | Tecnologia  |
| 2           | Literatura  |

| AutorID | Nome             |
|---------|------------------|
| 1       | João             |
| 2       | Ana              |
| 3       | Machado de Assis |

| LivroID | AutorID          |
|---------|------------------|
| 1       | 1                |
| 2       | 2                |
| 3       | 3                |

#### Exemplo 2: Sistema de Gestão Escolar

**Tabela original:**

| EstudanteID | Nome    | Curso          | Professor      |
|-------------|---------|----------------|----------------|
| 1           | João    | Informática    | Prof. Silva    |
| 2           | Maria   | Matemática     | Prof. Oliveira |
| 3           | Pedro   | Física         | Prof. Souza    |

**Após 1FN:**

| EstudanteID | Nome   | CursoID |
|-------------|--------|---------|
| 1           | João   | 1       |
| 2           | Maria  | 2       |
| 3           | Pedro  | 3       |

**Após 2FN:**

| CursoID | Curso        | ProfessorID |
|---------|--------------|-------------|
| 1       | Informática  | 1           |
| 2       | Matemática   | 2           |
| 3       | Física       | 3           |

| ProfessorID | Nome          |
|-------------|---------------|
| 1           | Prof. Silva   |
| 2           | Prof. Oliveira|
| 3           | Prof. Souza   |

**Após 3FN:**

| EstudanteID | Nome   | CursoID |
|-------------|--------|---------|
| 1           | João   | 1       |
| 2           | Maria  | 2       |
| 3           | Pedro  | 3       |

| CursoID | Curso        | ProfessorID |
|---------|--------------|-------------|
| 1       | Informática  | 1           |
| 2       | Matemática   | 2           |
| 3       | Física       | 3           |

| ProfessorID | Nome          |
|-------------|---------------|
| 1           | Prof. Silva   |
| 2           | Prof. Oliveira|
| 3           | Prof. Souza   |

### Conclusão

A normalização dos dados é um processo crítico para garantir a eficiência e a integridade do banco de dados. Ao seguir as regras das formas normais, podemos criar um banco de dados bem estruturado, que minimiza redundâncias e evita problemas de inconsistência de dados. Utilizando exemplos práticos, esperamos que você tenha entendido como aplicar esses conceitos em seus próprios projetos.
