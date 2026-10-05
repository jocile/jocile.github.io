---
title: Exemplo de uso
description: Em Python, um iterador é um objeto que implementa os métodos iter() e
  next(), permitindo que você percorra seus elementos um por um. A utilização de…
date: '2026-09-17'
draft: false
tags:
- programador/Python/padroes
---

## Iteradores em Python

Em Python, um iterador é um objeto que implementa os métodos `__iter__()` e `__next__()`, permitindo que você percorra seus elementos um por um. A utilização de iteradores é fundamental para a implementação de laços (`for` loops) e para a criação de objetos que podem ser iterados.

**Importância**:

- **Memória Eficiente**: Iteradores permitem o processamento de grandes conjuntos de dados sem a necessidade de carregar todos os dados na memória de uma só vez.
- **Flexibilidade**: Eles podem ser usados para criar sequências infinitas, fazer leitura de arquivos linha por linha, gerar streams de dados e muito mais.
- **Interface Uniforme**: Iteradores fornecem uma maneira uniforme de acessar elementos de uma coleção, independentemente de sua estrutura interna.

Vamos analisar o código:

```python
class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)
```

### Explicação Detalhada

1. **Definição da Classe `MeuIterador`**:

    ```python
    class MeuIterador:
    ```

    - A classe `MeuIterador` é definida para criar um iterador personalizado.

2. **Método `__init__`**:

    ```python
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
    ```

    - O método `__init__` é o construtor da classe, inicializando a lista de números (`numeros`) e o contador (`contador`) que será usado para rastrear a posição atual na iteração.

3. **Método `__iter__`**:

    ```python
    def __iter__(self):
        return self
    ```

    - O método `__iter__` deve retornar o próprio objeto iterador. Isso permite que a classe seja usada em loops `for` e outras construções que esperam um iterador.
    - No caso da nossa classe, `self` é retornado porque a própria classe é o iterador.

4. **Método `__next__`**:

    ```python
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
    ```

    - O método `__next__` é onde a lógica de iteração é definida.
    - Ele tenta acessar o próximo número na lista `numeros` usando o índice `contador`.
    - Se o índice estiver dentro dos limites da lista, ele multiplica o número por 2, incrementa o `contador` e retorna o resultado.
    - Se o índice estiver fora dos limites (causando um `IndexError`), ele levanta a exceção `StopIteration` para indicar que a iteração deve parar.

5. **Uso do Iterador no Loop `for`**:

    ```python
    for i in MeuIterador(numeros=[38, 13, 11]):
        print(i)
    ```

    - Aqui, um objeto `MeuIterador` é criado com a lista `[38, 13, 11]`.
    - O loop `for` chama implicitamente `__iter__()` para obter o iterador e então chama repetidamente `__next__()` para obter cada valor.
    - Os valores retornados por `__next__()` (números da lista multiplicados por 2) são impressos.

### Saída do Programa

A execução do programa produzirá a seguinte saída:

```python
76
26
22
```

Os valores são os elementos da lista `[38, 13, 11]` multiplicados por 2.

## **Principais Aplicações**

[python] Claro, vamos explorar as principais aplicações dos iteradores em Python com exemplos práticos para cada uma delas.

### 1. Leitura de Arquivos

Iteradores são comumente usados para ler arquivos linha por linha, o que é eficiente em termos de memória.

```python
def ler_arquivo(filepath):
    with open(filepath, 'r') as file:
        for linha in file:
            yield linha.strip()

for linha in ler_arquivo('meuarquivo.txt'):
    print(linha)
```

### 2. Processamento de Streams de Dados

Iteradores são ideais para processar streams de dados contínuos, como dados de sensores ou logs de servidores.

```python
import random
import time

def sensor_dados():
    while True:
        yield random.random()
        time.sleep(1)

# Exemplo de uso
for dados in sensor_dados():
    print(dados)
    # Para o exemplo, vamos limitar a 5 leituras
    if random.randint(1, 5) == 5:
        break
```

### 3. Geração de Sequências Infinitas

Iteradores podem gerar sequências infinitas, como uma sequência de números Fibonacci.

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Exemplo de uso
fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### 4. Implementação de Coleções Personalizadas

Podemos criar coleções personalizadas que podem ser iteradas de maneira específica.

```python
class Contagem:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def __iter__(self):
        self.atual = self.inicio
        return self

    def __next__(self):
        if self.atual <= self.fim:
            x = self.atual
            self.atual += 1
            return x
        else:
            raise StopIteration

# Exemplo de uso
for numero in Contagem(1, 5):
    print(numero)
```

### 5. Cache de Resultados (Memoization)

Decoradores com iteradores podem ser usados para cachear resultados de funções caras.

```python
import functools

def cache_decorator(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# Exemplo de uso
print(fatorial(5))  # Calcula e armazena no cache
print(fatorial(5))  # Recupera do cache
```

### 6. Validação de Dados

Iteradores podem ser usados para validar argumentos antes de executar a função.

```python
def validar_positivo_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Todos os argumentos devem ser positivos")
        return func(*args, **kwargs)
    return wrapper

@validar_positivo_decorator
def calcular_area(largura, altura):
    return largura * altura

# Exemplo de uso
print(calcular_area(3, 4))  # 12
# print(calcular_area(-1, 5))  # Levanta ValueError
```

## Padrões que Usam Iteradores

Iteradores são uma parte fundamental de muitos padrões de design em programação. Vamos explorar alguns padrões de design que utilizam iteradores e fornecer exemplos para cada um.

1. **Padrão Iterator**
2. **Padrão Composite**
3. **Padrão Decorator**
4. **Padrão Generator**
5. **Padrão Factory**

### 1. Padrão Iterator

O padrão Iterator fornece uma maneira de acessar os elementos de um objeto agregado sequencialmente sem expor sua representação subjacente. Em Python, isso é amplamente suportado pela interface de iteradores padrão.

**Exemplo:**

```python
class IteradorLista:
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice < len(self.lista):
            resultado = self.lista[self.indice]
            self.indice += 1
            return resultado
        else:
            raise StopIteration

# Exemplo de uso
lista = [1, 2, 3, 4, 5]
iterador = IteradorLista(lista)
for item in iterador:
    print(item)
```

### 2. Padrão Composite

O padrão Composite permite que objetos sejam compostos em estruturas de árvore para representar hierarquias parte-todo. Iteradores são usados para percorrer esses objetos compostos.

**Exemplo:**

```python
class Componente:
    def operacao(self):
        raise NotImplementedError

class Folha(Componente):
    def __init__(self, valor):
        self.valor = valor

    def operacao(self):
        return self.valor

class Composite(Componente):
    def __init__(self):
        self.children = []

    def adicionar(self, componente):
        self.children.append(componente)

    def operacao(self):
        resultados = []
        for child in self.children:
            resultados.append(child.operacao())
        return resultados

# Exemplo de uso
raiz = Composite()
raiz.adicionar(Folha(1))
raiz.adicionar(Folha(2))

subcomposite = Composite()
subcomposite.adicionar(Folha(3))
subcomposite.adicionar(Folha(4))

raiz.adicionar(subcomposite)

for resultado in raiz.operacao():
    print(resultado)
```

### 3. Padrão Decorator

O padrão Decorator permite que comportamentos sejam adicionados a objetos individuais, dinamicamente, sem afetar o comportamento de outros objetos da mesma classe. Decoradores em Python frequentemente usam iteradores para manipular a entrada e saída de funções.

**Exemplo:**

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@decorator
def funcao_exemplo(valor):
    print(f"Valor: {valor}")

# Exemplo de uso
funcao_exemplo(10)
```

### 4. Padrão Generator

Generadores em Python são uma forma especial de iteradores que permitem definir iteradores de uma maneira mais concisa usando a palavra-chave `yield`. Eles são muito utilizados para criar iteradores de maneira eficiente.

**Exemplo:**

```python
def gerador_exemplo():
    yield 1
    yield 2
    yield 3

# Exemplo de uso
for valor in gerador_exemplo():
    print(valor)
```

### 5. Padrão Factory

O padrão Factory é usado para criar objetos sem especificar a classe exata do objeto que será criado. Ele pode ser usado junto com iteradores para criar objetos iteráveis de maneira flexível.

**Exemplo:**

```python
class Produto:
    def operacao(self):
        raise NotImplementedError

class ProdutoConcreto1(Produto):
    def operacao(self):
        return "Produto 1"

class ProdutoConcreto2(Produto):
    def operacao(self):
        return "Produto 2"

class Fabrica:
    def criar_produto(self, tipo):
        if tipo == 1:
            return ProdutoConcreto1()
        elif tipo == 2:
            return ProdutoConcreto2()
        else:
            raise ValueError("Tipo desconhecido")

# Exemplo de uso
fabrica = Fabrica()
produtos = [fabrica.criar_produto(tipo) for tipo in (1, 2, 1)]

for produto in produtos:
    print(produto.operacao())
```

### Conclusão

Iteradores são fundamentais em muitos padrões de design, pois oferecem uma maneira eficiente e flexível de acessar e manipular coleções de objetos. Aqui estão algumas das principais aplicações:

- **Padrão Iterator**: Para percorrer coleções de objetos.
- **Padrão Composite**: Para percorrer estruturas de árvore hierárquicas.
- **Padrão Decorator**: Para modificar o comportamento de funções ou métodos de forma flexível.
- **Padrão Generator**: Para criar iteradores de forma concisa e eficiente.
- **Padrão Factory**: Para criar objetos iteráveis de maneira flexível.


> [!tip] Compreender como os iteradores são utilizados nesses padrões de design pode ajudar a escrever código mais eficiente, modular e fácil de manter.

Iteradores são uma ferramenta poderosa em Python que facilitam a iteração eficiente e flexível sobre coleções de dados. Eles são essenciais para a leitura eficiente de arquivos, processamento de streams de dados, geração de sequências infinitas, implementação de coleções personalizadas, caching de resultados e validação de dados.

Ao entender e utilizar iteradores, podemos escrever código mais eficiente e legível, especialmente quando trabalhamos com grandes conjuntos de dados ou fluxos contínuos de informações. As aplicações práticas demonstradas acima mostram como iteradores podem ser integrados em várias situações para melhorar a funcionalidade e a performance dos nossos programas.
