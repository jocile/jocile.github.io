---
title: Antigravity Awesome Skills
description: "funcionam como superpoderes modulares que o agente de IA decide equipar apenas quando detecta que a tarefa"
tags:
  - Inteligencia-artificial/Skill
---

O **[[Antigravity ide]] Awesome [[Skills]]** refere-se a um ecossistema de repositórios e marketplaces (como o do LobeHub) que disponibiliza pacotes de conhecimento especializado para a IDE Google [[Antigravity ide]]. Essas habilidades funcionam como **"superpoderes" modulares** que o agente de IA decide "equipar" apenas quando detecta que a tarefa do usuário exige aquela expertise específica.

Abaixo, detalho as principais habilidades e o funcionamento deste ecossistema com base nas fontes:

### 1. Filosofia e Vantagens Técnicas

Diferente das _[[Rules]]_ (regras passivas sempre ativas no prompt de sistema), as habilidades utilizam o conceito de **Divulgação Progressiva (Progressive Disclosure)**.

- **Economia de Contexto:** O agente só carrega as instruções pesadas e scripts quando necessário, evitando a "saturação de contexto" e o desperdício de tokens.
- **Gatilho Automático:** Ao contrário dos _[[Workflows]]_ (macros manuais disparadas por `/`), as habilidades são **acionadas automaticamente** pelo agente ao analisar a intenção da conversa.

### 2. Habilidades de Destaque no Ecossistema

Algumas das "Awesome [[Skills]]" mais influentes mencionadas incluem:

- **`design-md` (ou `conception-md`):** É considerada essencial para o fluxo de "Vibe Coding". Ela analisa projetos do Google Stitch via MCP e sintetiza um **sistema de design semântico** no arquivo `DESIGN.md`, que serve como a "fonte da verdade" visual do projeto. Ela traduz valores técnicos (como `rounded-full`) em descrições físicas ("em formato de pílula") para garantir consistência estética.
- **`ui-ux-pro-max`:** Uma habilidade robusta que contém mais de **100 regras de design e 67 estilos de interface**. Ela é usada para auditar e melhorar automaticamente a acessibilidade, o SEO e a performance visual do código gerado.
- **`stitch-loop`:** Permite que o agente crie **múltiplos projetos e páginas de forma autônoma** no Stitch em segundo plano, iterando designs sem intervenção manual.
- **`react-components`:** Especializada em converter layouts visuais do Stitch em componentes funcionais e escaláveis em React/TypeScript.

### 3. Habilidades Utilitárias e de Segurança

O repositório também inclui ferramentas para o rigor do desenvolvimento profissional:

- **`database-schema-validator`:** Utiliza scripts determinísticos para verificar se os arquivos SQL cumprem normas de segurança, como a presença obrigatória de chaves primárias e a proibição de comandos `DROP TABLE`.
- **`git-commit-formatter`:** Garante que o agente sempre escreva mensagens de commit seguindo o padrão **Conventional Commits** (ex: `feat(auth): ...`), mantendo o histórico do projeto organizado.
- **`license-header-adder`:** Insere automaticamente cabeçalhos de licença corporativa (como Apache 2.0) em todos os novos arquivos criados, lendo templates de uma pasta de recursos para evitar "alucinações" em textos legais.

### 4. Estrutura e Instalação

Uma habilidade no [[Antigravity ide]] é organizada em um diretório contendo obrigatoriamente um arquivo **`SKILL.md`**. Este arquivo funciona como o "cérebro" da habilidade, contendo metadados YAML para indexação e instruções em [[markdown]] que definem o objetivo, passos e restrições da IA.

Para instalar essas habilidades da comunidade, o usuário pode simplesmente copiar o link do repositório GitHub e enviá-lo ao chat do [[Antigravity ide]], solicitando a adição ao projeto global ou ao workspace local.

## Referências

- [GitHub - sickn33/antigravity-awesome-skills: The Ultimate Collection](https://github.com/sickn33/antigravity-awesome-skills)
- [Antigravity + Stitch cria sites INCRÍVEIS (Nova Skill/Habilidade) - YouTube](https://www.youtube.com/watch?v=qByqXaSLUFI)
