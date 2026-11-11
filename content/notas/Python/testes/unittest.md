---
title: Unittest
description: O unittest é um framework de teste unitário integrado ao Python. Ele fornece uma estrutura para escrever, executar e organizar testes automatizados para seu…
date: 2026-09-17
draft: false
tags:
  - tecnico/testing
  - python/unittest
  - tdd/postrun
  - auto-teste/unitario
---

## Explicando o unittest no Python

O `unittest` é um framework de teste unitário integrado ao Python. Ele fornece uma estrutura para escrever, executar e organizar testes automatizados para seu código Python.

### Benefícios do unittest

1. **Estrutura organizada**: O `unittest` fornece uma estrutura clara e padronizada para escrever testes, facilitando a manutenção e a adição de novos testes ao longo do tempo.
2. **Assertions integradas**: O `unittest` vem com uma variedade de métodos de asserção (como `assertEqual()`, `assertTrue()`, `assertRaises()`, etc.) que tornam a escrita de testes mais fácil e intuitiva.
3. **Relatórios de teste**: O `unittest` gera relatórios detalhados sobre a execução dos testes, incluindo informações sobre quais testes passaram ou falharam.
4. **Integração com outras ferramentas**: O `unittest` pode ser facilmente integrado a outras ferramentas de teste e automação, como ferramentas de cobertura de código e sistemas de integração contínua.

### Escrevendo testes com unittest

Para escrever testes com o `unittest`, você precisa criar classes de teste que herdam da classe `unittest.TestCase`. Cada método de teste deve começar com o prefixo `test_`. Aqui está um exemplo:

```python
import unittest

def add(a, b):
 return a + b

class TestMathFunctions(unittest.TestCase):
 def test_add_positive_numbers(self):
 self.assertEqual(add(2, 3), 5)

 def test_add_negative_numbers(self):
 self.assertEqual(add(-2, -3), -5)

 def test_add_zero(self):
 self.assertEqual(add(0, 0), 0)
```

Neste exemplo, temos uma função `add()` que soma dois números. A classe `TestMathFunctions` contém três métodos de teste que verificam o comportamento da função `add()` em diferentes cenários.

### Executando testes com unittest

Você pode executar os testes usando o comando `python -m unittest` no terminal. Isso irá descobrir e executar todos os testes definidos em seu código.

```py
$ python -m unittest
....
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

Você também pode usar o módulo `unittest` diretamente em seu código para executar os testes:

```python
if __name__ == '__main__':
 unittest.main()
```

O `unittest` é uma ferramenta poderosa e versátil para escrever testes automatizados em Python. Ele fornece uma estrutura sólida e padronizada, facilitando a manutenção e a evolução do conjunto de testes ao longo do tempo.

Vamos continuar explorando o módulo `unittest` em detalhes, aprofundando-se nos conceitos e nas práticas recomendadas. Esta seção cobrirá desde a criação básica de testes até técnicas mais avançadas de uso do `unittest`.

---

## Unittest em Detalhes

### 1. Estrutura Básica de um Teste com Unittest

- **Importação do Módulo:**

 ```python
 import unittest
 ```

- **Criação de uma Classe de Teste:**
- Todas as classes de teste devem herdar de `unittest.TestCase`.
- Os métodos de teste devem começar com a palavra "test" para que o framework os reconheça.

 ```python
 class TesteBasico(unittest.TestCase):
 def test_exemplo(self):
 self.assertEqual(soma(1, 2), 3)
 ```

### 2. Métodos Comuns de Asserção

- **assertEqual(a, b):** Verifica se `a` é igual a `b`.

 ```python
 self.assertEqual(soma(2, 2), 4)
 ```

- **assertTrue(x):** Verifica se `x` é verdadeiro.

 ```python
 self.assertTrue(verdadeiro)
 ```

- **assertFalse(x):** Verifica se `x` é falso.

 ```python
 self.assertFalse(falso)
 ```

- **assertIn(a, b):** Verifica se `a` está em `b`.

 ```python
 self.assertIn(3, [1, 2, 3])
 ```

- **assertRaises(exception, func, *args, **kwargs):** Verifica se uma exceção é levantada.

 ```python
 self.assertRaises(ValueError, int, 'a')
 ```

### 3. Configuração e Limpeza

- **setUp:** Método chamado antes de cada método de teste.

 ```python
 def setUp(self):
 self.lista = [1, 2, 3]
 ```

- **tearDown:** Método chamado após cada método de teste.

 ```python
 def tearDown(self):
 del self.lista
 ```

### 4. Rodando os Testes

- **Executar diretamente no script:**

 ```python
 if __name__ == '__main__':
 unittest.main()
 ```

### 5. Organização de Testes

- **Agrupando Testes:**
- Vários métodos de teste podem ser agrupados em uma única classe para testar funcionalidades relacionadas.

 ```python
 class TesteOperacoesBasicas(unittest.TestCase):
 def test_soma(self):
 self.assertEqual(soma(1, 2), 3)
 def test_subtracao(self):
 self.assertEqual(subtracao(4, 2), 2)
 ```

- **Dividindo em Múltiplos Arquivos:**
- Organize testes em diferentes arquivos para manter a estrutura do código limpa e gerenciável.

### 6. Testes de Exceção

- **Testando Exceções com Context Manager:**

 ```python
 with self.assertRaises(ZeroDivisionError):
 1 / 0
 ```

### 7. Test Suites

- **Criando um Test Suite:**
- Agrupa vários testes que podem ser executados juntos.

 ```python
 def suite():
 suite = unittest.TestSuite()
 suite.addTest(TesteOperacoesBasicas('test_soma'))
 suite.addTest(TesteOperacoesBasicas('test_subtracao'))
 return suite

 if __name__ == '__main__':
 runner = unittest.TextTestRunner()
 runner.run(suite())
 ```

### 8. Testando Código Assíncrono

- **Uso de Asyncio:** Unittest tem suporte para testar código assíncrono usando `asyncio`.

 ```python
 import asyncio

 class TesteAssincrono(unittest.TestCase):
 def test_async(self):
 loop = asyncio.get_event_loop()
 resultado = loop.run_until_complete(coroutine_exemplo())
 self.assertEqual(resultado, esperado)
 ```

### 9. Mocking

- **Mock Objects:** Usados para substituir partes do sistema em testes.

 ```python
 from unittest.mock import MagicMock

 def test_mock():
 mock = MagicMock()
 mock.metodo_retorna(3)
 mock.metodo.assert_called_with(3)
 ```

---

Com essas informações, você tem um guia detalhado para começar a escrever e executar testes utilizando o `unittest` no Python. O uso adequado de testes melhora a qualidade do software, reduz a introdução de bugs e facilita a manutenção do código ao longo do tempo.

## Referências

- [Documentação oficial do unittest](https://docs.python.org/pt-br/3/library/unittest.html)
- [UnitTest Framework Tutorial](https://www.tutorialspoint.com/unittest_framework/index.htm)
- [Boas práticas de testes unitários em Python](https://realpython.com/python-testing/)
- [TDD com Python Simple e Fácil. - YouTube](https://www.youtube.com/watch?v=umrpOLCIQdI)
- /testes
