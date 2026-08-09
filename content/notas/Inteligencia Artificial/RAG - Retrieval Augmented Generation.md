---
title: RAG - Retrieval Augmented Generation
description: "Geração Aumentada por Recuperação, é uma abordagem que melhora a qualidade das respostas de um modelo de linguagem (LLM) ao incorporar informações de fontes externas."
tags: 
  - Inteligencia-artificial/Agentes
---

## **Retrieval Augmented Generation**

A técnica **Retrieval Augmented Generation (RAG)**, ou Geração Aumentada por Recuperação, é uma abordagem que melhora a qualidade das respostas de um modelo de linguagem (LLM) ao incorporar informações de fontes externas. Em vez de depender apenas do conhecimento pré-treinado, o RAG permite que o modelo acesse dados relevantes de um banco de dados ou documentos e use essas informações adicionais para gerar respostas mais precisas e contextuais.

### **Como o RAG funciona:**

- **Recuperação de Informação:** Quando uma pergunta é feita, um sistema de recuperação (retriever) busca documentos ou dados relevantes em uma base de conhecimento externa. Essa base de conhecimento pode ser um banco de dados vetorial, documentos de texto, planilhas ou outras fontes de informação.
- **Geração Aumentada:** As informações recuperadas são então combinadas com a pergunta original e enviadas para a LLM. O modelo usa tanto seu conhecimento pré-treinado quanto as informações adicionais para gerar uma resposta.
- **Contexto Adicional:** O RAG adiciona um contexto específico à pergunta original, permitindo que o modelo dê respostas mais completas e precisas. Isso é especialmente útil quando o modelo não possui informações específicas em seu conhecimento pré-treinado.

### **Componentes Principais do RAG:**

- **Retriever:** Responsável por buscar as informações relevantes em um banco de dados vetorial ou outras fontes de conhecimento. O método de busca do Defy parece ser muito avançado e eficiente.
- **Banco de Dados Vetorial (Vector Database):** Um tipo de banco de dados que armazena informações como vetores numéricos, permitindo buscas eficientes por similaridade semântica. A incorporação (embeddings) transforma dados em vetores que representam seu significado, facilitando o cálculo da relevância entre eles.
    - O **Chroma** é um exemplo de banco de dados vetorial que pode ser utilizado com o [[Langchain]].
    - Os dados podem ser transformados em _chunks_ (pedaços) menores, para facilitar o processo de indexação e recuperação.
    - O processo de _overlap_ garante que não se percam informações quando os dados são divididos em pedaços.
    - A relevância semântica é um método de análise que identifica a relação entre informações com base no seu significado, e não apenas nas palavras usadas.
- **LLM (Modelo de Linguagem):** O modelo de linguagem que usa as informações recuperadas e a pergunta original para gerar a resposta.
- **[[Prompts]]:** O [[Prompts|Prompt]] é uma instrução enviada para a LLM, combinando a pergunta do usuário e informações relevantes do banco de dados.

### **Aplicações do RAG:**

- **Chatbots com Conhecimento Específico:** Permite a criação de chatbots que respondem a perguntas com base em informações específicas da empresa ou domínio, como documentos, manuais ou informações de produtos.
- **[[agentes de ia]] com Acesso a Dados:** [[agentes de ia]] podem utilizar o RAG para consultar dados externos e realizar tarefas que requerem informações adicionais além de seu conhecimento pré-treinado, como analisar dados financeiros ou responder a perguntas sobre eventos recentes.
- **Geração de Conteúdo Personalizado:** O RAG possibilita a criação de conteúdo personalizado, como newsletters ou relatórios, com base em fontes de informação específicas, como dados da web ou documentos da empresa.
- **Melhoria da Precisão das Respostas:** Ao fornecer dados contextuais ao modelo, o RAG reduz o risco de respostas imprecisas ou alucinações, tornando as respostas mais confiáveis.

### **Vantagens do RAG:**

- **Precisão e Confiabilidade:** Respostas mais precisas, baseadas em fontes de dados verificáveis.
- **Personalização:** Permite a adaptação de respostas com base em informações específicas.
- **Redução de Alucinações:** Diminui a probabilidade de respostas inventadas ou sem base factual.
- **Atualização Contínua:** Facilidade em atualizar o conhecimento do modelo com novas informações sem a necessidade de retreinar o modelo.

### **Desafios do RAG:**

- **Qualidade dos Dados:** A qualidade da informação na base de conhecimento afeta diretamente a qualidade das respostas. É necessário um processo de curadoria de dados para garantir informações precisas.
- **Complexidade:** Implementar o RAG pode ser complexo e envolver diferentes componentes, como _retrievers_, bancos de dados vetoriais e modelos de linguagem.
- **Custos:** O uso de modelos de linguagem e processamento de grandes volumes de dados pode gerar custos adicionais, especialmente em modelos de _deploy_ em nuvem.

**Exemplo Prático:** * Um chatbot de suporte ao cliente pode usar RAG para responder a perguntas sobre produtos, políticas da empresa e outros assuntos específicos, utilizando um banco de dados com informações atualizadas e relevantes.

- Um agente de análise de notícias pode utilizar RAG para recuperar informações relevantes de artigos da web e gerar resumos de eventos atuais.
- Um agente de pesquisa pode usar RAG para encontrar informações relevantes em documentos PDF ou outros formatos.

>[!summary] Em resumo, o RAG é uma técnica poderosa que permite que os modelos de linguagem gerem respostas mais precisas, contextuais e personalizadas, utilizando informações de fontes externas, superando as limitações de conhecimento de modelos pré-treinados e fornecendo respostas mais confiáveis e relevantes.

### Referências

- [O que é a Técnica de Retriever Augmented Generation (RAG) - Asimov Academy](https://hub.asimov.academy/tutorial/o-que-e-a-tecnica-de-retriever-augmented-generation-rag/)
