---
title: Publicando e reutilizando pacotes Python
date: 2026-09-29
draft: false
tags:
  - python
  - programação
  - biblioteca-padrao
description: "Transformar um código Python em uma biblioteca reutilizável e disponibilizá-la no PyPI."
---

## Publicando e reutilizando pacotes Python

Para transformar um código Python em uma biblioteca reutilizável e disponibilizá-la no PyPI, siga estas etapas:

### **1. Organizar o Código:**

- **Criar uma Estrutura de Pacotes:** Organize seu código em uma pasta principal que representará o nome da sua biblioteca. Dentro dessa pasta, coloque os arquivos do seu código. ^[[6. Módulos — Documentação Python 3.13.0](https://docs.python.org/pt-br/3/tutorial/modules.html#packages)]
- **Criar um Arquivo `__init__.py`:** Este arquivo, dentro da pasta principal, indica ao Python que a pasta é um pacote. Ele pode ser usado para importar classes e funções importantes do pacote para facilitar o acesso dos usuários.

#### Diagrama exemplo da Estrutura da Biblioteca "Panda Vídeo"

```
└── panda_video
    ├── LICENCE
    ├── README.md
    ├── setup.py
    └── src
        ├── __init__.py
        ├── main.py
        ├── panda_foo.py
        └── panda_video.py
    └── tests
        ├── __init__.py

```

**Explicação:**

- **panda_video:** Pasta principal da biblioteca, que representa o pacote em si.
- **`__init__.py`:** Arquivo especial que indica ao Python que a pasta é um pacote e permite importar classes diretamente do pacote. Neste caso, importa todas as classes da subpasta "wrapper".
- **src:** Subpasta contendo os arquivos com o código principal da biblioteca.
- **main.py, panda_foo.py, panda_video.py:** Arquivos que contêm as classes da biblioteca, como `Main`, `PandaFoo` e `PandaVideo`.

**Exemplo de Importação:**

```python
from panda_video import PandaVideo
```

### **2. Preparar Arquivos Essenciais:**

- **Criar um Arquivo `LICENSE`:** Defina a licença do seu projeto ^[[Licenciar um repositório - GitHub Docs](https://docs.github.com/pt/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)], como a [licença MIT](https://choosealicense.com/licenses/mit/), que é permissiva.
- **Criar um Arquivo `README.md`:** Escreva uma descrição detalhada do seu projeto ^[[Um modelo para fazer um bom README.md · GitHub](https://gist.github.com/lohhans/f8da0b147550df3f96914d3797e9fb89)], incluindo instruções de instalação e uso.

### **3. Criar o Arquivo `setup.py`:**

- **Importar `setup` do `setuptools`:** Esta ferramenta é crucial para empacotar sua biblioteca.
- **Definir Metadados:** No arquivo `setup.py`, defina informações como nome, versão, autor, descrição, licença, palavras-chave, pacotes incluídos, dependências e outros detalhes relevantes.

Exemplo de `setup.py`:

```python
from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='wrapper-panda-video',
    version='0.0.1',
    license='MIT License',
    author='Caio Sampaio',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='caio@pythonando.com.br',
    keywords='panda video',
    description=u'Wrapper não oficial do Panda Video',
    packages=['panda_video'],
    install_requires=['requests'],)
```

### **4. Empacotar a Biblioteca:**

- **Usar o Comando**:
 
`python setup.py sdist`

-  Este comando cria um pacote distribuível no formato `.tar.gz`, contendo todos os arquivos necessários.

### **5. Criar uma Conta no PyPI:**

- [**Acesse pypi.org e crie uma conta](https://pypi.org/account/register/).**

### **6. Instalar a Ferramenta `twine`:**

- **Use o comando**: 
 
`pip install twine`

- Esta ferramenta é recomendada para fazer o upload da sua biblioteca para o PyPI.

### **7. Fazer o Upload da Biblioteca:**

- Execute o comando para criar um repositório de teste:

`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

- Ou para criar um repositório oficial:

`twine upload dist/*`

- Este comando envia o pacote para o PyPI. Você precisará fornecer suas credenciais do PyPI.

### **8. Testar a Instalação:**

- **Crie um novo ambiente virtual.**
- **Instale sua biblioteca usando `pip install <nome-da-sua-biblioteca>`.**
- **Importe sua biblioteca em um script Python para testar se tudo funciona corretamente.**

Seguindo essas etapas, você pode transformar seu código Python em uma biblioteca reutilizável e compartilhá-la com a comunidade Python através do PyPI.

### Referências

![Publicando uma BIBLIOTECA PYTHON reutilizável no PYPI - YouTube](https://www.youtube.com/watch?v=_14MS9oFZZI)

[Pythonando - Publicando uma BIBLIOTECA PYTHON reutilizável no PYPI](https://doc.clickup.com/36904728/d/h/1367rr-543/246df89507b2ab3)

[Guia do usuário do Python Packaging](https://packaging.python.org/pt-br/latest/tutorials/packaging-projects/)
