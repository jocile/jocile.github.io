---
title: "Parâmetros de LLM"
description: "Diversos parâmetros podem ser ajustados para influenciar as respostas de um modelo de linguagem"
tags:
  - Inteligencia-artificial/LLM
---

## Configurando parâmetros da LLM

Diversos parâmetros podem ser ajustados para influenciar as respostas de um modelo de linguagem (LLM), impactando a criatividade, a precisão e o comportamento do agente de IA. Aqui estão os principais parâmetros, conforme detalhado nas fontes:

### **Temperatura**

Este é um dos parâmetros mais cruciais, pois controla o nível de aleatoriedade nas respostas da LLM.

- **Temperaturas mais altas** (próximas de 1) tornam as respostas mais criativas, variadas e até mesmo aleatórias, o que pode ser útil para geração de ideias ou textos menos formais.
- **Temperaturas mais baixas** (próximas de 0) tornam as respostas mais consistentes, determinísticas e factuais, seguindo mais rigorosamente o texto ou as informações fornecidas. Em aplicações que exigem precisão, como respostas baseadas em dados, o ideal é utilizar temperaturas baixas.

### **Top K e Top P

Esses parâmetros, relacionados com o RAG (Retrieval Augmented Generation), são utilizados para controlar como a LLM seleciona as informações mais relevantes em documentos externos. Eles afetam a similaridade e o re-ranking de resultados para obter a melhor resposta.

[System Prompt](System%20Prompt.md)

[Definindo a Personalidade do Agente de IA](Definindo%20a%20Personalidade%20do%20Agente%20de%20IA.md)

[Instrucoes Detalhadas no Prompt](Instrucoes%20Detalhadas%20no%20Prompt.md)

[Few-Shot Learning](Few-Shot%20Learning.md)

[Chain-of-Thought](Chain-of-Thought.md)

[Self-Consistency](Self-Consistency.md)

[Transformacao e Feedback](Transformacao%20e%20Feedback.md)

[Function Calling](Function%20Calling.md)

[Seletores de LLM](Seletores%20de%20LLM.md)

[Comprimento do Historico de Conversacao](Comprimento%20do%20Historico%20de%20Conversacao.md)

### **Modelos de Linguagem (LLM)**

A escolha do modelo de linguagem também afeta o comportamento e a qualidade das respostas. Modelos diferentes podem ter especialidades em diferentes tarefas, e alguns são mais adequados para tarefas específicas como resumo, tradução ou geração de código.

> [!info] É importante notar que a combinação desses parâmetros e técnicas pode gerar resultados diferentes, e é recomendado experimentar para encontrar a configuração ideal para cada aplicação. Além disso, o processo de criação de agentes de IA é interativo e requer ajustes contínuos com base no feedback do usuário e nos resultados obtidos.

### Exemplo prático

Vamos explorar um exemplo prático de como ajustar as respostas de um modelo de linguagem (LLM) utilizando a biblioteca Langchain, abordando alguns dos parâmetros e técnicas discutidas anteriormente:

**Cenário:** Criação de um tradutor de idiomas.

**Objetivo:** Construir um agente que traduza um texto fornecido pelo usuário para o idioma especificado, demonstrando o uso de prompts, modelos de linguagem e _chains_.

#### **Passo a Passo:**

1. **Configuração Inicial:**
    
    - Importação das bibliotecas necessárias do Langchain, incluindo `LLMChain`, `OpenAI`, e `PromptTemplate`.
    - Definição de uma chave de API para acessar o modelo da OpenAI.
    - Criação de uma instância do modelo de linguagem (LLM). Neste caso, usaremos um modelo da OpenAI, como o `gpt-3.5-turbo` ou `gpt-4`.
2. **Criação de um _Prompt Template_:**
    
    - Definição de um _template_ (modelo) para o prompt que será enviado para a LLM.
    - O _template_ incluirá instruções sobre a tarefa de tradução e um espaço reservado para o texto do usuário e para o idioma de destino, como em: _"Traduza o texto a seguir para {idioma}: {texto}"_.
    - Este _template_ permite que a LLM receba informações sobre o idioma para o qual traduzir e o texto a ser traduzido.
3. **Criação de uma _Chain_:**
    
    - Utilização da classe `LLMChain` do Langchain para criar uma cadeia de processamento.
    - A _chain_ combina o _prompt template_ definido no passo anterior com o modelo de linguagem (LLM) instanciado.
    - O fluxo de dados é o seguinte: o input do usuário é passado para o _prompt template_, este gera um prompt que é enviado para a LLM, que então gera uma resposta (a tradução).
4. **Execução da Tradução:**
    
    - O usuário fornece o texto a ser traduzido e o idioma de destino.
    - A _chain_ recebe o texto e o idioma de destino como _input_, o _prompt template_ gera um _prompt_ para a LLM, e a LLM retorna o texto traduzido.
5. **Ajustes e Otimização:**
    
    - **Temperatura:** Para garantir traduções mais precisas e menos aleatórias, a temperatura da LLM pode ser definida como um valor baixo (próximo de 0). Se o objetivo fosse criar traduções mais criativas, com variações estilísticas, a temperatura poderia ser ajustada para valores mais altos.
    - **System Prompt:** Caso seja desejado um tom específico para a tradução (formal, informal, etc.), um _system prompt_ poderia ser adicionado à configuração da LLM, instruindo-a sobre o estilo a ser utilizado.
    - **Exemplos (Few-Shot Prompting):** Para guiar melhor a LLM, poderiam ser adicionados exemplos de traduções no _prompt template_, mostrando como a tradução deve ser feita. Isso aumentaria a precisão e a qualidade da tradução.

#### **Exemplo de Código (Simplificado):**

```python
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Substitua pela sua chave de API da OpenAI
os.environ["OPENAI_API_KEY"] = "sua_chave_api"

# Inicialização do modelo de linguagem (LLM)
llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.2)  # Ajuste a temperatura

# Criação do prompt template
template = "Traduza o texto a seguir para {idioma}: {texto}"
prompt = PromptTemplate(template=template, input_variables=["idioma", "texto"])

# Criação da chain
chain = LLMChain(llm=llm, prompt=prompt)

# Texto a ser traduzido
texto_original = "Olá, mundo! Como você está?"
idioma_destino = "francês"

# Execução da tradução
resultado = chain.run(idioma=idioma_destino, texto=texto_original)

print(f"Texto original: {texto_original}")
print(f"Tradução para {idioma_destino}: {resultado}")

```

**Explicação do Código:**

- O código demonstra o uso de um modelo `OpenAI` para executar a tradução.
- O _template_ do _prompt_ é criado, definindo como a LLM deve interpretar a entrada.
- A _chain_ combina a LLM e o _prompt_ para traduzir o texto.
- A temperatura da LLM é ajustada para 0.2, o que faz com que a resposta seja mais precisa e menos aleatória.

**Resultado Esperado:**

O código deverá imprimir a tradução do texto para o idioma especificado. Por exemplo, para o texto "Olá, mundo! Como você está?" traduzido para francês, a saída seria algo como:

```
Texto original: Olá, mundo! Como você está?
Tradução para francês: Bonjour le monde! Comment allez-vous?
```

#### **Observações:**

- Este é um exemplo simplificado para ilustrar o conceito, outras funcionalidades da Langchain podem ser usadas para otimizar a precisão e a qualidade da tradução.
- O código pode ser expandido com outros parâmetros de configuração para a LLM, como `max_tokens` para limitar o comprimento das respostas, bem como a escolha de outros modelos de linguagem como o Llama 2 e Gemini.
- É possível utilizar a técnica de RAG (Retrieval Augmented Generation) se a tradução precisar de conhecimento específico e não trivial.

Este exemplo prático ilustra como os parâmetros e técnicas discutidos podem ser utilizados para modular as respostas de uma LLM de forma eficaz, aplicando conceitos como prompts, _chains_, e ajuste da temperatura.

### Referência

- [Tutorial básico de Langchain aprenda a desenvolver apps com ChatGPT, LLaMA, e Gemini - Vídeo 0 - YouTube](https://www.youtube.com/watch?v=nXynNB6XzAM&list=PLEx1BRi5A-snmGcMfJQyTpCAW6M0MUQi1)
