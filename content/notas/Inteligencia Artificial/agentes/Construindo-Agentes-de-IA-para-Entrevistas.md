---
title: Construindo agentes de IA para entrevistas
description: "A Inteligência Artificial evoluiu de sistemas de chat puramente reativos para entidades autônomas capazes de agir"
tags:
  - Inteligencia-artificial/Agentes
---

## Construindo um Agente de IA para Simulação de Entrevistas Técnicas com Gemini e OpenClaw

Esta documentação técnica foi estruturada como um guia conceitual e prático para professores, alunos e desenvolvedores interessados em entender a arquitetura de **Agentes de IA** e como implementá-los na prática para simular entrevistas de emprego reais em tecnologia.

---

### 1. O que é um Agente de IA?

A Inteligência Artificial evoluiu de sistemas de chat puramente reativos para entidades autônomas capazes de agir. Diferente de um chatbot comum, que vive preso a uma interface de chat e apenas responde a perguntas diretas, um **Agente de IA** possui **autonomia**. Ele consegue:

- Executar tarefas complexas de forma sequencial.
- Integrar-se a APIs externas (enviar e-mails, acessar bancos de dados, consultar o WhatsApp).
- Utilizar ferramentas do sistema operacional (ler e escrever arquivos, navegar na web).
- Tomar decisões dinâmicas com base em um objetivo definido.

#### A Analogia do "Pinóquio"

Para fins didáticos (ideal para salas de aula e explicações simples), podemos dividir a arquitetura de um agente em três componentes essenciais:

```
                  ┌───────────────────────────┐
                  │      1. O CÉREBRO         │
                  │   (Modelo LLM / API)      │
                  └─────────────┬─────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │       2. O CORPO          │
                  │  (Plataforma/Orquestrador)│
                  └─────────────┬─────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │       3. O CHÃO           │
                  │   (Ambiente/Sandbox)      │
                  └───────────────────────────┘
```

1. **O Cérebro (Modelo/LLM):** É o motor de raciocínio lógico e processamento de linguagem (ex: Gemini, GPT, Claude, Llama). Ele não executa ações diretamente no computador, apenas processa os dados e decide "o que fazer".
2. **O Corpo (Plataforma/Orquestrador):** É o software que dá "mãos e pernas" ao cérebro (ex: **OpenClaw**, **Hermes**, **Antigravity**, **CrewAI**). Ele traduz as decisões do cérebro em chamadas de sistema, requisições HTTP e execução de código.
3. **O Chão (Ambiente/Sandbox):** É o ambiente isolado onde o agente opera (ex: **Docker**, **WSL/Linux**, **VPS**). Por questões de segurança, **nunca** devemos rodar agentes com permissões amplas diretamente no nosso sistema operacional nativo (Windows/macOS), pois um agente autônomo pode tomar decisões destrutivas, como deletar arquivos importantes ou derrubar bancos de dados.

---

### 2. O Conceito de "Skills" (Habilidades)

Enquanto o prompt tradicional instrui a IA sobre *como agir* ("Atue como um programador sênior"), uma **[[Skills|Skill]]** (Habilidade) confere ao agente a *capacidade de executar ações estruturadas*.

- **Definição:** Uma Skill é um arquivo de configuração (geralmente escrito em Markdown ou YAML) que define habilidades específicas para o agente — como acessar o navegador, fazer web scraping de portais de notícias, usar chaves de API específicas ou estruturar saídas em JSON.
- **Vantagem:** Permite que o agente atue como um especialista altamente focado. Ao carregar a skill `interview-agent`, o agente assume o fluxo completo de:

> Análise da Vaga ➡️ Plano de Entrevista ➡️Condução Dinâmica ➡️Avaliação de Respostas ➡️Relatório em JSON

- **Guardrails (Limites de Segurança):** Dentro da Skill, definimos regras estritas de comportamento para evitar que o agente alucine ou tome decisões perigosas (como tentar executar comandos de terminal não autorizados).

---

### 3. Preparando o "Chão" (Ambiente de Desenvolvimento)

Para rodar o **[[OpenClaw]]** de forma completa, o uso de ambientes baseados em **Linux** (WSL no Windows) ou **Docker** é obrigatório. O OpenClaw rodando de forma nativa no Windows possui diversas limitações em suas habilidades.

#### Pré-requisitos

- Docker e Docker Compose instalados.
- Uma chave de API de um provedor de LLM (como a **Gemini API Key** do Google AI Studio ou a **OpenAI API Key**).

#### Passo 1: Estrutura de Arquivos

Crie um diretório para o projeto com a seguinte estrutura:

```text
meu-agente/
├── docker-compose.yml
├── .env
└── skills/
    └── interview-agent/
        └── skill.md
```

#### Passo 2: Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto e configure suas chaves de API:

```env
# Chave de API do Gemini (Google AI Studio)
GOOGLE_API_KEY=sua_chave_aqui

# Caso queira usar OpenAI, descomente a linha abaixo:
# OPENAI_API_KEY=sua_chave_aqui
```

#### Passo 3: Configuração do `docker-compose.yml`

O arquivo `docker-compose.yml` automatiza o download e a execução do contêiner do OpenClaw, montando a pasta de skills local dentro do contêiner.

```yaml
version: '3.8'

services:
  openclaw:
    image: openclaw/openclaw:latest
    container_name: openclaw_agent
    volumes:
      - ./skills:/app/skills
      - openclaw_data:/app/data
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8000:8000" # Porta da API/WebSocket do OpenClaw
      - "3000:3000" # Porta do Dashboard Web (se aplicável)
    restart: unless-stopped

volumes:
  openclaw_data:
```

Para iniciar o ambiente, execute o comando abaixo no terminal da pasta raiz:

```bash
docker compose up -d
```

---

### 4. Criando a Skill do Entrevistador (`interview-agent`)

Abaixo está o [código Markdown completo da Skill]((https://gist.github.com/jocile/0a61f048865d806ae39e04f7edfd7eaf)) que deve ser salvo no caminho `./skills/interview-agent/skill.md`. Esta skill instrui o [[OpenClaw]] a se comportar como um entrevistador técnico corporativo de alto nível, gerando saídas estruturadas em JSON para facilitar integrações futuras.

---

````markdown
---
name: interview-agent
description: Agente especialista em conduzir simulações de entrevistas técnicas com base em descrições de vagas reais.
---

# Skill de Simulação de Entrevistas Técnicas

Use esta skill sempre que o usuário solicitar a análise de uma vaga de emprego, a criação de um roteiro de entrevista, a condução de perguntas técnicas ou a geração de um relatório de feedback de candidatura.

## Diretrizes Gerais e Guardrails
*   **Foco Absoluto:** Conduza a simulação de forma estritamente profissional. Não responda a perguntas fora do contexto de entrevistas técnicas.
*   **Execução Segura:** Não execute comandos de terminal, não tente ler arquivos do sistema operacional e não faça requisições externas sem autorização.
*   **Condução Oral Dinâmica:** Faça apenas **uma pergunta por vez**. Nunca envie uma lista de perguntas de uma vez só.
*   **Sigilo de Rúbrica:** Nunca revele as respostas ideais ou os critérios de avaliação exatos para o candidato durante a entrevista.

---

## Fluxo de Execução

### Fase 1: Análise da Vaga

Quando o usuário fornecer a descrição de uma vaga de emprego, analise o texto e gere uma resposta estritamente estruturada em JSON com o seguinte formato:

```json
{
  "vaga": "Nome do Cargo",
  "nivel": "Júnior / Pleno / Sênior / Specialist",
  "competencias_tecnicas": ["Tecnologia 1", "Tecnologia 2"],
  "competencias_comportamentais": ["Soft Skill 1", "Soft Skill 2"],
  "sinais_de_alerta_risco": ["O que indica falta de senioridade para esta vaga"]
}
```

### Fase 2: Plano de Entrevista

A partir da análise da vaga, elabore um plano de entrevista estruturado internamente.
*   **Se a vaga for Sênior/Especialista:** O plano deve focar em design de sistemas (System Design), tradeoffs de arquitetura, escalabilidade, segurança e gestão de incidentes críticos.
*   **Se a vaga for Júnior/Pleno:** O plano deve focar em fundamentos de programação, algoritmos, boas práticas de código (Clean Code) e ferramentas do dia a dia.

Gere o plano no formato JSON:

```json
{
  "foco_da_avaliacao": "Objetivo principal da entrevista",
  "blocos_de_perguntas": [
    {
      "bloco": 1,
      "tema": "Arquitetura e Sistemas Críticos",
      "perguntas_sugeridas": ["Pergunta A", "Pergunta B"]
    }
  ]
}
```

### Fase 3: Condução da Entrevista (Interação Dinâmica)

Inicie a entrevista fazendo a primeira pergunta ao candidato.
*   Aguarde a resposta do usuário.
*   Avalie a resposta internamente usando os critérios da Fase 4.
*   **Ajuste Dinâmico:** Use a resposta do candidato para direcionar a próxima pergunta. Se o candidato citar uma tecnologia específica (ex: "trabalhei com microsserviços usando Kafka"), aprofunde a próxima pergunta nesse ponto para validar a profundidade técnica real.
*   Mantenha o formato padrão de envio de pergunta:
    `Pergunta [N]: [Texto da Pergunta]`

### Fase 4: Avaliação de Respostas (Interna)

Para cada resposta dada, execute uma classificação de desempenho interna:
*   **Fraco:** Resposta superficial, conceitualmente incorreta, sem evidências práticas ou que apresente riscos técnicos graves.
*   **Aceitável:** Resposta correta nos conceitos teóricos, mas com pouca profundidade prática ou falta de clareza nos tradeoffs.
*   **Forte:** Resposta rica em detalhes, demonstra vivência prática real, cita tradeoffs, decisões de arquitetura e resolução de problemas complexos.

### Fase 5: Relatório Final de Desempenho

Quando a entrevista for finalizada (ou o usuário solicitar o relatório), consolide a avaliação em um relatório estruturado em JSON:

```json
{
  "resumo_executivo": "Parecer geral sobre o candidato",
  "aderencia_ao_cargo": "Baixa / Média / Alta",
  "pontos_fortes": ["Ponto Forte 1", "Ponto Forte 2"],
  "riscos_e_lacunas": ["Lacuna identificada 1", "Lacuna identificada 2"],
  "competencias_avaliadas": [
    {
      "competencia": "Nome da Competência",
      "avaliacao": "Fraco / Aceitável / Forte",
      "evidencia": "O que o candidato disse que comprova isso"
    }
  ],
  "recomendacoes_de_estudo": ["Tópico de Estudo 1", "Tópico de Estudo 2"]
}
```
````

---

### 5. Executando e Simulando a Entrevista

Uma vez configurado o contêiner Docker e salva a skill, podemos interagir com o agente.

#### Inicializando o OpenClaw Dashboard

Para gerenciar o agente visualmente, acesse o painel web do OpenClaw. No terminal do contêiner Docker, execute:

```bash
openclaw dashboard
```

Isso abrirá uma interface web local (geralmente em `http://localhost:3000` ou `http://localhost:8000`).

#### O Processo de Bootstrapping (Configuração Inicial)

Na primeira execução, o agente precisa passar por um *bootstrapping* (configuração de identidade). Ele fará perguntas para definir sua persona. Responda de forma direta no chat:

1. **Quem é você?** "Você é o José, um entrevistador técnico profissional, com tom corporativo sério, sem uso de emojis."
2. **Qual seu fuso horário?** "América/Sao_Paulo (Fuso de Brasília)."

#### Iniciando a Simulação

Envie o comando para ativar a skill criada:

```text
Use a skill interview-agent
```

Em seguida, envie a descrição da vaga que deseja simular. O agente executará a **Fase 1 (Análise)** e a **Fase 2 (Plano)**, retornando os JSONs estruturados. Ele então iniciará a **Fase 3 (Condução)** com a primeira pergunta:

> **José (Agente):** "Pergunta 1: Me conte sobre o sistema backend mais crítico em que você trabalhou. Qual era seu papel e qual era o impacto disso no negócio?"

#### Exemplo de Interação Dinâmica e Ajuste de Rota

- **Você (Candidato):** "Trabalhei em um sistema de pagamentos de e-commerce. Eu liderei a migração de parte do monolito PHP para microsserviços em Go para aguentar a Black Friday."
- **José (Agente) - Avaliação Interna:** *Forte. O candidato demonstrou vivência real em migração de monolito para microsserviços e lidou com volumetria alta (Black Friday).*
- **José (Agente) - Ajuste de Pergunta:** "Pergunta 2: Excelente. Durante essa migração de PHP para Go, como vocês garantiram a consistência dos dados transacionais entre as duas bases sem gerar duplicidade de pagamentos?"

Note que o agente abandonou qualquer roteiro estático para aprofundar-se exatamente na arquitetura que você citou, simulando perfeitamente a postura de um entrevistador técnico sênior de grandes big techs.

---

### 6. Solução de Problemas (Troubleshooting)

Durante o desenvolvimento do laboratório prático, diversos problemas de ambiente podem surgir. Abaixo estão as correções documentadas para as falhas mais comuns:

#### Sintoma 1: O contêiner Docker sobe, mas o agente não reconhece as novas Skills

- **Causa:** O OpenClaw precisa recarregar o gateway de habilidades após novos arquivos serem inseridos fisicamente na pasta `./skills`.
- **Solução:** Acesse o terminal do contêiner Docker e force o reinício do gateway com os comandos:

    ```bash
    openclaw gateway restart
    # ou de forma global:
    openclaw restart
    ```

#### Sintoma 2: Erros de escrita ao criar arquivos de Skill dentro do Docker

- **Causa:** Muitas imagens Docker minimalistas não possuem editores de texto padrão como `nano` ou `vim` instalados por padrão.
- **Solução:** Você pode instalar os editores de dentro do contêiner executando:

    ```bash
    apt-get update && apt-get install -y nano
    ```

    Alternativamente, crie e edite os arquivos de Skill diretamente no seu editor de código na sua máquina hospedeira (como o VS Code ou Obsidian), pois a pasta `./skills` está mapeada em tempo real como um volume Docker.

#### Sintoma 3: O agente alucina e começa a responder suas próprias perguntas

- **Causa:** Falha nos Guardrails da Skill ou temperatura do modelo muito alta no provedor da API.
- **Solução:** No painel do OpenClaw, certifique-se de usar um nível de raciocínio (Reasoning) **Médio** para otimizar o consumo de tokens e a precisão das respostas. Reforce na instrução da Skill a frase: `"Aguarde a resposta do usuário antes de formular a próxima pergunta. Nunca responda por ele."`

---

### 7. Reflexão de Carreira: O Paradigma "AI-First"

A live encerra com uma profunda reflexão sobre o mercado de trabalho atual. 

- **A IA não vai roubar seu emprego:** Quem vai ocupar as melhores vagas são os profissionais que sabem orquestrar e gerenciar equipes de agentes de IA para multiplicar sua produtividade pessoal.
- **Startups de poucas pessoas:** Com a facilidade de criar "squads" de agentes autônomos (um agente para UX, um para backend, um para testes), desenvolvedores individuais estão construindo produtos funcionais (MVPs) e faturando alto com estruturas extremamente enxutas.
- **A importância da base técnica:** Embora pessoas não técnicas consigam colocar agentes simples para rodar usando linguagem natural, apenas profissionais com sólida base em arquitetura de software, segurança, Docker e APIs conseguirão escalar essas soluções de forma segura e profissional no ambiente corporativo.

---

### Tópicos Relacionados

- Engenharia de [[agentes de ia]] e [[notas/Inteligencia Artificial/Machine Learning/index]].
- [SKILL para simulação de entrevistas técnicas com Gemini e OpenClaw · GitHub](https://gist.github.com/jocile/0a61f048865d806ae39e04f7edfd7eaf)
- [GitHub - digitalinnovationone/potencializando-estudos-carreira-com-ia: Curso "Potencializando Seus Estudos e Carreira com IA: De Chatbots a Agentes" · GitHub](https://github.com/digitalinnovationone/potencializando-estudos-carreira-com-ia)
- [GitHub - digitalinnovationone/dio-pro-vitalicio-week-2026-agentes-ia: DIO PRO Vitalício Week: Agentes de IA · GitHub](https://github.com/digitalinnovationone/dio-pro-vitalicio-week-2026-agentes-ia)
- [Construa um Agente de IA com Gemini e OpenClaw para simular entrevistas das melhores vagas em tech - YouTube](https://www.youtube.com/watch?v=WmhV_RO7fDc)
