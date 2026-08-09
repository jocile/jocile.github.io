---
title: N8N
tags:
  - Inteligencia-artificial/Ferramentas
description: "é uma plataforma de automação de fluxo de trabalho de código aberto e baseada em nós."
---

# Entendendo o n8n: Automação Inteligente e Agentes de IA

Aprenda o que é o n8n, como funcionam seus fluxos de trabalho visuais, como instalá-lo e como criar seu primeiro Agente de Inteligência Artificial passo a passo.

## Visão Geral

 Com mais de [1300 integrações disponíveis](https://n8n.io/integrations/) , o ** [n8n](https://n8n.io/)** é uma plataforma de automação de fluxo de trabalho ([[Workflows|Workflow]] automation) de código aberto e baseada em nós (nodes). Ele permite que você conecte diferentes aplicativos, APIs e bancos de dados para que eles conversem entre si, automatizando tarefas repetitivas. 

Para estudantes, desenvolvedores e profissionais de TI, o n8n atua como uma ponte integradora. Você pode transformar processos manuais (como salvar leads em planilhas ou responder e-mails de suporte) em rotinas automáticas e inteligentes, sem precisar codificar tudo do zero.

## Por que escolher o n8n?

Ao contrário de outras ferramentas populares, o n8n oferece uma combinação única de interface visual com flexibilidade de código. 

![[O que é o n8n e como ele pode automatizar suas tarefas-1778362901340.png]]

### Integrações com mais de 400 serviços

O n8n conta com uma biblioteca de integrações que conecta rapidamente diferentes serviços e aplicativos. O n8n pode automatizar tarefas e economizar tempo com integrações como:

- [ActiveCampaign](https://www.activecampaign.com/)
- [Dropbox](https://www.dropbox.com/home)
- [Google Docs](https://docs.google.com/document/u/0/?pli=1)
- [HubSpot](https://br.hubspot.com/)
- [Mailchimp](https://mailchimp.com/pt-br/)
- [Mautic](https://www.mautic.org/)
- [Telegram](https://web.telegram.org/k/)
- [Todoist](https://todoist.com/pt-BR)
- [Trello](https://www.atlassian.com/br/software/trello)
- [WhatsApp](https://www.whatsapp.com/?lang=pt_BR) (via Twilio)

A plataforma open-source permite que qualquer pessoa construa integrações entre ferramentas de comunicação, armazenamento em nuvem e outras soluções amplamente utilizadas no dia a dia. Por exemplo, o n8n é capaz de automatizar respostas a e-mails, organizar arquivos no [Google Drive](https://workspace.google.com/intl/pt-BR/products/drive/) ou até mesmo interagir com redes sociais como o YouTube por meio de configurações visuais, sem precisar codificar.

### Templates

Com mais de [1000 templates prontos](https://n8n.io/workflows/) para diversos cenários, o n8n é ideal quando se precisa de uma solução prática, rápida e adaptável. Ele é recomendado para quem busca eficiência em tarefas como leitura e resposta automática de mensagens, categorização de dados e notificações automáticas.

### n8n vs Zapier

O Zapier é excelente para automações simples e rápidas (A -> B). No entanto, o n8n brilha quando você precisa de fluxos de trabalho longos, lógica avançada (loops, condicionais IF/ELSE), manipulação de dados em JSON e, principalmente, quando deseja fugir de custos altos por execução, graças à sua opção de auto-hospedagem.

### n8n vs Python

Se você já programa, pode se perguntar: *"Por que não fazer tudo em Python?"*
- **Use o n8n** para criar integrações rapidamente, aproveitar conexões prontas (como Google Sheets, Slack, Trello) e ter uma interface visual para depurar (debug) onde o fluxo quebrou.
- **Use [Python](https://www.python.org/)** quando o processo exigir cálculos matemáticos complexos, algoritmos próprios ou manipulação de dados em altíssimo volume que exijam performance pura.

## Preços e Planos

O n8n oferece dois caminhos principais: a nuvem oficial (Cloud) ou a auto-hospedagem (Self-hosted). O [n8n oferece três opções de planos](https://n8n.io/pricing/) – **Iniciador**, **Pro** e **Empresa**.

### Opções Cloud (Hospedado pelo n8n)

Ideal se você quer começar rápido e não quer gerenciar servidores.
- **Starter:** Focado em iniciantes. Oferece 2.500 execuções/mês e passos ilimitados. Ótimo para validar automações simples.
- **Pro:** Para pequenos times ou "solo builders". Aumenta para 10.000 execuções/mês e adiciona recursos de histórico e variáveis globais.
- **Business:** Focado em governança corporativa, com 40.000 execuções/mês, controle de versão (Git) e ambientes de teste (dev/prod).

### Auto-hospedado (Self-hosted)

A versão de código aberto é **gratuita** e permite execuções praticamente ilimitadas (limitadas apenas pela capacidade do seu servidor). É a escolha ideal se você tem conhecimentos técnicos, precisa manter dados sensíveis internamente (LGPD/compliance) ou quer escalar sem pagar por execução.

## Como Instalar o n8n

Você pode rodar o n8n localmente para estudos ou em um servidor para produção.

### Opção 1: Instalação Local (para estudos)

Se você já tem o [Node.js](https://nodejs.org/) instalado em seu computador:

1. Abra o terminal.
2. Execute o comando para instalar globalmente:
   `npm install n8n -g`
3. Inicie a plataforma:
   `n8n start`
4. Acesse no seu navegador: `http://localhost:5678`

### Opção 2: Servidor local via Docker (para estudos)

Usando [Docker](https://docs.n8n.io/hosting/installation/docker/)

1. Abra o terminal.
2. Execute o comando para instalar globalmente:

```shell
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

3. Acesse no seu navegador: `http://localhost:5678`

### Opção 3: Servidor VPS via Docker (Para produção)

Se você possui um servidor (como DigitalOcean ou AWS) com Docker instalado, crie um arquivo `docker-compose.yml`:

```yaml
version: '3'
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    volumes:
      - ~/.n8n:/home/node/.n8n
```
Em seguida, rode `docker-compose up -d` e acesse via IP do servidor na porta `5678`.

---

## A Nova Fronteira: n8n e Inteligência Artificial

O  [n8n](https://n8n.io/) evoluiu e agora possui o recurso **Advanced AI**, permitindo criar **Agentes de IA** (AI Agents) diretamente nos seus fluxos. Em vez de apenas seguir regras estritas, os Agentes tomam decisões baseadas em objetivos e podem usar ferramentas para buscar informações.

### Passo a Passo Prático: Criando um Agente de Pesquisa com IA

Neste tutorial, vamos criar um assistente que recebe uma pergunta no chat, pesquisa na Wikipedia e devolve a resposta resumida.

#### Antes de Começar
- Você precisa ter o n8n rodando (local ou nuvem).
- Ter uma chave de API de um modelo de linguagem (ex: OpenAI GPT-4o-mini).

#### Passos

**Passo 1: Crie o Gatilho de Chat**
1. Na tela em branco do n8n, clique em **Add first step**.
2. Pesquise e selecione o nó **Chat Trigger**. Este nó fornecerá uma interface de chat no próprio n8n para testarmos.

**Passo 2: Adicione o "Cérebro" (AI Agent)**
1. Clique no conector `+` à direita do *Chat Trigger*.
2. Pesquise e adicione o nó **AI Agent**. Ele avaliará a pergunta do usuário e decidirá o que fazer.

**Passo 3: Conecte o Modelo de Linguagem**
1. Na parte inferior do nó *AI Agent*, clique no `+` abaixo de **Chat Model**.
2. Selecione **OpenAI Chat Model** (ou outro de sua preferência).
3. Abra este nó, insira sua chave de API (Credentials) e escolha o modelo (ex: `gpt-4o-mini`).

**Passo 4: Adicione Memória (Window Buffer Memory)**
Para que a IA lembre do contexto da conversa e não apenas da última mensagem:
1. Volte ao nó *AI Agent* e clique no `+` abaixo de **Memory**.
2. Selecione **Window Buffer Memory**.
3. Defina o "Window Size" (ex: 5). Isso fará a IA lembrar das últimas 5 interações, economizando tokens da sua API.

**Passo 5: Equipe a IA com Ferramentas (Wikipedia)**
1. No nó *AI Agent*, clique no `+` abaixo de **Tools**.
2. Selecione a ferramenta **Wikipedia**.
3. Agora, a IA tem autonomia para criar consultas de busca e ler artigos da Wikipedia quando não souber uma resposta.

**Passo 6: Configure e Teste**
1. Abra o nó *AI Agent*, vá em **Options** e adicione uma **System message**.
2. Digite: *"Você é um assistente de pesquisa útil. Sempre pesquise na Wikipedia antes de responder perguntas factuais."*
3. Clique em **Chat** na parte inferior da tela do n8n.
4. Teste perguntando: *"Quem ganhou o prêmio Nobel de Física em 2023?"* e, em seguida, teste a memória perguntando: *"De qual país eles são?"*.

## Verifique se Funcionou

Você saberá que teve sucesso quando a janela de chat do n8n responder à sua pergunta com informações precisas e recentes, e você puder ver no histórico de execução que o nó da Wikipedia foi ativado automaticamente pelo Agente.

## Próximos Passos

- Explore a criação de fluxos conectando o n8n a planilhas ou ao Trello.
- Leia mais sobre a teoria de agentes em Engenharia de [[agentes de ia]].
- Aprofunde-se em [[Inteligência Artificial Overview-|Inteligência Artificial]] e [[Machine Learning]].

## Referências

- [GitHub - n8n-io/n8n: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. · GitHub](https://github.com/n8n-io/n8n)
- [Tutorial: Build an AI workflow in n8n \| n8n Docs](https://docs.n8n.io/advanced-ai/intro-tutorial/)
- [Building AI Agents: Chat Trigger, Memory, and System/User Messages Explained \[Part 1\] - YouTube](https://www.youtube.com/watch?v=yzvLfHb0nqE)
- [Do zero a seu primeiro agente de IA em 20 minutos (sem codar, com n8n) - YouTube](https://www.youtube.com/watch?v=DgxHP1LG5dM)
- [Curso N8N Gratuito Para Iniciantes 2026 \| Crie Automações com IA - YouTube](https://www.youtube.com/watch?v=-Ka4YKW7RwM)
- [É o fim do Python para automações? \| 3 projetos com N8N - YouTube](https://www.youtube.com/watch?v=l2cL07vsYMw)
