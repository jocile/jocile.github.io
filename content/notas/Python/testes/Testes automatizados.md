---
title: test_calculator.py
description: "Test-Driven Development (TDD) é uma abordagem de desenvolvimento de software que se baseia na repetição de um curto ciclo de desenvolvimento: primeiro o…"
date: 2026-09-17
draft: false
tags:
  - tecnico/testing
  - python/tdd
  - tdd/postrun
  - auto-teste/unitario
---

## TDD - testes automatizados

Test-Driven Development (TDD) é uma abordagem de desenvolvimento de software que se baseia na repetição de um curto ciclo de desenvolvimento: primeiro o desenvolvedor escreve um teste automatizado que define uma nova funcionalidade desejada ou uma melhoria, depois ele produz o código mínimo necessário para passar o teste, e finalmente refatora o novo código para padrões aceitáveis. Vamos explorar os principais conceitos e o fluxo do TDD.

### Benefícios do TDD

- **Feedback Imediato**: Ao escrever testes primeiro, os desenvolvedores recebem feedback imediato sobre se sua implementação está correta.
- **Código Mais Limpo e Melhor Design**: Refatoração constante resulta em código mais limpo e melhor design.
- **Documentação Viva**: Os testes servem como uma forma de documentação viva do que o código deve fazer.
- **Menos Bugs**: Bugs são capturados mais cedo no ciclo de desenvolvimento.

O TDD é uma prática poderosa que pode melhorar significativamente a qualidade do software. No entanto, como qualquer metodologia, requer prática e disciplina. Comece aplicando TDD em pequenos projetos ou funcionalidades e gradualmente adote-a em projetos maiores.

### Princípios Básicos do TDD

1. **Escreva o Teste Primeiro**: Antes de escrever o código que implementa uma funcionalidade, escreva um teste que falhe, pois a funcionalidade ainda não foi implementada.
2. **Faça o Teste Passar**: Escreva o código mais simples possível que faça o teste passar. O objetivo neste estágio é apenas fazer o teste passar, não se preocupar com a otimização ou limpeza do código.
3. **Refatore**: Com o teste passando, refatore o código. Melhore a estrutura e a clareza do código, mantendo todos os testes funcionando.

### Ciclo TDD

O ciclo TDD pode ser resumido em três etapas:

![[Pasted image 20240629231537.png]]

1. **Red**: Escreva um teste que falhe.
2. **Green**: Escreva o código necessário para fazer o teste passar.
3. **Refactor**: Refatore o código, melhorando sua estrutura sem alterar seu comportamento.

## Exemplo Prático com Python e `pytest`

Vamos ver um exemplo prático de TDD usando Python e `pytest`.

### 1. Escreva um Teste que Falhe

Primeiro, instalamos o `pytest` usando o comando no terminal: `pip install pytest`

Em seguida criamos um arquivo de teste `test_calculator.py` com um teste falhando para a funcionalidade de adição.

```python

def test_add():
 from calculator import add
 assert add(2, 3) == 5
```

Finalmente executamos o comando para verificar o resultado: `pytest`

### 2. Faça o Teste Passar

Agora, criamos o arquivo `calculator.py` com a implementação mínima para fazer o teste passar.

```python
# calculator.py

def add(a, b):
 return a + b
```

Agora executamos novamente o `pytest` para verificar o resultado. Você deve ver uma saída indicando que todos os testes passaram.

### 3. Refatore o Código

Neste caso, o código já está bem simples, então não há muito a refatorar. No entanto, se tivéssemos uma implementação mais complexa, este seria o momento de melhorar a estrutura do código.

## Tipos de Testes

- **Importância dos Testes:** Garantir que o código funcione como esperado e detectar erros o mais cedo possível.
- **Testes Automatizados vs. Manuais:** Os testes automatizados são executados por programas de teste, enquanto os testes manuais são feitos pelo desenvolvedor.

---

### 1. Teste de Unidade

- **Definição:** Um teste de unidade verifica o funcionamento de uma unidade específica de código, como uma função ou método.
- **Objetivo:** Garantir que cada parte individual do código funcione corretamente de forma isolada.

---

- **Exemplo Simples:**

 ```python
 def soma(a, b):
 return a + b

 def test_soma():
 assert soma(1, 2) == 3
 assert soma(-1, 1) == 0
 ```

---

#### Frameworks de Teste

- **[Unittest](unittest.md):** Um módulo padrão que já vem embutido no Python para criação e execução de testes.
- **Estrutura de um Teste com Unittest:**

 ```python
 import unittest

 class TestSoma(unittest.TestCase):
 def test_soma(self):
 self.assertEqual(soma(1, 2), 3)
 self.assertEqual(soma(-1, 1), 0)

 if __name__ == '__main__':
 unittest.main()
 ```

- **[Pytest](pytest.md):** Framework externo de testes em Python com recursos mais avançados.

---

### 2. Teste de Regressão

- **Definição:** Testes que verificam se alterações no código quebram funcionalidades existentes.
- **Importância:** Garantir que novas funcionalidades ou correções não introduzam novos bugs.

---

### 3. Teste de Integração

- **Definição:** Verifica se diferentes unidades de código funcionam bem juntas.
- **Objetivo:** Garantir que componentes interajam corretamente.

---

### 4. Cobertura de Testes

- **Definição:** Medida de quanto do seu código é coberto pelos testes.
- **Ferramentas:** Existem ferramentas como `coverage.py` que ajudam a medir a cobertura de testes.
- **Meta:** Idealmente, ter uma alta cobertura, mas também garantir que os testes sejam significativos.

---

### 5. Técnicas de Debugging

- **Print Statements:** Uso de prints para verificar o estado do programa.
- **Uso de Debuggers:** Ferramentas como `pdb` no Python para analisar passo a passo a execução do código.

---

## Erros Comuns e Como Evitá-los

- **Falsos Positivos/Negativos:** Testes que passam/falham quando não deveriam.
- **Manutenção de Testes:** Garantir que os testes sejam atualizados conforme o código evolui.
- **Testes Frágeis:** Testes que falham frequentemente por pequenas mudanças no código.

---

## Práticas Recomendadas

- **Escreva Testes Antes do Código:** TDD (Test-Driven Development).
- **Mantenha os Testes Simples e Claros:** Facilitar a manutenção e a compreensão.
- **Automatize a Execução dos Testes:** Use ferramentas de CI/CD para executar testes automaticamente a cada mudança no código.

---

## Referências

- [Python - Testes | Python | Tech Guide: guias do Profissional em T](https://techguide.sh/pt-BR/path/python/python-testing/)
- [Get Started - pytest documentation](https://docs.pytest.org/en/8.2.x/getting-started.html)
- [TDD com Python Simple e Fácil. - YouTube](https://www.youtube.com/watch?v=umrpOLCIQdI)
- /testes
