---
title: Pacotes que quero instalar
description: 'Objetivo: Criar e usar um ambiente virtual Python para gerenciar dependências
  de projetos.'
date: '2026-09-17'
draft: false
---

## Praticando com Ambiente Virtual no Python

**Objetivo:** Criar e usar um ambiente virtual Python para gerenciar dependências de projetos.

---

**Passo 1: O que é um ambiente virtual e por que usá-lo?**

- **Conceito:** Um ambiente virtual é uma ferramenta que isola dependências específicas de um projeto Python.
- **Por que usar?**
  - Evita conflitos entre dependências de diferentes projetos.
  - Permite usar diferentes versões de pacotes simultaneamente.

---

### **Passo 2: Preparando o Ambiente**

1. **Certifique-se de que o Python está instalado.**
   - No terminal, execute:

     ```bash
     python --version
     ```

   - Se não estiver instalado, baixe do site oficial [python.org](https://www.python.org/).

2. **Instale o `venv`, se necessário.**
   - Para usuários que não possuem o módulo instalado (especialmente em algumas distribuições Linux):

     ```bash
     sudo apt install python3-venv
     ```

---

### **Passo 3: Criando um Ambiente Virtual**

1. **Escolha um local para seu projeto.**
   - Por exemplo:

     ```bash
     mkdir projeto_python
     cd projeto_python
     ```

2. **Crie o ambiente virtual.**
   - Com Python 3:

     ```bash
     python3 -m venv env
     ```

3. **Entenda o que aconteceu:**
   - Foi criada uma pasta chamada `env`, que contém uma instalação independente do Python e suas ferramentas.

---

### **Passo 4: Ativando o Ambiente Virtual**

1. **Ative o ambiente virtual:**
   - No Windows:

     ```bash
     env\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source env/bin/activate
     ```

2. **Confirme que o ambiente está ativado:**
   - O prompt do terminal mudará, exibindo `(env)` antes do diretório atual.

---

### **Passo 5: Instalando Dependências**

1. **Instale pacotes no ambiente virtual.**
   - Exemplo: instalar o pacote `requests`:

     ```bash
     pip install requests
     ```

2. **Verifique os pacotes instalados:**

   ```bash
   pip list
   ```

3. **Salve as dependências do projeto:**
   - Gere um arquivo `requirements.txt`:

     ```bash
     pip freeze > requirements.txt
     ```

---

Exemplo de requirements.txt:

```Shell
httpx
pandas
pytest

# Instalando pacotes com versões específicas
black == 0.6.1  # igual a 0.6.1
django >= 4.1.1 # maior que 4.1.1
flask != 3.5    # diferente de 3.5
selenium ~= 1.1 # maior ou igual a 1.1, menor que 2

# Instalando pacotes de outro arquivo
-r requiremens_dev.txt
```

> [!info] O arquivo constraints.txt é usado para instalar somente as versões específicas!
>>>>>
### **Passo 6: Desativando o Ambiente Virtual**

1. **Saia do ambiente virtual:**

   ```bash
   deactivate
   ```

---

## **Atividade Prática**

- **Crie um ambiente virtual e instale um pacote.**
- **Crie um pequeno script para testar o pacote instalado.**
- **Por exemplo:**
  1. **Instale o `requests`:**

     ```bash
     pip install requests
     ```

  2. **Crie um arquivo `teste.py`:**

     ```python
     import requests

     response = requests.get('https://api.github.com')
     print(response.status_code)
     ```

  3. **Execute o script:**

     ```bash
     python teste.py
     ```

  4. **Desative o ambiente.**

---

### **Exemplo Prático: Recuperando Texto de uma Página Web**

Nesta atividade, utilizaremos o módulo `requests` para fazer requisições HTTP e o módulo `BeautifulSoup` da biblioteca `bs4` para extrair texto de uma página web.

---

### **Passo 1: Instalar Dependências**

Antes de começar, certifique-se de instalar as bibliotecas necessárias no ambiente virtual:

1. Ative seu ambiente virtual (veja os passos anteriores).
2. Instale os pacotes necessários:

   ```bash
   pip install requests beautifulsoup4
   ```

---

### **Passo 2: Criar o Script**

1. **Crie um arquivo Python chamado `extrai_texto.py`.**
2. **Escreva o seguinte código:**

```python
import requests
from bs4 import BeautifulSoup

# URL da página web a ser analisada
url = "https://www.wikipedia.org/"

# Fazendo a requisição para a página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraindo o texto principal
    texto = soup.get_text()
    
    # Exibindo as primeiras linhas do texto
    print("Texto extraído da página:")
    print(texto[:500])  # Exibe os primeiros 500 caracteres
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")
```

---

### **Passo 3: Executar o Script**

1. Certifique-se de estar no diretório do projeto.
2. Execute o script:

   ```bash
   python extrai_texto.py
   ```

---

### **O Que Esse Código Faz?**

1. **`requests.get(url)`**:
   - Faz uma requisição HTTP GET para a URL fornecida.
   - Retorna a resposta do servidor.

2. **`BeautifulSoup(response.text, 'html.parser')`**:
   - Analisa o conteúdo HTML retornado pela página.

3. **`soup.get_text()`**:
   - Extrai todo o texto visível da página, ignorando as tags HTML.

4. **`print(texto[:500])`**:
   - Exibe os primeiros 500 caracteres do texto extraído, garantindo que a saída seja legível no terminal.

---

### **Exemplo de Saída**

Ao executar o código acima para a página do Wikipedia, a saída será algo como:

```
Texto extraído da página:
Wikipedia
The Free Encyclopedia
English 1 000 000+ articles Español 500 000+ artículos ...

```

---

### **Desafio Extra**

1. **Filtrar o Texto Principal**: Modifique o script para extrair apenas o texto de uma tag específica, como `<p>` ou `<h1>`. Exemplo:

   ```python
   # Extraindo apenas os títulos (tag h1)
   for titulo in soup.find_all('h1'):
       print(titulo.get_text())
   ```

2. **Salvar o Texto em um Arquivo**:
   - Adicione este trecho ao final do código para salvar o texto em um arquivo:

     ```python
     with open('texto_extraido.txt', 'w', encoding='utf-8') as arquivo:
         arquivo.write(texto)
     print("Texto salvo em 'texto_extraido.txt'.")
     ```

---

Essa prática introduz conceitos fundamentais de web scraping e manipulação de texto no Python! 🚀
