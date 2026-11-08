---
title: Configurando o Pytest e Entendendo Teste Unitário
date: 2026-11-08
draft: false
tags:
  - python
  - pytest
  - testes-unitarios
  - desenvolvimento-de-software
description: Guia prático sobre configuração, convenções e conceitos fundamentais de testes unitários com pytest no Python.
---

Configurando o Pytest e Entendendo Teste Unitário

Um artigo conceitual sobre configuração, execução e conceitos fundamentais de testes com pytest.

Pytest é um framework de teste universal que simplifica a escrita de testes no Python, permitindo criar baterias de testes organizadas, parametrizadas e detalhadas.

## O Que é Pytest?

Pytest é uma ferramenta de testagem amplamente utilizada no ecossistema Python. Diferente do unittest padrão do Python, pytest oferece um paradigma mais simples e flexível para escrever testes unitários e de integração. A biblioteca utiliza o **pytest-discover**, que automatiza a descoberta de arquivos de teste baseados em convenções de nomenclatura (nomes começam com `test_` e terminam com `_test.py`).

O framework foi desenvolvido para ser minimalista, mas potente — permitindo testar desde funções simples até integrações complexas, com suporte nativo para parametrização, mocking, fixtures e geração de relatórios detalhados.

## Por Que Usar Pytest?

- **Sintaxe Simplificada**: Testes mais curtos e legíveis comparados ao unittest.
- **Descoberta Automática**: O pytest detecta automaticamente os testes conforme você executa o comando.
- **Flexibilidade em Configuração**: Suporta arquivos de configuração (`pyproject.toml`, `setup.cfg`, `pytest.ini`) para adaptar comportamentos como verbosidade e paths de busca.
- **Ferramentas Avançadas**: Recursos como *fixtures*, *parametrização*, *assertions* e *exceções customizadas*.
- **Comunidade Ativa**: Maior adoção na indústria, com extensões e plugins que estendem suas funcionalidades.

## Configuração do Pytest no Projeto

Para executar testes automaticamente, é necessário configurar corretamente o ambiente. No caso de projetos modernos, a configuração é feita via `pyproject.toml` usando ferramentas como **Poetry** ou **pip**.

O pytest executa seus testes buscando por arquivos que começam com `test_` e terminam em `_test.py`, além de métodos dentro desses arquivos que começam com `test_`.

```python
# pyproject.toml
[tool.poetry.dependencies]
pytest = "^8.2.2"
```

Depois de instalar as dependências, execute os testes via terminal:

```bash
pytest
```

Se não houver arquivos na pasta `tests`, o pytest retornará uma mensagem como "0 tests in 0 seconds", indicando que não foram encontrados.

## A Convenção de Nomenclatura de Testes

O nome do arquivo deve seguir convenções estritas para ser descoberto pelo pytest:

- Arquivos devem começar com `test_`
- Devem ter `_test.py` como sufixo (ou terminar em `.py` se não forem arquivos específicos, mas a prática mais comum é incluir o sufixo)

Exemplos válidos:

- `test_myservice.py`
- `conftest.py` (arquivo especial para fixtures globais)
- `test_utils_pytest.py` (caso você inclua `pytest` no nome do arquivo, pois o pytest usa a palavra-chave como parte da busca)

Os métodos dentro desses arquivos devem seguir a mesma regra: começar com `test_`. Exemplo:

```python
def test_meu_metodo():
    pass
```

## Como Escrever Seu Primeiro Teste

O primeiro passo é criar uma função que será testada. Por exemplo, criaremos um método que eleve um número ao quadrado na pasta `utils`:

```python
# utils.py
def eleva_quadrado(x):
    return x ** 2
```

Agora, crie o arquivo de teste. O nome do arquivo deve seguir a convenção: começar com `test_` e terminar com `_test.py`. No exemplo, criamos `test_utils_pytest.py`:

```python
# test_utils_pytest.py
from utils import eleva_quadrado

def test_eleva_quadrado_sucesso():
    resultado = eleva_quadrado(2)
    assert resultado == 4
```

Observe a sintaxe crucial: o pytest só executa uma validação se você usar a palavra-chave `assert`. Sem ela, o Python não verifica automaticamente o valor esperado.

## O Importante da Palavras-Chave Assert

A palavra-chave `assert` é uma funcionalidade do Python que permite criar comparações condicionais dentro de testes. Se a condição for falsa, o teste falha e uma mensagem de erro detalhada é exibida — indicando qual linha falhou e o porquê.

Exemplo de uso:

```python
# assert 4 == 10 → AssertionError (teste falha)
assert 4 == 10

# assert 4 == 4 → Assertion passes (teste passa)
assert 4 == 4
```

Se você omitir a palavra `assert`, o Python não realiza essa verificação. Isso é fundamental para entender por que testes sem `assert` são válidos apenas de forma superficial — eles passam sempre, mesmo com dados incorretos.

## Executando e Analisando os Testes

Pytest oferece várias opções de configuração para modificar o comportamento da execução:

- `-q`: Reduz a verbosidade (menos detalhes).
- `-v`: Aumenta a verbosidade (mostra mais detalhes).
- `--verbose` ou `-vv`: Mostra informações extras sobre falhas, erros e testes.
- `--minfail X`: Fica executando até que X testes falhem.
- `--q` (quiet): Desliga os relatórios padrão do pytest.

Ao executar com `pytest -vv`, você verá detalhadamente cada teste:

```bash
pytest -vv
```

Esse comando exibe o nome do módulo e cada teste, bem como sua status de *passed* ou *failed*.

## Teste Parametrizado: O Poder das Tuplas

Um dos recursos mais potentes do pytest é a **parametrização**. Isso permite que um único método de teste seja executado múltiplas vezes com diferentes entradas. A forma padrão envolve tuplas, onde cada elemento representa um par `(entrada_esperada, resultado_esperado)`.

Exemplo:

```python
def test_eleva_quadrado_parametrizado(test_input, expected):
    resultado = eleva_quadrado(test_input)
    assert resultado == expected
```

A chamada de teste seria assim:

```python
@pytest.mark.parametrize("test_input, expected", [
    (2, 4),
    (10, 100),
    (3, 9),
])
def test_eleva_quadrado_parametrizado(test_input, expected):
    resultado = eleva_quadrado(test_input)
    assert resultado == expected
```

O pytest executará o teste três vezes: uma para cada tupla fornecida. Isso torna seus testes mais concisos e evita repetição de código.

## Teste de Exceção com `raises`

Para testar se um método lança uma exceção específica, use a função `pytest.raises`. Essa funcionalidade permite capturar a exceção lançada pelo teste e verificar o conteúdo (como mensagem ou dados).

Exemplo:

```python
def test_eleva_quadrado_excecao_tipo_error():
    try:
        resultado = eleva_quadrado("A")  # "A" é string, não número
        assert False  # Nunca deve chegar aqui
    except TypeError as e:
        assert isinstance(e.value, TypeError)
```

Pytest oferece também uma maneira mais direta com `pytest.raises`:

```python
def test_eleva_quadrado_excecao_typo_error():
    with pytest.raises(TypeError) as e:
        eleva_quadrado("A")
    
    assert "str" in str(e.value), e.excon.text
```

A função captura a exceção, permitindo que você compare o conteúdo ou verifique propriedades específicas.

## Parametrizando Testes de Exceções

Para testar diversos cenários de erros, use parametrização junto com `pytest.raises`. Exemplo:

```python
@pytest.mark.parametrize("test_input", [
    1,
    None,
])
def test_eleva_quadrado_parametra_excecao(test_input):
    try:
        eleva_quadrado(test_input)
        assert False  # Nunca deve chegar aqui
    except TypeError as e:
        assert "str" in str(e.value), e.excon.text
```

Esse teste será executado duas vezes: uma com entrada `1` (que é número, mas o método pode não suportá-lo de forma adequada) e outra com entrada `None` (também inválido).

## Dicas e Boas Práticas

- **Seja Específico**: Testes claros e específicos facilitam a manutenção.
- **Use Asserts Corretamente**: Sempre que possível, valide o resultado esperado em testes unitários.
- **Monitore Falhas**: Use relatórios como `--verbose` para identificar falhas mais rapidamente.
- **Organize Pastas de Teste**: Mantenha arquivos de teste bem organizados (ex: por módulo ou funcionalidade).
- **Documentar Casos de Uso**: Use parametrização para documentar cenários variados em um único teste.

## Próximos Passos

- Aprenda sobre **fixtures** (funções de configuração) para gerenciar dependências entre testes.
- Estude como usar **mocks** para isolar dependências externas e simular comportamentos.
- Explore plugins do Pytest, como `pytest-cov`, que gera relatórios detalhados de cobertura de código.

Para continuar aprendendo:

- [Documentação Oficial do Pytest](https://docs.pytest.org/pt/latest/)
- [Guia de Configuração](https://docs.pytest.org/en/latest/reference.html)

---

Este artigo conceitual cobre os fundamentos para configurar, escrever e executar testes unitários com pytest. Aparamentos chave: convenções de nomenclatura, uso de `assert`, parametrização, e tratamento de exceções.

## Referências

- [[Conceitos de Testes Unitários]]
- [[Integração de Teste e Mocking]]
- [[Fixture e Dependência no Pytest]]
