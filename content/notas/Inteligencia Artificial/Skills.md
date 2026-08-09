---
title: Skills
aliases:
  - Skill
description: "são como playbooks que a IA lê para executar tarefas específicas, tornando-se especialista no seu negócio"
tags:
  - Inteligencia-artificial/Skill
---

# Skills

- As skills são como "playbooks" (manuais) que a IA lê para executar tarefas específicas, tornando-se especialista no seu negócio. 
- Prometem superar os "agentes" tradicionais, pois se adaptam melhor ao seu estilo de trabalho. 
- São definidas como pacotes de conhecimento especializado que estendem as capacidades dos agentes de IA de forma modular e sob demanda. 
- Elas atuam como o "cérebro" que direciona as ferramentas, transformando um modelo generalista (como o Gemini 3) em um especialista capaz de seguir padrões rigorosos e executar tarefas complexas

## Skills x agentes

- **Agentes vs. Skills** (0:39):
    - **Agentes:** Operam de forma autônoma e usam um "system prompt" com todas as instruções.
    - **Skills:** São "playbooks" que a IA lê sob demanda, com um "system prompt" mais enxuto que apenas indica a disponibilidade das skills.

|                   | Agentes                                          | Skills                                                                          |
| ----------------- | ------------------------------------------------ | ------------------------------------------------------------------------------- |
| O que é           | IAs que agem de forma autónoma                   | Playbooks que ensinam a IA a agir do seu jeito                                  |
| Modelo            | ✅                                                | ✅                                                                               |
| [[System Prompt]] | Todas instruções ficam no System Prompt          | System Prompt leve + skills ([[Prompts]]) carregados [[Workflows\|sob demanda]] |
| Tools             | Definidas na arquitetura do agente               | Podem estar na skill como scripts                                               |
| Memória           | Requer arquitetura externa (ex: RAG/ banco etc)  | Skill é a memória procedural (escrita uma vez, lida sempre)                     |
| Manutenção        | É mais fixo e difícil de evoluir (requer deploy) | Aprende conforme você usa                                                       |

As "skills" superam os "agentes" por várias razões, conforme explicado no vídeo:

- **Conhecimento Personalizado**: As skills resolvem o problema dos agentes que, por mais inteligentes que sejam, não conhecem a sua forma de trabalhar. Elas atuam como manuais que a IA lê antes de operar, tornando-se especialista no seu negócio e melhorando com o uso.
- **[[System Prompt]] Mais Enxuto e Eficiente**: Enquanto os agentes tradicionais precisam ter todas as instruções no "[[System Prompt]]", as skills permitem que o "[[System Prompt]]" seja mais limpo, apenas indicando a disponibilidade dos "playbooks" externos (as skills). O conteúdo detalhado da skill é carregado apenas quando necessário ([[Workflows]]).
- **Memória que Melhora com o Tempo (Retroalimentação)**: As skills têm a capacidade de melhorar com o tempo através da retroalimentação. Conforme você interage com o agente que usa uma skill, você pode pedir para ele registrar o que aprendeu, fazendo com que a skill evolua e se torne mais inteligente. Isso não é uma característica padrão dos agentes sem um banco externo.
- **Manutenção Simplificada** (3:12-3:36): A manutenção e evolução das skills são mais fáceis. Você pode instruir o agente a registrar novas informações na skill durante a conversa, sem a necessidade de fazer "deploy" (publicar uma nova versão) como é exigido na manutenção de agentes tradicionais.
- **Progressive Disclosure (Preservação da Janela de Contexto)**: As skills utilizam a janela de contexto de forma mais eficiente. Elas são carregadas apenas quando são necessárias, preservando a janela de contexto e tornando a IA mais efetiva. O "[[System Prompt]]" do agente apenas lista os nomes e descrições curtas das skills disponíveis, carregando o conteúdo completo de uma skill apenas se ela for solicitada ou ativada. Isso evita lotar a janela de contexto com informações que não são relevantes para a tarefa atual, o que acontece quando todas as instruções estão diretamente no "[[System Prompt]]" do agente.

## Ferramentas

- **Ferramentas e Memória**:
    - Skills podem usar "tools" (ferramentas) como scripts, semelhante aos agentes.
    - Skills possuem uma memória que melhora com o tempo, permitindo a retroalimentação e aprendizado.
- **Manutenção Simplificada**:
    - A manutenção de skills é mais fácil, sem necessidade de deploy, pois o aprendizado ocorre durante a interação.
- **O que são Skills na Prática**:
    - Skills são como "pastinhas" com arquivos dentro, como um manual de identidade de marca ou um guia para montar propostas comerciais.
    - A criadora demonstra uma skill para gerar ideias de vídeos do YouTube, que contém arquivos com instruções, dados de performance e referências de thumbnails.
    - A vantagem de serem "pastinhas" é a possibilidade de versionamento, permitindo melhorias ao longo do tempo.
- **Skills e Ferramentas (Scripts)**:
    - Skills podem chamar scripts como ferramentas, combinando a natureza não-determinística da IA com a determinística do código.
    - Isso permite que a skill execute ações específicas, como aplicar um branding em uma apresentação de PowerPoint.
- **Vantagens na Janela de Contexto**:
    - Skills utilizam a janela de contexto de forma eficiente, carregando apenas o necessário, o que os pesquisadores chamam de "progressive disclosure".
    - Ao contrário dos agentes que carregam tudo ou nada, as skills carregam apenas uma breve descrição, e só o conteúdo completo quando necessário.
- **Construindo uma Skill do Zero**:
    - A criadora demonstra como criar uma skill no Claude, mostrando que o próprio Claude pode auxiliar no processo.
    - Ela cria uma skill para gerar propostas comerciais, que inclui um roteiro de perguntas, estrutura padrão da proposta e informações sobre a consultoria Donus.
    - A skill gerada pode criar propostas em formatos como Word, PDF e PowerPoint.
- **Resultado Final e Conclusão**:
    - A proposta é gerada em PDF, mostrando que a skill funciona efetivamente.
    - A criadora ressalta a velocidade e a qualidade do resultado, mas também sugere melhorias futuras, como a integração da identidade visual.

## Exemplos Práticos e Integrações

Habilidades poderosas disponíveis para o ecossistema:

- **Stitch Skills:** Quando integradas ao Google Stitch via MCP ([[Model Context Protocol]]), permitem converter layouts em arquivos **design.md** (fonte da verdade), gerar componentes **React/TypeScript** modulares e criar o **Stitch Loop** (automação para gerar múltiplas páginas em segundo plano).
- **Desenvolvimento Geral:** Formatadores de mensagens de **Git Commit** seguindo padrões convencionais, adicionadores de cabeçalhos de licença corporativa e conversores de JSON para modelos Pydantic.
- **Auditorias e Performance:** Skills que realizam varreduras automáticas de **SEO**, verificam a performance web do projeto ou validam esquemas de banco de dados contra políticas de segurança internas

## Referências

- [Estenda Claude com skills - Claude Code Docs](https://code.claude.com/docs/pt/skills)
- [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Agente de IA é coisa do passado. Agora eu só uso SKILLS. - YouTube](https://www.youtube.com/watch?v=h_l8wCr7M2Q)
- [Antigravity Skills: A novidade MAIS INSANA (vai te dar superpoderes) - YouTube](https://www.youtube.com/watch?v=xhlSi0Sc6dc)
- [Agora a Anthropic revolucionou TUDO de novo! - YouTube](https://www.youtube.com/watch?v=yPoSJbLxbS8)
- [[Antigravity Awesome Skills]]
- [[Antigravity Kit]]
- [[Repositorios de Skills]]
