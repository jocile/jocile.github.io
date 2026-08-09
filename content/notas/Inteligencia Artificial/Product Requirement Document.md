---
title: Product Requirement Document
aliases:
  - PRD
  - documento de requisitos
description: documentação central que serve para instruir a inteligência artificial sobre como o projeto deve funcionar
tags:
  - Inteligencia-artificial
---

## Entendendo o Product Requirement Document (PRD) na Era da IA

>[!summary] Aprendi que o Documento de Requisitos do Produto funciona como o cérebro dinâmico que me permite orientar agentes de inteligência artificial no desenvolvimento de software, garantindo consistência técnica, evitando alucinações e servindo como um checklist de validação para os meus projetos.

O PRD é o "cérebro" dinâmico e a [[Documentacao Semantica|documentação central]] que instrui agentes de inteligência artificial sobre como um projeto de software deve funcionar.

### O que é o PRD?

No ecossistema de desenvolvimento orientado por IA (Vibe Coding) e ferramentas agênticas como o Google [[Antigravity ide]], o Product Requirement Document (PRD) evoluiu. Ele deixou de ser um artefato estático de "passagem de bastão" entre humanos para se tornar um repositório de intenção vital. 

O PRD atua como um guia estruturado que transforma você, o desenvolvedor ou idealizador, em um "gerente de projetos" perante a IA. Ele foca estritamente no **o que** o produto deve fazer, permitindo que a inteligência artificial traduza esses objetivos em arquitetura funcional e código, evitando resultados genéricos ou o temido "código espaguete".

### Por que é importante?

A criação de uma documentação técnica sólida não é burocracia, mas uma estratégia fundamental de economia de recursos e garantia de qualidade:

- **Prevenção de Erros e Retrabalho:** Um planejamento detalhado de apenas 10 minutos pode evitar 10 horas de correções futuras. A IA precisa de limites claros para não "alucinar" escopos.
- **Consistência Arquitetural:** Em projetos extensos (com 50 a 100 arquivos), o PRD fornece as diretrizes para manter a coesão que uma IA generalista poderia perder ao longo do processo.
- **Eficiência de Tokens:** Ao fornecer diretrizes técnicas claras antecipadamente, você evita o desperdício de tokens, impedindo que a IA gaste processamento tentando adivinhar soluções.
- **Base para Testes e Auditoria:** Ferramentas de segurança (como o Test Sprite) exigem um PRD em [[markdown]] para analisar se o sistema construído realmente atende aos [[requisitos]] definidos, funcionando como uma checklist de validação estruturada.

### Como Funciona

Para que um agente de IA execute um projeto com precisão cirúrgica, o PRD (geralmente nomeado como `prd.md`) deve conter uma estrutura otimizada para a compreensão da máquina. 

Um PRD "Vibe-Optimizado" inclui:

1. **Visão Geral e Personas:** O propósito do software e o público-alvo. Servem como a "Estrela do Norte" para a IA tomar decisões em casos de ambiguidades.
2. **Stack Tecnológica ou Tabela de Funcionalidades (MoSCoW):**: Definição explícita de linguagens, frameworks (ex: Next.js, FastAPI) e bancos de dados. Isso evita que a IA sugira ou utilize bibliotecas incompatíveis. Essa definição clara do que é obrigatório (_Must-have_) e do que não será incluído (_Won't-have_) serve para evitar o aumento de escopo (_scope creep_).
3. **Lista de Páginas e Fluxos de Usuário:** Mapeamento de todas as telas e o comportamento esperado ao interagir com botões ou [[Formulários]].
4. **Esquema de Banco de Dados:** Detalhamento das tabelas, relacionamentos, tipos de dados e políticas de segurança (como Row Level Security - RLS).
5. **Critérios de Aceitação e User Stories:** Instruções testáveis (formato Given-When-Then) e descrições do que o usuário deseja realizar.
6. **[[requisitos|Requisitos]] Não Funcionais:** Diretrizes claras sobre segurança (IAM, OAuth), performance e escalabilidade, que modelos generativos costumam negligenciar se não forem instruídos.
7. **Diretrizes de Design:** Referências visuais, paleta de cores e atmosfera do projeto (muitas vezes complementadas pelo arquivo `DESIGN.md`).

### Exemplos Práticos

#### Exemplo 1: Automação da Criação do PRD

Você não precisa escrever o PRD do zero manualmente. No Google [[Antigravity ide]], você pode usar **[[Workflows]]** especializados (como o "Genesis" ou o "SAS Builder"):
1. O agente de IA entra em modo de **Discovery** (Descoberta).
2. A IA realiza uma entrevista com você, fazendo perguntas de clarificação sobre orçamento, escala esperada e integrações.
3. Ao final, o agente sintetiza as respostas e gera automaticamente os artefatos de documentação, separando PRDs para frontend e backend.

#### Exemplo 2: Validação de Funcionalidades

Se o seu PRD define que "O usuário deve poder se cadastrar com e-mail e senha", o agente Antigravity usará isso como uma checklist. Após codificar, ele mapeia essa funcionalidade para um artefato (como uma captura de tela do formulário de login funcionando), provando que o requisito foi cumprido.

### Validação e Checklist

Em vez de apenas uma lista de desejos, o PRD torna-se uma **checklist de validação**. Cada funcionalidade descrita é mapeada para um **Artefato** (lista de tarefas, gravação de navegador ou captura de tela), fornecendo prova irrefutável de que o agente cumpriu os requisitos definidos no documento.

### Tópicos Relacionados

- [[Documentacao Semantica]]
- [[Antigravity ide]]
- [[Workflows]]
- [[requisitos]]
- [[Spec Driven Development]]

---
**Referências:**
- [ANTIGRAVITY Criou Meu E-commerce INTEIRO em 28 Minutos (Com UM PROMPT) - YouTube](https://www.youtube.com/watch?v=29IeTSdrWlY)
- [Antigravity: O Jeito CERTO de Construir com IA - YouTube](https://www.youtube.com/watch?v=VUVy4NKV_WE)
