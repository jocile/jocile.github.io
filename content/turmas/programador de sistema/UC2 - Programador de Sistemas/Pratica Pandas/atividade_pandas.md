---
title: Atividade com Python e Pandas
description: "Exemplo prático de manipulação de tabelas CSV com Python e Pandas."
tags:
  - banco-de-dados
  - Python/bd
  - Pandas
  - CSV
---

## 🎓 Atividade Prática: Analista de Dados Educacionais

Você foi contratado como Analista de Dados por uma escola de tecnologia.
Importe os cadastros separados e responda às perguntas da diretoria.

**Objetivo:** manipular e cruzar múltiplas tabelas com o Pandas para gerar um relatório consolidado de alunos, cursos e faturamento.

**Dica:** antes de rodar cada resposta, calcule o resultado esperado à mão (os dados são pequenos).

### Passo a passo

1. Carregar os três arquivos CSV no Pandas.
2. Combinar `matriculas` com `alunos` (coluna `id_aluno`).
3. Combinar o resultado com `cursos` (coluna `id_curso`).
4. Resultado esperado: um DataFrame com nome do aluno, curso e preço da mensalidade.

### Perguntas

1. Quais alunos têm pelo menos uma matrícula com status "Ativo"? (cada aluno aparece uma vez)
2. Quantas matrículas ativas há por curso? (cursos sem matrículas ativas devem aparecer com 0)
3. Qual o faturamento mensal total? (some o preço de cada matrícula ativa)
4. Qual a idade média dos alunos matriculados em "Python para Dados"? (considere alunos com matrícula ativa)
5. Quais alunos não têm nenhuma matrícula?
6. Bônus: qual curso gera o maior faturamento?

## 📊 Preparação: os três datasets

Mudanças em relação à versão original (para exercitar casos de borda):

- **Eduardo** (id 5) não tem matrícula nenhuma → diferença entre `inner` e `left`.
- **Diana** tem uma matrícula **Trancado** em SQL → status que não conta como ativo.
- **Web Design** só tem matrícula cancelada → curso com 0 ativas.
- **Ana** tem duas matrículas ativas → precisa de `drop_duplicates`.

### Passo 1: salvar e carregar os CSVs

```python
# Salvando os arquivos CSV (encoding utf-8 para não quebrar os acentos)
with open('alunos.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_aluno,nome_aluno,idade,cidade\n'
        '1,Ana Silva,21,São Paulo\n'
        '2,Bruno Costa,24,Rio de Janeiro\n'
        '3,Carlos Souza,19,Belo Horizonte\n'
        '4,Diana Martins,22,São Paulo\n'
        '5,Eduardo Lima,20,Fortaleza\n'
    )

with open('cursos.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_curso,nome_curso,preco_mensalidade\n'
        '101,Python para Dados,150\n'
        '102,Web Design Moderno,120\n'
        '103,Banco de Dados SQL,130\n'
    )

with open('matriculas.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_matricula,id_aluno,id_curso,status\n'
        '1001,1,101,Ativo\n'
        '1002,1,103,Ativo\n'
        '1003,2,101,Ativo\n'
        '1004,3,102,Cancelado\n'
        '1005,4,101,Ativo\n'
        '1006,4,103,Trancado\n'
    )

import pandas as pd

alunos = pd.read_csv('alunos.csv', encoding='utf-8')
cursos = pd.read_csv('cursos.csv', encoding='utf-8')
matriculas = pd.read_csv('matriculas.csv', encoding='utf-8')

# Sempre inspecione os dados depois de carregar
print(f'alunos: {alunos.shape} | cursos: {cursos.shape} | matriculas: {matriculas.shape}')
print(matriculas['status'].value_counts())
```

### Passos 2 e 3: consolidar as tabelas

```python
# inner join: só matrículas que têm aluno e curso correspondentes
consolidado = (
    matriculas
    .merge(alunos, on='id_aluno', how='inner')
    .merge(cursos, on='id_curso', how='inner')
)

# Confere se nenhuma matrícula foi perdida no cruzamento
assert len(consolidado) == len(matriculas), 'Alguma matrícula ficou sem aluno ou curso!'

print('Tabela consolidada:')
print(consolidado[['id_matricula', 'nome_aluno', 'nome_curso', 'preco_mensalidade', 'status']])
```

### Análise de dados

```python
# Subconjunto reutilizado nas perguntas: apenas matrículas ativas
ativas = consolidado[consolidado['status'] == 'Ativo']

"""## Pergunta 1: quais alunos têm matrícula ativa?

Esperado: Ana Silva, Bruno Costa, Diana Martins (Ana tem 2 matrículas, mas aparece 1 vez).
"""

alunos_ativos = (
    ativas[['id_aluno', 'nome_aluno']]
    .drop_duplicates()
    .sort_values('nome_aluno')
    .reset_index(drop=True)
)

print('Alunos com pelo menos uma matrícula ativa:')
print(alunos_ativos)

assert list(alunos_ativos['nome_aluno']) == ['Ana Silva', 'Bruno Costa', 'Diana Martins']

"""## Pergunta 2: matrículas ativas por curso (incluindo cursos com 0)

Esperado: Python para Dados = 3, Banco de Dados SQL = 1, Web Design Moderno = 0.

Se filtrássemos `consolidado` e agrupássemos direto, Web Design **sumiria**.
Para mantê-lo, partimos da tabela `cursos` com `how='left'`.
"""

matriculas_ativas_por_curso = (
    cursos
    .merge(matriculas[matriculas['status'] == 'Ativo'], on='id_curso', how='left')
    .groupby('nome_curso')['id_matricula']
    .count()                      # count() ignora NaN, então curso sem ativas = 0
    .sort_values(ascending=False)
)

print('Total de matrículas ativas por curso:')
print(matriculas_ativas_por_curso)

assert matriculas_ativas_por_curso['Python para Dados'] == 3
assert matriculas_ativas_por_curso['Banco de Dados SQL'] == 1
assert matriculas_ativas_por_curso['Web Design Moderno'] == 0

"""## Pergunta 3: faturamento mensal (somente matrículas ativas)

Esperado: R$ 580,00 → 150 + 130 + 150 + 150. A matrícula Trancada (130) e a Cancelada (120) não entram.
"""

faturamento_total = ativas['preco_mensalidade'].sum()

print('Faturamento mensal total (matrículas ativas):')
print(f'R$ {faturamento_total:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'))

assert faturamento_total == 580

"""## Pergunta 4: idade média em "Python para Dados"

Considera os alunos com matrícula **ativa** no curso, contando cada aluno uma vez.

Esperado: 22,3 anos → (21 + 24 + 22) / 3.
"""

alunos_python = (
    ativas[ativas['nome_curso'] == 'Python para Dados']
    [['id_aluno', 'idade']]
    .drop_duplicates()
)
idade_media_python = alunos_python['idade'].mean()

print('Idade média dos alunos ativos em Python para Dados:')
print(f'{idade_media_python:.1f} anos'.replace('.', ','))

assert round(idade_media_python, 1) == 22.3

"""## Pergunta 5: quais alunos não têm nenhuma matrícula?

Esperado: Eduardo Lima.

Um `inner` join nunca mostraria Eduardo. Usamos `how='left'` + `indicator=True`.
"""

alunos_sem_matricula = (
    alunos
    .merge(matriculas, on='id_aluno', how='left', indicator=True)
    .query("_merge == 'left_only'")
    [['id_aluno', 'nome_aluno']]
    .reset_index(drop=True)
)

print('Alunos sem matrícula:')
print(alunos_sem_matricula)

assert list(alunos_sem_matricula['nome_aluno']) == ['Eduardo Lima']

"""## Bônus: qual curso gera o maior faturamento?

Esperado: Python para Dados (R$ 450).
"""

faturamento_por_curso = (
    ativas
    .groupby('nome_curso')['preco_mensalidade']
    .sum()
    .sort_values(ascending=False)
)
curso_top = faturamento_por_curso.head(1)

print('Curso com maior faturamento:')
print(curso_top)

assert curso_top.index[0] == 'Python para Dados' and curso_top.iloc[0] == 450
```

### Relatórios em formato gráfico

```python
"""## Exibindo em formato de gráfico

Os dois gráficos usam **apenas matrículas ativas** e o mesmo mapa de cores por curso.
"""

import matplotlib.pyplot as plt

# Uma cor fixa por curso, para os dois gráficos ficarem consistentes
cores = {
    'Python para Dados': '#4F81BD',
    'Web Design Moderno': '#FFC000',
    'Banco de Dados SQL': '#92D050',
}

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# --- Gráfico 1: matrículas ativas por curso (inclui curso com 0) ---
dados_barras = matriculas_ativas_por_curso.sort_index()
barras = axes[0].bar(
    dados_barras.index,
    dados_barras.values,
    color=[cores[c] for c in dados_barras.index],
    edgecolor='black',
)
axes[0].bar_label(barras, padding=3)            # mostra o valor (inclusive o 0) sobre a barra
axes[0].set_title('Matrículas Ativas por Curso', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Curso')
axes[0].set_ylabel('Total de Matrículas Ativas')
axes[0].set_ylim(0, dados_barras.max() + 1)
axes[0].tick_params(axis='x', rotation=15)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)
axes[0].set_axisbelow(True)

# --- Gráfico 2: proporção do faturamento por curso (só ativas) ---
dados_pizza = faturamento_por_curso.sort_index()
axes[1].pie(
    dados_pizza.values,
    labels=dados_pizza.index,
    colors=[cores[c] for c in dados_pizza.index],
    autopct=lambda p: f'{p:.1f}%\n(R$ {p * dados_pizza.sum() / 100:.0f})',
    startangle=90,
    wedgeprops={'edgecolor': 'black'},
)
axes[1].set_title(
    f'Faturamento por Curso (Ativos), Total: R$ {faturamento_total:.0f}',
    fontsize=12, fontweight='bold',
)

plt.tight_layout()
plt.show()
```

---

>[!note] ➡️ [[atividade_pandas sqlite]]

>[!done] [Resolução no Google Colab](https://colab.research.google.com/drive/1RvLnozsApF7ce2_SQJCry6gAze8d93LO)
