---
title: Como criar agentes de ia
description: Anotações sobre criação de Agentes de IA usando frameworks
tags:
  - Inteligencia-artificial/Agentes
  - Inteligencia-artificial/Ferramentas 
---

# Como criar agentes de IA

![Como criar agentes de IA que não quebram seu código (Mastra AI + Typescript) - YouTube](https://www.youtube.com/watch?v=QoiqFrdGpAA)

Como criar agentes de IA poderosos usando **Mastra AI**, **Tavli** e **MCP** com **TypeScript**, visando simplificar o desenvolvimento de IA para desenvolvedores (0:00-1:12).

**Principais pontos abordados:**

- **Mastra AI:** É um framework que permite construir agentes de IA em **TypeScript**, mantendo o projeto tipado e familiar aos desenvolvedores, evitando a necessidade de microsserviços em Python (1:06-1:35). Foi criado pela mesma equipe por trás do Gatsby JS, com foco na experiência do desenvolvedor (1:37-2:15).
- **Estabilidade e Adoção:** O Mastra AI é uma ferramenta nova (lançada em 2024 na versão 1.0) e está se estabilizando. É recomendado para quem busca uma solução mais robusta para orquestrar fluxos complexos de IA, como workflows, RAGs e memória, sem a complexidade de outras ferramentas (2:40-4:05).
- **Pilares do Mastra:** Seus princípios fundamentais incluem agentes, workflows, streaming, MCPs, memórias, RAGs e workspaces (6:13-6:41). Um **workspace** é um ambiente sandbox que permite que o agente de IA crie e delete arquivos de forma autônoma sem afetar o projeto principal (6:24-6:41).
- **Mastra Studio:** É uma ferramenta que visualiza e gerencia os agentes, workflows e outras configurações da IA. Permite testar ferramentas e fluxos de forma isolada, além de oferecer observabilidade dos logs e uso da IA (8:11-9:14, 21:13-22:21).
- **Tavily:** Uma API de pesquisa inteligente em tempo real, ideal para agentes de IA que precisam pesquisar na internet, extrair informações e fazer web crawling. Oferece créditos de API gratuitos por mês e um plano profissional acessível (12:06-13:20).
- **Evitando Loops e Travamentos:** O vídeo destaca a importância de entender os princípios da IA para evitar que os agentes entrem em loops infinitos ou demorem excessivamente para concluir tarefas. O uso do comando "Esc" pode ajudar a interromper esses processos (15:09-15:43).
- **Contexts e MCP:** O Mastra AI pode ativar automaticamente "Contexts" e "MCPs" (Multi-Context Processing), que são mecanismos que permitem à IA ler e entender documentações de ferramentas como o Tavli, sem que o desenvolvedor precise fazer isso manualmente (15:53-16:32).
- **Aprendizado e Documentação:** A IA pode ser usada para aprender novas tecnologias mais rapidamente, criando agentes que pesquisam e resumem informações. Além disso, a IA pode documentar automaticamente o que foi feito em um projeto para facilitar o estudo e a revisão (10:04-10:50, 23:22-24:06).
- **Teste e Evolução:** O vídeo incentiva o teste prático do Mastra AI para avaliar sua aplicabilidade em diferentes projetos e como ele pode auxiliar no desenvolvimento de IA (27:45-29:11).

## Mastra AI

[Mastra AI](https://mastra.ai/docs) se destaca por várias razões, principalmente por focar na **experiência do desenvolvedor** e na **simplificação da criação de agentes de IA** dentro de um ambiente familiar de desenvolvimento (2:10-2:15):

- **Integração com TypeScript:** Permite construir agentes de IA mantendo todo o projeto tipado e organizado, integrando-se ao fluxo de trabalho existente do desenvolvedor (1:06-1:12).
- **Facilitação de Agentes Complexos:** Simplifica a orquestração de **workflows**, **RAGs** (Retrieval Augmented Generation) e gerenciamento de **memória** para agentes de IA, que geralmente são tarefas complexas (2:33-2:47).
- **Foco na Experiência do Desenvolvedor (DX):** Prioriza uma "developer experience" (DX) mais agradável e eficiente, tornando a criação de IA menos burocrática e mais intuitiva (2:47-3:08).
- **Ambientes Isolados (Workspaces):** Oferece a funcionalidade de "workspaces" (6:24-6:41), que são ambientes sandbox para os agentes de IA operarem, permitindo criar, deletar e manipular arquivos de forma autônoma sem impactar o código ou o projeto principal.
- **Mastra Studio:** Proporciona uma interface visual robusta para depuração, visualização e teste de agentes, workflows e ferramentas. Isso inclui observabilidade completa, permitindo ver tudo o que o agente está fazendo (8:11-9:14, 20:25-22:21, 26:06-26:20).
- **Automatização Inteligente:** Utiliza **Contexts** e **MCPs** (Multi-Context Processing) para que os agentes de IA leiam e compreendam documentações automaticamente, ativando ferramentas e funcionalidades quando necessário, reduzindo o esforço manual do desenvolvedor (15:53-16:32).
- **Flexibilidade de Integração:** Pode ser integrado em diversos tipos de projetos e frameworks, como Next.js, Astro, Svelte e Express (7:41-7:51).
