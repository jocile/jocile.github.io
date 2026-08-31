---
title: "Engenharia de prompt"
description: "Como criar prompts eficazes para obter os resultados desejados desses modelos."
tags:
  - Inteligencia-artificial/Prompt
---
## A **Engenharia de Prompt**

É um campo essencial no desenvolvimento de aplicações de Inteligência Artificial (IA), especialmente aquelas que utilizam modelos de linguagem grandes (LLMs). Essencialmente, ela se concentra na arte e ciência de criar prompts eficazes para obter os resultados desejados desses modelos. Essa área envolve tanto um conhecimento técnico quanto uma abordagem empírica para testar e refinar esses prompts.

A engenharia de prompt é um campo em constante evolução no desenvolvimento de aplicações de Inteligência Artificial (IA), especialmente aquelas que utilizam modelos de linguagem grandes (LLMs). Essa área se concentra na arte e ciência de criar prompts eficazes para obter os resultados desejados desses modelos.

A engenharia de prompt envolve tanto um conhecimento técnico quanto uma abordagem empírica para testar e refinar esses prompts. Isso significa que os profissionais nessa área precisam ter habilidades técnicas em áreas como programação, processamento de linguagem natural (NLP) e ciência de dados, além de uma abordagem criativa e experimentadora.

>[!summary] O que é
> * É um campo essencial no desenvolvimento de aplicações de IA que utiliza modelos de linguagem grandes (LLMs).
> * Concentra-se na criação de prompts eficazes para obter resultados desejados.
> * Envolve conhecimento técnico e abordagem empírica para testar e refinar os prompts.
> * Requer habilidades técnicas em áreas como programação, NLP e ciência de dados, além de uma abordagem criativa.

A engenharia de prompt tem diversas aplicações práticas. Por exemplo:

*   **Respostas Personalizadas**: Um modelo de IA pode ser treinado para gerar respostas personalizadas a partir de prompts específicos, como responder a perguntas sobre um produto ou serviço.
*   **Geração de Conteúdo**: A engenharia de prompt pode ser usada para criar conteúdo automático, como artigos, notícias ou até mesmo histórias de ficção.
*   **Análise de Sentimento**: Os prompts podem ser projetados para analisar o sentimento das pessoas em relação a um produto, serviço ou tema específico.

### **Conceitos Fundamentais**

- **Definição:** Engenharia de prompt é o processo de planejar, criar e testar prompts para gerar as melhores respostas de modelos de linguagem. Não é apenas sobre dar instruções, mas entender como os modelos interpretam essas instruções e como otimizá-las.
- **Importância:** Ela é considerada uma "meta-habilidade" que destrava outras habilidades, permitindo usar LLMs de maneira eficaz para diversos fins.
- **Abordagem Empírica:** A engenharia de prompt é baseada em resultados do mundo real, e não apenas em teoria. Isso significa que é necessário testar e ajustar os prompts com base nas respostas obtidas.
- **Simplicidade:** É importante começar com prompts simples e, se necessário, ir adicionando complexidade. Muitos problemas podem ser resolvidos com prompts diretos e bem formulados.

### **Componentes de um Prompt Eficaz**

![[Diagrama de Engenharia de Prompts.excalidraw]]

- **Persona:** Definir o papel ou a especialidade que o modelo deve assumir. Por exemplo, "Você é um especialista em marketing digital".
- **Roteiro:** Descrever o que você quer que o modelo faça. Por exemplo, "Crie um roteiro para um vídeo no YouTube".
- **Objetivo:** Especificar qual é o resultado desejado. Por exemplo, "O objetivo é aumentar o engajamento do público".
- **Modelo:** Explicar como você quer o resultado formatado. Por exemplo, "Quero o resultado em formato de lista".
- **Panorama (Contexto):** Fornecer informações adicionais que possam ajudar o modelo a entender o contexto.
- **Transformar:** Encorajar a iteração, dar feedback e pedir ajustes para aprimorar o resultado.

Exemplo usando os itens acima:

```
Você é um especialista em comunicação corporativa, responsável por criar mensagens claras e eficazes para anunciar mudanças organizacionais significativas. Crie um roteiro para uma apresentação de vídeo que seja transmitida para todos os funcionários da empresa. O objetivo é informar a equipe sobre as razões pelas quais essas mudanças são necessárias e como elas afetarão cada departamento. Quero o resultado em formato de lista, com títulos claros e exemplos práticos. Fornecer informações adicionais: A empresa está passando por uma reestruturação para se adaptar às mudanças no mercado e melhorar a eficiência operacional. O público-alvo são os funcionários da empresa, que precisam entender as razões pelas quais essas mudanças estão sendo implementadas e como elas afetarão suas rotinas diárias. Encoraje iteração: Por favor, ajuste o roteiro para refletir melhor a voz e o tom da comunicação corporativa da empresa.
```

### **Processo Recomendado para Desenvolver Prompts**

1. **Definir a tarefa e os critérios de sucesso:** Antes de começar a escrever um prompt, é crucial ter clareza sobre o que você deseja alcançar e como saberá se o resultado é satisfatório.
2. **Criar um prompt inicial:** Comece com um prompt simples e direto.
3. **Testar o prompt:** Use o modelo para gerar uma resposta e avalie se ela atende aos seus critérios de sucesso.
4. **Refinar o prompt:** Ajuste o prompt com base no resultado do teste. Adicione detalhes, especifique o formato, altere a persona, ou ajuste a instrução.
5. **Iterar:** Repita os passos de teste e refinamento até obter o resultado desejado.
6. **Produção:** Quando o prompt estiver otimizado, utilize-o para a tarefa desejada.

### **Técnicas Avançadas de Engenharia de Prompt**

- **Markdown:** Formatar o texto do prompt para melhorar a clareza. Títulos, subtítulos e listas podem ajudar o modelo a entender melhor a estrutura do prompt.
- **System Prompt:** Usar um "prompt do sistema" para definir como o modelo deve se comportar. É possível especificar o estilo de linguagem, o formato da resposta, e outras diretrizes.
- **Zero-Shot Prompting:** Fazer perguntas diretamente ao modelo, sem fornecer exemplos.
- **Few-Shot Prompting:** Fornecer exemplos de entradas e saídas para guiar o modelo.
- **Self-Consistency:** Gerar múltiplas respostas e pedir para o modelo compará-las e escolher aquela que tem a maior probabilidade de estar correta.
- **Chain-of-Thought (CoT):** Incentivar o modelo a detalhar o raciocínio passo a passo. Isso pode ser útil para problemas mais complexos.
- **Tree-of-Thought (ToT):** Expandir a técnica CoT para gerar múltiplas linhas de raciocínio e avaliá-las.
- **Geração de Conhecimento por Prompt:** Usar prompts para extrair conhecimento do modelo, o qual pode ser usado para aprimorar outros prompts.
- **Temperatura:** Controlar a criatividade do modelo através do parâmetro de "temperatura". Valores altos levam a respostas mais criativas e valores baixos levam a respostas mais factuais.
- **Consistência Própria:** Pedir para o modelo gerar várias respostas para um mesmo problema e avaliar qual tem maior probabilidade de estar correta, usando as próprias respostas como contexto.

### **Ferramentas e Técnicas Auxiliares**

- **Uso de APIs:** Para tarefas complexas, pode ser útil integrar o modelo a outras ferramentas ou APIs.
- **Testar diferentes modelos:** Nem todos os modelos de linguagem funcionam da mesma forma. É importante testar diferentes modelos para encontrar aquele que melhor se adapta à tarefa.
- **Iteração Contínua:** A engenharia de prompt é um processo contínuo de teste e ajuste. Esteja preparado para refinar seus prompts conforme necessário.

>[!abstract] A engenharia de prompt é uma habilidade fundamental para quem deseja tirar o máximo proveito dos modelos de linguagem. Ao dominar os conceitos e técnicas, é possível criar agentes e aplicações de IA mais eficazes e alinhados com as necessidades específicas.

## Referências

- [Engenharia de Prompt: O Guia Definitivo - YouTube](https://www.youtube.com/watch?v=1VDcke66TRE)
- [Custom instructions for ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)
- [Writing ChatGPT Prompts That Get Results (with Examples) \| Grammarly](https://www.grammarly.com/blog/ai/chatgpt-prompts/)
- [Instrucoes Detalhadas no Prompt](Instrucoes%20Detalhadas%20no%20Prompt.md)
- [[Diagrama de Engenharia de Prompts.excalidraw]]
