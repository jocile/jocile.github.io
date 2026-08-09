---
title: Antigravity IDE
tags:
  - Inteligencia-artificial/Ferramentas
description: "permite que agentes de IA ajam de forma proativa no código, terminal e navegador, enquanto o desenvolvedor atua como um supervisor ou regente."
---

## Google Antigravity

O [Antigravity](https://antigravity.google/) é um **IDE Agêntico** (Agentic IDE) desenvolvido pelo Google, projetado como um ambiente de desenvolvimento "agent-first". Diferente de IDEs tradicionais que apenas oferecem assistência de chat, o Antigravity permite que agentes de IA ajam de forma proativa no código, terminal e navegador, enquanto o desenvolvedor atua como um supervisor ou regente.

> [!note] Ferramentas como o Antigravity estão democratizando o desenvolvimento, permitindo que o foco mude da sintaxe do código para a arquitetura da solução.*

---

### 🚀 Atualizações Recentes (2025-2026)

- **Fevereiro de 2026:** Integração com o **Gemini 3.1 Pro**, trazendo capacidades superiores de raciocínio, depuração complexa e compreensão de bases de código extensas.
- **Dezembro de 2025:** Adição do **Gemini 3 Flash**, otimizando a latência para sugestões de código instantâneas e interações em tempo real.
- **Novembro de 2025:** Lançamento oficial da plataforma com suporte inicial para sistemas **Linux** e foco em desenvolvedores individuais (nível Professional gratuito).

---

### 🛠️ Funcionalidades

#### 1. Mission Control (Controle de Missão)

Uma interface centralizada para gerenciar múltiplos agentes de IA. Permite visualizar o progresso de diferentes tarefas simultaneamente, funcionando como uma "caixa de entrada" de alterações e marcos atingidos pela IA.

#### 2. Agentes Cross-surface

Os agentes do Antigravity possuem controle sincronizado sobre três superfícies principais:
- **Editor de Código:** Escrita e refatoração direta.
- **Terminal:** Execução de comandos, instalação de dependências e gerenciamento de servidores.
- **Navegador (Browser-in-the-loop):** Testes automatizados de interface e extração de dados em tempo real.

#### 3. Servidores MCP (Model Context Protocol)

Utiliza o protocolo aberto para conectar a IA a ferramentas externas de forma universal.
- **Integrações Nativas:** Stripe, PayPal, Supabase, Pinecone, Notion e GitHub.
- **Extensibilidade:** Conexão com MCPs ([[Model Context Protocol]]) externos como **n8n** (automação) e **Firecrawl** (scraping).

#### 4. Customizações: Regras e Workflows

- **Regras ([[Rules]]):** Instruções globais ou por workspace que definem o comportamento da IA (ex: "Sempre use Tailwind CSS", "Responda em Português").
- **[[Workflows]]:** [[Prompts]] estruturados e salvos que guiam o agente em processos repetitivos, como a criação de uma arquitetura de pastas específica.

#### 5. Skills (Habilidades)

Capacidades modulares que podem ser adicionadas. Exemplo: a [[Skills|Skill]] **Remotion**, que permite à IA gerar e editar vídeos programaticamente a partir de código.

---

### 🎓 Guia Inicial de Aprendizado

#### Passo 1: Preparação do Ambiente

1. Acesse [antigravity.google](https://antigravity.google/) e faça o download da versão para o seu sistema (atualmente focado em Linux).
2. Faça login com sua conta Google para acessar os modelos Gemini integrados.

#### Passo 2: Criando sua Primeira Missão

1. Abra o **Mission Control** e inicie um novo projeto.
2. Defina o objetivo principal (ex: "Criar um dashboard de finanças com React e Supabase").
3. Configure as **Regras do Projeto** para garantir que a IA siga seu estilo de codificação preferido.

#### Passo 3: Conectando Ferramentas (MCP)

1. Vá até a aba de **Integrations**.
2. Configure suas chaves de API para serviços essenciais (GitHub para controle de versão, Supabase para banco de dados).
3. Teste a conexão pedindo ao agente para "Listar as tabelas do meu banco de dados".

#### Passo 4: Colaboração com o Agente

1. Use o comando de linguagem natural para delegar tarefas: *"Crie a página de login e teste a responsividade no navegador"*.
2. Acompanhe o agente abrindo o terminal e o browser automaticamente para validar o trabalho.
3. Revise as alterações na aba de **Changes** antes de aceitá-las.

#### Passo 5: Deploy e Hospedagem

1. Uma vez finalizado, peça ao agente para preparar o build de produção.
2. Utilize integrações com **Vercel** ou **Hostinger** para tornar o aplicativo acessível publicamente.

---

### 🔐 Segurança e Boas Práticas

- **Gestão de Segredos:** Nunca forneça chaves de API diretamente no prompt; use arquivos `.env` ou o gerenciador de segredos do Antigravity.
- **Arquitetura:** Crie pastas de "Inspiração" com exemplos de design para que a IA mantenha a consistência visual.
- **Supervisão:** Lembre-se que, embora autônomos, os agentes exigem revisão humana para lógica de negócios crítica.

---

### Referências

#Antigravity #Inteligencia-artificial   #Ferramentas

- [Google Antigravity Documentation](https://antigravity.google/docs/home)
- [antigravity-awesome-skills/docs/GETTING\_STARTED.md](https://github.com/sickn33/antigravity-awesome-skills/blob/main/docs/GETTING_STARTED.md)
- [Como usar o AntiGravity melhor que 99% das pessoas - YouTube](https://www.youtube.com/watch?v=DIqLI5Vgacc)
- [[Como usar o Google Antigravity melhor que 99% das pessoas]]
- [How to Use AntiGravity Better than 99% of People - YouTube](https://www.youtube.com/watch?v=QZCYFJTv8jI)
- [Como Publicar seus Apps e Automações (Antigravity + Hostinger VPS) - YouTube](https://www.youtube.com/watch?v=2wxI6U-PxEo)
- [Do Design ao Deploy: Construindo um App 100% com Google + Supabase + Vercel - YouTube](https://www.youtube.com/watch?v=qVHbvibm2kY)
- [NotebookLM e Antigravity criam qualquer coisa! (projeto completo) - YouTube](https://www.youtube.com/watch?v=8ddBzjJdMbI)
- [[Antigravity Kit]]
- [[Antigravity Awesome Skills]]
