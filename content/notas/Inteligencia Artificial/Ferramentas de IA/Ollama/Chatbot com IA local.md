---
title: Chatbot com IA local
description: Como usar um processo para que o código interaja com o modelo de forma programática para realizar tarefas de geração de texto.
tags:
  - Inteligencia-artificial/Ferramentas
  - Inteligencia-artificial/Ollama
---

## Criando um Chatbot com IA local

O modelo Llama 3 pode ser usado em código [[Python]] para gerar respostas através da biblioteca [[Langchain]].

>[!summary] Em resumo, o processo de criação de um chatbot local utilizando Python, Langchain e o modelo Llama 3, abrange desde a configuração do ambiente até a implementação prática para a geração de respostas programadas. A utilização do modelo Llama 3 com [[Langchain]] em [[Python]] envolve a **importação**, a **instanciação**, a **definição do prompt**, a **invocação do modelo** e o **processamento da resposta**. Esse processo permite que o código interaja com o modelo de forma programada para realizar tarefas de geração de texto.

Para usar o Llama 3 em Python, primeiro, é necessário importar a classe [[Ollama local]] de `langchain_community.llms`. Em seguida, cria-se um objeto `Ollama` especificando o modelo a ser usado, neste caso, "Llama 3". Após instanciar o modelo, a função `invoke` é utilizada para passar um prompt e obter uma resposta.

### Passo a passo

O passo a passo para usar o modelo Llama 3 em código Python, utilizando a biblioteca [[Langchain]], é o seguinte:

Inicialmente certifique-se que a LLm local como o [Ollama local](Ollama%20local.md) está devidamente instalado para executar o [llama3.1](https://ollama.com/library/llama3.1).

#### **Importar as Bibliotecas Necessárias**

- **Importar as bibliotecas necessárias:** Inicialmente, é preciso importar as classes e funções necessárias da biblioteca [Langchain](Langchain.md). No caso do modelo Llama 3, importa-se a classe [[Ollama local]] do módulo `langchain_community.llms`.

Para começar a trabalhar com o modelo Llama 3 utilizando a biblioteca [[Langchain]], é necessário importar as classes e funções necessárias utilizando o pip. Isso inclui a classe [[Ollama local]] do módulo `langchain_community.llms`. Lembre-se de criar um ambiente virtual antes:

#### **Criando Ambiente Virtual e Instalando Bibliotecas**

Antes de começar, é importante criar um ambiente virtual para evitar conflitos com outras bibliotecas instaladas no Python padrão. Você pode usar o `python -m venv` para criar um novo ambiente virtual.

```bash
python -m venv meu-ambiente-virtual
```

Após criar o ambiente virtual, ative-o executando:

```bash
source meu-ambiente-virtual/bin/activate  # (Linux/Mac)
meu-ambiente-virtual\Scripts\activate  # (Windows)
```

Com o ambiente virtual ativado, você pode instalar as bibliotecas necessárias utilizando `pip`:

#### **Importando Bibliotecas**

Agora que as bibliotecas estão instaladas, é hora de importar as classes e funções necessárias para trabalhar com o modelo Llama 3. Você precisará da classe `Ollama` do módulo `langchain_community.llms`.

```bash
pip install langchain_community
pip install langchain langchain-ollama ollama  
```

### Importação das Classes e Funções Necessárias

Após instalar as dependências, você precisará importar as classes e funções necessárias para trabalhar com o modelo Llama 3. Isso inclui a classe `Ollama` do módulo `langchain_community.llms`.

```python
from langchain_community.llms import Ollama
```

### Configuração do Modelo

Para utilizar o modelo Llama 3, você precisará criar uma instância da classe `Ollama`. Isso pode ser feito passando as credenciais necessárias para acessar o modelo.

```python
model = Ollama()
```

Agora que você tem a instância do modelo configurada, você estará pronto para utilizar o modelo Llama 3 com a biblioteca [[Langchain]].

- **Instanciar o modelo:** Cria-se um objeto do tipo [[Ollama local]], especificando qual modelo será utilizado. Nesse caso, o modelo a ser usado é "Llama 3". Este objeto é que permitirá interagir com o modelo Llama 3. Por exemplo, a linha `model = Ollama(model="llama3")` instancia o modelo.
    
- **Definir o prompt (input):** O próximo passo é definir a entrada, ou seja, o prompt que será enviado para o modelo. Este prompt pode ser uma pergunta, uma instrução ou qualquer texto que se deseja que o modelo processe. No exemplo simples, o prompt é "hello world".
    
- **Invocar o modelo para obter uma resposta:** Utiliza-se o método `invoke` do objeto [[Ollama local]] para enviar o prompt para o modelo e obter uma resposta. O método `invoke` recebe o prompt como parâmetro e retorna a resposta gerada pelo modelo. Por exemplo, `result = model.invoke(input)` envia o input para o modelo e armazena o resultado em `result`.
    
- **Processar e utilizar a resposta:** A resposta obtida do modelo pode ser armazenada em uma variável e utilizada conforme a necessidade do programa. Em geral, a resposta é um texto que pode ser exibido para o usuário, ou usado em outras partes do código.
    

Além disso, o código Python também pode incluir outras funcionalidades, como:

- Definir parâmetros como a temperatura para controlar a aleatoriedade das respostas.
- Encapsular a chamada ao modelo em funções para facilitar o reuso do código.
- Utilizar diferentes tipos de memória para manter o histórico das interações.
- Combinar a chamada ao modelo com outros processos dentro de uma chain, que podem incluir [[Prompts]] e parsers.

É importante destacar que a biblioteca [[Langchain]] está em constante desenvolvimento, com novas funcionalidades e atualizações sendo adicionadas frequentemente, o que pode implicar mudanças na forma como os modelos são utilizados.

### Exemplos

Exemplo simplificado:

```python
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.1", base_url="http://localhost:11434",)

result = model.invoke(input="Hello world!")
print(result)

```

O código fornecido demonstra o seguinte processo:

- Importa-se a classe `OllamaLLM` da biblioteca `langchain_ollama`.
- Cria-se um objeto chamado `model` especificando o modelo "Lama 3".
- Define-se um input, neste caso, "hello world".
- Utiliza-se o método `invoke` do objeto `model` para passar o input e gerar uma resposta.
- A resposta é armazenada na variável `result`.
- Finalmente, a resposta é impressa no console.

Exemplo com função em loop:

```python
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Responda a questão abaixo.

Aqui está a conversação até agora: {contexto}

Questão: {questão}

Resposta:
"""

model = OllamaLLM(model="llama3.1", base_url="http://localhost:11434",)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    contexto = ""
    print("Bem-vindo ao chatbot! Digite 's' para sair.")
    while True:
        questao = input("Você: ")
        if questao.lower() == "s":
            break
        resultado = chain.invoke({"contexto": contexto, "questão": questao})
        print("Bot: ", resultado)
        contexto += f"\nUsuario: {questao}\nAI: {resultado}\n"


if __name__ == "__main__":
    handle_conversation()

```

O código fornecido demonstra o seguinte processo:

- Importa-se a classe `OllamaLLM` da biblioteca `langchain_ollama`.
- Cria-se um objeto `Ollama` chamado `model` especificando o modelo "Lama 3".
- Define-se um input dentro de um loop, neste caso, "s" para sair.
- Utiliza-se o método `invoke` do objeto `model` para passar o input e gerar uma resposta.
- A resposta é armazenada na variável `resultado`.
- Finalmente, a resposta é impressa no console.
- A variável `contexto` recebe a pregunta e a resposta para ser lembrada;
- O loop repete o repete o pedido de um novo `iput` com a pergunta do usuário até que seja digitado "s" para sair.

Em resumo, o código Python utiliza a biblioteca [[Langchain]] para importar o modelo Llama 3, enviando um prompt e obtendo uma resposta de forma programática.

### Referências

- [IA no seu PC com Ollama, LM Studio, GPT4All - YouTube](https://www.youtube.com/watch?v=Ar1lF4yVIss)
- [Create a LOCAL Python AI Chatbot In Minutes Using Ollama - YouTube](https://www.youtube.com/watch?v=d0o89z134CQ)
- [[Ollama local]]
- [[Langchain]]
- [[engenharia de prompt]]
