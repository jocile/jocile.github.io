---
title: Unittestgui
description: O unittestgui é uma interface gráfica (GUI) para o framework de testes
  unitários unittest do Python. Ele facilita a execução e visualização dos testes,…
date: '2026-09-17'
draft: false
---

O `unittestgui` é uma interface gráfica (GUI) para o framework de testes unitários `unittest` do Python. Ele facilita a execução e visualização dos testes, tornando o processo mais intuitivo e fácil de usar. Aqui estão os principais passos para utilizar o `unittestgui`:

## 1. Instalar o unittestgui

Primeiro, você precisa instalar o `unittestgui` usando o `pip`:

```bash
pip install unittestgui
```

## 2. Criar os testes unitários

Escreva seus testes unitários usando o `unittest` conforme o padrão. Por exemplo:

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
```

## 3. Iniciar o unittestgui

Para iniciar a interface gráfica, execute o seguinte comando no terminal:

```bash
unittestgui
```

Isso abrirá a janela do `unittestgui`.

## 4. Carregar os testes

No `unittestgui`, clique em "Load Tests" e selecione o arquivo Python contendo seus testes unitários. O `unittestgui` irá descobrir automaticamente todos os testes definidos no arquivo.

## 5. Executar os testes

Após carregar os testes, você pode executá-los clicando no botão "Run Tests". O `unittestgui` exibirá os resultados dos testes em uma interface amigável, mostrando quais testes passaram ou falharam[1].

## Recursos adicionais do unittestgui

- Você pode selecionar testes específicos para executar, filtrando por nome ou marcando/desmarcando as caixas de seleção ao lado de cada teste[1].
- O `unittestgui` exibe informações detalhadas sobre os testes, incluindo o tempo de execução e mensagens de erro em caso de falha[1].
- Há opções para definir configurações adicionais, como o diretório de trabalho e variáveis de ambiente[1].

O `unittestgui` torna o processo de execução de testes unitários mais acessível e visual, especialmente para desenvolvedores que preferem uma interface gráfica em vez de linha de comando. Ele é uma ferramenta útil para melhorar a produtividade e a confiabilidade do seu código Python[2].

Citations:\
[1] <https://academy.pega.com/pt-br/topic/unit-tests/v3>\
[2] <https://www.nimblework.com/pt-br/agile/testes-unitarios/>\
[3] <https://escoladaprogramacao.com.br/testes-unitarios-com-jest-para-iniciantes-domine-o-basico-rapidamente/>\
[4] <https://blog.formacao.dev/testes-unitarios-em-python-usando-unittest/>\
[5] <https://awari.com.br/unit-test-frontend-como-essa-habilidade-pode-impulsionar-sua-carreira-em-tecnologia/>
