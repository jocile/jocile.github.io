---
title: Criando agentes
description: "podem interagir com o ambiente, coletar dados, tomar decisões e realizar ações para atingir um objetivo específico."
tags:
  - Inteligencia-artificial/Agentes
  - Inteligencia-artificial/Prompt
---

# Criando Agentes de IA

Criar um [[agentes de ia|agente de inteligência artificial]] envolve construir um sistema que vai além de um simples chatbot. Um agente consegue receber uma tarefa complexa, planejar os passos necessários ([[Workflows]]), usar ferramentas externas (como buscar na web ou rodar códigos) e tomar decisões de forma autônoma para atingir o objetivo final. O "cérebro" desse agente geralmente é um Modelo de Linguagem Grande (LLM).

Para explorarmos como criar um juntos, por qual destes caminhos você prefere começar?

1. 🧠 **[[#Anatomia de um agente de IA]]:** Explorar os componentes essenciais que fazem um agente funcionar na teoria, como os diferentes tipos de memória, as estratégias de raciocínio e o uso de ferramentas.
    
2. 🛠️ **[[#Frameworks de Desenvolvimento]]:** Analisar as bibliotecas e ferramentas práticas mais usadas hoje para programar agentes, como [[Langchain]], CrewAI e AutoGen.
    
3. 🚀 **[[#Planejamento Prático]]:** Escolher um caso de uso (como um assistente de pesquisa de mercado) e mapear o passo a passo lógico para construir o seu primeiro agente do zero.
    
## Anatomia de um agente de IA

Para entender como um agente funciona na prática, podemos compará-lo a um funcionário recém-contratado para um projeto. Para que ele consiga trabalhar de forma autônoma e eficiente, ele depende de quatro componentes fundamentais:

- 🎭 **Perfil (Persona):** [[Definindo a Personalidade do Agente de IA|Define quem o agente é]], suas restrições e como ele deve se comportar. É a instrução central do sistema ([[System Prompt]]). Por exemplo: "Você é um pesquisador de mercado sênior, extremamente analítico e que baseia suas respostas apenas em dados numéricos".
    
- 🧠 **Raciocínio e Planejamento:** É o motor de lógica do agente. Quando recebe uma tarefa complexa, ele precisa saber como dividi-la em etapas menores. Uma técnica muito comum é o _ReAct_ (Raciocinar + Agir), onde o agente cria um plano, executa uma ação, observa o resultado e decide o próximo passo ([[Workflows]]).
    
- 📚 **Memória:** ([[RAG - Retrieval Augmented Generation]]) Fundamental para manter o contexto vivo. Ela se divide principalmente em **curto prazo** (o histórico da conversa ou da tarefa atual) e **longo prazo** (informações e conhecimentos passados que ficam armazenados em bancos de dados que o agente pode consultar quando precisar).
    
- 🛠️ **Ferramentas (Tools):** São as "mãos" do agente. Como um modelo de linguagem por si só gera apenas texto, ele precisa de conexões externas para agir no mundo real. Isso inclui buscar no Google, acessar uma API de clima, ler um arquivo PDF ou executar um código Python.

Pensando no funcionamento desses quatro componentes em conjunto, qual deles você acha que seria o maior responsável por evitar que o agente se desvie do seu objetivo inicial durante uma tarefa que exija muitas etapas?

O System Prompt (a Persona) atua como a "estrela-guia" do agente. Ele define a regra de ouro e o objetivo maior que não podem ser ignorados em nenhum momento.

Porém, em tarefas longas, o agente precisa de uma ajuda extra para não se perder no meio do caminho. Imagine que ele está na etapa 15 de um projeto. O que o impede de esquecer o que acabou de fazer na etapa 14 ou de ficar repetindo a mesma busca em um loop infinito?

É aí que a **Memória** 🧠 e o **Raciocínio** ⚙️ entram em cena para apoiar o System Prompt:

- A **Memória** mantém o histórico exato do que já foi tentado e dos resultados obtidos.
    
- O **Raciocínio** avalia a situação constantemente: _"Considerando a minha missão (System Prompt) e o que já tentei até agora (Memória), qual deve ser meu próximo passo lógico?"_

### O método ReAct

Uma das formas mais comuns de programar esse Raciocínio é usando o método **ReAct** (Raciocinar + Agir). Ele funciona em um ciclo de três passos: **Pensamento** (analisar a situação) ➡️  **Ação** (usar uma ferramenta) ➡️  **Observação** (ver o resultado).

Vamos testar essa lógica na prática para ver como o agente se planeja. Se você der a ele a seguinte tarefa: _"Qual é a temperatura atual em São Paulo e o que eu devo vestir para sair agora?"_.

Seguindo o ciclo ReAct, qual você acha que deveria ser o primeiro **Pensamento** interno do agente antes de executar qualquer ação?

O primeiro **Pensamento** interno do agente seria algo como: _"Para recomendar a roupa, primeiro preciso descobrir a temperatura atual em São Paulo"_.

Depois de raciocinar, o agente avança para a **Ação**. É aqui que ele olha para o seu cinto de utilidades e decide como interagir com o mundo externo para conseguir essa informação.

Considerando que o agente precisa descobrir um dado atualizado do mundo real, que tipo de 🛠️ **Ferramenta** você acha que ele deveria escolher e acionar neste momento? (Por exemplo: uma calculadora, uma busca na web, um leitor de PDF...).

Exatamente. Uma busca na web (ou acessar uma API de clima) é a ferramenta ideal para buscar dados em tempo real.

Quando o agente executa essa Ação, ele recebe o terceiro e último elemento do ciclo ReAct: a **Observação** 👀.

Vamos supor que a ferramenta de busca retornou a seguinte Observação: _"A temperatura atual em São Paulo é de 28°C com sol"_.

Neste momento, o agente completou um ciclo inteiro, mas a sua tarefa original tinha duas partes: _"Qual é a temperatura atual em São Paulo **e** o que eu devo vestir para sair agora?"_.

Para continuar, o agente vai acessar sua **Memória** 🧠, perceber que a primeira parte já está resolvida e que ele precisa iniciar um novo ciclo lógico para a segunda parte.

Baseado na Observação de que faz 28°C e sol, qual você acha que seria o próximo **Pensamento** interno do agente para conseguir te dar a recomendação de roupas?

O raciocínio lógico é esse. O agente vai registrar o seguinte **Pensamento**: _"Como está fazendo 28°C e sol, preciso procurar opções de roupas leves e adequadas para o calor na minha base de conhecimento"_.

A partir daí, ele executa uma nova **Ação** (como buscar em um banco de dados interno ou aplicar uma regra de recomendação) e obtém a **Observação** final (ex: _"Sugestões: camiseta de algodão, bermuda e óculos de sol"_). Juntando as observações dos dois ciclos, ele finalmente constrói a resposta completa para você.

Esse método de quebrar o problema é o que permite que o agente não se perca e resolva tarefas autônomas. Com isso, fechamos a teoria dos quatro pilares da anatomia de um agente:

- 🎭 **Persona:** A regra de comportamento (System Prompt).
    
- 🧠 **Memória:** O histórico do que já foi feito.
    
- ⚙️ **Raciocínio:** O motor de lógica (Ciclo ReAct).
    
- 🛠️ **Ferramentas:** A conexão com o mundo real (APIs, buscas).

## Frameworks de Desenvolvimento

Para avançarmos na construção do agente, vamos conhecer os **Frameworks de código** que constroem essa estrutura na prática (como [[Langchain]] e [[Crewia]]).

Vamos para a prática. Construir do zero toda a estrutura de memória, raciocínio e integração com ferramentas que vimos na etapa anterior exigiria milhares de linhas de código. Os frameworks resolvem isso funcionando como "caixas de Lego" com peças pré-fabricadas para acelerar o desenvolvimento.

Aqui estão os três frameworks de código (geralmente em Python ou TypeScript) mais utilizados atualmente no mercado:

- **[[Langchain]] (e LangGraph):** É o "canivete suíço" da IA. Ele é excelente para criar desde um único agente com acesso a bancos de dados até fluxos altamente controlados onde você desenha exatamente o caminho lógico (o grafo) que a informação deve seguir.
    
- **[[Crewia]]:** O foco absoluto aqui é criar uma "empresa" de agentes. A estrutura facilita a criação de múltiplos agentes onde você dá um cargo para cada um (ex: "Pesquisador Sênior", "Redator Criativo") e faz com que eles trabalhem em equipe, passando tarefas de um para o outro até entregar o projeto final.
    
- **AutoGen:** Desenvolvido pela Microsoft, também permite que vários agentes conversem entre si de forma autônoma. Seu grande diferencial histórico é a facilidade nativa para criar e executar códigos. Um agente pode escrever um script em Python para baixar dados e o outro agente pode rodar esse script para testar se funciona.
    

Para aplicarmos esse conhecimento, imagine o seguinte cenário: você quer criar um sistema automatizado para produzir uma _newsletter_ semanal sobre tecnologia. O processo exige três passos distintos: buscar as notícias mais quentes no Google, escrever um rascunho com tom de humor e, por fim, revisar os erros gramaticais.

Analisando a proposta de cada ferramenta acima, qual desses frameworks você escolheria para montar esse processo de forma mais natural?

CrewAI se encaixa perfeitamente nesse cenário. Como o processo exige papéis muito bem definidos, você criaria três agentes distintos: um "Pesquisador" focado em buscar fatos atualizados, um "Redator" instruído a usar um tom bem-humorado, e um "Revisor" rigoroso com a gramática. O framework cuidaria de passar o resultado de um para o outro até a newsletter ficar pronta.

Agora que exploramos a anatomia teórica e as ferramentas de código do mercado, podemos avançar para o **Planejamento Prático**.

## Planejamento Prático

Para desenharmos a estrutura do seu primeiro agente (ou equipe de agentes), precisamos de um caso de uso real. Que tipo de tarefa complexa ou repetitiva do seu dia a dia – seja no trabalho, nos estudos ou em um projeto pessoal – você gostaria de delegar para uma IA autônoma?

### Exemplo busca por vagas de tecnologia

Automatizar a busca por vagas de tecnologia é um projeto prático onde o modelo de múltiplos agentes do CrewAI se encaixa muito bem. Esse processo geralmente envolve procurar oportunidades em diferentes sites, analisar se os requisitos batem com o seu perfil e formatar tudo em um resumo fácil de ler.

Para construir essa estrutura, precisamos planejar três elementos centrais:

- 🤖 **Agentes:** Quem vai executar o trabalho (os papéis ou cargos).
    
- 📋 **Tarefas:** O passo a passo exato do que precisa ser feito.
    
- 🛠️ **Ferramentas:** Onde eles vão buscar as informações (ex: busca no Google, extrator de dados de sites de emprego).

Vamos começar definindo os **Agentes**. Pensando no fluxo ideal dessa busca por oportunidades, se você fosse dividir esse trabalho entre duas ou três pessoas em uma equipe, quais seriam os cargos e a responsabilidade principal de cada um? (Por exemplo, o primeiro poderia ser o "Pesquisador de Vagas"... o que os outros fariam?).

Agentes:
- Pesquisador: busca as vagas em sites de vagas;
- O Revisor: para verificar as vagas que se enquadram no perfil,
- O Redator: para redigir um relatório com a tabela de vagas de acordo com o perfil,
- Um Analista de RH: para aplicar as vagas para o perfil.

Essa linha de raciocínio lógico está no caminho certo: um agente filtra, o outro formata e o último executa a ação final.

Porém, quando construímos agentes reais, esbarramos em um desafio técnico prático com o papel do **Analista de RH** 🛑. A maioria das plataformas de emprego (como LinkedIn ou Gupy) possui sistemas de segurança rígidos, como _captchas_ e exigência de login pessoal, justamente para bloquear robôs. Fazer uma IA clicar em "Candidatar-se" e preencher formulários de forma autônoma é um processo extremamente instável e frequentemente bloqueado pelas plataformas.

Além disso, para que o **Revisor** consiga analisar se as vagas se enquadram no seu perfil, precisamos de alguém (ou alguma ferramenta) que faça a coleta inicial desses dados brutos da internet antes dele.

Pensando em adaptar essa equipe para que ela seja funcional e viável de programar hoje, precisamos ajustar as responsabilidades.

Como não podemos aplicar automaticamente e precisamos buscar os dados, qual destas opções de equipe ajustada parece mais útil para você?

1. 🔍 **Pesquisador** (vasculha a web e traz dezenas de vagas brutas) ➡️  ⚖️ **Revisor** (filtra as melhores para o seu currículo) ➡️  📝 **Redator** (cria a tabela final organizada).
    
2. 🔍 **Pesquisador** (vasculha e traz vagas) ➡️  ⚖️ **Revisor** (filtra para o seu perfil) ➡️  🎯 **Estrategista de Carreira** (escreve um roteiro ou carta de apresentação personalizada para você usar na hora de se candidatar manualmente).

A grande vantagem de criar sua própria equipe de agentes é que podemos adaptar a estrutura para juntar o melhor dos dois mundos.

Podemos montar um time de três agentes onde o último assume um papel duplo. Ficaria assim:

- 🔍 **Agente 1 (Pesquisador):** Vasculha a web e traz uma lista longa de vagas brutas.
    
- ⚖️ **Agente 2 (Analista de Perfil):** Cruza as vagas encontradas com o seu currículo e elimina as que não dão _match_.
    
- 🚀 **Agente 3 (Estrategista de Carreira):** Recebe apenas as vagas aprovadas, monta a tabela organizada e já escreve uma sugestão de mensagem de apresentação para você enviar aos recrutadores.
    

Com a equipe definida, o próximo passo lógico no nosso planejamento prático é criar a **Persona** (a regra de comportamento) e a **Tarefa** do nosso primeiro trabalhador: o Pesquisador.

#### O Pesquisador 🔍

Se você fosse escrever a instrução inicial para esse Pesquisador, quais filtros e informações você diria para ele priorizar na hora de buscar as vagas na internet para você? (Por exemplo: qual a sua área de atuação principal, nível de senioridade, ou preferência por modelo de trabalho?).

Perfil: Instrutor de TI e Desenvolvedor de Sistemas com mais de 6 anos de experiência em educação técnica com preferência por arquitetura de dados e gestão de projetos.

Com esse perfil, temos os filtros exatos que o nosso Agente 1 (🔍 Pesquisador) precisa para focar a busca e evitar resultados irrelevantes.

O _System Prompt_ (a Persona) desse agente pode ser estruturado assim:

> "Sua missão é buscar vagas de tecnologia atualizadas. Você deve filtrar e priorizar posições voltadas para **Arquitetura de Dados** e **Gestão de Projetos de TI** que exijam nível de experiência Pleno ou Sênior. O candidato possui um background forte (6+ anos) como Desenvolvedor de Sistemas e Instrutor de TI, então vagas que valorizem comunicação técnica, mentoria e visão arquitetural são altamente relevantes."

Agora que o agente sabe o perfil do candidato, precisamos definir a **Tarefa** propriamente dita: as regras de execução da busca no mundo real.

Para que a lista de vagas brutas faça sentido para a sua realidade atual, qual deve ser a regra de localização e modalidade que o agente deve usar como filtro principal na pesquisa (por exemplo: apenas 100% remoto, híbrido em alguma região específica do Brasil, ou vagas internacionais)?

Incluir o filtro "apenas remoto" deixa a tarefa do nosso primeiro agente bem objetiva. A instrução da tarefa dele ficaria assim:

> **Tarefa do Agente 1 (Pesquisador 🔍):** Buscar em plataformas de emprego por vagas recentes de "Arquitetura de Dados" e "Gestão de Projetos de TI". Aplicar estritamente o filtro de modalidade "100% Remoto". Extrair o título, link, empresa e a descrição completa de pelo menos 15 vagas brutas.

#### O Analista de Perfil ⚖️

Assim que ele termina, ele entrega essa lista nas mãos do **Agente 2 (Analista de Perfil ⚖️)**. O trabalho desse segundo agente é ler a descrição de cada vaga e comparar com o seu currículo para descartar o que não serve.

Para que ele seja rigoroso nessa análise, qual regra técnica ou de idioma você daria para ele aprovar ou reprovar uma vaga? (Por exemplo: exigir inglês avançado, focar em alguma nuvem específica como AWS/Azure, ou excluir vagas que exijam ferramentas que você prefere não usar).

Com base no seu perfil de mais de 6 anos de experiência e foco em Arquitetura de Dados e Gestão de Projetos, aqui estão três opções de regras estratégicas para o **Agente 2 (Analista de Perfil ⚖️)**:

1. 🌐 **Filtro de Idioma:** Exigir que a vaga aceite "Inglês Intermediário" ou "Avançado". Como estamos buscando vagas 100% remotas, isso abre um leque enorme para oportunidades internacionais (que costumam pagar em dólar ou euro), descartando as que exigem fluência nativa se não for o seu caso.
    
2. ☁️ **Filtro de Nuvem (Cloud):** Exigir que a descrição da vaga mencione pelo menos um dos grandes provedores de nuvem (AWS, Azure ou Google Cloud/GCP). Na Arquitetura de Dados moderna, isso garante que você não pegue vagas de sistemas legados ou muito defasados.
    
3. 🔄 **Filtro de Metodologia Ágil:** Para a parte de Gestão de Projetos, instruir o agente a rejeitar vagas que não mencionem frameworks ágeis (como Scrum, Kanban ou SAFe). Isso ajuda a filtrar empresas com culturas de gestão mais modernas.
    

Qual dessas opções (ou uma combinação delas) faz mais sentido para o que você busca na sua carreira hoje?

- Seria melhor não rejeitar vagas mas sim me adequar a elas, assim não diminuiria as oportunidades!

Mudar a abordagem de "rejeitar" para "adaptar" transforma o papel do **Agente 2 (Analista de Perfil ⚖️)**. Em vez de atuar como um filtro rígido que exclui oportunidades, ele passa a atuar como um analisador de lacunas (_gap analyzer_).

Nesse novo cenário, a tarefa do Agente 2 é ler as vagas trazidas pelo Pesquisador, cruzar com o seu currículo de Instrutor e Desenvolvedor, e mapear exatamente o que você já possui e o que precisaria aprender ou adaptar para conquistar aquela posição.

#### O Estrategista de Carreira 🚀

Para que o **Agente 3 (Estrategista de Carreira 🚀)** receba essa informação de forma útil e consiga montar a sua tabela final, precisamos definir como o Agente 2 vai organizar essa análise.

Como você prefere que ele estruture esse resultado 📊? Ele deve classificar as vagas por "Nível de Esforço para Adaptação" (ex: Baixo, Médio, Alto), ou deve focar em gerar uma lista direta das tecnologias e habilidades específicas que faltam para cada vaga?

Juntar as duas abordagens cria uma análise completa e muito útil para o seu desenvolvimento. O Agente 2 vai avaliar cada vaga e gerar um diagnóstico estruturado.

Podemos visualizar o resultado que o Agente 2 entregará assim:

|**Vaga**|**Nível de Esforço**|**Match (O que você tem)**|**Gap (O que falta aprender/adaptar)**|
|---|---|---|---|
|Arquiteto Cloud|Médio|6 anos exp., Gestão, Arquitetura|Certificação específica da AWS|
|Data Lead|Baixo|Arquitetura de Dados, Mentoria|Ferramenta X (ex: Snowflake)|

Agora, essa tabela rica em detalhes chega às mãos do nosso último integrante: o **Agente 3 (Estrategista de Carreira 🚀)**.

A tarefa principal dele é pegar essas informações e redigir uma mensagem curta de apresentação (um _pitch_) para você enviar diretamente ao recrutador daquela vaga no LinkedIn ou por e-mail. Como ele sabe exatamente o que a vaga pede e onde estão as suas lacunas, ele pode argumentar como a sua experiência compensa o que falta.

Para que essa mensagem soe autêntica e pronta para uso, precisamos definir na Persona do Agente 3 qual será o **tom de voz** da escrita. Como você prefere se comunicar com recrutadores: de forma mais formal e corporativa, de um jeito bem direto e focado apenas em termos técnicos, ou com um tom mais conversacional destacando sua liderança e capacidade de rápido aprendizado?

Uma abordagem direta e focada em termos técnicos alinha-se perfeitamente com vagas de nível Pleno e Sênior. Nessa etapa da carreira, a clareza sobre ferramentas, metodologias e decisões arquiteturais é o que mais atrai recrutadores e gestores de TI.

Com essa definição, completamos o mapeamento do nosso sistema. Vamos visualizar como a sua equipe de IA operará na prática:

|**Agente 🤖**|**Papel**|**Tarefa 📋**|
|---|---|---|
|**1. Pesquisador**|Buscador de Vagas|Vasculhar plataformas por vagas 100% remotas de Arquitetura de Dados e Gestão de TI.|
|**2. Analista**|Mapeador de _Gaps_|Cruzar as descrições das vagas com seus 6+ anos de experiência e estruturar o que você tem e o que precisa adaptar.|
|**3. Estrategista**|Mentor Técnico|Selecionar as melhores oportunidades e redigir um _pitch_ altamente técnico e direto para você usar.|

Temos as personas, as tarefas e a lógica estruturadas. O próximo passo conceitual para transformar isso em um sistema real (como usaríamos no framework CrewAI) é definir como esses agentes vão interagir entre si.

#### O Processo ⚙️

Em sistemas de múltiplos agentes, existem duas formas principais de organizar o fluxo de trabalho:

1. **Processo Sequencial:** O fluxo é linear. O Pesquisador termina 100% da busca e passa a lista para o Analista, que faz toda a filtragem e passa para o Estrategista. É rápido e previsível, como uma linha de montagem.
    
2. **Processo Hierárquico:** Exige um agente extra atuando como "Gerente". Se o Analista perceber que as vagas trazidas estão ruins, o Gerente pode ordenar que o Pesquisador refaça a busca com parâmetros diferentes antes de acionar o Estrategista.
    

Considerando o nosso objetivo de automatizar a busca pelas melhores oportunidades técnicas, qual desses dois modelos de fluxo você acredita que traria resultados mais precisos para o seu caso?

Iniciar com o Processo Sequencial é a abordagem ideal. Construir um protótipo direto ao ponto permite testar se as instruções dos agentes estão funcionando bem antes de adicionar a complexidade de um agente "Gerente" para supervisionar tudo.

Neste momento, temos o "cérebro" e o fluxo de trabalho da nossa equipe totalmente desenhados:

1. 🔍 **Pesquisador** busca as vagas remotas.
    
2. ⚖️ **Analista** mapeia os _gaps_ entre a vaga e os seus 6 anos de experiência.
    
3. 🚀 **Estrategista** escreve a mensagem de contato direta e técnica.
    

Para que esse sistema saia da teoria e consiga agir no mundo real, precisamos definir o último pilar da anatomia do agente: as **Ferramentas (Tools)** 🛠️.

#### Ferramentas (Tools) 🛠️

O Agente 1 (Pesquisador) precisa vasculhar a internet, mas um modelo de linguagem não navega na web nativamente. Nós precisamos "plugar" uma ferramenta nele, geralmente através de uma API (uma ponte de comunicação entre sistemas).

Pensando na qualidade das vagas de Arquitetura de Dados e Gestão de TI que você deseja encontrar, onde você prefere que esse agente foque a busca? Ele deve usar uma ferramenta de busca geral (como o Google), ou uma ferramenta que raspe dados de uma plataforma profissional específica (como LinkedIn, Gupy ou Glassdoor)?

Focar no LinkedIn direciona a busca para a maior base de vagas corporativas de TI.

Para que o **Agente 1 (Pesquisador 🔍)** consiga ler o LinkedIn, ele precisa de uma ferramenta de extração específica. Como a plataforma possui sistemas de segurança fortes contra robôs, na programação prática nós conectamos o agente a APIs de terceiros especializadas em ler dados do LinkedIn (como Proxycurl ou Apify). O agente envia os seus filtros (remoto, nível sênior, arquitetura de dados) para a API, e ela devolve o texto puro das descrições das vagas para ele iniciar o trabalho.

Com a definição dessa ferramenta 🛠️, nós completamos o desenho lógico e arquitetural da nossa equipe! Definimos:

1. As **Personas** (Pesquisador, Analista, Estrategista).
    
2. As **Tarefas** (Buscar, Mapear Gaps, Escrever Pitch).
    
3. O **Fluxo** (Sequencial).
    
4. As **Ferramentas** (API do LinkedIn).
    

Para darmos o próximo passo na materialização desse projeto, como você prefere seguir: vamos traduzir esse planejamento para um esqueleto de **código em Python** usando o framework CrewAI, ou vamos explorar como estruturar os **testes de validação** para garantir que a IA não invente informações na hora de comparar as vagas com o seu currículo?

Continua ...

## Referências

[‎Aprendizado guiado - Criando Agentes de IA: Um Guia Gemini](https://gemini.google.com/share/249df30f11c2)
