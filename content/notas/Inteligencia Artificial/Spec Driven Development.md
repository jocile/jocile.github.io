---
title: Spec Driven Development
aliases:
  - SDD
description: "estruturando o contexto através de fases de pesquisa, planejamento e implementação "
tags:
  - Inteligencia-artificial
---

# Spec-Driven Development (SDD): Escalando o Desenvolvimento com Agentes de IA

>[!summary] Eu utilizo o Spec-Driven Development para escalar o desenvolvimento de sistemas complexos com agentes de inteligência artificial, estruturando o contexto através de fases de pesquisa, planejamento e implementação para que eu possa delegar a escrita do código e focar na revisão de artefatos e análise arquitetural.

## Introdução: O Problema do Contexto em Coding Agents

Apesar dos avanços surpreendentes nos modelos de Inteligência Artificial (como Claude, GPT-4, etc.), depender exclusivamente do modelo não é suficiente para o desenvolvimento de sistemas complexos. O que separa um resultado medíocre de um sistema completo e funcional é o **contexto** fornecido ao agente. 

Muitos desenvolvedores falham ao tentar implementar grandes funcionalidades (ex: um sistema de recomendações que altera dezenas de arquivos) de duas formas:
1. Quebrando o problema em partes tão pequenas que a IA perde o contexto do todo.
2. Inserindo um [[Product Requirement Document|documento de requisitos]] (PRD) gigantesco de uma só vez, o que polui a janela de contexto, aumenta o custo de tokens e eleva drasticamente a chance de alucinações.

É aqui que entra o **Spec-Driven Development (SDD)**: um padrão de desenvolvimento focado em otimizar o contexto para obter resultados precisos, escaláveis e sem retrabalho.

## Context Engineering e o Fluxo RPI

A janela de contexto de uma IA possui limites. Quanto maior a janela, maior a chance de a IA se perder ou alucinar. Para evitar isso, o SDD utiliza o conceito de **RPI (Research, Plan, Implement)**:

1. **Research (Pesquisa):** Em uma janela de contexto ampla, o agente explora a base de código, utiliza ferramentas (MCPs) e entende o problema.
2. **Plan (Planejamento):** Todo o aprendizado da fase de pesquisa é salvo em arquivos Markdown estruturados. A janela original é descartada.
3. **Implement (Implementação):** Em uma nova janela (limpa e focada), o agente utiliza os arquivos Markdown gerados para implementar o código, economizando tokens e garantindo precisão.

## As Fases do Spec-Driven Development

O SDD estrutura o planejamento técnico e as tarefas de forma que agentes de IA tenham *guardrails* (limites) claros. O processo é dividido nas seguintes fases:

### 1. Specify (Especificação) - *Obrigatória*

A criação de uma *Spec* (Especificação) traduz o problema de negócio para um formato digerível pela IA. Uma boa spec contém:
- O problema a ser resolvido.
- Os objetivos e metas da funcionalidade.
- O que está **fora de escopo**.
- Histórias de Usuário (*User Stories*).

### 2. Design (Desenho da Solução) - *Opcional*

Para projetos maiores, as decisões arquiteturais não devem ficar repetidas em cada tarefa. O documento de design centraliza:
- Diagramas de arquitetura.
- Componentes que serão reutilizados.
- Decisões técnicas importantes.

### 3. Tasks (Quebra de Tarefas)

A IA divide o trabalho em tarefas entregáveis. O grande diferencial aqui é a **paralelização**. A ferramenta analisa o que deve ser feito de forma sequencial e o que pode ser paralelizado.  
Cada tarefa deve conter:
- O que será feito e onde (arquivos específicos).
- O que será reutilizado.
- Pré-requisitos (quais tarefas devem ser concluídas antes).
- *Definition of Done* (Critérios de Aceitação).

### 4. Implement (Implementação e Subagentes)

Na hora de codificar, em vez de sobrecarregar um único agente, o sistema utiliza **Subagentes**. Como as tarefas já estão quebradas e mapeadas, múltiplos subagentes podem ser acionados em paralelo para escrever o código de diferentes partes do sistema simultaneamente, acelerando a entrega e isolando o contexto de cada modificação.

### A "Constituição" e os Limites da IA

Agentes de IA precisam de regras claras (*Guardrails*). No SDD, cria-se um arquivo de **Constituição**, que define o que é inegociável no projeto. Exemplos de regras em uma Constituição:
- "Todos os novos métodos devem ter cobertura de testes unitários escrita antes da implementação."
- "Siga estritamente os princípios SOLID."
- "Não insira namespaces diretamente no meio do código; importe-os no topo do arquivo."

## Memória Persistente: O Arquivo STATE.md

Durante a implementação, o agente toma várias microdecisões. O SDD gera um arquivo chamado `STATE.md`, que atua como a memória do estado atual do projeto.\
Isso permite que você feche a sessão, inicie um novo agente no dia seguinte e diga: *"Continue o projeto a partir do estado atual"*. O agente lerá o `STATE.md` e retomará o trabalho exatamente de onde parou.

## O Novo Papel do Desenvolvedor

Com o SDD, a escrita braçal do código e dos testes unitários é delegada à IA. O tempo do desenvolvedor (ou Engenheiro de Agentes) é realocado para atividades de maior valor:
- **Revisão de Artefatos:** Validar se a especificação faz sentido e se as tarefas geradas cobrem todos os cenários.
- **Refinamento com PO/PM:** Utilizar comandos como `clarify` para que a IA aponte ambiguidades nos requisitos antes mesmo de escrever a primeira linha de código, melhorando a comunicação com a área de negócios.
- **Análise Arquitetural:** Garantir que a solução proposta pela IA atende aos padrões do sistema.

## Ferramentas Práticas

Para implementar essa metodologia no dia a dia, você pode utilizar:
- **[TLC Spec-Driven Skill](https://mcpmarket.com/tools/skills/spec-driven-development-tlc):** Uma [[Skills|Skill]] global altamente flexível para estruturar specs e tarefas.
- **[GitHub Spec Kit](https://github.com/github/spec-kit):** Uma ferramenta de linha de comando (`specify init`, `specify plan`) que gera a estrutura de pastas, a Constituição e os prompts necessários para a IA.


---

### Referências

#sdd #Inteligencia-artificial #Projeto 

- [[Product Requirement Document]]
- [[Principais Artefatos do SDD]]
- [Spec-Driven Development (SDD), onde o código é o detalhe final...](https://www.linkedin.com/pulse/spec-drive-development-sdd-onde-o-c%C3%B3digo-%C3%A9-detalhe-final-teixeira-tkyef/)
- [GitHub - github/spec-kit: 💫 Toolkit to help you get started with Spec-Driven Development · GitHub](https://github.com/github/spec-kit)
- [Kiro: Move beyond AI coding to agentic engineering](https://kiro.dev/)
- [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
- [What is Spec-Driven Development? \| Spec Kit Documentation](https://github.github.com/spec-kit/concepts/sdd.html)
- [spec-kit/spec-driven.md at main · github/spec-kit · GitHub](https://github.com/github/spec-kit/blob/main/spec-driven.md)
- [GitHub - Fission-AI/OpenSpec: Spec-driven development (SDD) for AI coding assistants. · GitHub](https://github.com/Fission-AI/OpenSpec/)
