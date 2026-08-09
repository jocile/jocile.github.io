---
title: Modelo de IA Ideal para o seu Hardware
description: "Este guia traduz a engenharia por trás dos parâmetros em decisões práticas"
tags:
  - Inteligencia-artificial/Ollama
---
# Modelo de IA Ideal para o seu Hardware

# Como Escolher o Modelo de IA Ideal para o seu Hardware (Ollama & Claude Code)

Para quem opera na fronteira da IA local em 2026, a barreira de entrada deixou de ser o custo de subscrição e passou a ser a eficiência da arquitetura. Como Arquiteto de Sistemas, vejo muitos usuários frustrados por tentarem rodar modelos pesados em hardware inadequado. Este guia traduz a engenharia por trás dos parâmetros em decisões práticas para que você configure o **Claude Code** com o máximo de performance.

---

### 1. O Conceito Fundamental: Parâmetros vs. Memória de Vídeo (VRAM)

O "cérebro" de um modelo de linguagem é composto por **parâmetros** (os "B" de 8B, 30B). Na computação local, o gargalo não é o processamento bruto da CPU, mas a capacidade e a velocidade da **VRAM** (em PCs com GPUs dedicadas) ou da **Memória Unificada** (em ecossistemas Mac).

A grande mudança em 2026 é a popularização dos modelos **MoE (Mixture of Experts)**. Diferente dos modelos "Densos", onde cada token processado exige o cálculo de todos os parâmetros, os modelos MoE ativam apenas uma fração (especialistas) por vez. Isso permite que um modelo de 30B ofereça inteligência de alto nível ocupando menos espaço e rodando com a velocidade de um modelo de 3B.

**A Regra de Ouro da Memória (Edição 2026)** Para modelos quantizados (formato **GGUF q4_K_M**), calcule aproximadamente **0.7 GB a 1 GB de VRAM para cada 1 bilhão de parâmetros**. No entanto, modelos MoE "socam acima do seu peso": um **Qwen 3.5 Coder 30B-A3B** (que ativa apenas 3B parâmetros) pode rodar em GPUs de 16GB, enquanto um modelo denso de 30B exigiria 24GB+ apenas para o carregamento base.

_Compreendido o peso dos parâmetros, vamos analisar as faixas de hardware específicas para o seu computador._

---

### 2. Categorização por Perfil de Hardware

A performance depende de como o modelo se acomoda na memória. Em Macs, a Memória Unificada permite maior flexibilidade, enquanto em PCs, a VRAM da GPU é o limite rígido.

|Nível de Hardware|VRAM / Memória Mínima|Capacidade Esperada (Local)|
|---|---|---|
|**Budget** (Entrada)|8 GB - 12 GB|Roda modelos leves (7B-8B). Ideal para edições de arquivo único e scripts simples.|
|**Mid-Range** (Intermediário)|16 GB - 24 GB|**O Sweet Spot.** Suporta modelos MoE como **Gemma 4 26B** ou **Qwen 3.5 30B-A3B**.|
|**High-End** (Entusiasta)|24 GB+ (GPU) / 64 GB+ (Mac)|Modelos densos de 30B+ ou MoE massivos (480B). Foco em refatoração de sistemas inteiros.|

_Além da VRAM bruta, a arquitetura do modelo define a velocidade e a eficiência da execução._

---

### 3. Modelos Densos vs. Otimizados (MoE e Quantização)

Para maximizar seu hardware, você deve priorizar modelos com arquiteturas eficientes:

- **MoE (Mixture of Experts):** O exemplo de elite é o **Gemma 4 26B MoE**. Ele possui 26 bilhões de parâmetros totais para conhecimento, mas ativa apenas **3.8B** para processamento. Resultado? Velocidades de até 300 tokens/segundo em hardware Mac moderno, mantendo a precisão de modelos muito maiores.
- **Quantização (GGUF):** Quase todos os modelos no Ollama são quantizados. O formato `q4_K_M` é o padrão da indústria para 2026, reduzindo o uso de memória em mais de 50% com perda de precisão quase imperceptível para codificação.
- **Active vs. Total:** Ao escolher um modelo, verifique o sufixo (ex: A3B significa 3 bilhões de parâmetros ativos). Isso dita a velocidade real de resposta.

_Agora que você entende a eficiência, vamos olhar para os modelos recomendados para fluxos de trabalho com Claude Code._

---

### 4. Catálogo de Seleção: Modelos Recomendados (2026)

O ecossistema Ollama agora permite alternar entre execução local pura e modelos em nuvem (Cloud) que não consomem VRAM local.

#### **Modelos Locais Leves (8B-14B)**

_Ideais para laptops e máquinas com 16GB de RAM total._

- **Qwen 3.5 Coder 4B/8B:** O mais ágil para correções rápidas de bugs.
- **Llama 3.2 8B:** Excelente equilíbrio entre instrução e lógica geral.
- **Phi-4 14B:** A escolha para quem precisa de lógica matemática superior em hardware leve.

#### **Modelos Locais Médios/Pesados (20B-30B+)**

_Exigem GPUs de 16GB-24GB ou Macs com 32GB+._

- **Qwen 3.5 Coder 30B-A3B:** Atualmente o "padrão ouro" para agentes locais; o MoE permite rodar com 16GB de VRAM, embora 24GB sejam recomendados para janelas de contexto longas.
- **Gemma 4 26B MoE:** O equilíbrio perfeito entre inteligência e velocidade de geração.
- **gpt-oss:20b:** Modelo robusto para automação de infraestrutura.

#### **Modelos Cloud (Zero VRAM Local)**

_Se o seu hardware é limitado, use a infraestrutura do Ollama Cloud para rodar modelos gigantes sem custo de VRAM local._

- **GLM-5:cloud:** Performance de ponta para arquiteturas complexas.
- **MiniMax-M2.7:cloud:** Especializado em fluxos de agentes e alta velocidade.
- **Qwen 3.5:cloud:** Versão completa sem as limitações de memória da sua máquina.

_A escolha do modelo não depende apenas dos parâmetros, mas também do gerenciamento do cache de memória._

---

### 5. O Impacto Crítico da Janela de Contexto e o KV Cache

A **Janela de Contexto** é onde o Claude Code armazena o histórico do projeto e os arquivos lidos. Tecnicamente, isso é gerenciado pelo **KV Cache** (Key-Value Cache) na sua VRAM.

O problema: **Contexto consome VRAM adicional além dos parâmetros.** Um modelo que ocupa 14GB de VRAM pode saltar para 22GB se você carregar 64k tokens de contexto. Para agentes como o Claude Code, que precisam "ler" múltiplos arquivos, uma janela pequena (4k-8k) resultará em um agente que "esquece" o código que acabou de analisar.

**Dica Pro: Configuração de Contexto** O Claude Code exige, no mínimo, **32k a 64k tokens** para ser útil. No Ollama local, você deve ajustar isso manualmente via `PARAMETER num_ctx`. **Atenção:** Modelos `:cloud` no Ollama (ex: `GLM-5:cloud`) processam a janela de contexto completa nos servidores da Ollama, poupando 100% da sua VRAM local para outras tarefas.

---

### 6. Roteiro de Decisão: Estratégia Híbrida

Como arquiteto, recomendo uma **Estratégia Híbrida**: use modelos locais para tarefas de arquivo único e mude para a nuvem em refatorações complexas.

#### **O Novo Comando Padrão**

Esqueça a configuração manual de variáveis de ambiente. Em 2026, a recomendação primária para iniciar qualquer ferramenta é o comando unificado: `ollama launch claude` Este comando automatiza as variáveis Anthropic e permite selecionar o modelo via menu interativo.

#### **Tabela de Decisão Final**

|Se seu hardware tem...|E a tarefa é...|Estratégia Recomendada|Comando Ollama|
|---|---|---|---|
|**6 GB VRAM**|Simples / Scripting|**Local Leve**|`ollama launch claude --model qwen3.5-coder:4b`|
|**8 GB VRAM**|Simples / Scripting|**Local Leve**|`ollama launch claude --model qwen3.5-coder:7b`|
|**16 GB - 24 GB**|Dev Diário / Agente|**Local MoE**|`ollama launch claude --model gemma4:26b`|
|**Qualquer HW**|Refatoração de Sistema|**Ollama Cloud**|`ollama launch claude --model glm-5:cloud`|
|**Mac Studio / 4090**|Pesquisa / Raciocínio|**Local Pesado**|`ollama launch claude --model qwen3.5-coder:30b`|

Com este roteiro, você garante estabilidade e evita erros de _Out of Memory_ (OOM), permitindo que o Claude Code opere como um verdadeiro membro sênior da sua equipe de desenvolvimento.

[Ollama](https://ollama.com/)
