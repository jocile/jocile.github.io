---
title: Plataformas de agentes de ia
description: plataformas para a criação de agentes de IA, cada uma com suas particularidades e níveis de complexidade. Segue uma lista categorizada para melhor compreensão
tags:
  - Inteligencia-artificial/Ferramentas
---

## Plataformas de agentes de ia

Existem diversas ferramentas e plataformas para a criação de [[agentes de ia]], cada uma com suas particularidades e níveis de complexidade. Segue uma lista categorizada para melhor compreensão:

### **Plataformas e Ferramentas com Interface Gráfica (No-Code/Low-Code)**

- **[Assistentes da OpenAI (API)](https://openai.com/index/openai-api/):** A plataforma da OpenAI, acessível via API, permite criar assistentes com instruções personalizadas (**[[System Prompt]]**), acesso opcional a documentos e ferramentas externas através de **[[Function Calling]]**. Embora seja considerada "quase de graça" devido a um bônus inicial, requer o cadastro de um cartão de crédito.
-  [Poe.com](https://poe.com/login)Esta plataforma permite interagir com diversos modelos de linguagem e criar bots personalizados. Utiliza modelos como Cloud, ChatGPT, Llama e Flux.
- [**Taskade:**](https://www.taskade.com) Apresentada como uma plataforma que combina funcionalidades de organização de projetos com agentes de IA, permitindo criar documentos e interagir com eles, além de formar equipes de agentes. Apesar de ser considerada um pouco confusa por um dos autores, oferece a possibilidade de criar times de agentes que interagem entre si.
- [relevanceai.com](https://relevanceai.com/): Oferece agentes, times de agentes, ferramentas, integrações e APIs. Possui templates para começar, e permite adicionar ferramentas, incluindo análise de áudio, e subagentes. Inclui um flow builder similar ao Zapier. Tem um plano gratuito com 100 créditos diários.
- [superagentes.ai](https://superagentes.ai/): Uma plataforma que se destaca por permitir a criação de agentes de forma gratuita, com funcionalidades como banco de conhecimento e integração com o YouTube. Oferece um programa de afiliados e planos pagos para funcionalidades avançadas. Permite criar agentes com regras específicas e extrair um padrão para otimizar.
- **Botpress, Typebot, M-chat e Voiceflow:** São mencionadas como ferramentas para criação de chatbots tradicionais ou com funcionalidades adicionais de IA.
- **[Zapier](https://zapier.com/) e [Make](https://www.make.com/en):** Ferramentas de automação que podem ser utilizadas para conectar diferentes serviços e aplicativos, incluindo agentes de IA. O Make, em particular, é destacado como uma alternativa ao Zapier, com maior flexibilidade e custos mais acessíveis.

### **Plataformas Open Source (Código Aberto)**

- **[dify.ai](https://dify.ai/):** Uma plataforma open source para criação de agentes que pode ser instalada em servidores próprios, oferecendo maior controle e privacidade dos dados. Permite criar fluxos de decisão para diferentes agentes, puxar conhecimento via API e possui um método avançado de [[RAG - Retrieval Augmented Generation]]. É considerada mais profissional e viável para produtos vendidos a clientes devido ao seu controle e personalização.
- [llama-flow](https://www.npmjs.com/package/llama-flow): Uma plataforma que se destaca pela possibilidade de criar um frontend e mini aplicativos, além de ser open source. Oferece opções para criação de agentes, flows e prompts dinâmicos, além de ter integração com diversos modelos de linguagem. Similar ao Defy, mas com a vantagem de permitir a criação de interfaces personalizadas.
- **[n8n](https://n8n.io/)**: Ferramenta de automação open source que, em conjunto com outras plataformas, permite reproduzir funcionalidades de outras plataformas de forma personalizada. É citada como uma ferramenta flexível e com potencial para integrações avançadas.

### **Bibliotecas e Frameworks de Programação (Com Código)**

- **[[Langchain]]:** Uma biblioteca para criar aplicações de IA, incluindo agentes, com foco em conectar componentes e criar cadeias de processamento (**chains**). Permite o uso de prompts, modelos de linguagem e ferramentas. Utiliza o conceito de 'react' para agentes, onde eles tomam decisões sobre qual ferramenta usar.
- **[CrewAI](https://www.crewai.com/):** Um framework para criar agentes de IA com uma estrutura de tripulação, onde agentes trabalham em conjunto para cumprir um objetivo específico. Tem uma hierarquia procedural e permite criar projetos com tarefas e ferramentas.
- **[AutoGen - Microsoft](https://microsoft.github.io/autogen/stable/index.html):** é um framework open source da Microsoft que permite a criação de aplicações usando múltiplos agentes que podem conversar entre si e usar ferramentas para atingir objetivos complexos.

### **Conceitos e Ferramentas Complementares**

- **[[RAG - Retrieval Augmented Generation]]:** Uma técnica que permite que a IA acesse e utilize informações de documentos externos para complementar seu conhecimento. Essencial para criar agentes que respondam a perguntas baseadas em dados específicos.
- **[[Function Calling]]:** Permite que agentes de IA chamem ferramentas externas e APIs.
- **[[System Prompt]]:** Instruções que definem como o agente deve se comportar.

Embora existam diversas ferramentas, os conceitos básicos para a criação de agentes de IA são similares entre elas. É recomendado experimentar várias plataformas para entender os conceitos e escolher aquela que melhor se adapta às suas necessidades. Além disso, algumas ferramentas open source como Defy e n8n são recomendadas para quem busca maior personalização e controle. O **AutoGen** é uma ferramenta para quem busca flexibilidade na criação de aplicações com múltiplos agentes.

- [[Lista de ferramentas de IA]]
