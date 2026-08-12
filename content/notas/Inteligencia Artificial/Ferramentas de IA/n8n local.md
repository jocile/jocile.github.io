---
title: N8N local
tags:
  - Inteligencia-artificial/Ferramentas
description: "é uma plataforma de automação de fluxo de trabalho de código aberto e baseada em nós."
---

# Automação Inteligente e Agentes de IA

## Como Instalar o n8n

Você pode rodar o n8n localmente para estudos ou em um servidor para produção.

## 1. Configurar o Ollama (Hospedeiro)

Conectar o Ollama local ao n8n rodando em Docker exige atenção à rede, pois o contêiner do n8n precisa acessar o sistema hospedeiro (host).

O Ollama precisa aceitar conexões externas e não apenas do `localhost` local.

- Linux:
    
    - Execute `sudo systemctl edit ollama.service`.
    - Adicione as linhas:
        
```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```
        
    - Salve e reinicie: `sudo systemctl daemon-reload && sudo systemctl restart ollama`. [1, 2]
    
- Windows:
    
    - Feche o Ollama na barra de tarefas.
    - Abra o Terminal (PowerShell) e defina a variável: `setx OLLAMA_HOST "0.0.0.0"`.
    - Reinicie o Ollama. [3]
    
- Mac:
    
    - Feche o Ollama por completo.
    - Abra o Terminal e execute: `launchctl setenv OLLAMA_HOST "0.0.0.0"`.
    - Abra o aplicativo Ollama novamente. [4]
    

## 2. Configurar o n8n (Docker) [5]

O n8n precisa apontar para o IP correto da máquina hospedeira.

- No Linux:
    
    - Use a flag `--add-host` para mapear o host.
    - Comando para rodar o n8n:
        
```bash
docker run -d --name n8n -p 5678:5678 --add-host=host.docker.internal:host-gateway n8nio/n8n
```
        
    
- No Windows / Mac:
    
    - O Docker já mapeia o host automaticamente.
    - Comando padrão para rodar o n8n:
        
```bash
docker run -d --name n8n -p 5678:5678 n8nio/n8n
```
        
        [6, 7]
    

## 3. Configurar o Nó no n8n

Dentro da interface web do n8n (geralmente em `http://localhost:5678`): [8]

1. Crie um novo fluxo de trabalho (Workflow).
2. Adicione o nó Ollama Chat Model ou Ollama Embeddings.
3. Clique em Create New Credential (Criar Nova Credencial).
4. No campo Base URL, insira: `docker.internal`.
5. Salve a credencial.
6. No campo Model, digite o nome exato do modelo baixado (ex: `llama3`, `mistral`). [9, 10, 11]

Se você deseja avançar na automação, me informe:

- Qual sistema operacional você está usando no computador?
- Qual modelo de IA (LLM) você pretende rodar no Ollama?
- Qual é o objetivo final do seu fluxo de trabalho no n8n?

Com esses detalhes, posso fornecer o comando Docker Compose exato ou um exemplo de fluxo pronto.

  

[1] [https://www.itflashcards.com](https://www.itflashcards.com/blog/pt/ollama-openwebui-ejecuta-llm/)

[2] [https://dev.to](https://dev.to/lmartns/como-instalar-e-rodar-uma-ia-localmente-no-seu-computador-25nb)

[3] [https://pt.linkedin.com](https://pt.linkedin.com/pulse/ollama-windows-guia-completo-de-instala%C3%A7%C3%A3o-dos-santos-filho-qjmcf)

[4] [https://pt.linkedin.com](https://pt.linkedin.com/pulse/ollama-windows-guia-completo-de-instala%C3%A7%C3%A3o-dos-santos-filho-qjmcf)

[5] [https://www.reddit.com](https://www.reddit.com/r/AI_Agents/comments/1l59h5x/how_do_i_setup_n8n_locally_with_dockerterminal/?tl=pt-br)

[6] [https://www.dio.me](https://www.dio.me/articles/comunicacao-entre-containers-e-o-host-usando-o-hostdockerinternal-20c273fafe24)

[7] [https://especialistan8n.com.br](https://especialistan8n.com.br/instalacao-do-n8n/)

[8] [https://www.datacamp.com](https://www.datacamp.com/pt/tutorial/local-ai)

[9] [https://horadecodar.com.br](https://horadecodar.com.br/tutorial-instalacao-n8n-passo-a-passo/)

[10] [https://www.hostinger.com](https://www.hostinger.com/br/tutoriais/como-integrar-n8n-com-ollama)

[11] [https://www.hostinger.com](https://www.hostinger.com/br/tutoriais/n8n-api)

## Tipos de instalação

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

4. Acessando a rede local:
`docker run -d --name n8n -p 5678:5678 --add-host=host.docker.internal:host-gateway n8nio/n8n`

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

## Integrações com mais de 400 serviços

O [[n8n]] conta com uma biblioteca de integrações que conecta rapidamente diferentes serviços e aplicativos. O n8n pode automatizar tarefas e economizar tempo com integrações como:

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

## Templates

Com mais de [1000 templates prontos](https://n8n.io/workflows/) para diversos cenários, o n8n é ideal quando se precisa de uma solução prática, rápida e adaptável. Ele é recomendado para quem busca eficiência em tarefas como leitura e resposta automática de mensagens, categorização de dados e notificações automáticas.

## Auto-hospedado (Self-hosted)

A versão de código aberto é **gratuita** e permite execuções praticamente ilimitadas (limitadas apenas pela capacidade do seu servidor). É a escolha ideal se você tem conhecimentos técnicos, precisa manter dados sensíveis internamente (LGPD/compliance) ou quer escalar sem pagar por execução.

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
- Aprofunde-se em [[Inteligência Artificial]] e [[notas/Inteligencia Artificial/Machine Learning/index|Machine Learning]].

## Referências

- [GitHub - n8n-io/n8n: Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. · GitHub](https://github.com/n8n-io/n8n)
- [Tutorial: Build an AI workflow in n8n \| n8n Docs](https://docs.n8n.io/advanced-ai/intro-tutorial/)
- [Building AI Agents: Chat Trigger, Memory, and System/User Messages Explained \[Part 1\] - YouTube](https://www.youtube.com/watch?v=yzvLfHb0nqE)
- [Do zero a seu primeiro agente de IA em 20 minutos (sem codar, com n8n) - YouTube](https://www.youtube.com/watch?v=DgxHP1LG5dM)
- [Curso N8N Gratuito Para Iniciantes 2026 \| Crie Automações com IA - YouTube](https://www.youtube.com/watch?v=-Ka4YKW7RwM)
- [É o fim do Python para automações? \| 3 projetos com N8N - YouTube](https://www.youtube.com/watch?v=l2cL07vsYMw)
