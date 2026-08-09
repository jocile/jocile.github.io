---
title: Estruturando projeto BookTalk
description: "como criar um aplicativo do zero usando ferramentas gratuitas versus ferramentas pagas"
tags:
  - Inteligencia-artificial/Ferramentas
  - Inteligencia-artificial/Vídeo
---

![Duas IAs Criaram Esse App SOZINHAS: Eu só assisti (Google Stitch + Antigravity é INSANO) - YouTube](https://www.youtube.com/watch?v=Mt4dH9MqYEw)

O vídeo apresenta um fluxo de trabalho de ponta a ponta para criar aplicativos usando duas IAs do Google: _Google Stitch_ para design de interface e _Antigravity_ para geração de código.

Os pontos principais incluem:

- **Visão Geral do Workflow** (1:13): O _Google Stitch_ atua como o "arquiteto", criando o design e o fluxo do aplicativo, enquanto o _Antigravity_ atua como o "engenheiro", construindo o código com base nesse design. A conexão entre as duas ferramentas é feita através do _MCP (Model Context Protocol)_, que permite que o _Antigravity_ leia o design do _Stitch_ em tempo real para gerar um código mais fiel ao layout.
- **Google Stitch** (3:11): A ferramenta foi atualizada e agora inclui um "Idea Agent" (3:47) que auxilia na ideação do produto, conversando com o usuário e fazendo perguntas para refinar o conceito antes de gerar qualquer design. O vídeo demonstra a criação de um aplicativo de resenhas de livros, o _BookTalk_, com várias telas e funcionalidades (4:18).
- **Antigravity** (6:36): O _Antigravity_ é uma IDE gratuita do Google que gera código com IA. O vídeo mostra como conectar o _Antigravity_ ao _Stitch_ via _MCP Server_ (11:00) usando uma chave de API, permitindo que o _Antigravity_ acesse e interprete os projetos do _Stitch_.
- **Construção e Teste do Projeto** (12:56): O _Antigravity_ constrói o projeto inteiro, incluindo componentes React e Next.js, rotas, autenticação e banco de dados. O vídeo demonstra a execução do aplicativo, destacando a funcionalidade de login, feed, e páginas de livros (16:09).
- **Desafios e Dicas** (17:43): O apresentador observa que, embora o projeto seja funcional, o design final do _Antigravity_ nem sempre é 100% fiel ao design do _Stitch_, especialmente em projetos maiores com muitas telas. Ele recomenda aprimorar os prompts no _Stitch_ e utilizar a funcionalidade "Annotate" para refinar detalhes. O vídeo também sugere que o _MCP_ mantém a sincronização, permitindo que o _Antigravity_ leia as atualizações do _Stitch_.
