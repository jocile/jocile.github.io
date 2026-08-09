---
title: Comparativo ferramentas gratuitas versus pagas
description: "como criar um aplicativo do zero usando ferramentas gratuitas versus ferramentas pagas"
tags:
  - Inteligencia-artificial/Ferramentas
  - Inteligencia-artificial/Vídeo
---

# Comparativo usando ferramentas gratuitas versus pagas

![Dá Pra Criar um App Profissional Só com Ferramentas Free? - YouTube](https://www.youtube.com/watch?v=FbS2uEw9GIk)

O vídeo demonstra como criar um aplicativo do zero usando ferramentas gratuitas versus ferramentas pagas/profissionais, comparando as diferenças entre elas.

## **Visão Geral do Aplicativo e Ferramentas** (0:00-0:41)

- O aplicativo desenvolvido é um sistema de agendamento de banho e tosa para pets.
- **Ferramentas Gratuitas:** O desenvolvimento utiliza Stitch para design, Google AI Studio para geração de código, Supabase para banco de dados e backend, e Vercel para hospedagem.
- **Ferramentas Pagas/Profissionais:** O processo envolve Claude Code para geração de código, PostgreSQL direto na VPS para banco de dados e Vercel para hospedagem.

## As ferramentas utilizadas no vídeo

- **Ferramentas gratuitas:**    
    - Stitch (0:47-2:25)
    - Google AI Studio (2:25-3:30)
    - Supabase (8:13-9:16)
    - Vercel (para hospedagem)
- **Ferramentas pagas/profissionais:**    
    - Claude Code (45:23-46:01)
    - PostgreSQL (55:40-59:02)
    - TestSprite (1:09:30-1:17:12)
    - Vercel (para hospedagem)
    - Next.js (1:23:38)
    - Prisma (1:24:03)

## **Processo de Criação do Aplicativo (Versão Gratuita)**

- **Design com Stitch** (0:47-2:25): O vídeo mostra como usar o Stitch, uma ferramenta do Google, para criar designs de interface de usuário.
- **Geração de Código com Google AI Studio** (2:25-3:30): O design do Stitch é exportado para o Google AI Studio, que gera a primeira página do aplicativo.
- **Desafios com Supabase e RLSs** (8:13-9:16): O Supabase é uma boa ferramenta para banco de dados e backend, mas o sistema de RLSs (Row Level Security) pode complicar funcionalidades avançadas, como sistemas multi-inquilino com vários níveis de acesso.
- **Dificuldades e Limitações do Modelo Gratuito** (14:30-15:47): Ferramentas gratuitas podem apresentar lentidão, exigir mais trabalho para correção de erros e serem menos eficientes para construir aplicações robustas e complexas.
- **Configuração do Supabase** (22:47-23:46): Demonstração da criação de um novo projeto no Supabase, configurando nome, senha e habilitando a API de dados e RLSs.
- **Problemas de Autenticação e Armazenamento de Imagens** (29:13-32:25): São destacados problemas comuns como a dificuldade de salvar imagens e a ocorrência de _loops_ devido à complexidade de gerenciar permissões no Supabase, enfatizando a necessidade de atenção extra ao usar ferramentas gratuitas para aplicações mais robustas.

### Workflow usado com ferramentas gratuitas

O [[Workflows|Workflow]] utilizado com as ferramentas gratuitas no vídeo para criar o aplicativo é o seguinte:

1. **Design da Interface (Stitch)** (0:47-2:25): O processo começa com a criação do design da interface do usuário no Stitch, uma ferramenta do Google.
2. **Geração de Código (Google AI Studio)** (2:25-3:30): O design do Stitch é exportado para o Google AI Studio, que automaticamente gera o código para a primeira página do aplicativo.
3. **Backend e Banco de Dados (Supabase)** (8:13-9:16, 22:47-23:46): O Supabase é utilizado para configurar o banco de dados e o backend do aplicativo. Ele lida com a segurança e o acesso dos usuários através de RLSs (Row Level Security) e funções.
4. **Hospedagem (Vercel)**: Após o desenvolvimento, o aplicativo é hospedado na Vercel, que oferece opções de hospedagem gratuita e paga.

## **Processo de Criação do Aplicativo (Versão Paga/Profissional)**

- **Utilização do Claude Code e VPS** (45:23-46:01): O vídeo explica como instalar a extensão Claude Code e utilizar uma VPS (Servidor Virtual Privado) para hospedar o banco de dados e o aplicativo.
- **Configuração do Banco de Dados PostgreSQL na VPS** (55:40-59:02): O Cloud Code é usado para auxiliar na configuração do PostgreSQL 16 na VPS, incluindo a criação do banco de dados e a obtenção da URL de conexão.
- **Implementação de Autenticação e Funcionalidades** (1:00:35-1:01:21): O Claude Code auxilia na implementação de autenticação e outras funcionalidades no aplicativo, com o código sendo gerado e implementado automaticamente.
- **Funcionalidades Completas com o Modelo Pago** (1:04:45-1:09:07): O aplicativo no modelo pago demonstra o cadastro de pets, agendamento de serviços, edição de informações e gerenciamento de status de agendamentos, tudo funcionando de forma fluida e sem as dificuldades encontradas no modelo gratuito.
- **Testes de Segurança com TestSprite** (1:09:30-1:17:12): O TestSprite é introduzido como uma ferramenta essencial para verificar a segurança do aplicativo, analisar o front-end e o back-end, e identificar erros ou vulnerabilidades.
- **Deploy na Vercel** (1:17:14-1:22:36): O projeto é preparado para o deploy na Vercel, incluindo a criação de um repositório no GitHub, o _push_ do código e a configuração das variáveis de ambiente para o deploy. O vídeo mostra a atualização em tempo real do aplicativo online após as alterações.

### Workflow usado com ferramentas pagas

O [[Workflows|Workflow]] utilizado com as ferramentas pagas no vídeo para criar o aplicativo é o seguinte:

1. **Hospedagem e Banco de Dados (VPS com PostgreSQL)** (44:33-46:41): O processo começa com a configuração de uma VPS (Virtual Private Server) e a instalação do PostgreSQL como banco de dados direto na VPS.
2. **Desenvolvimento e Refatoração (Claude Code)** (45:05-53:00): O Claude Code é usado como ambiente principal para desenvolver e refatorar o aplicativo. Ele permite converter projetos de diferentes frameworks (como React para Next.js) e integra funcionalidades de backend e frontend.
3. **Conexão com Banco de Dados (Prisma)** (54:28-55:10): O Prisma é utilizado como ORM (Object-Relational Mapping) para facilitar a conexão e manipulação do banco de dados PostgreSQL na VPS.
4. **Autenticação (JWT)** (1:23:58-1:24:01): Um sistema de autenticação JWT ([[json]] Web Token) é implementado para gerenciar o acesso dos usuários de forma segura.
5. **Testes de Segurança e Funcionalidade (TestSprite)** (1:09:30-1:17:12): O TestSprite é empregado para verificar a segurança e funcionalidade do aplicativo, identificando possíveis erros ou falhas.
6. **Deploy e Automação (Vercel)** (1:09:09-1:20:00): O projeto é preparado e enviado para a Vercel para o deploy, e o Claude Code automatiza o processo de commit e push para o repositório, garantindo

## Monetização e cotas

No ecossistema atual de ferramentas agênticas do Google ([[Antigravity ide]] e Stitch), a distinção entre planos gratuitos e pagos envolve principalmente **limites de uso (cotas)**, **capacidade de raciocínio dos modelos** e **infraestrutura de hospedagem**.

Abaixo estão os detalhes sobre como funcionam essas modalidades conforme as fontes:

### 1. Google Antigravity e AI Studio

- **Acesso Gratuito:** O [[Antigravity ide]] está disponível em "Public Preview" sem custo para indivíduos com contas pessoais do Gmail. Ele oferece uma cota gratuita para usar modelos premium como o Gemini 3 Pro.
- **Limites de Taxa (Rate Limits):** No plano gratuito, as APIs têm limites que, se atingidos, podem bloquear o uso por algumas horas (geralmente 4 a 5 horas) ou até dias.
- **Opções Pagas:** Para uso profissional e ininterrupto, recomenda-se uma assinatura do Google (como o plano Pro de aproximadamente R$ 389/mês citado nas fontes), que garante limites maiores e evita esperas pelo reset das cotas. No Google AI Studio, o usuário pode configurar um método de pagamento no Google Cloud para continuar usando a ferramenta via chave de API própria caso esgote a cota gratuita.

### 2. Google Stitch

- **Cota Mensal Gratuita:** O Stitch é gratuito via Google Labs, mas opera com um sistema de créditos mensais que resetam a cada 30 dias.
- **Limites por Modo:**
    - **Modo Padrão (Gemini 2.5 Flash):** Até **350 gerações** por mês.
    - **Modo Pro/Experimental (Gemini 2.5 Pro):** Entre **50 e 200 gerações** por mês, permitindo maior fidelidade e uso de imagens de referência.
- **Perspectiva Futura:** Como é um produto experimental, o Google pode introduzir planos pagos ou ajustar essas cotas conforme a ferramenta amadurece.

### 3. Hospedagem e Produção

Embora a criação do software possa ser gratuita, mantê-lo online exige decisões sobre planos:

- **Vercel/Netlify:** Oferecem planos **Hobby (gratuitos)** para projetos pessoais. O plano gratuito da Vercel, por exemplo, é limitado a cerca de 50.000 visualizações por mês.
- **Hostinger (VPS):** É uma opção **paga** (ex: planos a partir de R$ 35/mês) necessária para quem deseja que a aplicação rode 24h por dia em um servidor dedicado, independente do computador local estar ligado.

### 4. Diferença Estratégica (Free vs. Pro)

Embora o plano gratuito seja excelente para **MVPs e prototipagem rápida**, as ferramentas pagas (como o Claude Code pago) oferecem um **raciocínio superior**, cometem menos erros básicos e são preparadas para **alta escala** e sistemas robustos que envolvem pagamentos e segurança complexa. Além disso, o uso de **[[Skills|Skill]]** e **[[Workflows|Workflow]]** no [[Antigravity ide]] ajuda a economizar tokens, o que é crucial para gerenciar os custos em qualquer um dos planos.

## **Comparativo e Conclusões Finais** (1:22:47-1:26:39)

- Há diferenças significativas entre as ferramentas gratuitas e pagas.
- **Ferramentas Gratuitas:** Ideais para aplicativos básicos com poucas funcionalidades (CRUD simples). Podem levar a mais erros, frustrações e exigir mais tempo de desenvolvimento para funcionalidades complexas.
- **Ferramentas Pagas/Profissionais:** Oferecem uma estrutura mais robusta e eficiente, permitindo o desenvolvimento de aplicações complexas e em alta escala com menos [[Prompts]] e erros.
- O modelo pago utiliza um backend separado com Next.js e Prisma, e um sistema de autenticação JWT, enquanto o modelo gratuito usa o Supabase como backend base.

## Conteúdo relacionado

Aqui estão alguns vídeos relacionados sobre como criar aplicativos, com foco em ferramentas gratuitas e IA:

- **As 4 Melhores IAs para criar aplicativos completos 100% de graça - sem codigo** [http://www.youtube.com/watch?v=bVZwPlv6df4:](http://www.youtube.com/watch?v=bVZwPlv6df4:) Este vídeo apresenta quatro IAs que permitem criar aplicativos completos sem código e de forma gratuita.
- **Como Criei UM APP com IA pra Vender em 12 horas** [http://www.youtube.com/watch?v=KnaW6AxXdCo:](http://www.youtube.com/watch?v=KnaW6AxXdCo:) Compartilha a experiência de criar um aplicativo usando IA em um curto período de tempo.
- **O Google fez de novo: Crie e Publique Apps 100% GRÁTIS com o Google AI Studio** [http://www.youtube.com/watch?v=U4XNeOAsoq4:](http://www.youtube.com/watch?v=U4XNeOAsoq4:) Um vídeo que explora como criar e publicar aplicativos gratuitamente usando o Google AI Studio.
- **Testei 9 IAs que CRIAM APPS! Qual é a MELHOR em 2025?** [http://www.youtube.com/watch?v=fAJr-fGQsQE:](http://www.youtube.com/watch?v=fAJr-fGQsQE:) Este vídeo testa nove plataformas de IA para criação de aplicativos para determinar qual é a melhor em 2025.

[Criado com ![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-16dp/logo_gemini_2025_color_2x_web_16dp.png)Gemini](https://gemini.google.com/)
