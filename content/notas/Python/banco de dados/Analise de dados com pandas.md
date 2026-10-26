---
title: Análise de dados com pandas
description: O pandas é uma biblioteca poderosa para a manipulação e análise de dados
  em Python. Ele fornece estruturas de dados rápidas, flexíveis e expressivas,…
date: '2026-09-17'
draft: false
tags:
  - banco-de-dados
  - Python
  - Pandas
---

O [[Pandas]] é uma biblioteca poderosa para a manipulação e análise de dados em Python. Ele fornece estruturas de dados rápidas, flexíveis e expressivas, projetadas para tornar o trabalho com "dados relacionais" ou "etiquetados" fácil e intuitivo. Aqui estão algumas razões pelas quais é útil instalar o `pandas`:

1. **Leitura de Dados**: Facilita a leitura de dados de várias fontes, como arquivos CSV, bancos de dados SQL, arquivos Excel, entre outros.
2. **Manipulação de Dados**: Permite operações eficientes de manipulação de dados, como filtragem, agregação, ordenação e fusão.
3. **Análise Estatística**: Oferece funções integradas para análises estatísticas e sumarização de dados.
4. **Visualização**: Facilita a criação de gráficos e visualizações de dados usando bibliotecas como `matplotlib` e `seaborn`.
5. **Integração com SQL**: Permite a integração com bancos de dados SQL para carregar e manipular dados diretamente dentro do ambiente de análise.

## Instalando o Pandas

Instale a biblioteca `pandas` utilizando o comando `pip`:

```bash
pip install pandas
```

## Exemplos de Uso do Pandas

Vamos utilizar `pandas` para realizar algumas operações de leitura e análise de dados com os dados inseridos no banco de dados SQLite.

## Leitura de Dados

Vamos carregar os dados da tabela `Produto` em um DataFrame do pandas.

```python
import pandas as pd

df_produtos = pd.read_sql_query("SELECT * FROM Produto", conn)
print(df_produtos)
```

## Análise Descritiva

Realize uma análise descritiva dos dados para obter um resumo estatístico das colunas numéricas.

```python
# Análise descritiva
print(df_produtos.describe())
```

## Filtragem e Agregação de Dados

Vamos realizar algumas operações de filtragem e agregação para entender melhor os dados.

```python
# Filtrando produtos com preço acima de 100
produtos_caros = df_produtos[df_produtos['Preco'] > 100]
print(produtos_caros)

# Agregando dados para obter a média de preços por categoria
media_precos_por_categoria = df_produtos.groupby('ID_Categoria')['Preco'].mean()
print(media_precos_por_categoria)
```

## Visualização de Dados

Crie visualizações simples para entender melhor a distribuição dos dados. Para isso, é comum usar bibliotecas como `matplotlib`.

```python
import matplotlib.pyplot as plt

# Histograma dos preços dos produtos
df_produtos['Preco'].hist(bins=10)
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.title('Distribuição de Preços dos Produtos')
plt.show()

# Gráfico de barras da média de preços por categoria
media_precos_por_categoria.plot(kind='bar')
plt.xlabel('ID da Categoria')
plt.ylabel('Preço Médio')
plt.title('Preço Médio por Categoria')
plt.show()
```

## Conclusão

A utilização do `pandas` proporciona uma interface intuitiva e poderosa para trabalhar com dados, facilitando o processo de análise e visualização.

O `pandas` é uma ferramenta essencial para qualquer cientista de dados ou desenvolvedor que trabalhe com grandes volumes de dados, fornecendo funcionalidades robustas para transformar e analisar dados de maneira eficiente.

[[atividade_pandas]]
