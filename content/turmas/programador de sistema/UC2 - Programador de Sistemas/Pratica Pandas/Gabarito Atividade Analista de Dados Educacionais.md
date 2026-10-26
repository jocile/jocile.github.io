---
title: "Gabarito: Atividade Analista de Dados Educacionais"
date: 2026-10-26
tags:
  - pandas
  - sqlite
  - sql
  - python
  - gabarito
  - atividade-pratica
description: "Soluções em Pandas e SQLite, resultados esperados, erros comuns e respostas dos desafios da atividade de análise de dados."
---

> [!warning] Material do professor
> Esta nota está com `draft: true` e **não é publicada** pelo Quartz. Não mova para uma pasta pública sem trocar para `draft: false`.

> [!abstract] Como usar
> Cada pergunta traz a solução em **Pandas** e em **SQL**, o resultado esperado e os erros mais comuns. Os blocos de código são sequenciais: rode-os na ordem, em um mesmo notebook.

## 0. Preparação

```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

dados_alunos = [
    (1, 'Ana Silva', 21, 'São Paulo'),
    (2, 'Bruno Costa', 24, 'Rio de Janeiro'),
    (3, 'Carlos Souza', 19, 'Belo Horizonte'),
    (4, 'Diana Martins', 22, 'São Paulo'),
    (5, 'Eduardo Lima', 20, 'Fortaleza'),
]
dados_cursos = [
    (101, 'Python para Dados', 150),
    (102, 'Web Design Moderno', 120),
    (103, 'Banco de Dados SQL', 130),
]
dados_matriculas = [
    (1001, 1, 101, 'Ativo'),
    (1002, 1, 103, 'Ativo'),
    (1003, 2, 101, 'Ativo'),
    (1004, 3, 102, 'Cancelado'),
    (1005, 4, 101, 'Ativo'),
    (1006, 4, 103, 'Trancado'),
]

# Pandas
alunos = pd.DataFrame(dados_alunos, columns=['id_aluno', 'nome_aluno', 'idade', 'cidade'])
cursos = pd.DataFrame(dados_cursos, columns=['id_curso', 'nome_curso', 'preco_mensalidade'])
matriculas = pd.DataFrame(dados_matriculas, columns=['id_matricula', 'id_aluno', 'id_curso', 'status'])

# SQLite
conn = sqlite3.connect(':memory:')
conn.execute('PRAGMA foreign_keys = ON')
conn.executescript("""
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
conn.executemany("INSERT INTO alunos VALUES (?,?,?,?)", dados_alunos)
conn.executemany("INSERT INTO cursos VALUES (?,?,?)", dados_cursos)
conn.executemany("INSERT INTO matriculas VALUES (?,?,?,?)", dados_matriculas)
conn.commit()

def sql(consulta):
    return pd.read_sql_query(consulta, conn)
```

## 1. Consolidação (`merge` × `JOIN`)

```python
# Pandas
consolidado = (
    matriculas
    .merge(alunos, on='id_aluno', how='inner')
    .merge(cursos, on='id_curso', how='inner')
)
assert len(consolidado) == len(matriculas)   # nenhuma matrícula perdida
ativas = consolidado[consolidado['status'] == 'Ativo']
```

```python
# SQL
conn.executescript("""
DROP VIEW IF EXISTS vw_consolidado;
CREATE VIEW vw_consolidado AS
SELECT m.id_matricula, a.id_aluno, a.nome_aluno, a.idade, a.cidade,
       c.nome_curso, c.preco_mensalidade, m.status
FROM matriculas m
JOIN alunos a ON a.id_aluno = m.id_aluno
JOIN cursos c ON c.id_curso = m.id_curso;
""")
assert len(sql("SELECT * FROM vw_consolidado")) == 6
```

> [!success] Esperado
> 6 linhas, uma por matrícula, com nome do aluno, curso e preço da mensalidade.

## 2. Pergunta 1: alunos ativos

```python
# Pandas
ativos_pd = (
    ativas[['nome_aluno']]
    .drop_duplicates()
    .sort_values('nome_aluno')
    .reset_index(drop=True)
)

# SQL
ativos_sql = sql("""
SELECT DISTINCT nome_aluno
FROM vw_consolidado
WHERE status = 'Ativo'
ORDER BY nome_aluno
""")

assert ativos_pd.equals(ativos_sql)
assert list(ativos_pd['nome_aluno']) == ['Ana Silva', 'Bruno Costa', 'Diana Martins']
```

> [!success] Esperado
> Ana Silva, Bruno Costa e Diana Martins.

> [!bug] Erros comuns
>
> - Esquecer `drop_duplicates` / `DISTINCT`: Ana aparece duas vezes.
> - Incluir Diana pelo status `Trancado` e não pelo `Ativo`: ela já entra pela matrícula 1005.
> - Devolver a lista de **matrículas** (4 linhas) em vez de **alunos** (3 linhas).

## 3. Pergunta 2: matrículas ativas por curso

```python
# Pandas: partir de cursos com how='left'
por_curso_pd = (
    cursos.merge(matriculas[matriculas['status'] == 'Ativo'], on='id_curso', how='left')
    .groupby('nome_curso')['id_matricula'].count()      # count() ignora NaN → 0
    .rename('matriculas_ativas')
    .reset_index()
    .sort_values(['matriculas_ativas', 'nome_curso'], ascending=[False, True])
    .reset_index(drop=True)
)

# SQL: filtro no ON, não no WHERE
por_curso_sql = sql("""
SELECT c.nome_curso, COUNT(m.id_matricula) AS matriculas_ativas
FROM cursos c
LEFT JOIN matriculas m
       ON m.id_curso = c.id_curso AND m.status = 'Ativo'
GROUP BY c.id_curso, c.nome_curso
ORDER BY matriculas_ativas DESC, c.nome_curso
""")

assert por_curso_pd.equals(por_curso_sql)
assert dict(zip(por_curso_pd['nome_curso'], por_curso_pd['matriculas_ativas'])) == {
    'Python para Dados': 3, 'Banco de Dados SQL': 1, 'Web Design Moderno': 0}
```

> [!success] Esperado
> Python para Dados: 3 · Banco de Dados SQL: 1 · Web Design Moderno: 0.

> [!bug] Erros comuns
>
> - `ativas.groupby('nome_curso').size()` devolve só 2 cursos: **Web Design some**.
> - Filtro no `WHERE m.status = 'Ativo'` com `LEFT JOIN`: o `NULL` do curso sem matrículas é descartado e o resultado volta a ter só 2 linhas.
> - Usar `COUNT(*)` no lugar de `COUNT(m.id_matricula)`: Web Design apareceria com **1**, porque a linha do `LEFT JOIN` existe mesmo sem matrícula.

## 4. Pergunta 3: faturamento mensal

```python
# Pandas
fat_pd = ativas['preco_mensalidade'].sum()

# SQL
fat_sql = sql("""
SELECT SUM(preco_mensalidade) AS faturamento_mensal
FROM vw_consolidado
WHERE status = 'Ativo'
""").iloc[0, 0]

assert fat_pd == fat_sql == 580
print(f'R$ {fat_pd:.2f}')
```

> [!success] Esperado
> **R$ 580,00** = 150 (Ana/Python) + 130 (Ana/SQL) + 150 (Bruno/Python) + 150 (Diana/Python).

> [!bug] Erros comuns
>
> - **R$ 710**: contar a matrícula `Trancado` da Diana (130).
> - **R$ 830**: não filtrar o status (soma as 6 matrículas, incluindo `Cancelado` e `Trancado`).
> - **R$ 700**: somar `Cancelado` e `Ativo` e esquecer só o `Trancado` (ou qualquer filtro que deixe passar a matrícula 1004, de 120, com a 1006 de fora).

## 5. Pergunta 4: idade média em "Python para Dados"

```python
# Pandas
idade_pd = (
    ativas[ativas['nome_curso'] == 'Python para Dados']
    [['id_aluno', 'idade']]
    .drop_duplicates()['idade']
    .mean()
)

# SQL
idade_sql = sql("""
SELECT AVG(idade) AS idade_media
FROM (
    SELECT DISTINCT id_aluno, idade
    FROM vw_consolidado
    WHERE status = 'Ativo' AND nome_curso = 'Python para Dados'
)
""").iloc[0, 0]

assert abs(idade_pd - idade_sql) < 1e-9 and round(idade_pd, 1) == 22.3
print(f'{idade_pd:.1f} anos')
```

> [!success] Esperado
> **22,3 anos** = (21 + 24 + 22) ÷ 3 = 67 ÷ 3.

> [!bug] Erros comuns
>
> - Formatar com `:.0f` e mostrar "22 anos".
> - Esquecer o `DISTINCT` na subconsulta. Neste curso cada aluno aparece uma vez, então o resultado não muda, mas o hábito é importante: se Ana tivesse duas matrículas em Python, ela pesaria o dobro na média.

## 6. Pergunta 5: alunos sem matrícula

```python
# Pandas: indicator=True cria a coluna _merge
sem_mat_pd = (
    alunos
    .merge(matriculas, on='id_aluno', how='left', indicator=True)
    .query("_merge == 'left_only'")
    [['nome_aluno']]
    .reset_index(drop=True)
)

# SQL: o IS NULL fica no WHERE
sem_mat_sql = sql("""
SELECT a.nome_aluno
FROM alunos a
LEFT JOIN matriculas m ON m.id_aluno = a.id_aluno
WHERE m.id_matricula IS NULL
ORDER BY a.nome_aluno
""")

assert sem_mat_pd.equals(sem_mat_sql)
assert list(sem_mat_pd['nome_aluno']) == ['Eduardo Lima']
```

> [!success] Esperado
> Eduardo Lima.

> [!tip] Para discutir em aula
> Por que aqui o filtro vai no `WHERE` e na pergunta 2 ia no `ON`? Na pergunta 2 queremos **manter** todos os cursos e restringir só quais matrículas são contadas. Aqui queremos **descartar** os alunos que têm par e ficar só com os que não têm.

## 7. Pergunta 6 (bônus): maior faturamento

```python
# Pandas
fat_por_curso = (
    ativas.groupby('nome_curso')['preco_mensalidade'].sum()
    .sort_values(ascending=False)
)
top_pd = fat_por_curso.head(1)

# SQL
top_sql = sql("""
SELECT nome_curso, SUM(preco_mensalidade) AS faturamento
FROM vw_consolidado
WHERE status = 'Ativo'
GROUP BY nome_curso
ORDER BY faturamento DESC
LIMIT 1
""")

assert top_pd.index[0] == top_sql.loc[0, 'nome_curso'] == 'Python para Dados'
assert top_pd.iloc[0] == top_sql.loc[0, 'faturamento'] == 450
```

> [!success] Esperado
> Python para Dados, com **R$ 450** (3 × 150).

## 8. Gráficos (desafio 6)

```python
cores = {
    'Python para Dados': '#4F81BD',
    'Web Design Moderno': '#FFC000',
    'Banco de Dados SQL': '#92D050',
}

df_alunos = sql("""
SELECT c.nome_curso, COUNT(m.id_matricula) AS total
FROM cursos c
LEFT JOIN matriculas m ON m.id_curso = c.id_curso AND m.status = 'Ativo'
GROUP BY c.id_curso, c.nome_curso
ORDER BY c.nome_curso
""")
df_fat = sql("""
SELECT nome_curso, SUM(preco_mensalidade) AS faturamento
FROM vw_consolidado
WHERE status = 'Ativo'
GROUP BY nome_curso
ORDER BY nome_curso
""")
total_fat = df_fat['faturamento'].sum()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

barras = axes[0].bar(df_alunos['nome_curso'], df_alunos['total'],
                     color=[cores[c] for c in df_alunos['nome_curso']], edgecolor='black')
axes[0].bar_label(barras, padding=3)
axes[0].set_title('Matrículas Ativas por Curso', fontsize=12, fontweight='bold')
axes[0].set_ylim(0, df_alunos['total'].max() + 1)
axes[0].tick_params(axis='x', rotation=15)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].set_axisbelow(True)

axes[1].pie(df_fat['faturamento'], labels=df_fat['nome_curso'],
            colors=[cores[c] for c in df_fat['nome_curso']],
            autopct=lambda p: f'{p:.1f}%\n(R$ {p * total_fat / 100:.0f})',
            startangle=90, wedgeprops={'edgecolor': 'black'})
axes[1].set_title(f'Faturamento por Curso (Ativos), Total: R$ {total_fat:.0f}',
                  fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
```

> [!success] Esperado
> Barras 3 / 1 / 0 (a barra do Web Design aparece com o rótulo 0). Pizza com Python 77,6% (R$ 450) e SQL 22,4% (R$ 130); Web Design fica de fora da pizza porque o faturamento é 0.

> [!bug] Erro comum
> Plotar `consolidado` sem filtrar: o gráfico passa a somar R$ 830 e Web Design aparece com R$ 120.

## 9. Desafios extras: respostas

### Desafio 5: faturamento por cidade

```python
# Pandas
fat_cidade_pd = (
    ativas.groupby('cidade')['preco_mensalidade'].sum()
    .sort_values(ascending=False)
)

# SQL
fat_cidade_sql = sql("""
SELECT cidade, SUM(preco_mensalidade) AS faturamento
FROM vw_consolidado
WHERE status = 'Ativo'
GROUP BY cidade
ORDER BY faturamento DESC
""")

assert fat_cidade_pd.to_dict() == dict(zip(fat_cidade_sql['cidade'], fat_cidade_sql['faturamento']))
assert fat_cidade_pd.to_dict() == {'São Paulo': 430, 'Rio de Janeiro': 150}
```

> [!success] Esperado
> São Paulo: R$ 430 (Ana 150 + 130, Diana 150) · Rio de Janeiro: R$ 150. Belo Horizonte e Fortaleza não aparecem, porque não têm matrícula ativa.

### Desafios 1 a 4: o que acontece

> [!example]- Desafio 1: matricular Eduardo
> Exemplo: `INSERT INTO matriculas VALUES (1007, 5, 102, 'Ativo')`.
>
> - Pergunta 1: Eduardo entra na lista de alunos ativos (4 alunos).
> - Pergunta 2: Web Design passa de 0 para 1.
> - Pergunta 3: o faturamento sobe de 580 para **700** (+120).
> - Pergunta 5: a lista fica **vazia**.
> - Pergunta 4 não muda (ele não está em Python).
> Se a nova matrícula for `Cancelado` ou `Trancado`, só a pergunta 5 muda.

> [!example]- Desafio 2: Diana de `Trancado` para `Ativo`
> `UPDATE matriculas SET status = 'Ativo' WHERE id_matricula = 1006`.
>
> - Pergunta 1: **não muda** (Diana já era ativa pela matrícula 1005).
> - Pergunta 2: Banco de Dados SQL passa de 1 para **2**.
> - Pergunta 3: o faturamento sobe de 580 para **710** (+130).
> - Pergunta 4: **não muda** (a matrícula alterada é em SQL, não em Python).
> - Pergunta 6: **não muda** (Python continua com 450, SQL fica com 260).

> [!example]- Desafio 3: `id_curso = 999`
> No SQLite, com `PRAGMA foreign_keys = ON`: `sqlite3.IntegrityError: FOREIGN KEY constraint failed`. Sem o `PRAGMA`, o SQLite **aceita** (ele não valida por padrão). O Pandas sempre aceita: um `DataFrame` não conhece chaves estrangeiras. O erro só aparece depois, quando o `merge` com `how='inner'` descarta a linha sem avisar. É por isso que o `assert len(consolidado) == len(matriculas)` existe.

> [!example]- Desafio 4: status `'Pendente'`
> `sqlite3.IntegrityError: CHECK constraint failed`. A regra `CHECK (status IN ('Ativo', 'Cancelado', 'Trancado'))` barra valores fora da lista. Aproveite para comentar que o Pandas aceitaria `'ativo'`, `'ATIVO'` ou `'Ativo '` e que isso quebraria o filtro `== 'Ativo'` sem nenhum erro.

## 10. Sugestão de critérios de correção

| Critério | O que observar |
| --- | --- |
| Consolidação | Dois cruzamentos corretos e conferência do número de linhas. |
| Filtros | Só `Ativo` entra nas perguntas 1 a 4 (Trancado e Cancelado ficam de fora). |
| Casos de borda | Ana sem duplicar, Web Design com 0, Eduardo na pergunta 5. |
| `LEFT JOIN` | Filtro no `ON` na pergunta 2 e `IS NULL` no `WHERE` na pergunta 5. |
| Conferência | Célula que compara Pandas e SQL após cada pergunta. |
| Apresentação | Média com uma casa decimal, gráficos filtrados e com títulos corretos. |
