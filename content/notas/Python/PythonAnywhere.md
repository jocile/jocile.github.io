---
title: Criando aplicativos Web com Python
date: 2026-10-06
draft: false
tags:
  - python
  - flask
  - pythonanywhere
  - deploy
description: "O PythonAnywhere é uma plataforma de hospedagem na nuvem que permite executar e hospedar aplicações Python de forma fácil e rápida, com suporte a frameworks WSGI como Flask."
---

O PythonAnywhere é uma plataforma de hospedagem na nuvem que permite executar e hospedar aplicações Python de forma fácil e rápida. Algumas características importantes do PythonAnywhere:

- É um ambiente de desenvolvimento integrado (IDE) online que fornece acesso via navegador a consoles Python e Bash[^1]
- Permite hospedar aplicações web escritas em Python usando qualquer framework WSGI, como Flask e Django[^1]
- Oferece uma interface web para gerenciar seus aplicativos, ambientes virtuais e arquivos[^1]
- Possui planos gratuitos e pagos, sendo uma opção acessível para iniciantes e projetos menores[^4]

Para começar a aprender a usar o PythonAnywhere:

1. Crie uma conta gratuita no site do PythonAnywhere (https://www.pythonanywhere.com/)[^1]
2. Explore o painel de controle e familiarize-se com as diferentes guias, como "Consoles", "Files" e "Web"[^1]
3. Aprenda a criar e ativar ambientes virtuais Python usando os comandos `virtualenv` e `workon`[^4]
4. Instale o Flask e outras dependências necessárias em seu ambiente virtual usando `pip`[^4]
5. Crie uma aplicação Flask básica localmente e teste seu funcionamento[^2][^3]
6. Faça o upload de sua aplicação Flask para o PythonAnywhere usando SFTP ou Git[^4]
7. Configure sua aplicação Flask no PythonAnywhere usando a guia "Web" e a configuração WSGI[^2][^3][^5]
8. Implemente e teste sua aplicação Flask hospedada no PythonAnywhere

O PythonAnywhere é uma ótima ferramenta para aprender a desenvolver e implantar aplicações web em Python, especialmente para iniciantes. Sua interface web intuitiva e recursos gratuitos tornam acessível a hospedagem de projetos Python.

## Como usar

Aqui está um passo a passo detalhado para fazer o deploy de uma aplicação Flask no PythonAnywhere:

### Passo 1: Criar uma conta no PythonAnywhere

1. Acesse o site do PythonAnywhere (https://www.pythonanywhere.com/) e crie uma conta.
2. Faça login na sua conta.

### Passo 2: Criar uma nova aplicação web

1. No painel de controle do PythonAnywhere, clique em "Web".
2. Clique em "Add a new web app".
3. Escolha a opção "Manual configuration" e clique em "Next".
4. Selecione a versão do Python que você está usando (por exemplo, Python 3.9) e clique em "Next".
5. Defina o caminho para o arquivo principal da sua aplicação Flask (por exemplo, `/home/seu-usuario/mysite/app.py`) e clique em "Next".

### Passo 3: Configurar a aplicação Flask

1. No painel de controle, clique na guia "Files" e navegue até o diretório onde sua aplicação Flask está localizada.
2. Crie um arquivo `requirements.txt` listando todas as dependências do seu projeto, usando o comando `pip freeze > requirements.txt`.
3. Crie um arquivo `Procfile` especificando o comando para iniciar sua aplicação Flask, por exemplo: `web: gunicorn app:app`.

### Passo 4: Configurar o ambiente virtual

1. No painel de controle, clique na guia "Consoles" e inicie um novo console "Bash".
2. Crie um ambiente virtual usando `virtualenv --python=python3.9 myvenv` (substitua 3.9 pela versão do Python que você está usando).
3. Ative o ambiente virtual usando `source myvenv/bin/activate`.
4. Instale as dependências usando `pip install -r requirements.txt`.

### Passo 5: Configurar a aplicação Flask

1. Volte para a guia "Web" e clique no botão "Reload" para atualizar a configuração da sua aplicação.
2. Verifique se o "WSGI configuration file" está apontando corretamente para o arquivo principal da sua aplicação Flask (por exemplo, `/home/seu-usuario/mysite/app.py`).

### Passo 6: Acessar a aplicação implantada

1. Após a configuração estar completa, você poderá acessar sua aplicação Flask através da URL fornecida pelo PythonAnywhere (por exemplo, `https://seu-usuario.pythonanywhere.com`).

Esse passo a passo mostra como implantar uma aplicação Flask no PythonAnywhere. Lembre-se de substituir `seu-usuario` pelo seu nome de usuário no PythonAnywhere e `python3.9` pela versão do Python que você está usando. Certifique-se também de configurar quaisquer variáveis de ambiente necessárias para sua aplicação.

## Referências

[DIO - criando-aplicativos-web-com-python](https://web.dio.me/articles/criando-aplicativos-web-com-python)

[^1]: https://dev.to/theakira/deploy-de-uma-aplicacao-flask-com-pythonanywhere-5ddk
[^2]: https://www.pythonanywhere.com/forums/topic/31418/
[^3]: https://www.pythonanywhere.com/forums/topic/27355/
[^4]: https://gist.github.com/farhad0085/d49f086f171a8a853b89ed5a92e4bc1f
[^5]: https://help.pythonanywhere.com/pages/Flask/

[^6]: https://dev.to/theakira/deploy-de-uma-aplicacao-flask-com-pythonanywhere-5ddk
[^7]: https://www.youtube.com/watch?v=z7dYIKm4np8
[^8]: https://pythonhow.com/python-tutorial/flask/deploy-flask-web-app-pythonanywhere/
[^9]: https://www.youtube.com/watch?v=S79R9F01Nzg
[^10]: https://circleci.com/blog/automating-flask-deployments-with-pythonanywhere/