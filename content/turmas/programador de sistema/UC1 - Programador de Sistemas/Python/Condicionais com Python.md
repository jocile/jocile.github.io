---
title: "Condicionais com Python"
date: 2026-09-23
draft: false
tags:
  - python
  - programacao
  - logica
description: "Expressões lógica e condicionais com Python, incluindo if, else, elif, match case e tratamento de exceções."
---

## Estrutura if/else

A estrutura if/else permite executar um bloco de código se a condição for verdadeira, ou outro se for falsa. A sintaxe é a seguinte:

```python
if condicao:
    # bloco de código a ser executado se a condição for verdadeira
else:
    # bloco de código a ser executado se a condição anteriores for falsa

```

Exemplos: Usando a estrutura if-else para fazer escolhas:

```python
x = 10
if x > 0:
    print("x é positivo")
else:
    print("x é negativo ou zero")

```

Escreva um programa em Python que peça ao usuário para digitar uma palavra e verifique se a palavra é um palíndromo (ou seja, se ela é igual quando lida de trás para frente).

```python
palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")

```

Nesse algoritmo, usamos a função input() para pedir que o usuário digite uma palavra. Em seguida, usamos um condicional if para verificar se a palavra é igual a ela mesma quando lida de trás para frente (usando a técnica de slicing com a notação [::-1]). Se a palavra for um palíndromo, exibimos uma mensagem indicando isso. Caso contrário, exibimos uma mensagem indicando que a palavra não é um palíndromo.

## Condicional aninhada if/elif/else

São condicionais seguidas ou dentro de outras condicionais. A estrutura if/elif/else permite executar diferentes blocos de código dependendo de uma ou mais condições. A sintaxe é a seguinte:

```python
if condicao1:
    # bloco de código a ser executado se a condicao1 for verdadeira
elif condicao2:
    # bloco de código a ser executado se a condicao1 for falsa e a condicao2 for verdadeira
else:
    # bloco de código a ser executado se todas as condições anteriores forem falsas

```

```python
# Fazendo escolhas múltiplas usando a estrutura if-elif-else
x = 10
if x < 0:
    print("x é negativo")
elif x == 0:
    print("x é zero")
else:
    print("x é positivo")

```

Exemplo: Elabore um algoritmo para checar se uma pessoa pode dirigir:

```python
idade = 18
tem_carteira = True

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Não pode dirigir, pois não tem carteira de motorista")
else:
    print("Não pode dirigir, pois é menor de idade")

```

Nesse exemplo, temos duas condições aninhadas: a primeira checa se a pessoa é maior de idade, e a segunda checa se ela tem carteira de motorista. Se ambas as condições forem verdadeiras, o programa imprime a mensagem "Pode dirigir". Caso contrário, o programa imprime uma mensagem diferente.

>[!info] Note que condicionais aninhadas podem ser úteis quando precisamos checar várias condições em sequência. No entanto, elas podem tornar o código mais difícil de ler e entender, especialmente se tivermos muitas condições aninhadas. Por isso, é importante avaliar cuidadosamente se essa é a melhor abordagem para o problema em questão.

## Expressão ternária

A expressão ternária é uma forma concisa de escrever uma condicional em uma única linha de código. A sintaxe é a seguinte:

```python
valor_se_verdadeiro if condicao else valor_se_falso
```

Exemplos:

```python
# Usando o operador condicional para simplificar o código
x = 10
result = "x é positivo" if x > 0 else "x é negativo ou zero"
print(result)

```

Exemplo: uma função que retorna a maior idade.

```python
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)
```

Nesse exemplo, a expressão idade >= 18 é avaliada primeiro. Se for verdadeira, a variável status receberá o valor "maior de idade". Caso contrário, status receberá o valor "menor de idade". O resultado impresso no console será "maior de idade", já que a idade é igual a 18, e portanto maior ou igual a 18.

>[!info] Note que a expressão ternária pode ser muito útil para simplificar o código em casos onde a condição é simples e não é necessário executar um grande bloco de código em cada caso. No entanto, em casos onde a condição é mais complexa ou é necessário executar várias instruções em cada caso, a estrutura if/elif/else é geralmente mais adequada.

## Match Case

O Match Case, introduzido no Python 3.10, é uma nova estrutura de controle de fluxo que visa tornar o código mais legível e organizado, especialmente quando se trata de lidar com múltiplas comparações de valores. Ele funciona de maneira similar ao switch-case encontrado em outras linguagens, mas com algumas vantagens e particularidades.

**Como funciona:**

1. **Expressão a ser comparada:** A estrutura `match` inicia com a expressão que será comparada com os diferentes casos. Essa expressão pode ser uma variável, um literal ou qualquer outra expressão válida em Python.
    
2. **Casos:** Em seguida, são definidos os diferentes casos a serem considerados. Cada caso é iniciado pela palavra-chave `case`, seguida do valor a ser comparado com a expressão. É possível utilizar padrões de correspondência, como curingas (`*`) e ranges (`1..5`), para maior flexibilidade.
    
3. **Ações:** Cada caso pode conter um ou mais blocos de código a serem executados se a comparação for bem-sucedida. Esses blocos podem conter qualquer instrução válida em Python.
    
4. **Caso padrão (opcional):** Por fim, é possível definir um caso padrão, representado por `_`, que será executado caso nenhum dos outros casos seja verdadeiro.

**Exemplo básico:**

```python
dia = "segunda"

match dia:
  case "segunda":
    print("Segunda-feira!")
  case "terça":
    print("Terça-feira!")
  case "quarta":
    print("Quarta-feira!")
  case _:
    print("Dia inválido!")
```

**Vantagens do Match Case:**

- **Maior legibilidade:** O código fica mais organizado e fácil de entender, especialmente quando se trata de múltiplas comparações.
- **Menos aninhamentos:** Elimina a necessidade de aninhamentos complexos de instruções `if/elif/else`, tornando o código mais conciso.
- **Melhor manutenabilidade:** Facilita a leitura e modificação do código, especialmente em projetos maiores.
- **Maior expressividade:** Permite utilizar padrões de correspondência mais flexíveis e expressivos.

**Casos de uso:**

- Comparar valores de variáveis com diferentes opções.
- Analisar resultados de funções ou APIs.
- Tratar diferentes tipos de erros ou exceções.
- Implementar menus ou interfaces de usuário com diversas opções.

**Observações:**

- O Match Case é uma nova funcionalidade e ainda não está disponível em todas as versões do Python. Certifique-se de estar utilizando a versão 3.10 ou superior.
- O Match Case não substitui completamente as instruções `if/elif/else`. Em alguns casos, elas ainda podem ser mais adequadas.
- É importante utilizar o Match Case de forma adequada para evitar código ilegível ou confuso.

## Exceções

Podemos fazer testes para evitar erros, e assim permitir que o programa se recupere e continue executando mesmo em situações inesperadas.

Por exemplo, o programa tenta ler dois números do usuário e realizar uma divisão entre eles. No entanto, como podemos ter vários tipos de erros nessa operação (o usuário pode digitar um valor que não é um número inteiro, ou pode tentar dividir por zero), utilizamos a estrutura try/except para capturar e tratar esses erros. Confira no seguinte código em Python:

```python
try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
    print("O resultado da divisão é:", resultado)
except ValueError:
    print("Erro: um dos valores digitados não é um número inteiro")
except ZeroDivisionError:
    print("Erro: divisão por zero")
except Exception as e:
    print("Ocorreu um erro inesperado:", e)

```

Neste exemplo, dentro do bloco try, tentamos ler os valores e realizar a divisão. Se algum erro ocorrer, o programa pula para o bloco except correspondente. Nesse caso, temos três blocos except: um para tratar erros de ValueError (que ocorre quando o usuário digita um valor que não é um número inteiro), um para tratar erros de ZeroDivisionError (que ocorre quando o usuário tenta dividir por zero) e um último bloco para tratar erros genéricos (usando a classe Exception).

>[!info] Se nenhum erro ocorrer durante a execução do bloco try, o programa segue em frente e imprime o resultado da divisão. Caso contrário, o programa imprime uma mensagem de erro apropriada para o tipo de erro capturado.

## Exercícios

1. Escreva um programa que peça ao usuário para digitar a sua idade e informe se ele é maior ou menor de idade.
2. Escreva um programa que peça ao usuário para digitar dois números e informe qual é o maior.
3. Escreva um programa que peça ao usuário para digitar uma letra e informe se ela é uma vogal ou uma consoante.
4. Escreva um programa que peça ao usuário para digitar um número e informe se ele é positivo, negativo ou zero.
5. Escreva um programa que peça ao usuário para digitar o seu salário e informe qual é o seu imposto de renda de acordo com a tabela abaixo:
   - Até R\$ 1.903,98: isento
   - De R\$ 1.903,99 até R\$ 2.826,65: 7,5%
   - De R\$ 2.826,66 até R\$ 3.751,05: 15%
   - De R\$ 3.751,06 até R\$ 4.664,68: 22,5%
   - Acima de R$ 4.664,68: 27,5%
6. Escreva um programa que peça ao usuário para digitar a sua altura e o seu peso e informe se ele está abaixo do peso, no peso ideal ou acima do peso. Para isso, utilize o índice de massa corporal (IMC), que é calculado pela fórmula:
   - Para homens: peso ideal = (72.7 x altura) - 58
   - Para mulheres: peso ideal = (62.1 x altura) - 44.7

%%

## Resolução dos exercícios

### 1. maior de idade

Escreva um programa que peça ao usuário para digitar a sua idade e informe se ele é maior ou menor de idade.

```python
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

```

### 2. número maior

Escreva um programa que peça ao usuário para digitar dois números e informe qual é o maior.

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")

```

### 3. vogal ou consoante

Escreva um programa que peça ao usuário para digitar uma letra e informe se ela é uma vogal ou uma consoante.

```python
letra = input("Digite uma letra: ")
vogais = "aeiou"
if letra.lower() in vogais:
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

```

### 4. número positivo ou negativo

Escreva um programa que peça ao usuário para digitar um número e informe se ele é positivo, negativo ou zero.

```python
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

```

### 5. imposto de renda

Escreva um programa que peça ao usuário para digitar o seu salário e informe qual é o seu imposto de renda de acordo com a tabela abaixo:

- Até R\$ 1.903,98: isento
- De R\$ 1.903,99 até R\$ 2.826,65: 7,5%
- De R\$ 2.826,66 até R\$ 3.751,05: 15%
- De R\$ 3.751,06 até R\$ 4.664,68: 22,5%
- Acima de R$ 4.664,68: 27,5%

```python
salario = float(input("Digite o seu salário: "))
if salario <= 1903.98:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 0.075
elif salario <= 3751.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
    imposto = salario * 0.225
else:
    imposto = salario * 0.275
print("O imposto de renda a ser pago é R$", imposto)

```

### 6. peso ideal

Escreva um programa que peça ao usuário para digitar a sua altura e o seu peso e informe se ele está abaixo do peso, no peso ideal ou acima do peso. Para isso, utilize o índice de massa corporal (IMC), que é calculado pela fórmula:

- Para homens: peso ideal = (72.7 x altura) - 58
- Para mulheres: peso ideal = (62.1 x altura) - 44.7

```python
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M ou F): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", peso_ideal)
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", peso_ideal)
else:
    print("Sexo inválido. Por favor, digite M ou F.")

```

Nesse código, pedimos ao usuário para digitar sua altura em metros e seu sexo. Depois, usamos um if/elif/else para calcular o peso ideal com base na fórmula correspondente ao sexo. Note que usamos o método upper() para converter a string do sexo em letras maiúsculas, o que torna a comparação mais robusta (pois não depende do usuário digitar exatamente as letras maiúsculas ou minúsculas corretas).

>[!tip] Esse código pode ser facilmente modificado para aceitar outros tipos de unidades (como centímetros) ou para permitir que o usuário digite sua idade ou outros fatores relevantes para o cálculo do peso ideal.

%%

## Referências

[[Referencias sobre Python]]
