---
title: Ambientes Virtuais Com Venv
description: Ambientes virtuais são uma ferramenta essencial para desenvolvedores
  Python, pois permitem isolar as dependências de projetos diferentes, evitando conflitos…
date: '2026-09-17'
draft: false
---

## Ambientes virtuais com venv

Ambientes virtuais são uma ferramenta essencial para desenvolvedores Python, pois permitem isolar as dependências de projetos diferentes, evitando conflitos de versão e facilitando a gestão de pacotes. Neste artigo, vamos explorar o que são ambientes virtuais, como criá-los e utilizá-los, além de ferramentas avançadas para gerenciar esses ambientes.

## 1. O Que São Ambientes Virtuais?

Ambientes virtuais são diretórios isolados no sistema de arquivos que contêm uma instalação específica do Python e seus pacotes. Ao usar um ambiente virtual, você garante que cada projeto possa ter suas próprias dependências, independentemente das versões instaladas globalmente no sistema. o ambiente virtual padrão do Python é o venv.

## 2. Criando e Usando Ambientes Virtuais com `venv`

### 2.1 Criando um Ambiente Virtual

O módulo `venv` é parte da biblioteca padrão do Python e é usado para criar ambientes virtuais. Para criar um ambiente virtual, você pode usar o seguinte comando:

```bash
python -m venv meu_ambiente
```

Este comando cria um diretório chamado `meu_ambiente`, que contém uma instalação isolada do Python.

### 2.2 Ativando o Ambiente Virtual

Depois de criar o ambiente virtual, você precisa ativá-lo. A ativação depende do sistema operacional que você está usando:

- **Windows**:

  ```bash
  meu_ambiente\Scripts\activate
  ```

- **Linux/Mac**:

  ```bash
  source meu_ambiente/bin/activate
  ```

Uma vez ativado, qualquer pacote instalado usando `pip` será instalado apenas nesse ambiente virtual.

### 2.3 Desativando o Ambiente Virtual

Para desativar o ambiente virtual, você pode usar o comando:

```bash
deactivate
```

## 3. Usando `pip` com Ambientes Virtuais

Quando o ambiente virtual está ativado, o `pip` instalado nesse ambiente é usado para gerenciar pacotes. Isso significa que qualquer instalação ou atualização de pacotes será feita apenas dentro do ambiente virtual.

### 3.1 Instalando Pacotes

Para instalar um pacote no ambiente virtual:

```bash
pip install nome_do_pacote
```

### 3.2 Listando Pacotes Instalados

Para listar todos os pacotes instalados no ambiente virtual:

```bash
pip list
```

### 3.3 Salvando Dependências

Para salvar as dependências do projeto em um arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Arquivo requirements.txt

O arquivo requirements.txt é usado para documentar as dependências de um projeto. Isso permite que outras pessoas recriem o mesmo ambiente virtual com as mesmas versões de pacotes, garantindo a reprodutibilidade do projeto.

Considerações para Repositórios Git

É importante não incluir a pasta do ambiente virtual (.venv) no seu repositório Git, pois ela contém arquivos específicos da sua máquina. Em vez disso, inclua o arquivo requirements.txt, que contém a lista de dependências necessárias para configurar o ambiente.

### 3.4 Instalando Dependências de um Arquivo

Para instalar as dependências listadas em um `requirements.txt`:

```bash
pip install -r requirements.txt
```

[venv — Criação de ambientes virtuais — Documentação Python 3.13.0](https://docs.python.org/pt-br/3.13/library/venv.html)
