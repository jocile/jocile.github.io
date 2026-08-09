---
title: code smells
description: "são padrões no código fonte que indicam problemas e melhorias"
tags:
  - Inteligencia-artificial
---

## code smells

**code smells** (ou *cheiro de código*) são características ou padrões no código fonte que indicam **problemas mais profundos** na estruturação do software. Embora os code smells não sejam bugs — pois nem sempre causam falhas no programa —, muitas vezes sinalizam questões que dificultam a manutenção, compreensão ou expansão do código, e podem levar a defeitos ou ineficiências no futuro[^2][^3][^5].

O conceito foi popularizado por Kent Beck e Martin Fowler nos anos 1990 e formalizado no livro *Refactoring: Improving the Design of Existing Code* de Fowler, publicado em 1999[^2][^4].

### Pontos-chave sobre code smells

- Eles sugerem práticas de programação deficientes, como má modularização, complexidade excessiva ou violações aos princípios orientados a objetos[^1][^5].
- Os code smells tendem a acumular-se ao longo do tempo à medida que o software evolui e a manutenção é negligenciada[^1].
- Tipos comuns de code smells incluem:
    - **Bloaters:** Classes ou métodos muito grandes que lidam com muitas responsabilidades ou se tornaram excessivamente volumosos[^1][^2].\
    *Violações* (ou *Dirties*) são códigos cujas intenções originais foram violadas, mas não explicitamente ruins. Ex: usar variáveis locais para armazenar dados que deveriam ser de uma classe.
    - **Violações:** Mesmo que acima
    - **Código duplicado:** Ocorrência repetida do mesmo ou código semelhante, prejudicando a manutenção[^3][^5].
    - **Métodos longos ou listas de parâmetros excessivas:** Funções fazendo mais do que deveriam ou com muitos parâmetros, reduzindo a legibilidade e reutilização[^5].
    - **Violação de Single Responsibility Principle (SRP):** Uma classe ou função tem mais de uma responsabilidade.
    - **Shotgun surgery:** Quando uma única alteração requer modificações em múltiplos lugares[^1][^3]. 
    - **Data clumps:** Agrupamentos repetitivos de itens de dados, sugerindo má abstração[^3][^5].
    - **Abusos da orientação a objetos:** Uso incorreto de conceitos OO como herança e encapsulamento[^1][^5].
    - **Código morto (Dead code):** Código não usado ou inalcançável que polui o repositório[^5].
- Os code smells impedem mudanças futuras e aumentam os riscos e custos da evolução do software[^1].
- Identificar code smells precocemente ajuda a prevenir acúmulo de dívida técnica (technical debt) e degradação sistêmica[^8].

### Tratamento dos code smells

- A maneira principal para lidar com os code smells é através de **refatoração** — reestruturar o código sem mudar seu comportamento externo, visando melhorar a estrutura e legibilidade[^5].
- Refatoração pode incluir quebrar métodos grandes, simplificar chamadas de função e abstrair código duplicado[^5].
- Refatorar regularmente ajuda a manter o código saudável[^5].
- Ferramentas automatizadas como SonarQube, Visual Studio Code, etc., podem detectar code smells e auxiliar na correção[^5][^6].

Em resumo, os code smells funcionam como *alertas* no desenvolvimento de software, indicando áreas onde o código precisa ser limpo e melhorado para evitar problemas futuros, aumentar a manutenibilidade e apoiar uma evolução sustentável do sistema[^5][^6].

### Prompts para identificar code smells

1. **"Analise este trecho de código e identifique possíveis code smells presentes."**
    
2. **"Quais code smells você pode encontrar neste arquivo/função/classe?"**
    
3. **"Detecte code smells comuns em projetos Java/Python/JavaScript e explique por quê."**
    
4. **"Liste os principais code smells que podem surgir ao longo do tempo em um sistema legado."**
    
5. **"Dê exemplos de code smells típicos em programação orientada a objetos."**

### Prompts para explicar conceitos de code smells

1. **"Explique o que é o code smell 'Long Method' e por que ele é problemático."**
    
2. **"Como o code smell 'Duplicated Code' pode impactar a manutenção do software?"**
    
3. **"Qual a diferença entre code smells e bugs?"**
    
4. **"Por que o code smell 'Shotgun Surgery' deve ser evitado?"**
    
5. **"Como identificar o code smell 'Data Clumps' e qual é a melhor forma de refatorar?"**

### Prompts para sugerir refatorações baseadas em code smells

1. **"Mostre como refatorar um método longo para torná-lo mais legível e modular."**
    
2. **"Dê exemplos de refatoração para eliminar código duplicado em um projeto."**
    
3. **"Quais técnicas de refatoração são recomendadas para resolver o code smell 'Bloaters'?"**
    
4. **"Como refatorar um código com muitos parâmetros para métodos?"**
    
5. **"Sugira passos para melhorar um código que sofre de 'Shotgun Surgery'."**

### Exemplos práticos

Aqui estão exemplos práticos para cada um dos prompts sugeridos anteriormente sobre code smells, com trechos de código ilustrativos e explicações:

#### 1. Identificando code smells

**Prompt:** “Analise este trecho de código e identifique possíveis code smells presentes.”

```python
def processa(funcionario, salario, bonus, horas, horas_extras, deducao, descontos):
    result = salario + bonus + (horas_extras * 20) - deducao - descontos
    print(f"Funcionario: {funcionario}")
    print(f"Salario final: {result}")
    log_funcionario(funcionario)
```

**Code smells presentes:**

- Long Parameter List (lista de parâmetros longa)
- Data Clumps (muitos dados são passados juntos repetidamente)
- Baixa coesão de responsabilidades

#### 2. Explicando code smells

**Prompt:** “Explique o que é o code smell 'Long Method' e por que ele é problemático.”

**Exemplo:**

```java
public void processOrder(Order order) {
    calculateDiscounts(order);
    updateInventory(order);
    printReceipt(order);
    sendOrderConfirmationEmail(order);
    logOrder(order);
    // ...muitos outros passos aqui
}
```

**Problema:** O método faz muita coisa, dificultando testes e manutenção.

#### 3. Refatorando code smells

**Prompt:** “Mostre como refatorar um método longo para torná-lo mais legível e modular.”

**Antes:**

```javascript
function salvarPedido(pedido) {
  validarPedido(pedido);
  calcularFrete(pedido);
  aplicarDesconto(pedido);
  atualizarEstoque(pedido);
  enviarConfirmacao(pedido);
}
```

**Depois (dividido em métodos menores):**

```javascript
function salvarPedido(pedido) {
  validarEReservar(pedido);
  aplicarPreco(pedido);
  finalizarPedido(pedido);
}

function validarEReservar(pedido) {
  validarPedido(pedido);
  atualizarEstoque(pedido);
}

function aplicarPreco(pedido) {
  calcularFrete(pedido);
  aplicarDesconto(pedido);
}

function finalizarPedido(pedido) {
  enviarConfirmacao(pedido);
}
```

#### 4. Code smell “Duplicated Code” e como remover

**Antes:**

```python
def calcula_total_com_desconto(produtos):
    total = sum(produtos)
    if total > 100:
        total = total * 0.9
    return total

def calcula_total_sem_desconto(produtos):
    total = sum(produtos)
    return total
```

**Depois (removendo duplicidade):**

```python
def calcula_total(produtos, aplica_desconto=False):
    total = sum(produtos)
    if aplica_desconto and total > 100:
        total = total * 0.9
    return total
```

#### 5. Refatorando muitos parâmetros (“Long Parameter List”)

**Antes:**

```java
public void criarCadastro(String nome, String sobrenome, String endereco, String telefone, String email, String rg, String cpf) { /* ... */ }
```

**Depois (usando objeto):**

```java
public void criarCadastro(Pessoa pessoa) { /* ... */ }
```

Se quiser um exemplo aprofundado sobre algum dos code smells mencionados ou ver exemplos em outra linguagem de programação, é só pedir!

<div style="text-align: center">⁂</div>

## Referências

[Perplexity - code smells](https://www.perplexity.ai/search/code-smells-qN84aJ3aSDe0BbSZm_z_2w?0=r)

[^1]: <https://refactoring.guru/pt-br/refactoring/smells>

[^2]: <https://coodesh.com/blog/dicionario/o-que-e-code-smell/>

[^3]: <https://en.wikipedia.org/wiki/Code_smell>

[^4]: <https://pt.wikipedia.org/wiki/Code_smell>

[^5]: <https://www.techtarget.com/searchsoftwarequality/tip/Understanding-code-smells-and-how-refactoring-can-help>

[^6]: <https://www.sonarsource.com/learn/code-smells/>

[^7]: <https://www.opsera.io/blog/what-is-code-smell>

[^8]: <https://www.dio.me/articles/entendendo-code-smells-e-a-importancia-de-identifica-los-precocemente>

[^9]: <https://www.reddit.com/r/learnprogramming/comments/x2ewxi/all_code_smells_oneliner_guide/>

[^10]: <https://blog.codinghorror.com/code-smells/>
