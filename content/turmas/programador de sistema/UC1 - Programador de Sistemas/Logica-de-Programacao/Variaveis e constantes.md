---
title: Variáveis e constantes
description: Conceitos fundamentais sobre variáveis e constantes em programação.
tags:
  - Lógica
---

## 1. O que são Variáveis?

Variáveis são espaços reservados na memória do computador destinados a armazenar dados que podem ser alterados durante a execução de um programa.

*   **Conceito:** Funcionam como uma "caixa" com um rótulo (nome), onde você guarda um valor.
*   **Mutabilidade:** O valor contido na variável pode ser substituído por outro ao longo do tempo.
*   **Regras de nomeação:** Geralmente não devem começar com números e não devem conter espaços ou caracteres especiais.

**Exemplo:**
```python
pontuacao = 10
pontuacao = 20  # O valor foi alterado
```

---

## 2. O que são Constantes?

Constantes são valores fixos que não sofrem alteração durante toda a execução do programa.

*   **Conceito:** Assim como a variável, é um espaço na memória, mas seu valor é definido uma única vez.
*   **Utilidade:** Utilizadas para representar valores imutáveis, como o valor de PI (3.14) ou configurações de sistema que não devem mudar.
*   **Convenção:** Em muitas linguagens, utiliza-se letras maiúsculas para identificar constantes (ex: `VALOR_MAXIMO`).

**Exemplo:**
```python
PI = 3.14159
TAXA_JUROS = 0.05
```

---

## 3. Diferenças Principais

| Característica | Variável | Constante |
| :--- | :--- | :--- |
| **Valor** | Pode ser alterado | Fixo (imutável) |
| **Uso** | Dados dinâmicos | Dados fixos/configurações |
| **Exemplo** | Nome de usuário, placar | PI, dias da semana |

---

## 4. Tipos de Dados Comuns

Tanto variáveis quanto constantes precisam estar associadas a um tipo de dado para que o computador saiba como processá-las:

*   **Inteiro (int):** Números sem casas decimais (ex: 1, 10, -5).
*   **Ponto Flutuante (float):** Números com casas decimais (ex: 3.14, 2.5).
*   **String (str):** Sequência de caracteres/texto (ex: "Olá, mundo!").
*   **Booleano (bool):** Valores lógicos (Verdadeiro ou Falso).

---

### Dicas de Boas Práticas

1.  **Nomes descritivos:** Use nomes que indiquem o que a variável armazena (ex: `precoProduto` em vez de apenas `x`).
2.  **Consistência:** Siga o padrão de escrita da linguagem (ex: `camelCase` ou `snake_case`).
3.  **Use constantes quando necessário:** Sempre que um valor não precisar mudar, declare-o como constante para tornar o código mais seguro e legível.
