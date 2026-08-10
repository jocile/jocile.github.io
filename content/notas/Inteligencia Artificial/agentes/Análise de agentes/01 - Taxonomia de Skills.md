---
title: 01 - Taxonomia de Skills
tags:
  - Inteligencia-artificial/Agentes
  - Inteligencia-artificial/Skill
description: Classificação de habilidades de agentes de IA
---

# Taxonomia de Habilidades

Entender a **Taxonomia de Habilidades** é o passo fundamental, pois antes de construir ou avaliar um agente, precisamos saber o que ele é capaz de fazer.

Para analisar as skills de um [[agentes de ia]], costumamos dividi-las em quatro grandes pilares. Veja como elas se estruturam:

## 🗂️ A Anatomia das [[Skills]] de um Agente

|**Pilar de Habilidade**|**Descrição**|**Exemplo Prático**|
|---|---|---|
|🧠 **Raciocínio & Planejamento**|A capacidade de quebrar uma meta complexa em subtarefas menores e corrigir a rota quando algo dá errado.|Um agente que decide pesquisar o preço de 3 hotéis antes de sugerir uma viagem.|
|🛠️ **Uso de Ferramentas (_Tool Use_)**|A habilidade de interagir com o mundo externo, APIs, bancos de dados ou executar código.|O agente usar uma calculadora para resolver uma conta ou rodar um script Python.|
|💾 **Memória**|A capacidade de reter informações. Pode ser de **curto prazo** (o contexto da conversa atual) ou de **longo prazo** (histórico guardado em um banco de dados vetorial).|Lembrar o nome do usuário que foi dito 10 mensagens atrás ou lembrar de uma preferência do cliente salva no mês passado.|
|🗣️ **Interação & Percepção**|Como o agente se comunica com humanos, com outros agentes (multi-agentes) ou processa diferentes mídias (visão, áudio).|Um agente que analisa um print de tela enviado pelo usuário para resolver um bug no sistema.|

Para começarmos a nossa análise prática, imagine que queremos criar um **Agente Assistente de Compras** que ajuda o usuário a encontrar o melhor produto na internet e gerar um relatório.

Pensando nesses quatro pilares acima, qual pilar você acha que seria o mais crítico para esse agente verificar se um produto realmente está em estoque em uma loja real? Por que?

### 🛠️ Uso de ferramentas

Exatamente! Acertou em cheio. 🎯

O pilar de **Uso de Ferramentas (_Tool Use_)** é o mais crítico nessa situação. Sem ele, o agente ficaria limitado apenas ao conhecimento que recebeu durante o seu treinamento (que é estático e fica desatualizado).

Para verificar o estoque em tempo real, o agente precisa sair do seu "cérebro" isolado e interagir com o mundo externo. Ele faz isso através de:

- 🌐 **APIs de e-commerce:** Consultando diretamente o sistema da loja.    
- 🔍 **Web Scraping:** Acessando a página do produto e extraindo a informação atualizada.    

Agora que mapeamos a importância das ferramentas, vamos dar um passo adiante no raciocínio do agente.

Imagine que a ferramenta de busca avisa ao agente: _"O produto acabou na Loja A, mas tem em estoque na Loja B por um preço mais alto"_.

Para decidir se ele deve apenas avisar o usuário ou procurar em uma Loja C, qual dos outros três pilares (**Raciocínio & Planejamento**, **Memória** ou **Interação**) o agente terá que usar para tomar essa decisão? Por que você acha isso?

### 🧠 Raciocínio & Planejamento

Isso mesmo! Você identificou perfeitamente. 🧠

Para tomar esse tipo de decisão, o agente precisa usar o pilar de **Raciocínio & Planejamento**.

Diante de um imprevisto (como a falta de estoque na Loja A), o modelo de linguagem que controla o agente avalia o novo cenário e reconstrói o plano de ação. Ele "pensa": _“Se o objetivo principal é encontrar o melhor preço e o produto acabou na opção mais barata, preciso recalcular a rota e buscar uma alternativa antes de responder ao usuário”_.

Agora que passamos pelos conceitos principais de como classificar essas competências, podemos fechar esse pilar entendendo como elas se conectam.

Imagine o fluxo completo do nosso **Agente Assistente de Compras**:

1. O usuário pede um produto.    
2. O agente puxa na **Memória** as preferências do usuário.    
3. Ele usa o **Raciocínio** para criar um plano de busca.    
4. Ele usa as **Ferramentas** para checar os sites e estoques.    
5. Ele usa a **Interação** para responder ao usuário com clareza.    

Para consolidar esse conhecimento sobre a taxonomia antes de avançarmos para os frameworks (como esses agentes são construídos), o que você acha que aconteceria com a experiência do usuário se o agente tivesse excelentes ferramentas e raciocínio, mas a sua habilidade de **Memória** fosse igual a zero? Como isso afetaria o comportamento dele?

### 🧠 Memória

- Acho que ele não seguiria adiante do passo 2 do fluxo.
- Que excelente intuição! Você identificou o ponto exato onde o sistema quebraria. 🧠

Se a **Memória** do agente fosse igual a zero, aconteceria exatamente isto:

1. O usuário diria suas preferências (ex: _"Quero um tênis de corrida azul, tamanho 41"_).    
2. O agente avançaria para o passo seguinte, mas esqueceria instantaneamente o que foi dito na mensagem anterior. 💨    
3. Ele acabaria buscando qualquer tênis, de qualquer cor ou tamanho, ignorando totalmente o que o usuário precisa. Ele ficaria "preso" em um loop, perguntando a mesma coisa várias vezes.    

Na análise de agentes, dizemos que a memória é o que dá **consistência** e **contexto** para a tomada de decisão.

Com isso, fechamos o nosso primeiro pilar: **A Taxonomia de Habilidades (O quê)**. Você já consegue classificar o que um agente faz em Raciocínio, Ferramentas, Memória e Interação. 📁

Podemos agora avançar para o segundo objetivo que havíamos planejado: **Frameworks de Agentes (Como funciona)**. ⚙️

Para entender como essas habilidades são injetadas na prática, por qual destes conceitos você prefere começar a explorar?

1. **[[02 - A personalidade do agente|Prompts de Sistema]] (System Prompts):** Como as instruções iniciais moldam a personalidade e o limite das habilidades do agente.    
2. **Arquitetura de ReAct (Reason + Act):** O ciclo de pensamento que os frameworks usam para fazer o agente pensar antes de usar uma ferramenta.
