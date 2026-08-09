---
title: OpenClaw
description: "um assistente pessoal capaz de realizar diversas tarefas"
tags:
  - Inteligencia-artificial/Agentes
  - Inteligencia-artificial/Ferramentas
---

## Agente pessoal OpenClaw

É uma ferramenta de IA que promete ser um assistente pessoal capaz de realizar diversas tarefas, como gerenciar e-mails, mensagens de WhatsApp e agendamentos (0:13-0:22). Ele pode ser executado localmente ou em um VPS (0:30) e se conecta a IAs existentes como a Open AI (4:48).

## Características

- **Nome e Popularidade** (1:09): Inicialmente lançado com outros nomes como Cloud Bot e Mbot, o [OpenClaw](https://github.com/openclaw/openclaw) é o nome definitivo. A ferramenta ganhou grande popularidade, com mais de 116.000 estrelas no GitHub e milhões de visitantes em uma semana (2:31-2:44).
- **Funcionalidades** (3:55): **==Ele funciona como um aplicativo de bate-papo==**, tem memória persistente para manter o contexto das conversas (4:11), controla o navegador (4:21) e executa comandos na máquina do usuário (4:32). Além disso, é compatível com "agent skills", que permitem a criação de novas funcionalidades, como processar PDFs e preencher formulários (7:11-8:19).
- **Segurança e Riscos** (2:50): Apesar de ser uma ferramenta de código aberto, ainda está em fase beta e apresenta riscos de segurança. O acesso a dados sensíveis, a capacidade de tomar ações destrutivas e a possibilidade de "prompt injection" são preocupações (15:00-15:56). O vídeo demonstra como a ferramenta pode acessar pastas do computador do usuário se tiver permissão (14:14-14:29).
- **Recomendações de Segurança** (9:29): Para mitigar os riscos de segurança ao implantar localmente, é recomendado o uso de Docker, que restringe as operações a um contêiner (10:03-10:08). O vídeo também menciona a Hostinger como uma opção de VPS com soluções prontas para instalação em um clique e um cupom de desconto (10:11-11:18).
- **Controle de Custos** (12:01): É crucial monitorar o uso de tokens ao conectar o OpenClaw a APIs pagas, como a Open AI, para evitar custos elevados (12:01-12:23).

## Automatização

O OpenClaw automatiza a web através do seu **controle de navegador** (4:21).

Ele consegue:

- Acessar um navegador da sua máquina, como o _Brave_ (4:26-4:29).
- Realizar **várias ações** no navegador (4:30-4:31).
- **Preencher formulários** em sites (7:31).
- **Navegar na internet** para você (0:59-1:07).

Essa capacidade permite que o OpenClaw execute tarefas como **comprar leite em um site toda segunda-feira**, se você o instruir a fazer isso (7:02-7:09). Além disso, ele consegue acessar e manipular o navegador se este já tiver autenticações salvas (15:46-15:52).

## Aprendizagem do OpenClaw

O OpenClaw inova com as "skills" (ou habilidades) através de um formato chamado **agent skills** (7:13-7:14), que permite que o agente aprenda a usar diferentes ferramentas.

As principais inovações com as skills são:

- **Extensão de funcionalidades**: As skills permitem que o OpenClaw realize tarefas específicas para as quais não foi originalmente programado. Por exemplo, ele pode processar PDFs, extrair textos e tabelas, preencher formulários e juntar documentos (7:55-8:03).
- **Facilidade de criação e modificação**: É **bem simples** implementar novas skills (7:44-7:46), e os usuários podem criar as suas próprias, modificar as existentes ou utilizar as disponíveis em um **hub de skills** (7:22-7:37).
- **Formato intuitivo**: O formato das skills é em **markdown** (7:53-7:54), o que torna a criação e compreensão dessas habilidades mais acessível, mesmo para quem não tem conhecimento técnico avançado (7:48-7:51).
- **Estrutura pronta**: O repositório do OpenClaw oferece uma estrutura pronta para a criação de skills, incluindo referências e assets (8:08-8:19), facilitando o processo de desenvolvimento.

Essa capacidade de estender e personalizar as funcionalidades através das skills é um dos grandes diferenciais do OpenClaw (3:57-3:59).

## Cuidados com a segurança

O OpenClaw é considerado perigoso principalmente devido ao **alto nível de acesso** que ele exige ao computador do usuário (9:34).

Os principais motivos para essa periculosidade são:

- **Vazamento de dados sensíveis** (15:02): Ele processa entradas não confiáveis e pode expor informações confidenciais se não for configurado corretamente. O vídeo mostra um caso em que o OpenClaw revelou o local de arquivos com chaves de API (13:52-14:07) e outros casos de vazamento de dados através de injeção de prompt via e-mail (16:09-16:17).
- **Acesso a dados confidenciais e ações destrutivas** (15:17): Por ter acesso à máquina do usuário, ele pode tomar ações externas que comprometem a integridade dos dados ou até mesmo realizar ações destrutivas (15:28-15:36).
- **Alto privilégio e autonomia** (15:31): A ferramenta pode executar comandos no Shell, modificar arquivos do sistema e navegar no navegador, o que a torna capaz de causar grandes danos se for mal utilizada (15:38-15:56).
- **Vulnerabilidades em desenvolvimento**: Por ser uma ferramenta ainda em beta e considerada "rudimentar" por alguns especialistas, ela pode apresentar falhas e "alucinações", ou seja, comportamentos imprevisíveis que podem levar a ações indesejadas.

É crucial que, ao utilizar o OpenClaw, o usuário tenha **total controle sobre a segurança** da ferramenta (13:34) e siga as recomendações para se proteger, como utilizar Docker para restringir o acesso a um contêiner (10:03).

## Referências

- Fonte: [A FEBRE OPENCLAW! - YouTube](https://www.youtube.com/watch?v=5WJEKNEYb6Y)
- [NÃO instale o OpenClaw no seu computador pessoal \| OpenClaw: além do hype, quais são os riscos? - YouTube](https://www.youtube.com/watch?v=gcnlX8pu0Ug)
  