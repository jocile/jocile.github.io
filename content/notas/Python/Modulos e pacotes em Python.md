---
title: "Módulos e pacotes em Python"
date: 2026-09-29
draft: false
tags:
  - python
  - desenvolvimento
  - pacotes
description: "Guia sobre criação, estruturação e publicação de módulos e pacotes em Python, incluindo uso do Pypi, Setuptools e Twine."
---

## Módulos

Módulo: objeto que serve como unidade organizacional do código que é carregado pelo comando de import.

Vantagens da modularização:

- Legibilidade
- Manutenção
- Reaproveitamento de código

## Pacotes

Pacote: coleção de módulos com hierarquia.

Vantagens de criar um pacote:

- Facilidade de compartilhamento
- Facilidade de instalação

## Conceitos

- Pypi: repositório público oficial de pacotes
- Wheel e Sdist: dois tipos de distribuições
- Setuptools: pacote usado em setup.py para gerar as distribuições
- Twine: pacote usado para subir as distribuições no repositório Pypi

## Estruturas

Módulo simples:

```text
└── project_name/
    ├── README.md
    ├── setup.py
    ├── requirements.txt
    └── package_name/
        ├── __init__.py
        ├── file1_name.py
        ├── file2_name.py
```

Exemplos de chamada para o pacote simples:

- `import package_name.file1_name`
- `from package_name import file1_name`

Vários módulos:

```text
└── project_name/
    ├── README.md
    ├── setup.py
    ├── requirements.txt
    └── package_name/
        ├── __init__.py
        ├── module1_name/
            ├── file1_name.py
            ├── file2_name.py
        ├── module2_name/
            ├── file1_name.py
            ├── file2_name.py
```

Exemplos de chamada para o pacote com vários módulos:

- `import package_name.module1_name.file1_name`
- `from package_name.module1_name import file1_name`

## Passos para criar um projeto

- Fork do template
- Adição do conteúdo dos módulos do projeto
- Edição do  arquivo setup.py
- Edição do requirements.txt
- Edição do README.md

## Exemplo:

```text
image-processing-package/
    README.md
    setup.py
    requirements.txt
    image_processing/
        __init__.py
        processing/
            __init__.py
            combination.py
            transformation.py
        utils/
            __init__.py
            to.py
            plot.py
```

- `setup.py`: Usado para especificar como o pacote deve ser construído.
- `requeriments.txt`: Usado para passar as dependências que devem ser instaladas com o seu pacote. Opcionalmente, podem ser especificadas as versões.
 - `README.md`: Será exibido como documentação na página do Pypi do seu pacote. Foi usado markdown.

## Comandos de instalação

```shell
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
```

Comandos para criar distribuições:

`python setup.py sdist bdist_wheel`

## Publicando o pacote

Passos necessários:

![[Modulos e pacotes em Python-1747434703885.png]]

Passos para subir o pacote:

- Criar conta no Test Pypi
- Publicar no Test Pypi
- Instalar pacote usando Test Pypi
- Testar pacote
- Criar conta no Pypi
- Publicar no Pypi
- Instalar pacote usando Pypi

Comando para publicar no Test Pypi:

`python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

Comando para instalar o pacote de teste:

`pip install –-index-url https://test.pypi.org/simple/ image-processing`

Comando para publicar no Pypi:

`python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`

Comando para instalar o pacote:

`python -m pip install package_name`

## Referências

%%
 - [web.dio.me/lab/descomplicando-a-criacao-de-pacotes-de-processamento-de-imagens-em-python](https://web.dio.me/lab/descomplicando-a-criacao-de-pacotes-de-processamento-de-imagens-em-python/learning/4dfcac97-0cde-45f2-9932-beeff1a0bd3b?back=/track/suzano-python-developer)%%
- [Ajuda · PyPI](https://pypi.org/help/)
- [tiemi (Karina Kato) · GitHub](https://github.com/tiemi/)
- [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
- [Good Integration Practices - pytest documentation](https://docs.pytest.org/en/latest/goodpractices.html)
- [Tox - automation project](https://tox.wiki/en/latest/)
- [[Publicando e reutilizando pacotes Python]]
