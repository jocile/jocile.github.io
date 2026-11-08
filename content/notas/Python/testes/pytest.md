---
title: Pytest
description: O pytest é um framework de teste unitário popular e poderoso para Python.
  Ele fornece uma interface simples e intuitiva para escrever e executar testes, além…
date: '2026-09-17'
draft: false
tags:
- programador
---

## Criando testes com o pytest

O `pytest` é um framework de teste unitário popular e poderoso para Python. Ele fornece uma interface simples e intuitiva para escrever e executar testes, além de oferecer recursos avançados para facilitar o desenvolvimento orientado a testes (TDD).

### Benefícios do pytest

1. **Sintaxe simples e legível**: O `pytest` usa uma sintaxe clara e direta para escrever testes, tornando-os fáceis de ler e entender.
2. **Descoberta automática de testes**: O `pytest` descobre automaticamente os testes em seu código, eliminando a necessidade de especificar manualmente quais testes devem ser executados.
3. **Asserts intuitivos**: O `pytest` usa asserts nativos do Python, tornando a escrita de testes mais natural e intuitiva.
4. **Parametrização de testes**: O `pytest` permite a parametrização de testes, facilitando a execução de um mesmo teste com diferentes conjuntos de dados de entrada.
5. **Plugins e extensões**: O `pytest` possui uma ampla gama de plugins e extensões disponíveis, adicionando funcionalidades adicionais, como geração de relatórios, cobertura de código e muito mais.

O `pytest` é uma biblioteca poderosa para testes automatizados em Python, que facilita a criação de testes, a execução desses testes e a geração de relatórios sobre os resultados. Vamos explorar alguns conceitos básicos e exemplos para entender melhor como usar o `pytest`.

### Instalação do `pytest`

Para verificar se ele foi instalado digite o seguinte comando no terminal:

```shell
pytest --version
```

Se não estiver instalado, para instalar o `pytest` usando o gerenciador de pacotes `pip`:

```bash
pip install pytest
```

### Estrutura Básica de um Teste

Um teste básico no `pytest` envolve a criação de funções de teste dentro de arquivos que começam ou terminam com `test`. Vamos criar um exemplo simples para ilustrar.

### Exemplo Simples

Crie um arquivo chamado `test_example.py` e adicione o seguinte conteúdo:

```python
def func(x):
 return x + 1

def test_func():
 assert func(3) == 5
```

Aqui temos uma função `func` que adiciona 1 ao argumento `x` e um teste `test_func` que verifica se `func(3)` retorna 4.

### Executando os Testes

Para executar os testes, você pode simplesmente usar o comando:

```bash
pytest
```

O `pytest` automaticamente descobre e executa todos os arquivos de teste e funções de teste.

### Relatórios de Teste

O `pytest` fornece um relatório detalhado sobre os testes executados, indicando quais testes passaram e quais falharam. Isso ajuda a identificar rapidamente onde estão os problemas no seu código.

### Escrevendo testes com pytest

Para escrever testes com o `pytest`, basta criar funções de teste que comecem com o prefixo `test_`. Aqui está um exemplo:

```python
def add(a, b):
 return a + b

def test_add_positive_numbers():
 assert add(2, 3) == 5

def test_add_negative_numbers():
 assert add(-2, -3) == -5

def test_add_zero():
 assert add(0, 0) == 0
```

Neste exemplo, temos uma função `add()` que soma dois números. As funções `test_add_positive_numbers()`, `test_add_negative_numbers()` e `test_add_zero()` são funções de teste que verificam o comportamento da função `add()` em diferentes cenários.

### Executando testes com pytest

Para executar os testes usando o `pytest`, basta executar o comando `pytest` no terminal a partir do diretório raiz do seu projeto.

```py
$ pytest
============================= test session starts =============================
platform darwin -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/project
collected 3 items

test_math.py... [100%]

============================== 3 passed in 0.01s ===============================
```

O `pytest` descobrirá automaticamente todos os testes em seu código e os executará.

### Configuração e Plugins

O `pytest` é altamente configurável e possui uma vasta coleção de plugins que podem ser usados para estender sua funcionalidade. Por exemplo, você pode adicionar um arquivo `pytest.ini` no diretório raiz do seu projeto para configurar o `pytest`:

```ini
[pytest]
addopts = -v
```

Isso faz com que o `pytest` rode em modo verboso, fornecendo mais detalhes sobre cada teste.

### Testando Exceções

Você também pode testar se uma função lança uma exceção esperada usando a cláusula `raises`:

```python
import pytest

def test_raises():
 with pytest.raises(ZeroDivisionError):
 1 / 0
```

## Conclusão

O `pytest` é uma ferramenta essencial para garantir a qualidade do código Python, proporcionando uma maneira fácil e eficiente de criar e executar testes automatizados. Com uma ampla gama de funcionalidades e plugins, ele se adapta a projetos de qualquer tamanho, ajudando a manter o código robusto e livre de bugs.

Você pode encontrar mais detalhes e funcionalidades avançadas na [documentação oficial do pytest](https://docs.pytest.org/en/stable/).

Se precisar de exemplos mais avançados ou de como integrar o `pytest` em um ambiente de desenvolvimento específico, sinta-se à vontade para perguntar!

> [!TIP] O `pytest` é uma excelente alternativa ao `unittest` para escrever testes unitários em Python. Sua sintaxe simples, descoberta automática de testes e recursos avançados o tornam uma escolha popular entre os desenvolvedores Python.

## Referências

- [Documentação oficial do pytest](https://docs.pytest.org/en/stable/)
- [Tutoriais e exemplos de pytest](https://realpython.com/pytest-python-testing/)
- [Boas práticas de testes com pytest](https://docs.pytest.org/en/stable/goodpractices.html)
- [Como criar testes Unitários com Python: Tutorial de Pytest - YouTube](https://www.youtube.com/watch?v=7U1P1N_Kzik)
- /testes
