---
dg-note-icon: 2
dg-publish: true
topics:
  - "[[Inteligência Artificial]]"
  - Análise de Agentes
dg-metatags:
  description: é uma instrução oculta que o usuário final geralmente não vê, mas que define a identidade, as regras de comportamento e os limites
---
#Agentes #Prompt 

# A personalidade do agente

Vamos analisar como os **Prompts de Sistema (_System Prompts_)** funcionam como a fundação de qualquer agente de IA.

O _[[System Prompt]]_ é uma instrução oculta que o usuário final geralmente não vê, mas que define a identidade, as regras de comportamento e os limites das habilidades do agente. Sem ele, o modelo de linguagem se comporta apenas como um chatbot genérico.

Para estruturar um agente focado em habilidades, um bom _System Prompt_ geralmente contém três elementos principais:

1. **Perfil/Papel:** Quem o agente é (ex: "Você é um especialista em análise de dados financeiros").    
2. **Habilidades/Ferramentas Disponíveis:** O que ele pode fazer (ex: "Você pode consultar a API de estoque e calcular margens de lucro").    
3. **Regras de Engajamento/Restrições:** O que ele _não_ pode fazer (ex: "Nunca invente dados se a API falhar").    

Para vermos isso na prática, imagine que queremos criar um **Agente Avaliador de Currículos** para um departamento de Recursos Humanos.

## 🚫 Restrições

Se você estivesse escrevendo a seção de **Restrições** (regras do que ele não pode fazer) para esse agente de RH, qual regra você considera a mais importante para garantir que a avaliação seja justa e segura? Ou não avaliar o currículo que não corresponda aos requisitos exigidos pela vaga!

Essa é uma excelente regra de negócio! Ao colocar essa restrição no _System Prompt_, você ensina o agente a aplicar um filtro inicial rigoroso, poupando tempo da equipe de Recursos Humanos.

No jargão de agentes de IA, esse tipo de instrução molda o **comportamento de tomada de decisão** do agente.

Se fôssemos traduzir a sua ideia para o _System Prompt_ estruturado que o agente vai ler, a seção de regras ficaria mais ou menos assim:

> **[REGRAS E RESTRIÇÕES]**
> 
> - **Filtro Obrigatório:** Você deve extrair os requisitos técnicos da vaga e compará-los com o currículo enviado.
>     
> - **Critério de Rejeição:** Se o candidato não cumprir os requisitos mínimos obrigatórios (ex: tempo de experiência ou formação específica), encerre a análise imediatamente e classifique o currículo como "Não Compatível". Não avance para a fase de feedback detalhado nesses casos.
>     

Agora, imagine que esse mesmo agente de RH recebeu um currículo muito bom, mas o arquivo está em formato de imagem (um print ou foto) e não em texto.

Para que o agente consiga ler esse currículo, o desenvolvedor precisa ativar uma habilidade específica no modelo de IA.

Pensando nos pilares que vimos antes (Raciocínio, Ferramentas, Memória, Interação/Percepção), qual recurso técnico o modelo precisa ter para lidar com essa imagem?

1. **Memória de longo prazo** (banco de dados vetorial).    
2. **Visão computacional** (capacidade multimodal de processar imagens).    
3. **API de busca web** (ferramenta de navegação).    

Qual dessas opções daria ao agente a skill necessária para ler a foto do currículo?

## 👁️ Visão computacional

Exatamente! É a opção 2. 👁️

Para que um agente de IA consiga analisar um currículo que não é um arquivo de texto, ele precisa ter uma habilidade multimodal, especificamente a de **Visão Computacional**. Sem esse recurso, ele "enxerga" apenas caracteres. Essa skill permite que ele interprete a imagem, extraia as informações textuais relevantes e, só então, comece o processo de análise que vimos anteriormente.

Se dermos um passo atrás e olharmos para como isso tudo se conecta no prompt do sistema, teríamos:

1. **[PERFIL]** "Você é um especialista em recrutamento e seleção."    
2. **[REGRAS]** "Compare o currículo com os requisitos da vaga; se não corresponder, rejeite imediatamente." (Sua instrução anterior!)    
3. **[HABILIDADES ADICIONAIS]** "Você é capaz de processar imagens de documentos (OCR) para extrair texto de currículos em formato gráfico." (A nossa nova habilidade de visão!)
    

### Criando a Estrutura de Avaliação

Agora que você já entende a anatomia de um _System Prompt_ e como inserimos habilidades nele, podemos ver como essa estrutura se torna operacional.

A figura abaixo resume visualmente como organizamos um agente robusto: partimos de um **Perfil** claro, definimos as suas **Ferramentas**, estabelecemos as **Restrições** (aquelas regras críticas que discutimos) e, por fim, descrevemos o **Processo de Raciocínio** (o "como ele deve pensar").

[IMAGE]

O diagrama acima mostra que um agente não é apenas um modelo de linguagem, mas um sistema composto.

Para fecharmos essa análise sobre _System Prompts_, vamos imaginar um cenário de falha. Se você, como analista de IA, notar que o agente de RH está sendo **rancoroso** e dando feedbacks **grosseiros** aos candidatos rejeitados, em qual das 4 seções do diagrama acima você focaria o ajuste para corrigir esse comportamento?

1. Perfil / Identidade    
2. Ferramentas    
3. Restrições    
4. Processo de Raciocínio / Fluxo

## 👤 O perfil do agente

Exatamente! Se o agente está sendo grosseiro ou inadequado no tom, o problema está na definição de quem ele é: o **Perfil / Identidade** 👤.

É nessa seção do prompt que definimos a persona, o tom de voz (ex: "gentil", "profissional", "empático") e como ele deve tratar o usuário. Se o perfil não estiver bem calibrado, o agente pode adotar uma postura indesejada.

Com isso, passamos pelos dois pontos principais de como os agentes funcionam por trás dos panos usando _System Prompts_! 🛠️

Agora podemos avançar para a última parte do nosso plano inicial: **Métricas e Avaliação (Como medir)**. Afinal, como analista de IA, você precisará testar se as habilidades do agente estão realmente funcionando antes de colocá-lo no mercado.

Para entender como avaliamos um agente, imagine que você quer testar a skill de **Filtro Obrigatório** (rejeitar currículos sem os requisitos) que criamos para o nosso agente de RH.

Como você faria esse teste?

1. Enviando apenas currículos perfeitos para ver se ele aprova todos.    
2. Enviando uma mistura de currículos bons e currículos que de fato **não cumprem** os requisitos, para ver se ele realmente rejeita os incorretos.    

Qual dessas abordagens faz mais sentido para avaliar essa habilidade específica?
