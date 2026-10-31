---
title: Ambientes Virtuais Com Poetry
description: Poetry é outra ferramenta de gerenciamento de dependências para Python.
  Ela permite declarar as bibliotecas de que seu projeto depende e gerencia essas…
date: '2026-09-17'
draft: false
---

Poetry é outra ferramenta de gerenciamento de dependências para Python. Ela permite declarar as bibliotecas de que seu projeto depende e gerencia essas bibliotecas para você. Poetry também suporta o empacotamento e a publicação de projetos no PyPI.

## Principais Comandos do Poetry

```bash
poetry                    # lista todos os comandos do Poetry
poetry add nome_do_pacote # Adiciona um novo pacote
poetry remove nome_do_pacote # Remove umpacote
poetry install            # Instala os pacotes adicionados
poetry show -t        # Mostra pacotes instalados e suas dependências
poetry shell              # Ativa um ambiente virtual
poetry env list           # Lista os ambientes virtuais
poetry env info --path    # Mostra o diretório do ambiente virtual
poetry config virtualenvs.in-project true # Cria sempre o ambiente virtual na mesma pasta do projeto
poetry build              # Prepara o pacote para publicar no Pypi
poetry publish            # Publica o pacote no Pypi
```

### Instalação do Poetry

Um erro comum é instalar o Poetry no próprio ambiente virtual que ele gerenciará, portanto ele deve ser instalado no ambiente virtual criado pelo Pipx, com o comando:

`pipx install poetry`

>[!info] O [Pipx](https://pipx.pypa.io/stable/) é a atualização do Pip que instala e executa aplicações em um ambiente virtual isolado!

### Criando um Projeto com Poetry

Para iniciar um novo projeto:

```bash
python -m venv .venv   # Cria um ambiente virtual na pasta .env
.venv\Scripts\activate # Ativa o ambiente virtual
poetry new meu_projeto # cria um projeto 
cd meu_projeto         # Muda para a pasta do projeto
poetry init            # Cria as configurações em um projeto já existente
```

### Adicionando Dependências com Poetry

Para adicionar dependências:

```bash
poetry add nome_do_pacote
```

### Instalando Dependências com Poetry

Para instalar todas as dependências do projeto adicionadas no `pyproject.toml:

```bash
poetry install
```

### Referências

- [python-poetry.org/docs/](https://python-poetry.org/docs/)
- [Python GitHub Workflow | Poetry, Pytest, GitHub Actions - YouTube](https://www.youtube.com/watch?v=HNhjWqZaFog)
