---
title: TOON
description: "pode reduzir significativamente os custos de processamento de dados em modelos de linguagem"
tags:
  - Inteligencia-artificial
---

## TOON vs. JSON: O Guia Definitivo para Economia de Tokens em LLMs

Aprenda como o formato **TOON** pode reduzir significativamente os custos de processamento de dados em modelos de linguagem (LLMs) em comparação ao tradicional **[[json]]**.

### Visão Geral

No mundo do desenvolvimento com Inteligência Artificial, o formato de dados não afeta apenas a legibilidade; ele impacta diretamente o **custo por token** e a **janela de contexto**. O TOON (*Token-Oriented Object Notation*) surge como uma alternativa otimizada para enviar grandes volumes de dados estruturados para modelos como GPT, Claude e Gemini, focando na eficiência técnica em vez da estética humana.

---

### O que é TOON?

**TOON** significa **Token-Oriented Object Notation**. É um formato de serialização projetado especificamente para ser interpretado por LLMs. Sua principal característica é a redução drástica de repetições estruturais.

> [!INFO] A Sacada do TOON
> Em vez de repetir o nome de cada chave (como `"id"`, `"nome"`, `"preco"`) para cada item de uma lista, o TOON declara o esquema uma única vez no cabeçalho e organiza os valores de forma compacta.

### Por que ele é importante para estudantes de IA?

Se você está construindo sistemas que processam catálogos de produtos, logs de servidores ou tabelas extensas, o uso de JSON convencional pode "desperdiçar" milhares de tokens apenas repetindo nomes de campos. Para um aluno ou desenvolvedor, entender o TOON significa:
1. **Redução de Custos:** Menos tokens enviados = conta menor no final do mês.
2. **Melhor Aproveitamento do Contexto:** Você consegue enviar mais dados reais dentro do mesmo limite de caracteres do modelo.
3. **Acurácia:** Menos "ruído" (chaves repetidas) pode ajudar o modelo a focar nos dados que importam.

---

### TOON vs. JSON: A Diferença na Prática

A maior vantagem do TOON aparece em **dados tabulares** (listas de objetos uniformes).

#### Exemplo Comparativo

**No JSON (Formatado):**

```json
[
  {"nome": "Elefante", "dieta": "Herbívoro", "habitat": "Savana"},
  {"nome": "Tubarão", "dieta": "Carnívoro", "habitat": "Oceano"}
]
```

*Aqui, as aspas, chaves e nomes de campos são repetidos em cada linha.*

**No TOON:**

```text
animals: [name, diet, habitat]
- African Elephant, mammal, savanna
- Great White Shark, fish, ocean
```

*O esquema é definido uma vez. Os registros viram linhas simples.*

#### Tabela de Benchmarks

| Cenário | Economia de Tokens | Veredito |
| :--- | :--- | :--- |
| **Dados Tabulares / Uniformes** | **30% a 60%** | TOON é excelente |
| **Logs e Eventos** | **~60%** | TOON reduz custo operacional |
| **Estruturas Complexas/Aninhadas** | **Marginal ou Nula** | JSON é mais seguro |

---

### Quando usar cada um?

#### Escolha o TOON quando

- Você tem listas grandes com a mesma estrutura de campos (ex: lista de 100 produtos).
- O custo de tokens é uma preocupação crítica no seu projeto.
- Você está enviando dados para a **entrada (input)** do modelo.

#### Continue com o JSON quando

- A prioridade é a **compatibilidade** com outros sistemas (APIs, Front-end).
- Os dados são heterogêneos (cada objeto tem campos diferentes).
- Você precisa de **Structured Output** (o modelo deve responder em um formato rígido para o código ler).
- A equipe ainda não está familiarizada com novos formatos.

---

### Como Testar no seu Laboratório (Python)

Se você é aluno da trilha de **Python** ou **IA**, pode testar o TOON facilmente.

#### 1. Instalação

```bash
pip install git+https://github.com/toon-format/toon-python.git
```

#### 2. Código de Exemplo

```python
from toon_format import encode, estimate_savings

# Seus dados originais
data = {
    "cursos_senac": [
        {"titulo": "Python para IA", "carga_horaria": 40, "nivel": "Intermediário"},
        {"titulo": "Desenvolvimento Web", "carga_horaria": 60, "nivel": "Básico"},
    ]
}

# Converte para TOON
toon_data = encode(data)
print("--- Formato TOON ---")
print(toon_data)

# Estima a economia
savings = estimate_savings(data)
print(f"\nEconomia estimada: {savings['savings_percentage']:.2f}%")
```

---

### Conclusão: O Caminho da Decisão

Não troque o JSON pelo TOON por "moda". Siga esta lógica:

1. **Minifique seu JSON:** Antes de tudo, remova espaços e quebras de linha do seu JSON de envio.
2. **Meça o Custo:** Se o JSON minificado ainda for muito caro, teste o TOON.
3. **Híbrido é Melhor:** Mantenha seu banco de dados e APIs em JSON. Use o TOON apenas na "ponte" de conversa com a IA.

> [!TIP] Dica de Ouro
> O TOON não é um substituto para o JSON no sistema todo, mas sim uma ferramenta de otimização de **inferência**.

---

## Referências

- [TOON - Token-Oriented Object Notation](https://toonformat.dev/)
- [É o fim do JSON Prompting? O hype do TOON faz sentido? - YouTube](https://www.youtube.com/watch?v=KO6a3QYpZbo)

**Tópicos Relacionados:**
- [[engenharia de prompt|Engenharia de Prompts]]
- [[Python para Dados]]
- [[Parâmetros de LLM]]
- [[json|Formato JSON]]
