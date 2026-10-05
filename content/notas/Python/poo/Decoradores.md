---
title: Decoradores
description: Os decoradores em Python são uma maneira poderosa e conveniente de modificar
  ou estender o comportamento de funções ou métodos. Eles permitem adicionar…
date: '2026-09-17'
draft: false
tags:
- programador/Python/POO
- programador/padroes
---

## Padrão Decorador em Python

Os decoradores em Python são uma maneira poderosa e conveniente de modificar ou estender o comportamento de funções ou métodos. Eles permitem adicionar funcionalidade adicional a uma função existente sem modificar diretamente o código dessa função. Os decoradores são aplicados a funções usando a sintaxe `@decorator_name` logo acima da definição da função.

Vamos analisar o código fornecido:

```python
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

ola_mundo()
```

## Definição

```python
    def meu_decorador(funcao):
        def envelope():
            print("faz algo antes de executar")
            funcao()
            print("faz algo depois de executar")
        return envelope
```

- Aqui, `meu_decorador` é uma função que recebe uma função (`funcao`) como argumento.
- Dentro de `meu_decorador`, é definida uma função `envelope` que envolve a função `funcao` passada.
- A função `envelope` imprime uma mensagem antes e depois de chamar `funcao`.
- A função `meu_decorador` retorna a função `envelope`.

**Aplicação do Decorador**:

```python
    @meu_decorador
    def ola_mundo():
        print("Olá mundo!")
```

- O decorador `@meu_decorador` é aplicado à função `ola_mundo`.
- Isso é equivalente a `ola_mundo = meu_decorador(ola_mundo)`.
- Como resultado, `ola_mundo` é agora substituído por `envelope`.

**Execução da Função Decorada**:

```python
    ola_mundo()
```

- Quando `ola_mundo` é chamada, na verdade, a função `envelope` é executada.
- A saída será:

```plaintext
      faz algo antes de executar
      Olá mundo!
      faz algo depois de executar
```

## Resumo do Processo

- A função `meu_decorador` é definida para modificar o comportamento de outra função.
- A função `ola_mundo` é decorada com `meu_decorador`, que a envolve com a função `envelope`.
- Quando `ola_mundo` é chamada, o código adicional definido no decorador (`envelope`) é executado antes e depois da execução de `ola_mundo`.

## Vantagens dos Decoradores

1. **Reutilização de Código**:
    - Decoradores permitem encapsular lógica comum que pode ser reutilizada em várias funções, reduzindo a duplicação de código.
    - Decoradores permitem reutilizar código comum em várias funções sem duplicação.

2. **Separação de conceitos**:
    - Eles ajudam a manter a lógica principal das funções limpa e separada de preocupações auxiliares como logging, autenticação, caching, etc.
    - Facilita a separação de lógica auxiliar (como logging, autenticação, etc.) da lógica principal da função.

3. **Modularidade**:
    - Decoradores podem ser facilmente combinados e aplicados de forma modular a diferentes partes do código, melhorando a flexibilidade e a manutenção do software.

4. **Leitura e Manutenção**:
    - Adicionar um decorador a uma função é mais legível e fácil de manter do que embutir a mesma lógica dentro de várias funções.

5. **Composição**: Vários decoradores podem ser compostos para adicionar múltiplas camadas de comportamento.

> [!NOTE] Os decoradores são uma ferramenta muito útil para melhorar a modularidade e a legibilidade do código em Python, facilitando a adição de funcionalidades transversais de maneira limpa e eficiente.

## Decoradores com passagem de valores

Vamos analisar e explicar o novo código fornecido que é uma combinação dos conceitos explicados anteriormente, adicionando funcionalidade antes e depois da execução da função decorada e permitindo o uso de argumentos.

```python
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")

ola_mundo("João", 1000)
```

### Explicação do código

**Definição do Decorador**:

```python
    def meu_decorador(funcao):
        def envelope(*args, **kwargs):
            print("faz algo antes de executar")
            funcao(*args, **kwargs)
            print("faz algo depois de executar")
        return envelope
```

- `meu_decorador` é uma função que recebe outra função (`funcao`) como argumento.
- Dentro de `meu_decorador`, a função `envelope` é definida. Esta função:
	- Imprime "faz algo antes de executar".
	- Chama a função `funcao` com os argumentos fornecidos (`*args` e `**kwargs`).
	- Imprime "faz algo depois de executar".
- `meu_decorador` retorna a função `envelope`.

**Aplicação do Decorador**:

```py
    @meu_decorador
    def ola_mundo(nome, outro_argumento):
        print(f"Olá mundo {nome}!")
```

- O decorador `@meu_decorador` é aplicado à função `ola_mundo`.
- Isso significa que `ola_mundo` é substituída por `envelope`, que agora contém a lógica adicional.

**Execução da Função Decorada**:

```plaintext
    ola_mundo("João", 1000)
```

 Quando `ola_mundo` é chamada com os argumentos `"João"` e `1000`, na verdade, a função `envelope` é executada.\
    - A execução de `envelope` segue estes passos:\
        - Imprime "faz algo antes de executar".\
        - Chama `funcao(*args, **kwargs)`, que é `ola_mundo("João", 1000)`.\
        - `ola_mundo` imprime "Olá mundo João!".\
        - Imprime "faz algo depois de executar".

### Saída do Programa

A execução do programa produzirá a seguinte saída:

```plaintext
faz algo antes de executar
Olá mundo João!
faz algo depois de executar
```

### Explicação Adicional

- **Flexibilidade com `*args` e `**kwargs`**:
  - Usar `*args` e `**kwargs` na definição de `envelope` permite que ela aceite qualquer número de argumentos posicionais e nomeados, tornando o decorador aplicável a uma ampla gama de funções com diferentes assinaturas.
- **Estrutura do Decorador**:
  - O decorador é composto por três partes principais:
    1. **Função externa** (`meu_decorador`): recebe a função original como argumento.
    2. **Função interna** (`envelope`): executa a lógica adicional e chama a função original.
    3. **Retorno** da função interna: a função `envelope` é retornada, substituindo a função original decorada.

### Resumo

- O decorador `meu_decorador` adiciona comportamento antes e depois da execução da função decorada.
- A função `ola_mundo`, quando decorada, primeiro executa a lógica adicional definida em `envelope` e depois a lógica original.
- Este padrão é útil para adicionar funcionalidades como logging, validação, temporização, etc., de maneira reutilizável e sem modificar diretamente as funções originais.

## Decoradores com introspecção

> [!TIP] Decoradores têm a capacidade de conhecer seus parâmetros em tempo de execução.

Vamos analisar e explicar o novo código fornecido, que utiliza a biblioteca `functools` para criar um decorador mais sofisticado e que preserva metadados da função original.

```python
import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")

print(ola_mundo.__name__)
```

### Explicação do código

1. **Importação do módulo `functools`**:

```python
    import functools
```

- `functools` é um módulo da biblioteca padrão do Python que fornece funções de ordem superior para manipular ou decorar outras funções.

```python
    def meu_decorador(funcao):
        @functools.wraps(funcao)
        def envelope(*args, **kwargs):
            funcao(*args, **kwargs)
        return envelope
```

- A função `meu_decorador` recebe uma função (`funcao`) como argumento.
- Dentro de `meu_decorador`, a função `envelope` é definida para aceitar qualquer número de argumentos posicionais e nomeados (`*args` e `**kwargs`).
- A função `envelope` chama `funcao` com esses argumentos.
- `@functools.wraps(funcao)` é um decorador que copia os metadados (nome, docstring, etc.) de `funcao` para `envelope`. Isso é importante para preservar a identidade da função original.
- `meu_decorador` retorna a função `envelope`.

**Aplicação do Decorador**:

```python
    @meu_decorador
    def ola_mundo(nome, outro_argumento):
        print(f"Olá mundo {nome}!")
```

- O decorador `@meu_decorador` é aplicado à função `ola_mundo`.
- Isso é equivalente a `ola_mundo = meu_decorador(ola_mundo)`.
- Como resultado, `ola_mundo` é agora substituído por `envelope`.

**Impressão do Nome da Função**:

```python
    print(ola_mundo.__name__)
```

- Esta linha imprime o nome da função `ola_mundo`.
- Devido ao uso de `@functools.wraps(funcao)`, o nome impresso será `ola_mundo`, preservando o nome original da função.
- Sem `@functools.wraps`, o nome impresso seria `envelope`, que é o nome da função interna no decorador.

### Explicação Adicional

- **Função `functools.wraps`**:
  - `functools.wraps` é um decorador para usar em funções wrapper (como `envelope`). Ele atualiza a função wrapper para parecer mais com a função original que está sendo decorada.
  - Preserva o nome da função, docstrings, argumentos anotados e outras propriedades da função original.
- **Uso de `*args` e `**kwargs`**:
  - `*args` permite que a função `envelope` aceite qualquer número de argumentos posicionais.
  - `**kwargs` permite que a função `envelope` aceite qualquer número de argumentos nomeados.
  - Isso faz com que `envelope` seja muito flexível e capaz de decorar funções com diferentes assinaturas.

### Resumo

- O decorador `meu_decorador` define uma função `envelope` que envolve a função original, permitindo a execução da função original com qualquer conjunto de argumentos.
- `@functools.wraps` é usado para preservar os metadados da função original.
- A função decorada (`ola_mundo`) ainda mantém seu nome original devido ao uso de `@functools.wraps`.

> [!NOTE] Este código demonstra uma maneira mais robusta de criar decoradores em Python, garantindo que a função decorada retenha seus metadados originais, o que é útil para depuração e documentação.

## Aplicação

Vamos explorar mais profundamente como os decoradores podem ser aplicados em diferentes contextos e as vantagens que eles trazem para o desenvolvimento de software.

Aplicações Comuns dos Decoradores:

### **Log de Execução**

Decoradores são frequentemente usados para adicionar logs antes e depois da execução de funções. Isso é útil para rastrear o fluxo do programa e depurar problemas.

```python
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Chamando a função {func.__name__} com argumentos {args} e {kwargs}")
            result = func(*args, **kwargs)
            print(f"Função {func.__name__} retornou {result}")
            return result
        return wrapper

    @log_decorator
    def soma(a, b):
        return a + b

    soma(2, 3)
```

Saída:

```plaintext
      Chamando a função soma com argumentos (2, 3) e {}
      Função soma retornou 5
```

### Autenticação e Autorização

Decoradores podem ser usados para verificar permissões de acesso antes de executar certas funções, como em aplicativos web.

```python
    def autenticacao_decorator(func):
        def wrapper(usuario, *args, **kwargs):
            if not usuario.esta_autenticado:
                raise PermissionError("Usuário não autenticado")
            return func(usuario, *args, **kwargs)
        return wrapper

    @autenticacao_decorator
    def acessar_recurso(usuario, recurso_id):
        return f"Acesso ao recurso {recurso_id} concedido para {usuario.nome}"

    class Usuario:
        def __init__(self, nome, esta_autenticado):
            self.nome = nome
            self.esta_autenticado = esta_autenticado

    usuario = Usuario("João", True)
    print(acessar_recurso(usuario, 42))
```

### Caching

Decoradores podem ser usados para cachear resultados de funções, melhorando a performance ao evitar chamadas repetidas a funções caras.

```python
    import functools

    def cache_decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args in cache:
                return cache[args]
            result = func(*args, **kwargs)
            cache[args] = result
            return result
        return wrapper

    @cache_decorator
    def fatorial(n):
        if n == 0:
            return 1
        return n * fatorial(n - 1)

    print(fatorial(5))
```

### Medição de Tempo

Decoradores podem medir e registrar o tempo de execução de uma função, útil para análise de desempenho.

```python
    import time

    def tempo_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            result = func(*args, **kwargs)
            fim = time.time()
            print(f"Tempo de execução de {func.__name__}: {fim - inicio} segundos")
            return result
        return wrapper

    @tempo_decorator
    def funcao_pesada():
        time.sleep(2)
        return "Feito"

    print(funcao_pesada())
```

Saída:

```plaintext
      Tempo de execução de funcao_pesada: 2.0021 segundos
      Feito
```

### Validação de Dados

Decoradores podem ser usados para validar argumentos antes de executar a função.

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

    print(calcular_area(3, 4))
    # calcular_area(-1, 5) # Levanta ValueError
```

## Conclusão

Os decoradores são uma ferramenta poderosa em Python que permitem modificar o comportamento de funções de maneira limpa, reutilizável e modular. Eles são amplamente utilizados em diversos contextos para adicionar funcionalidades como logging, autenticação, caching, medição de tempo e validação de dados, entre outros. O uso de decoradores pode melhorar significativamente a estrutura, a legibilidade e a manutenção do código.
