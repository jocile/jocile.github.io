---
title: Atividade com Python e Pandas com Sqlite
description: "Atividade prática: cruze alunos, cursos e matrículas com Pandas e SQLite para calcular matrículas ativas, faturamento e perfil dos alunos."
tags:
  - banco-de-dados
  - Python/bd
  - Pandas
  - CSV
---

>[!note] ⬅️ [[atividade_pandas]]

> [!abstract] Objetivo
> Manipular e cruzar múltiplas tabelas com [[Pandas]] e com SQL (SQLite) para gerar um relatório consolidado de alunos, cursos e faturamento da escola.

## 🎓 Contexto

Você foi contratado como **Analista de Dados** por uma escola de tecnologia. Os cadastros estão em três tabelas separadas e a diretoria precisa de respostas sobre matrículas, faturamento e perfil dos alunos.

Cada pergunta será resolvida **duas vezes**: primeiro com Pandas, depois com SQL. Ao final, compare os resultados.

> [!tip] Antes de programar
> Os dados são pequenos. Para cada pergunta, **calcule a resposta à mão** e só depois confira com o código.

## 📊 1. Os três datasets

### Tabela `alunos`

```csv
id_aluno,nome_aluno,idade,cidade
1,Ana Silva,21,São Paulo
2,Bruno Costa,24,Rio de Janeiro
3,Carlos Souza,19,Belo Horizonte
4,Diana Martins,22,São Paulo
5,Eduardo Lima,20,Fortaleza
```

### Tabela `cursos`

```csv
id_curso,nome_curso,preco_mensalidade
101,Python para Dados,150
102,Web Design Moderno,120
103,Banco de Dados SQL,130
```

### Tabela `matriculas`

```csv
id_matricula,id_aluno,id_curso,status
1001,1,101,Ativo
1002,1,103,Ativo
1003,2,101,Ativo
1004,3,102,Cancelado
1005,4,101,Ativo
1006,4,103,Trancado
```

> [!info] Atenção aos casos de borda
> Os dados foram montados para exigir cuidado:
>
> - **Eduardo** não tem nenhuma matrícula.
> - **Ana** tem duas matrículas ativas.
> - **Diana** tem uma matrícula `Trancado` (que **não** conta como ativa).
> - **Web Design Moderno** só tem uma matrícula `Cancelado`, ou seja, 0 ativas.

## 🛠️ 2. Passo a passo

1. **Carregar** os três arquivos CSV (`alunos.csv`, `cursos.csv`, `matriculas.csv`) no Pandas. Use `encoding='utf-8'` para preservar os acentos.
2. **Combinar** `matriculas` com `alunos` pela coluna `id_aluno`.
3. **Combinar** o resultado com `cursos` pela coluna `id_curso`.
4. **Conferir** que nenhuma matrícula foi perdida no cruzamento (o número de linhas deve continuar sendo 6).

> [!success] Resultado esperado
> Um único DataFrame com **nome do aluno**, **curso** e **preço da mensalidade** de cada matrícula.

## 📈 3. Análise e relatórios

> [!question] Como responder
> Para cada pergunta: (1) calcule à mão, (2) resolva com Pandas, (3) resolva com SQL, (4) confira se os dois resultados são iguais.

### Pergunta 1: Alunos ativos

Quais alunos têm **pelo menos uma matrícula** com status `Ativo`? Cada aluno deve aparecer **uma única vez**.

> [!success]- Resposta esperada
> Ana Silva, Bruno Costa e Diana Martins.
> *Ana tem duas matrículas ativas, mas aparece uma vez só.*

### Pergunta 2: Matrículas ativas por curso

Qual é o número total de matrículas ativas **por curso**? Cursos sem matrículas ativas devem aparecer com **0**.

> [!success]- Resposta esperada
>
> - Python para Dados: 3
> - Banco de Dados SQL: 1
> - Web Design Moderno: 0

> [!warning] Armadilha
> Se você filtrar o status `Ativo` **antes** de agrupar, o curso Web Design desaparece do resultado. Pense em qual tabela deve ser o ponto de partida do cruzamento.

### Pergunta 3: Faturamento mensal

Qual é o faturamento total mensal da escola? **Some o preço da mensalidade de cada matrícula ativa.**

> [!success]- Resposta esperada
> **R$ 580,00** (150 + 130 + 150 + 150). As matrículas `Trancado` e `Cancelado` não entram.

### Pergunta 4: Perfil dos alunos

Qual é a idade média dos alunos com matrícula **ativa** no curso "Python para Dados"? Conte cada aluno uma vez.

> [!success]- Resposta esperada
> **22,3 anos** ((21 + 24 + 22) ÷ 3). Exiba com uma casa decimal: arredondar para 22 esconde informação.

### Pergunta 5: Alunos sem matrícula

Quais alunos **não têm nenhuma matrícula**?

> [!success]- Resposta esperada
> Eduardo Lima.

> [!tip] Dica
> Um cruzamento que só mantém linhas com par (`inner`) nunca mostraria Eduardo. Qual tipo de cruzamento mantém todos os alunos?

### Pergunta 6 (bônus): Maior faturamento

Qual curso gera o **maior faturamento** considerando apenas matrículas ativas?

> [!success]- Resposta esperada
> Python para Dados, com **R$ 450**.

## 🗄️ 4. Versão com SQLite no Google Colab

O módulo `sqlite3` já vem com o Python. Crie o banco com as três tabelas, insira os mesmos dados e responda às mesmas perguntas com SQL.

| Pandas | SQL |
| --- | --- |
| `pd.merge(a, b, on='x')` | `JOIN ... ON` |
| `how='left'` | `LEFT JOIN` |
| `df[df.col == x]` | `WHERE col = x` |
| `.drop_duplicates()` | `SELECT DISTINCT` |
| `.groupby('col').count()` | `GROUP BY col` + `COUNT(...)` |
| `.sum()` / `.mean()` | `SUM(...)` / `AVG(...)` |
| `.sort_values()` | `ORDER BY` |
| `.head(1)` | `LIMIT 1` |

> [!info] Regras do banco
> Ative `PRAGMA foreign_keys = ON` (o SQLite não valida chaves estrangeiras por padrão) e use um `CHECK` para limitar o status a `Ativo`, `Cancelado` e `Trancado`.

> [!warning] `ON` × `WHERE` no `LEFT JOIN`
> Na pergunta 2, o filtro `status = 'Ativo'` deve ficar no **`ON`**. No `WHERE`, a linha do curso sem matrículas é descartada e o `LEFT JOIN` perde o efeito. Na pergunta 5, o `IS NULL` fica no **`WHERE`**. Entenda por que a regra muda.

## 🚀 5. Desafios extras

1. Matricule Eduardo em um curso. Quais respostas mudam? O faturamento muda?
2. Troque o status da matrícula 1006 de `Trancado` para `Ativo`. **Preveja** quais valores mudam antes de rodar.
3. Tente inserir uma matrícula com `id_curso = 999`. O SQLite aceita? E o Pandas?
4. Tente inserir o status `Pendente`. Qual regra do banco impede?
5. Calcule o faturamento **por cidade** do aluno, em Pandas e em SQL.
6. Gere um gráfico de barras com as matrículas ativas por curso (o curso com 0 deve aparecer) e uma pizza com a proporção do faturamento.

## ✅ 6. Entregável

- Notebook do Google Colab com as perguntas resolvidas em **Pandas e SQL**, lado a lado.
- Uma célula de conferência após cada pergunta, mostrando que os dois resultados coincidem.
- Os gráficos do desafio 6, usando **apenas matrículas ativas**.

## 🎓 Atividade Prática: Analista de Dados Educacionais

Você foi contratado como Analista de Dados por uma escola de tecnologia. Sua missão é importar os cadastros separados e responder às perguntas da diretoria.

### Objetivo da atividade

Manipular e cruzar múltiplas tabelas de dados usando o [[Pandas]] para gerar um relatório consolidado de alunos, cursos e faturamento da escola.

### Passo a passo do desafio

- Passo 1: Carregar os três arquivos CSV no Pandas.
- Passo 2: Combinar a tabela de matriculas com a tabela de alunos (usando a coluna em comum id_aluno).
- Passo 3: Em seguida, combinar o resultado anterior com a tabela de cursos (usando a coluna id_curso).
- Resultado esperado: Um único DataFrame contendo o nome do aluno, o curso que ele faz e o preço da mensalidade.

### Análise e Relatórios (As Perguntas)

- Filtro: Quem são os alunos com matrículas com o status "Ativo"?
- Agrupamento (groupby): Qual é o número total de matrículas ativas por curso?
- Cálculo Financeiro: Qual é o faturamento total mensal da escola considerando apenas as matrículas ativas?
- Análise de Perfil: Qual é a idade média dos alunos que se matricularam no curso de "Python para Dados"?

## 📊 1. Preparação (Os Três Datasets) com SQLite

O módulo `sqlite3` já vem com o Python, então não precisa instalar nada. Cada bloco abaixo é uma célula.

### Passo 1: criar o banco e as tabelas

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('escola.db')   # use ':memory:' para um banco temporário
conn.execute('PRAGMA foreign_keys = ON')  # SQLite não valida FK por padrão
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS matriculas;
DROP TABLE IF EXISTS cursos;
DROP TABLE IF EXISTS alunos;

CREATE TABLE alunos (
    id_aluno   INTEGER PRIMARY KEY,
    nome_aluno TEXT NOT NULL,
    idade      INTEGER,
    cidade     TEXT
);

CREATE TABLE cursos (
    id_curso          INTEGER PRIMARY KEY,
    nome_curso        TEXT NOT NULL,
    preco_mensalidade REAL NOT NULL
);

CREATE TABLE matriculas (
    id_matricula INTEGER PRIMARY KEY,
    id_aluno     INTEGER NOT NULL REFERENCES alunos(id_aluno),
    id_curso     INTEGER NOT NULL REFERENCES cursos(id_curso),
    status       TEXT NOT NULL CHECK (status IN ('Ativo', 'Cancelado', 'Trancado'))
);
""")
```

### Passo 2: inserir os dados

```python
cur.executemany("INSERT INTO alunos VALUES (?,?,?,?)", [
    (1, 'Ana Silva', 21, 'São Paulo'),
    (2, 'Bruno Costa', 24, 'Rio de Janeiro'),
    (3, 'Carlos Souza', 19, 'Belo Horizonte'),
    (4, 'Diana Martins', 22, 'São Paulo'),
])

cur.executemany("INSERT INTO cursos VALUES (?,?,?)", [
    (101, 'Python para Dados', 150),
    (102, 'Web Design Moderno', 120),
    (103, 'Banco de Dados SQL', 130),
])

cur.executemany("INSERT INTO matriculas VALUES (?,?,?,?)", [
    (1001, 1, 101, 'Ativo'),
    (1002, 1, 103, 'Ativo'),
    (1003, 2, 101, 'Ativo'),
    (1004, 3, 102, 'Cancelado'),
    (1005, 4, 101, 'Ativo'),
])
conn.commit()
```

> Alternativa que mantém o espírito do "carregar CSV": criar os CSVs como no original e usar `pd.read_csv(...).to_sql('alunos', conn, index=False, if_exists='replace')`. A desvantagem é que isso não cria chaves nem `CHECK`.

### Passo 3: consolidar com `JOIN` (e guardar numa VIEW)

```python
cur.executescript("""
DROP VIEW IF EXISTS vw_consolidado;
CREATE VIEW vw_consolidado AS
SELECT m.id_matricula, a.nome_aluno, a.idade, c.nome_curso,
       c.preco_mensalidade, m.status
FROM matriculas m
JOIN alunos a ON a.id_aluno = m.id_aluno
JOIN cursos c ON c.id_curso = m.id_curso;
""")

pd.read_sql_query("SELECT * FROM vw_consolidado", conn)
```

A `VIEW` evita repetir os dois `JOIN`s em cada pergunta.

### Perguntas

**1. Quem são os alunos com matrícula ativa?**

```python
pd.read_sql_query("""
SELECT DISTINCT nome_aluno
FROM vw_consolidado
WHERE status = 'Ativo'
ORDER BY nome_aluno
""", conn)
```

Esperado: Ana, Bruno e Diana.

**2. Matrículas ativas por curso (incluindo cursos com 0)**

```python
pd.read_sql_query("""
SELECT c.nome_curso, COUNT(m.id_matricula) AS matriculas_ativas
FROM cursos c
LEFT JOIN matriculas m
       ON m.id_curso = c.id_curso AND m.status = 'Ativo'
GROUP BY c.id_curso, c.nome_curso
ORDER BY matriculas_ativas DESC
""", conn)
```

Esperado: Python 3, SQL 1, Web Design 0. O filtro `status = 'Ativo'` está no `ON`, e não no `WHERE`, justamente para o curso sem ativos não sumir. Vale mostrar isso aos alunos.

**3. Faturamento mensal (só ativas)**

```python
pd.read_sql_query("""
SELECT SUM(preco_mensalidade) AS faturamento_mensal
FROM vw_consolidado
WHERE status = 'Ativo'
""", conn)
```

Esperado: R$ 580.

**4. Idade média em "Python para Dados"**

```python
pd.read_sql_query("""
SELECT ROUND(AVG(idade), 1) AS idade_media
FROM vw_consolidado
WHERE nome_curso = 'Python para Dados'
""", conn)
```

Esperado: 22,3.

### Gráficos

```python
import matplotlib.pyplot as plt

df_alunos = pd.read_sql_query("""
SELECT c.nome_curso, COUNT(m.id_matricula) AS total
FROM cursos c
LEFT JOIN matriculas m ON m.id_curso = c.id_curso AND m.status = 'Ativo'
GROUP BY c.id_curso
""", conn)

df_fat = pd.read_sql_query("""
SELECT nome_curso, SUM(preco_mensalidade) AS faturamento
FROM vw_consolidado
WHERE status = 'Ativo'
GROUP BY nome_curso
""", conn)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

df_alunos.plot(kind='bar', x='nome_curso', y='total', legend=False,
               color='#4F81BD', edgecolor='black', ax=axes[0])
axes[0].set_title('Matrículas Ativas por Curso', fontweight='bold')
axes[0].set_xlabel('Curso'); axes[0].set_ylabel('Total')
axes[0].tick_params(axis='x', rotation=15)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

df_fat.set_index('nome_curso')['faturamento'].plot(
    kind='pie', autopct='%1.1f%%', startangle=90, ax=axes[1],
    wedgeprops={'edgecolor': 'black'})
axes[1].set_title('Faturamento por Curso (Ativos)', fontweight='bold')
axes[1].set_ylabel('')

plt.tight_layout()
plt.show()
```

### Fechar e (opcional) baixar o banco

```python
conn.close()

# from google.colab import files
# files.download('escola.db')   # abre no DB Browser for SQLite, por exemplo
```

---

## Dica didática

Uma sequência boa é resolver cada pergunta **primeiro em Pandas e depois em SQL**, comparando os resultados lado a lado. Observe que `merge` = `JOIN`, `df[df.col == x]` = `WHERE` e `groupby` = `GROUP BY`. Se quiser, posso montar essa versão comparativa em duas colunas ou transformar tudo em um notebook `.ipynb` pronto para o Colab.

>[!done] [Resolução no Gooble Colab](https://colab.research.google.com/drive/1t4RiMtGy8G618wU1hxLyBhumlSHOF4DV?usp=sharing)
