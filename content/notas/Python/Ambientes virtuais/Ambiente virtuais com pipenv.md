---
title: Ambiente Virtuais Com Pipenv
description: Pipenv é uma ferramenta que combina a gestão de dependências com a criação
  de ambiente virtual para seus projetos. Ele adiciona ou remove pacotes…
date: '2026-09-17'
draft: false
---

## Introdução ao Pipenv

Pipenv é uma ferramenta que combina a gestão de dependências com a criação de ambiente virtual para seus projetos. Ele adiciona ou remove pacotes automaticamente do arquivo `Pipfile` conforme você instala e desinstala pacotes.

### Principais Comandos do Pipenv

- `pip install pipenv`: Instala o gerenciador de pacotes pipenv.
- `pipenv` : mostra todos os comandos disponíveis no pipenv;
- `pipenv install nome_do_pacote`: Instala um pacote e adiciona ao `Pipfile`.
- `pipenv uninstall nome_do_pacote`: Remove um pacote.
- `pipenv graph`: Lista todos os pacotes instalados e suas dependências.
- `pipenv lock`: Gera uma lista de pacotes instalados e suas versões.
- `pipenv requirements`: gera um arquivo `requirements.txt` do `Pipfile.lock`.
- `pipenv sync`: instala todos os pacotes do `Pipfile.lock`.
- `pipenv check` : procura por vulnerabilidades nas dependências.
- `pipenv clean` : desinstala pacotes que não estão na lista do pipenv;
- `pipenv --python 3.12` : cria um novo projeto com Python 3.12;
- `pipenv install --dev` : instala todas as dependências para um projeto;
- `pipenv --rm` : remove um projeto;
- `pipenv install -e`: instala um `setup.py` no ambiente virtual;
- `pipenv shell`: acessa um terminal no ambiente virtual;

#### Exemplo Comandos do Pipenv

```bash
python -m venv meu_ambiente   # Criando o ambiente virtual
meu_ambiente\Scripts\activate # Ativando o ambiente no Windows
pip install pipenv            # Instalando o venv no ambiente
pipenv install nome_do_pacote
pipenv graph
pipenv uninstall nome_do_pacote
```

### Referências

- [Pipenv: Python Dev Workflow for Humans — pipenv 2024.4.0 documentation](https://pipenv.pypa.io/en/latest/)
- [Gerenciando dependências de aplicações - Python Packaging User Guide](https://packaging.python.org/pt-br/latest/tutorials/managing-dependencies/)
