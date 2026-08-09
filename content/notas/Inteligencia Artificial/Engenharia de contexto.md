---
title: Engenharia de contexto
description: "é o processo fundamental de fornecer informações estruturadas e diretrizes claras para uma IA"
tags:
  - Inteligencia-artificial/Skill
---
# Engenharia de contexto

## Conceitos

A **engenharia de contexto** é o processo fundamental de fornecer informações estruturadas e diretrizes claras para uma IA (como no ecossistema Google [[Antigravity ide]] e Stitch), transformando-a de uma "generalista" em uma especialista no seu projeto específico. Sem essa prática, as IAs tendem a gerar resultados genéricos, o chamado "código espaguete", ou cometer erros graves, como expor chaves de API sensíveis no front-end por não conhecerem os padrões de segurança do ambiente.

### 1. Os Três Pilares da Estruturação

Para gerenciar o contexto de forma profissional, o desenvolvedor utiliza três ferramentas distintas:

- **[[Rules]] (Regras):** São diretrizes **passivas e sempre ativas** que residem no prompt de sistema. Elas definem a "personalidade" do agente, stacks preferenciais (ex: Next.js, FastAPI) e restrições inegociáveis, como proibição de código bloqueante.
- **[[Workflows]] (Fluxos de Trabalho):** São **macros manuais** disparadas pelo usuário (geralmente via comando `/`) para tarefas complexas e repetitivas, como auditorias de segurança, commits inteligentes ou o "Genesis" de um novo projeto.
- **[[Skills]] (Habilidades):** Diferente das regras, as habilidades são pacotes de conhecimento **on-demand**. Elas só são carregadas quando a IA detecta que a tarefa exige aquela expertise específica, o que ajuda a evitar a **saturação de contexto** e o desperdício de tokens.

### 2. Documentação Estratégica como Memória

A engenharia de contexto utiliza arquivos específicos para servir como "fonte da verdade" e memória de longo prazo:

- **[[Product Requirement Document|PRD]] (Documento de [[requisitos|Requisitos]] de Produto):** Definir a visão, funcionalidades e critérios de aceitação antes de gerar qualquer código evita conflitos lógicos e retrabalho futuro.
- **`design.md`:** Atua como um **contrato visual semântico**. Ele traduz valores técnicos de CSS em descrições que a IA entende (ex: mudar "rounded-lg" para "cantos suavemente arredondados"), garantindo que novas telas sigam o mesmo padrão estético sem "alucinações" visuais.
- **`GEMINI.md` ou `summary.md`:** Arquivos que funcionam como memória persistente, mantendo instruções de longo prazo e resumos de sessões anteriores para que o agente não "esqueça" decisões arquiteturais importantes.

### 3. Benefícios e Otimização

- **Redução da Dívida Técnica:** Um planejamento de contexto de 10 minutos pode evitar 10 horas de correções. Com regras bem escritas, a IA já gera o código certo de primeira em 25% a 70% dos casos, reduzindo a necessidade de code reviews manuais.
- **Gestão de Tokens:** Colocar muitas regras (ex: 50 regras) em um único projeto pode causar **"context rot" (podridão de contexto)**, onde a IA se confunde com instruções irrelevantes. Por isso, a engenharia de contexto exige ser estratégico, separando o que é essencial ([[Rules]]) do que é especializado ([[Skills]]).

Em suma, a engenharia de contexto move o papel do desenvolvedor de um "digitador de código" para um **orquestrador arquitetural**. O objetivo é guiar os agentes autônomos através de um "vibe coding" responsável, onde a intenção e a estrutura são tão importantes quanto a sintaxe final.

## Referências

- [Antigravity: O Jeito CERTO de Construir com IA - YouTube](https://www.youtube.com/watch?v=VUVy4NKV_WE)
