---
title: "Atividade Analista de Dados Educacionais"
date: 2026-10-26
draft: false
tags:
  - pandas
  - python
  - analise-de-dados
  - iniciante
  - atividade-pratica
description: "Versão guiada sobre tabelas, merge, filtro, agrupamento e média com Pandas, passo a passo, usando os dados de uma escola de tecnologia."
---

> [!abstract] O que você vai fazer
> Você vai trabalhar como **analista de dados de uma escola** e responder a 4 perguntas da diretoria usando Python e Pandas. Cada pergunta é dividida em **passos pequenos**, com explicação, dica e resposta para conferir.

> [!tip] Como estudar esta nota
>
> 1. Leia a explicação.
> 2. **Tente escrever o código sozinho** (os espaços `____` são para você completar).
> 3. Só então abra a resposta (as caixas dobráveis abrem ao clicar no título).
> 4. Se errou, tudo bem: leia a seção **Erros comuns de iniciante**, mais abaixo, e tente de novo.
>
> No Google Colab, escreva cada bloco de código em uma célula e rode com `Shift + Enter`.

Quer o desafio completo, com SQL e casos mais difíceis? Veja a [[atividade-analista-dados-educacionais|versão completa]].

---

## 🧠 1. A ideia por trás de tudo

Imagine que a secretaria da escola guarda as informações em **três cadernos separados**:

| Caderno | O que guarda |
| --- | --- |
| 📒 **alunos** | quem são os alunos (nome, idade, cidade) |
| 📗 **cursos** | quais cursos existem e quanto custa a mensalidade |
| 📘 **matrículas** | qual aluno está em qual curso e se a matrícula está ativa |

O problema: o caderno de matrículas **só tem números**. Ele diz "o aluno `1` está no curso `101`", mas não diz *quem* é o aluno `1` nem *qual* é o curso `101`.

Para descobrir, você precisa **procurar o número no outro caderno**. Em Pandas, essa "procura e junção" se chama **`merge`**.

```text
matrícula 1001:  aluno 1,  curso 101
                   │          │
                   ▼          ▼
         procura em alunos   procura em cursos
         → Ana Silva         → Python para Dados
```

> [!info] Conceitos desta nota
>
> - **Tabela** (no Pandas: `DataFrame`): uma planilha com linhas e colunas.
> - **Linha**: um registro (um aluno, uma matrícula...).
> - **Coluna**: uma característica (nome, idade, status...).
> - **Chave** (`id_aluno`, `id_curso`): o número que identifica cada registro e permite ligar as tabelas.
> - **`merge`**: junta duas tabelas usando uma chave em comum.

---

## 📊 2. Os dados

### 📒 alunos

| id_aluno | nome_aluno | idade | cidade |
| --- | --- | --- | --- |
| 1 | Ana Silva | 21 | São Paulo |
| 2 | Bruno Costa | 24 | Rio de Janeiro |
| 3 | Carlos Souza | 19 | Belo Horizonte |
| 4 | Diana Martins | 22 | São Paulo |

### 📗 cursos

| id_curso | nome_curso | preco_mensalidade |
| --- | --- | --- |
| 101 | Python para Dados | 150 |
| 102 | Web Design Moderno | 120 |
| 103 | Banco de Dados SQL | 130 |

### 📘 matriculas

| id_matricula | id_aluno | id_curso | status |
| --- | --- | --- | --- |
| 1001 | 1 | 101 | Ativo |
| 1002 | 1 | 103 | Ativo |
| 1003 | 2 | 101 | Ativo |
| 1004 | 3 | 102 | Cancelado |
| 1005 | 4 | 101 | Ativo |

> [!question] Antes de programar: pense
> Olhando só as tabelas, **sem código**, tente responder:
>
> 1. Quantas matrículas estão ativas?
> 2. Quanto a escola recebe por mês com as matrículas ativas?
>
> Anote suas respostas. Você vai conferi-las no final.

---

## 🛠️ 3. Passo a passo

### Passo 1: criar as tabelas no Python

Primeiro importamos o Pandas (a biblioteca que trabalha com tabelas). Depois criamos cada tabela escrevendo, **coluna por coluna**, os valores que ela tem.

```python
import pandas as pd

alunos = pd.DataFrame({
    'id_aluno':   [1, 2, 3, 4],
    'nome_aluno': ['Ana Silva', 'Bruno Costa', 'Carlos Souza', 'Diana Martins'],
    'idade':      [21, 24, 19, 22],
    'cidade':     ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'],
})

cursos = pd.DataFrame({
    'id_curso':          [101, 102, 103],
    'nome_curso':        ['Python para Dados', 'Web Design Moderno', 'Banco de Dados SQL'],
    'preco_mensalidade': [150, 120, 130],
})

matriculas = pd.DataFrame({
    'id_matricula': [1001, 1002, 1003, 1004, 1005],
    'id_aluno':     [1, 1, 2, 3, 4],
    'id_curso':     [101, 103, 101, 102, 101],
    'status':       ['Ativo', 'Ativo', 'Ativo', 'Cancelado', 'Ativo'],
})
```

> [!tip] Sempre olhe os dados depois de criar
> Use `print()` para ver uma tabela e conferir se ficou como esperado.
>
> ```python
> print(matriculas)
> ```

> [!info]- Por que cada coluna é uma lista?
> Cada lista é uma coluna, e a **posição** na lista é a linha. O primeiro valor de cada lista forma a primeira linha: `id_matricula = 1001`, `id_aluno = 1`, `id_curso = 101`, `status = 'Ativo'`. Por isso todas as listas de uma mesma tabela precisam ter o **mesmo tamanho**.

### Passo 2: juntar matrículas com alunos

Queremos trazer o **nome do aluno** para a tabela de matrículas. A coluna em comum é `id_aluno`.

```python
consolidado = pd.merge(matriculas, alunos, on='id_aluno')
print(consolidado)
```

> [!info]- O que o `merge` fez?
> Para cada linha de `matriculas`, ele procurou em `alunos` a linha com o mesmo `id_aluno` e **colou** as colunas `nome_aluno`, `idade` e `cidade` ao lado. A tabela continua com **5 linhas** (uma por matrícula), mas agora com mais colunas.

### Passo 3: juntar o resultado com cursos

Agora trazemos o **nome do curso** e o **preço**. A coluna em comum é `id_curso`.

```python
consolidado = pd.merge(consolidado, cursos, on='id_curso')

# Mostra só as colunas que interessam
print(consolidado[['id_matricula', 'nome_aluno', 'nome_curso', 'preco_mensalidade', 'status']])
```

> [!success]- Resultado esperado
>
> | id_matricula | nome_aluno | nome_curso | preco_mensalidade | status |
> | --- | --- | --- | --- | --- |
> | 1001 | Ana Silva | Python para Dados | 150 | Ativo |
> | 1002 | Ana Silva | Banco de Dados SQL | 130 | Ativo |
> | 1003 | Bruno Costa | Python para Dados | 150 | Ativo |
> | 1004 | Carlos Souza | Web Design Moderno | 120 | Cancelado |
> | 1005 | Diana Martins | Python para Dados | 150 | Ativo |

> [!check] Conferência rápida
> A tabela `consolidado` deve ter **5 linhas**, as mesmas 5 matrículas. Se tiver menos ou mais, algo deu errado no `merge`. Para contar:
>
> ```python
> print(len(consolidado))   # deve mostrar 5
> ```

---

## 📈 4. As quatro perguntas da diretoria

### ❓ Pergunta 1: Quem são os alunos com matrícula ativa?

**Em português, em dois passos:**

1. Fique só com as linhas em que o `status` é `Ativo`.
2. Mostre os nomes, **sem repetir** (a Ana tem duas matrículas).

**Complete o código:**

```python
# Passo 1: filtrar
ativos = consolidado[consolidado['status'] == '____']

# Passo 2: nomes sem repetição
print(ativos['nome_aluno'].unique())
```

> [!tip]- Dica
> O texto dentro das aspas precisa ser **exatamente igual** ao que está na coluna `status`, incluindo letra maiúscula. Olhe a tabela de matrículas.

> [!success]- Resposta
>
> ```python
> ativos = consolidado[consolidado['status'] == 'Ativo']
> print(ativos['nome_aluno'].unique())
> ```
>
> Resultado: Ana Silva, Bruno Costa e Diana Martins (o formato da lista pode variar um pouco conforme a versão do Pandas).
>
> Carlos não aparece porque a matrícula dele está `Cancelado`. Ana aparece **uma vez só** graças ao `unique()`, que significa "valores únicos, sem repetir".

> [!info]- Como funciona `consolidado[consolidado['status'] == 'Ativo']`?
> Leia de dentro para fora:
>
> 1. `consolidado['status'] == 'Ativo'` cria uma lista de **verdadeiro/falso**, um para cada linha: `[True, True, True, False, True]`.
> 2. `consolidado[ ... ]` mantém só as linhas em que o valor é `True`.
>
> É como passar uma peneira: só fica o que cumpre a condição.

### ❓ Pergunta 2: Quantas matrículas ativas há por curso?

**Em português:** com as matrículas ativas (que você já filtrou), **agrupe por curso** e **conte** quantas linhas cada curso tem.

**Complete o código:**

```python
print(ativos.groupby('____').size())
```

> [!tip]- Dica
> Queremos um grupo para cada **curso**. Qual coluna guarda o nome do curso?

> [!success]- Resposta
>
> ```python
> print(ativos.groupby('nome_curso').size())
> ```
>
> Resultado:
>
> | nome_curso | quantidade |
> | --- | --- |
> | Banco de Dados SQL | 1 |
> | Python para Dados | 3 |

> [!info]- O que é `groupby`?
> É como separar as matrículas em **pilhas**, uma pilha por curso, e depois contar quantas há em cada pilha. `.size()` é o "contador" de cada pilha.

> [!question]- Reparou que falta um curso?
> **Web Design Moderno** não aparece, porque nenhuma matrícula dele está ativa. Isso é normal no `groupby`: ele só mostra os grupos que existem nos dados filtrados. Se a diretoria quisesse ver "Web Design: 0", seria preciso um tipo de `merge` diferente (o `how='left'`). Isso está na [[atividade-analista-dados-educacionais|versão completa]].

### ❓ Pergunta 3: Qual é o faturamento mensal?

**Em português:** com as matrículas ativas, **some** a coluna `preco_mensalidade`.

**Complete o código:**

```python
total = ativos['____'].sum()
print(f'R$ {total:.2f}')
```

> [!tip]- Dica
> Use o nome da coluna que guarda o preço. E lembre: cada **matrícula** ativa paga uma mensalidade. Ana paga duas porque está em dois cursos.

> [!success]- Resposta
>
> ```python
> total = ativos['preco_mensalidade'].sum()
> print(f'R$ {total:.2f}')
> ```
>
> Resultado: **R$ 580.00**, que vem de 150 + 130 + 150 + 150.
>
> A matrícula cancelada de Carlos (120) **não entra**, porque ela já foi filtrada em `ativos`.

> [!info]- O que significa `f'R$ {total:.2f}'`?
>
> - O `f` antes das aspas permite colocar variáveis dentro do texto, entre `{ }`.
> - `:.2f` mostra o número com **2 casas decimais**.

### ❓ Pergunta 4: Qual é a idade média dos alunos de "Python para Dados"?

**Em português, em dois passos:**

1. Fique só com as linhas em que o curso é `Python para Dados`.
2. Calcule a **média** da coluna `idade`.

**Complete o código:**

```python
# Passo 1: filtrar o curso
python = consolidado[consolidado['nome_curso'] == '____']

# Passo 2: média das idades
media = python['idade'].____()
print(f'{media:.1f} anos')
```

> [!tip]- Dica
> A função que calcula a média em Pandas tem o mesmo nome da palavra em inglês: *mean*.

> [!success]- Resposta
>
> ```python
> python = consolidado[consolidado['nome_curso'] == 'Python para Dados']
> media = python['idade'].mean()
> print(f'{media:.1f} anos')
> ```
>
> Resultado: **22.3 anos**, porque (21 + 24 + 22) ÷ 3 = 22,33...
>
> Usamos `:.1f` (uma casa decimal) para não esconder a parte decimal: arredondar para 22 faria a média parecer exata.

---

## ✅ 5. Confira suas respostas

| Pergunta | Resultado esperado |
| --- | --- |
| 1. Alunos ativos | Ana Silva, Bruno Costa, Diana Martins |
| 2. Matrículas ativas por curso | Python para Dados: 3 · Banco de Dados SQL: 1 |
| 3. Faturamento mensal | R$ 580,00 |
| 4. Idade média em Python | 22,3 anos |

> [!question] Compare com o que você previu no começo
> Quantas matrículas ativas você contou à mão? (O certo é **4**.) E o faturamento? Se sua conta à mão bateu com o código, você entendeu a lógica. Se não bateu, descubra **onde** foi a diferença: ela costuma estar em uma matrícula cancelada ou em uma matrícula contada duas vezes.

---

## 🧯 Erros comuns de iniciante

> [!bug]- `=` e `==` são coisas diferentes
>
> - `=` **guarda** um valor: `idade = 21`.
> - `==` **compara** dois valores: `status == 'Ativo'` pergunta "é igual a Ativo?".
>
> No filtro, sempre use `==`.

> [!bug]- `KeyError: 'nome'`
> Você escreveu o nome de uma coluna que não existe. Confira como está escrito na tabela: aqui é `nome_aluno`, não `nome`. Para ver todos os nomes de colunas:
>
> ```python
> print(consolidado.columns)
> ```

> [!bug]- O filtro não devolve nenhuma linha
> O texto entre aspas não é exatamente igual ao dos dados. `'ativo'` (minúsculo) é diferente de `'Ativo'`. Letras maiúsculas e espaços importam.

> [!bug]- `NameError: name 'ativos' is not defined`
> Você rodou uma célula que usa `ativos` **antes** de rodar a célula que a cria. No Colab, rode as células **de cima para baixo**.

> [!bug]- `SyntaxError`
> Quase sempre é um parêntese, colchete ou aspas que ficou **aberto** sem fechar. Confira se cada `(`, `[` e `'` tem o seu par.

> [!bug]- O número de linhas depois do `merge` está estranho
> Depois de cada `merge`, use `len(tabela)` para contar as linhas. Aqui devem ser sempre **5**. Se mudou, confira se usou a coluna certa em `on=`.

---

## 📚 Mini glossário

| Termo | Significa | Exemplo |
| --- | --- | --- |
| `DataFrame` | Uma tabela no Pandas | `alunos` |
| `merge` | Junta duas tabelas por uma coluna em comum | `pd.merge(matriculas, alunos, on='id_aluno')` |
| Filtro | Mantém só as linhas que cumprem uma condição | `df[df['status'] == 'Ativo']` |
| `unique()` | Valores sem repetição | `ativos['nome_aluno'].unique()` |
| `groupby` | Separa as linhas em grupos | `groupby('nome_curso')` |
| `size()` | Conta quantas linhas há em cada grupo | `.size()` |
| `sum()` | Soma os valores de uma coluna | `['preco_mensalidade'].sum()` |
| `mean()` | Média dos valores de uma coluna | `['idade'].mean()` |
| `len()` | Quantidade de linhas | `len(consolidado)` |

---

## 🚀 Próximos passos

Quando as quatro perguntas estiverem fáceis, tente estes desafios, do mais simples ao mais difícil:

1. **Mude um dado:** troque o status da matrícula 1004 para `'Ativo'` e rode tudo de novo. **Antes de rodar**, preveja: qual será o novo faturamento? (Dica: some 120.)
2. **Nova pergunta:** quantos alunos moram em São Paulo? Use um filtro em `alunos` e `len()`.
3. **Outra soma:** qual é o faturamento **só do curso Python para Dados**? Combine filtro e `sum()`.
4. **Ordenar:** mostre os cursos do maior para o menor faturamento. Pesquise `sort_values`.
5. **Mesma atividade em SQL:** o SQLite faz as mesmas coisas com outra linguagem. Veja a [[atividade_pandas sqlite|atividade analista dados educacionais versão completa]].

> [!success] Parabéns!
> Se você chegou até aqui, já sabe **juntar tabelas, filtrar, agrupar, somar e tirar médias**. Essas cinco ações aparecem em quase toda análise de dados, de qualquer área.
