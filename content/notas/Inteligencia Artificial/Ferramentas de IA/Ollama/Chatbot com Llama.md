---
title: Chatbot com Llama
description: "criar modelos de linguagem avançados que podem ser utilizados para realizar tarefas como responder perguntas, gerar texto e mais."
tags:
  - Inteligencia-artificial/Ferramentas
  - Inteligencia-artificial/Ollama
---

## Criando um Chatbot com Llama em Python

> [!abstract] Neste artigo, vamos criar um chatbot utilizando a tecnologia Llama (Large Language Model Meta AI) em [[Python]]. Com Llama, podemos criar modelos de linguagem avançados que podem ser utilizados para realizar tarefas como responder perguntas, gerar texto e mais.

### Instalando o Llama

Para começar, precisamos instalar o Llama em nosso computador. Isso pode ser feito baixando o aplicativo do [[Ollama local]] e seguindo as instruções de instalação.

### Configurando o Ambiente Virtual

Depois de instalar o Llama, precisamos criar um ambiente virtual para que possamos instalar as dependências necessárias para nosso projeto. Isso pode ser feito utilizando a ferramenta `python -m venv` e criando um [[Ambientes virtuais com venv]] chamado "chatbot".

### Instalando Dependências

Com o ambiente virtual criado, precisamos instalar as dependências necessárias para nosso projeto. Isso inclui o módulo [[Langchain]], que é uma biblioteca que facilita a interação com os modelos de linguagem Llama.

### Criando o Chatbot

Agora que temos as dependências instaladas, podemos criar o chatbot. Isso pode ser feito criando um novo arquivo Python chamado `main.py` e adicionando o seguinte código:

```python
import langchain
from langchain import Chain

# Crie uma instância do modelo Llama 3
model = langchain.Model.load("llama:3")

# Crie uma cadeia de operações para interagir com o modelo
chain = Chain(model=model)

# Defina a função handle_conversation para lidar com as conversas
def handle_conversation(context, question):
    # Gere uma resposta utilizando o modelo Llama
    response = chain.run(question)
    
    # Adicione a resposta ao contexto da conversa
    context += f"Bot: {response}\n"
    
    return context

# Defina a função main para iniciar a conversa
def main():
    context = ""
    while True:
        user_input = input("Usuário: ")
        
        if user_input.lower() == "exit":
            break
        
        question = user_input
        context = handle_conversation(context, question)
    
    print(context)

if __name__ == "__main__":
    main()
```

### Executando o Chatbot

Agora que temos o código do chatbot pronto, podemos executá-lo utilizando a ferramenta `python`. Isso pode ser feito digitando `python main.py` no terminal.

### Conclusão

> [!summary] Neste artigo, demos um exemplo de como criar um chatbot utilizando a tecnologia Llama em Python. Com essa tecnologia, podemos criar modelos de linguagem avançados que podem ser utilizados para realizar tarefas complexas. Esperamos que esse exemplo tenha sido útil e que você possa criar seus próprios projetos com Llama!

### Referências

- [Create a LOCAL Python AI Chatbot In Minutes Using Ollama - YouTube](https://www.youtube.com/watch?v=d0o89z134CQ)
