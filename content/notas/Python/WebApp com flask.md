---
title: WebApp com flask
aliases:
- Flask
description: "como colocar uma aplicação ou um site no PythonAnywhere"
tags:
  - Python
  - flask
---
## Como Colocar um App no PythonAnywhere

Neste artigo, explicarei como colocar uma aplicação ou um site no PythonAnywhere. 

## O que é o PythonAnywhere?

PythonAnywhere é uma plataforma que funciona como um SaaS (Software as a Service). Isso significa que você paga para usar o serviço e ele fornece todas as informações necessárias, cobrando apenas pelo que você usa. 

## Benefícios do PythonAnywhere

- **Gratuito no início**: Você pode colocar um aplicativo na nuvem de graça.
- **Planos acessíveis**: O primeiro plano pago custa cerca de cinco dólares por mês.
- **Facilidade de uso**: A plataforma é intuitiva e fácil de usar.

## Algoritmo

1. **Criação e Configuração de Conta no PythonAnywhere**:
   - Visite o site PythonAnywhere e crie uma conta gratuita.
   - Confirme seu e-mail para ativar a conta.
   - Acesse o editor e confirme a configuração básica.

2. **Configuração de Repositório no GitHub**:
   - Crie uma conta no GitHub e configure um novo repositório para armazenar seu código.
   - Use o GitHub Desktop para gerenciar o repositório localmente e sincronizar com o GitHub.

3. **Desenvolvimento da Aplicação com Flask**:
   - Crie um ambiente virtual no Python e instale o Flask.
   - Desenvolva sua aplicação Flask localmente, incluindo a configuração de templates HTML para renderização.

4. **Preparação e Deploy do Código no PythonAnywhere**:
   - Configure o ambiente virtual no PythonAnywhere para corresponder ao local.
   - Carregue o código no PythonAnywhere usando o Git.
   - Ajuste as configurações de Web App no PythonAnywhere para rodar a aplicação Flask.

5. **Teste e Acesso Público**:
   - Teste a aplicação para garantir que está funcionando corretamente.
   - Confirme que a aplicação está acessível publicamente através do link fornecido pelo PythonAnywhere.

## Passos para Colocar um App no PythonAnywhere

### 1. Criar uma Conta no PythonAnywhere

1. Acesse [PythonAnywhere](https://www.pythonanywhere.com).
2. Clique em "Sign Up".
3. Escolha um nome de usuário, e-mail e senha.
4. Confirme seu e-mail.

### 2. Criar uma Conta no GitHub

1. Acesse [GitHub](https://www.github.com) e crie uma conta.
2. Após criar a conta, faça login.
3. Crie um novo repositório. 

### 3. Instalar o GitHub Desktop

1. Baixe e instale o [GitHub Desktop](https://desktop.github.com).
2. Abra o GitHub Desktop e conecte-o à sua conta do GitHub.

### 4. Configurar o Ambiente de Desenvolvimento

1. No GitHub Desktop, crie um novo repositório com o nome que preferir.
2. Abra o repositório no Visual Studio Code (ou outro editor de sua preferência).

### 5. Desenvolver a Aplicação em Python

1. Utilize a biblioteca Flask, que é fácil e poderosa para desenvolvimento web com Python.
2. Crie um arquivo `app.py` e adicione o código básico do Flask.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

3. Crie a pasta `templates` e, dentro dela, o arquivo `index.html`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu App</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
```

### 6. Configurar o Ambiente Virtual

1. No terminal, crie um ambiente virtual.

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```

2. Instale as dependências necessárias.

```bash
pip install flask
pip freeze > requirements.txt
```

### 7. Subir o Código para o GitHub

1. No terminal, inicialize o repositório Git.

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <URL do repositório>
git push -u origin master
```

### 8. Configurar o PythonAnywhere

1. No PythonAnywhere, clique em "Web" e depois em "Add a new web app".
2. Escolha Flask e a versão do Python que você está usando.
3. Configure o caminho do seu arquivo `app.py`.
4. Conecte o repositório do GitHub ao PythonAnywhere.

### 9. Deploy da Aplicação

1. No terminal do PythonAnywhere, puxe o código do GitHub.

```bash
git pull origin master
```

2. Reinicie a aplicação web no PythonAnywhere.

## Conclusão

Seguindo esses passos, você terá sua aplicação Python rodando na nuvem usando PythonAnywhere. Espero que tenham gostado. Qualquer dúvida, deixe um comentário que responderei assim que possível. 

## Referências

- [Vídeo explicativo: Como colocar um App no PythonAnywhere - YouTube](https://www.youtube.com/watch?v=pnkdTMLCh88)
- [Tutorial: Quickstart — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

Para este guia, utilizei diversas fontes e referências que fornecem informações detalhadas sobre cada etapa do processo. Aqui estão algumas das principais referências usadas:

1. **Documentação do PythonAnywhere**:
   - [PythonAnywhere Help](https://help.pythonanywhere.com) fornece tutoriais e guias detalhados sobre como hospedar aplicativos Python na plataforma.

2. **Documentação do GitHub**:
   - [GitHub Docs](https://docs.github.com) oferece informações completas sobre como criar e gerenciar repositórios no GitHub, além de como usar o GitHub Desktop.

3. **Documentação do Flask**:
   - [Flask Documentation](https://flask.palletsprojects.com) é a fonte oficial para aprender a usar o Flask para desenvolvimento web em Python.

4. **Documentação do Visual Studio Code**:
   - [Visual Studio Code Docs](https://code.visualstudio.com/docs) fornece guias sobre como usar este popular editor de código, incluindo a integração com o GitHub.

5. **Tutoriais Online e Artigos**:
   - Diversos tutoriais online e artigos de blogs que explicam como configurar ambientes virtuais, instalar pacotes Python, e conectar repositórios Git ao PythonAnywhere.
