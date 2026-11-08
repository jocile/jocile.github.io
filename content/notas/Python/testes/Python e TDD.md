---
title: "Python e TDD"
date: 2026-11-08
draft: false
tags:
  - python
  - tdd
  - testing
  - qualidade-do-código
description: "Guia prático de Test-Driven Development em Python utilizando unittest, com ciclo Red-Green-Refactor."
---

Para usar Python e TDD (Test-Driven Development) de forma eficiente, você deve seguir um ciclo contínuo conhecido como Red, Green, Refactor (Vermelho, Verde, Refatorar). Em vez de escrever o código e depois testar, você inverte o processo: escreve o teste primeiro para identificar o que sua aplicação deveria fazer, vê o teste falhar e, então, escreve o código para corrigir essa falha.

Abaixo, apresentamos o passo a passo prático de como aplicar o TDD para identificar, corrigir erros e evoluir uma aplicação Python utilizando a biblioteca nativa unittest.

## 🔄 O Ciclo TDD: Red, Green, Refactor

1. **RED (Falhar)** → Escreva um teste que falha porque a funcionalidade não existe.
2. **GREEN (Passar)** → Escreva o código mínimo necessário para o teste passar.
3. **REFACTOR (Melhor)** → Limpe o código, remova duplicidades e melhore o design.

## 💻 Exemplo Prático: Criando uma Calculadora de Descontos

Imagine que precisamos criar uma função que calcula descontos para um e-commerce. Se o valor for acima de R$ 100, damos 10% de desconto. Se for menor, nenhum desconto é aplicado.

### Passo 1: Escrever o Teste Primeiro (Red 🔴)

Crie um arquivo chamado `test_calculadora.py`. Como a função `calcular_desconto` ainda não existe, o teste vai falhar imediatamente.

```python
import unittest

# Importamos a função que ainda vamos criar
from calculadora import calcular_desconto

class TestCalculadoraDesconto(unittest.TestCase):

    def test_desconto_para_valores_acima_de_cem(self):
        # Cenário: Valor de R$ 150 deve ter 10% de desconto (R$ 15)
        resultado = calcular_desconto(150)
        self.assertEqual(resultado, 15)

    def test_sem_desconto_para_valores_baixos(self):
        # Cenário: Valor de R$ 80 não deve ter desconto (R$ 0)
        resultado = calcular_desconto(80)
        self.assertEqual(resultado, 0)

if __name__ == '__main__':
    unittest.main()
```

Use o código com cuidado. Ao executar `python test_calculadora.py`, você verá um erro (`ModuleNotFoundError` ou `ImportError`). O teste falhou com sucesso! Você identificou o primeiro "erro": a ausência do código.

### Passo 2: Escrever o Código Mínimo (Green 🟢)

Crie o arquivo `calculadora.py` e escreva apenas o código necessário para fazer o teste passar. Não tente criar o código perfeito agora.

```python
def calcular_desconto(valor):
    if valor > 100:
        return valor * 0.1
    return 0
```

Use o código com cuidado. Execute o teste novamente: `python test_calculadora.py`. Agora ele passará com sucesso. O comportamento esperado foi validado.

### Passo 3: Refatorar (Refactor 🔵)

Se o código estiver confuso ou com números mágicos, limpe-o. Como os testes estão criados, você pode alterar o código com segurança. Se você quebrar algo, o teste avisará.

```python
# Versão refatorada e mais limpa
LIMITE_DESCONTO = 100
PERCENTUAL_DESCONTO = 0.1

def calcular_desconto(valor):
    if valor > LIMITE_DESCONTO:
        return valor * PERCENTUAL_DESCONTO
    return 0
```

Use o código com cuidado.

## 🔍 Como o TDD Ajuda a Identificar e Corrigir Erros (Bugs)

Quando um bug é reportado em produção (ex: "A calculadora está aceitando valores negativos e dando desconto negativo!"), o processo de correção usando TDD segue uma lógica muito clara:

1. Não mexa no código da aplicação ainda.
2. Escreva um teste que reproduza exatamente o bug. Esse teste vai falhar (**Red**), provando que o erro existe.
3. Corrija o código da aplicação até que o novo teste passe (**Green**).
4. Garante que nada mais quebrou: Todos os outros testes antigos devem continuar passando.

### Exemplo de correção de bug

Adicione o teste do bug no seu arquivo `test_calculadora.py`:

```python
def test_valor_negativo_deve_retornar_erro(self):
    # Valores negativos devem levantar um erro de valor (ValueError)
    with self.assertRaises(ValueError):
        calcular_desconto(-50)
```

Use o código com cuidado. Ao rodar, o teste falha porque a função aceita o valor negativo. Agora você corrige a aplicação no `calculadora.py`:

```python
def calcular_desconto(valor):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    if valor > LIMITE_DESCONTO:
        return valor * PERCENTUAL_DESCONTO
    return 0
```

Use o código com cuidado. Rode os testes. O bug foi corrigido, e você tem certeza de que o resto da aplicação continua funcionando.

## 🛠️ Principais Ferramentas e Práticas para Python

- **Pytest**: Embora `unittest` venha nativo no Python, o Pytest é a ferramenta mais utilizada no mercado. Ele torna a escrita de testes muito mais simples, rápida e legível (substitui os `self.assert...` por `assert` puros do Python).
- **Foque em Testes Unitários**: Teste pequenas partes isoladas (funções, métodos) para que seja fácil descobrir exatamente onde o erro está quando um teste falhar.
- **Mantenha os testes rápidos**: O ciclo TDD exige que você rode os testes a cada poucos minutos. Se eles demorarem para rodar, você perderá o hábito de usá-los.

Para te ajudar a aplicar isso no seu cenário real, me conte:

- Você já tem uma aplicação existente ou está começando um projeto do zero?
- Qual é o tipo de aplicação? (Web/API, automação de scripts, análise de dados?)
- Prefere que eu mostre como configurar o Pytest, que é o padrão de mercado mais moderno?
