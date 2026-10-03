---
title: Pandas
description: uma biblioteca de código aberto em Python, usada principalmente para manipulação e análise de dados
date: '2026-09-17'
draft: false
tags:
  - programador/Python/arquivos
---

## Manipulando arquivos com Pandas

Imagine que você tem uma caixa mágica onde pode colocar todos os seus brinquedos, organizá-los, limpá-los e até mesmo transformá-los em novas formas! No mundo dos dados, temos uma ferramenta mágica chamada **Pandas** que faz exatamente isso. Com ela, você pode ler dados de diferentes fontes, limpá-los, filtrá-los e transformá-los do jeito que quiser. Neste artigo, vamos explorar como usar essa biblioteca incrível de maneira simples e divertida. Prepare-se para se tornar um mestre na manipulação de dados com Pandas!

## O que é Pandas?

Pandas é uma biblioteca de código aberto em Python, usada principalmente para manipulação e análise de dados. Ela oferece estruturas de dados e operações para manipular tabelas numéricas e séries temporais de forma fácil e eficiente. Com Pandas, você pode realizar tarefas como leitura de dados, limpeza, transformação e análise de maneira simplificada.

## Utilidade Prática do Pandas

Pandas é extremamente útil em várias áreas, incluindo:

1. **Análise de Dados**: Analistas de dados usam Pandas para limpar, filtrar e transformar dados antes de fazer análises mais profundas.
2. **Ciência de Dados**: Cientistas de dados utilizam Pandas para preparar os dados antes de aplicarem modelos de machine learning.
3. **Engenharia de Dados**: Engenheiros de dados usam Pandas para processar e transformar grandes volumes de dados antes de armazená-los ou movê-los para outras plataformas.
4. **Automação de Processos**: Em projetos de automação, Pandas pode ser usado para processar e analisar dados automaticamente, sem intervenção manual.

## Começando com Pandas

Para começar a usar o Pandas, você precisa instalá-lo. Isso pode ser feito usando o pip:

```bash
pip install pandas
```

Depois de instalado, podemos importar a biblioteca em nosso script Python:

```python
import pandas as pd
```

Saiba mais sobre o PIP: [Modulos em Python](Modulos%20em%20Python.md)

## Leitura e Gravação de Arquivos de Texto

Vamos começar lendo dados de um arquivo CSV. Suponha que temos um arquivo chamado `dados.csv` que contém informações sobre brinquedos.

### Exemplo de Arquivo CSV (`dados.csv`)

```csv
nome,idade,preco
Boneca,30.0
Carrinho,50.0
Trem,45.0
```

Para ler este arquivo em um DataFrame do Pandas, usamos a função `read_csv`:

```python
df = pd.read_csv('dados.csv')
print(df)
```

### Saída

```markdown
       nome  idade  preco
0    Boneca      5   30.0
1  Carrinho      8   50.0
2      Trem      7   45.0
```

### Gravação em um Arquivo de Texto (CSV)

Depois de manipular os dados, podemos salvá-los em um novo arquivo CSV:

```python
df.to_csv('saida.csv', index=False)
```

O parâmetro `index=False` diz ao Pandas para não incluir números de linha no arquivo Excel, como se disséssemos "não precisamos de etiquetas de linha".

## Leitura e Gravação de Arquivos Excel

Além de arquivos CSV, o Pandas pode ler e escrever arquivos Excel. Vamos ver como fazer isso.

### Leitura de um Arquivo Excel

```python
df_excel = pd.read_excel('dados.xlsx')
print(df_excel)
```

### Gravação em um Arquivo Excel

Depois de manipular os dados, podemos salvá-los em um arquivo Excel:

```python
df.to_excel('saida.xlsx', index=False)
```

## Manipulação de Dados em SQLite

Pandas também pode se conectar a bancos de dados SQLite para ler e gravar dados.

### Criando uma Conexão com SQLite

Para isso, precisamos da biblioteca `sqlite3`:

```python
import sqlite3
conn = sqlite3.connect('dados.db')
```

### Leitura de Dados do SQLite

Podemos ler dados de uma tabela SQLite usando a função `read_sql`:

```python
df_sql = pd.read_sql('SELECT * FROM brinquedos', conn)
print(df_sql)
```

### Gravação de Dados no SQLite

Podemos gravar um DataFrame em uma tabela SQLite usando a função `to_sql`:

```python
df.to_sql('brinquedos', conn, if_exists='replace', index=False)
```

## Limpeza de Dados

Os dados que lemos nem sempre estão prontos para uso imediato. Às vezes, precisamos limpar esses dados, removendo valores ausentes ou corrigindo inconsistências.

### Preenchendo Valores Ausentes

Quando trabalhamos com dados do mundo real, frequentemente encontramos valores ausentes (também conhecidos como NaN - Not a Number). Esses valores podem surgir por vários motivos, como erros na coleta de dados ou informações incompletas. No Pandas, podemos lidar com esses valores ausentes de várias maneiras. Uma abordagem comum é preencher esses valores ausentes com uma estatística como a média, mediana ou moda.

Vamos detalhar como preencher valores ausentes com a média da coluna. Suponha que nosso DataFrame `df` tenha algumas idades ausentes:

#### Exemplo de DataFrame com Valores Ausentes

```python
import pandas as pd

data = {
    'nome': ['Boneca', 'Carrinho', 'Trem'],
    'idade': [5, None, 7],
    'preco': [30.0, 50.0, 45.0]
}
df = pd.DataFrame(data)
print(df)
```

#### Saída

```py
       nome  idade  preco
0    Boneca    5.0   30.0
1  Carrinho    NaN   50.0
2      Trem    7.0   45.0
```

Como podemos ver, o valor da idade para "Carrinho" está ausente. Vamos preencher este valor ausente com a média das idades presentes na coluna.

#### Passo a Passo para Preencher Valores Ausentes

1. **Calcular a Média da Coluna `idade`**:\
   A primeira etapa é calcular a média dos valores existentes na coluna `idade`. No Pandas, podemos fazer isso facilmente usando o método `.mean()`.

   ```python
   media_idade = df['idade'].mean()
   print(f"Média da coluna 'idade': {media_idade}")
   ```

   #### Saída

   ```py
   Média da coluna 'idade': 6.0
   ```

2. **Preencher Valores Ausentes com a Média**:\
   Agora que temos a média, usamos o método `.fillna()` para substituir os valores ausentes pela média calculada. O parâmetro `inplace=True` é usado para modificar o DataFrame original diretamente.

   ```python
   df['idade'].fillna(media_idade, inplace=True)
   print(df)
   ```

   #### Saída

   ```shell
          nome  idade  preco
   0    Boneca    5.0   30.0
   1  Carrinho    6.0   50.0
   2      Trem    7.0   45.0
   ```

### Explicação Detalhada dos Comandos

- `df['idade'].mean()`: Calcula a média dos valores na coluna `idade`, ignorando automaticamente os valores ausentes.
- `df['idade'].fillna(media_idade, inplace=True)`: Preenche os valores ausentes na coluna `idade` com a média calculada. O parâmetro `inplace=True` garante que a alteração seja feita no DataFrame original, sem necessidade de criar uma cópia.

### Importância da Limpeza de Dados

Limpar dados ausentes é uma etapa crucial na preparação de dados para análise. Valores ausentes podem distorcer os resultados da análise e afetar negativamente os modelos de machine learning. Ao preencher valores ausentes, estamos assegurando que nossos dados estejam completos e prontos para a próxima etapa da análise.

### Exemplo Completo

Vamos ver um exemplo completo que inclui a leitura de dados, preenchimento de valores ausentes, e filtragem e transformação dos dados, e finalmente salvando os dados processados em um arquivo Excel.

```python
import pandas as pd

# Dados de exemplo com valores ausentes
data = {
    'nome': ['Boneca', 'Carrinho', 'Trem'],
    'idade': [5, None, 7],
    'preco': [30.0, 50.0, 45.0]
}
df = pd.DataFrame(data)

# Preenchendo valores ausentes na coluna 'idade' com a média
df['idade'].fillna(df['idade'].mean(), inplace=True)

# Filtrando dados onde o preço é maior que 40
df_filtrado = df[df['preco'] > 40]

# Aumentando o preço dos brinquedos filtrados em 10%
df_filtrado['preco'] = df_filtrado['preco'] * 1.1

# Salvando o DataFrame filtrado e transformado em um arquivo Excel
df_filtrado.to_excel('brinquedos_filtrados.xlsx', index=False)

print("Dados processados e salvos com sucesso!")
```

## Filtragem e Transformação de Dados

Depois de limpar os dados, podemos querer filtrar e transformar esses dados. Vamos supor que queremos selecionar apenas os brinquedos com preço superior a 40 e aumentar o preço em 10%.

### Filtrando Dados

```python
df_filtrado = df[df['preco'] > 40]
print(df_filtrado)
```

### Saída

```shell
       nome  idade  preco
1  Carrinho    6.0   50.0
2      Trem      7   45.0
```

### Transformando Dados

Vamos aumentar o preço dos brinquedos filtrados em 10%.

```python
df_filtrado['preco'] = df_filtrado['preco'] * 1.1
print(df_filtrado)
```

### Saída

```shell
       nome  idade  preco
1  Carrinho    6.0   55.0
2      Trem      7   49.5
```

## Salvando o Resultado

Podemos salvar os dados filtrados e transformados em um novo arquivo CSV, Excel ou banco de dados SQLite para uso futuro.

### Salvando em CSV

```python
df_filtrado.to_csv('brinquedos_filtrados.csv', index=False)
```

### Salvando em Excel

```python
df_filtrado.to_excel('brinquedos_filtrados.xlsx', index=False)
```

### Salvando em SQLite

```python
df_filtrado.to_sql('brinquedos_filtrados', conn, if_exists='replace', index=False)
```

## Conclusão

E aí, o que achou da nossa jornada pelo mundo mágico do Pandas? Com essa poderosa biblioteca, transformar dados se torna tão divertido quanto brincar com seus brinquedos favoritos!

Você aprendeu a ler e salvar arquivos de texto, Excel e banco de dados SQLite, além de limpar e preparar dados, filtrar e transformar informações. Agora, você está pronto para enfrentar desafios de análise de dados que aparecerem pelo caminho.

Não se esqueça de seguir nas redes sociais para mais aventuras no mundo dos dados e truques incríveis de programação! Vamos juntos continuar explorando e descobrindo novas maneiras de fazer mágica com dados.
