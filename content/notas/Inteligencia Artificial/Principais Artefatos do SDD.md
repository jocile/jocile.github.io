---
title: Principais Artefatos do SDD
description: "estruturando o planejamento e implementação em uma anatomia de arquivos de texto"
tags:
  - Inteligencia-artificial
---

# Principais Artefatos do SDD

Os artefatos do Spec-Driven Development ([[Spec Driven Development|SDD]]) são documentos e estruturas formais utilizados como a "única fonte da verdade" para agentes de Inteligência Artificial escreverem, validarem e iterarem código. Em vez do código fonte principal, a especificação torna-se o contrato executável do projeto.Para uma visão geral de como o SDD funciona e como agentes de IA utilizam esses artefatos para guiar o projeto:

O ecossistema do SDD baseia-se em uma anatomia de arquivos de texto (geralmente em formato Markdown) onde a intenção do software é detalhada antes de qualquer linha de código ser gerada[^1].

- **`SPEC.md`** (Especificação de Intenção):  
    O artefato mais importante. Define o *O Que* e o *Porquê*. Ele encapsula histórias de usuário (*user stories*), regras de negócio, restrições, limites de escopo e os critérios de aceitação. Deve ser agnóstico quanto à tecnologia utilizada[^2]. [spec-template.md](https://github.com/github/spec-kit/blob/main/templates/spec-template.md)
- **`CONSTITUTION.md`** (Princípios Fundamentais):  
    Comum em toolkits de código aberto como o [Spec Kit](https://blog.dsacademy.com.br/spec-driven-development-a-nova-arquitetura-de-engenharia-de-software-na-era-dos-agentes-de-ia-parte-3/), este arquivo estabelece as regras inegociáveis do projeto. Inclui a stack tecnológica, regras arquiteturais, convenções de lint, padronização de commits e políticas de acessibilidade[^1]. [constitution-template.md](https://github.com/github/spec-kit/blob/main/templates/constitution-template.md)
- **`PLAN.md`** (Estratégia Técnica):  
    Traduz a intenção abstrata do `SPEC.md` em decisões técnicas concretas. Define o *Como*: escolhas de bibliotecas, estrutura de pastas, fluxos de banco de dados e abordagens de arquitetura, servindo como o planejamento global para os subagentes[^3]. [plan-template.md](https://github.com/github/spec-kit/blob/main/templates/plan-template.md)
- **`TASKS.md`** (Tarefas e Execução):  
    Derivado do plano técnico, divide o trabalho de forma otimizada para o entendimento dos agentes. Cada tarefa define o que deve ser feito, quais arquivos serão alterados, pré-requisitos e critérios de conclusão para execução em paralelo[^4]. [tasks-template.md](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md)
- **[AGENTS.md](https://agents.md/)** (Configuração de Agentes):  
    Em abordagens multi-agentes (como o uso do [Codex](https://mmarcosab.medium.com/um-caminho-para-usar-spec-driven-development-com-codex-ba5f37efa152)), este artefato documenta a divisão de responsabilidades, por exemplo: quem é o Agente Arquiteto (especificação), o Agente Engenheiro (implementação) e o Agente Revisor (validação)[^5]. 

---

### Referências

- [Spec Driven Development (SDD): a habilidade que vai separar quem SOBREVIVE à IA - YouTube](https://www.youtube.com/watch?v=8azw00qmfVE)

[^1]: O ecossistema do SDD baseia-se em uma anatomia de arquivos de texto onde a intenção do software é detalhada antes da geração de código. [Spec-Driven Development: A Nova Arquitetura de Engenharia de Software na Era dos Agentes de IA – Parte 3 - Data Science Academy](https://blog.dsacademy.com.br/spec-driven-development-a-nova-arquitetura-de-engenharia-de-software-na-era-dos-agentes-de-ia-parte-3/)
[^2]: O artefato define o *O Que* e *Porquê*, encapsulando histórias de usuário, regras de negócio, restrições e critérios de aceitação, sendo agnóstico quanto à tecnologia. [Spec-Driven Development: A Nova Arquitetura de Engenharia de Software na Era dos Agentes de IA – Parte 2 - Data Science Academy](https://blog.dsacademy.com.br/spec-driven-development-a-nova-arquitetura-de-engenharia-de-software-na-era-dos-agentes-de-ia-parte-2/)
[^3]: O `PLAN.md` traduz a intenção abstrata em decisões técnicas concretas, definindo escolhas de bibliotecas, estrutura de pastas e abordagens arquiteturais para os subagentes. [YouTube](https://www.youtube.com/watch?v=YFDp-smGYqQ), blog DSAcademy
[^4]: O `TASKS.md` divide o trabalho em tarefas otimizadas com pré-requisitos claros e critérios de conclusão, facilitando a execução paralela dos agentes. YouTube tutorials ([Spec-Driven Development: O Fim do Vibe Coding - YouTube](https://www.youtube.com/watch?v=cAcGrs7RHBM))
[^5]: Documenta a divisão entre Agente Arquiteto (especificação), Engenheiro (implementação) e Revisor (validação). Medium blog por Marcos Abreu
