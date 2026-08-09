---
title: "Agente sobre minha empresa"
description: "Como construir um modelo de linguagem que possa responder perguntas e fornecer informações baseadas em um conjunto de dados."
tags:
  - Inteligencia-artificial/Agentes 
---

## Criando um Assistente Virtual com Python e LangChain

Neste artigo, vamos criar um assistente virtual utilizando [Python](Python.md) e a biblioteca [Langchain](Langchain.md). O objetivo é construir um modelo de linguagem que possa responder perguntas e fornecer informações baseadas em um conjunto de dados.

### O Que Vamos Criar?

--------------------

Vamos criar um assistente virtual que pode:

- Responder perguntas sobre uma empresa
- Fornecer informações sobre os funcionários da empresa
- Encontrar documentos relevantes para uma pergunta específica

### Começando o Projeto

----------------------

Para começar, precisamos criar um arquivo `.env` com a chave de acesso à API da OpenAI. Em seguida, precisamos carregar o conjunto de dados em formato CSV.

#### Carregando o Conjunto de Dados

---------------------------------

Utilizaremos a biblioteca L Chain para carregar o conjunto de dados. Primeiramente, precisamos criar uma variável `Loader` e instanciar a classe `csv Loader`, passando o caminho do arquivo CSV como argumento.

```python
import csv_loader

loader = csv_loader.CsvLoader('path/to/your/data.csv')
```

Em seguida, podemos carregar os documentos utilizando o método `load`.

```python
documents = loader.load()
```

### Entendendo o RAG

-------------------

O RAG (Retrieve-Augmented Generation) é uma técnica que permite ao modelo de linguagem pesquisar no conjunto de dados e encontrar as informações mais relevantes para uma pergunta específica.

#### Criando as Embeddings

-------------------------

Para utilizar o RAG, precisamos criar as embeddings dos documentos. Isso pode ser feito utilizando a biblioteca L Chain.

```python
from lchain import berings

berings = Bering('path/to/your/model')
```

Em seguida, podemos carregar os documentos e converter para vetores.

```python
vector_store = bering.load_documents(documents)
```

### Criando o Modelo de Linguagem

------------------------------

Agora que temos as embeddings, precisamos criar o modelo de linguagem. Isso pode ser feito utilizando a biblioteca [Langchain](Langchain.md).

```python
from lchain import chat

chat = Chat('path/to/your/model')
```

Em seguida, podemos criar um prompt padrão para o modelo de linguagem.

```python
prompt_template = 'Você é o atendente de uma empresa. Seu trabalho é conversar com clientes e consultar a base de conhecimento da empresa.'
```

### Conversando com o Assistente

------------------------------

Agora que temos o modelo de linguagem, podemos conversar com ele.

```python
user_input = input('O que você gostaria de perguntar? ')
response = chat.invoke(user_input)
print(response)
```

E pronto! Agora você pode conversar com o assistente virtual que criamos.

## Referências

- [[agentes de ia]]
- [Construí uma IA que sabe tudo sobre minha empresa (Usando Python e Langchain) - YouTube](https://www.youtube.com/watch?v=xNCBS_aJTgo)
- [AI Agents: O Guia Revolucionário para Dominar a Tecnologia que Vai Comandar o Futuro](https://web.dio.me/articles/ai-agents-a-revolucao-autonoma-chegou-5d44080cf23a)
- #Inteligencia-artificial #Agentes 
