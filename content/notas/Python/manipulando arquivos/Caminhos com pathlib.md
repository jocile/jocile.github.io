---
title: Caminhos com pathlib
description: A biblioteca pathlib é a forma recomendada no Python para manipular caminhos de diretórios e arquivos. Ela é uma biblioteca padrão e não precisa de instalação.
date: '2026-10-03'
draft: false
tags:
- arquivos
- pathlib
- python
---

A biblioteca `pathlib` é a forma recomendada no Python para manipular caminhos de diretórios e arquivos. Ela é uma biblioteca padrão e não precisa de instalação.

## 1. Construindo caminhos com pathlib

A palavra *path* significa caminho. A biblioteca `pathlib` é focada justamente na manipulação desses caminhos de forma orientada a objetos.

```python
from pathlib import Path

# Exemplo de criação de caminho
print(Path('primeira_pasta/segunda_pasta'))
# Saída: primeira_pasta/segunda_pasta (macOS/Linux) ou primeira_pasta\segunda_pasta (Windows)

print(type(Path('primeira_pasta/segunda_pasta')))
```

> [!TIP] Compatibilidade entre Sistemas Operacionais
> Em Windows, caminhos utilizam barra invertida (`\`) como separador. macOS e Linux utilizam a barra simples (`/`). A utilização de `Path()` torna seu script compatível com todos os sistemas operacionais, gerenciando essa diferença automaticamente.

### Criando manualmente caminhos para arquivos

Podemos criar caminhos combinando pastas e nomes de arquivos:

```python
from pathlib import Path

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    print(Path('primeira_pasta/segunda_pasta', nome))

# Outra forma utilizando o operador de divisão (/)
for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    print(Path('primeira_pasta/segunda_pasta') / nome)
```

> [!WARNING] Regra do operador `/`
> O Python executa o comando da esquerda para a direita. O primeiro ou o segundo valor da operação devem ser um objeto do tipo `Path`. Se nenhum dos dois primeiros for `Path`, o código resultará em um erro.

```python
homePath = Path('C:/Users/Al')
pasta = Path('spam')
subPasta = 'pasta'
print(homePath / pasta / subPasta)
# Saída: C:\Users\Al\spam\pasta
```

## 2. O diretório Home

Os sistemas operacionais possuem uma pasta dedicada aos arquivos de cada usuário (documentos, downloads, imagens, etc.). É importante saber localizar esse diretório, pois ele compõe o caminho absoluto de muitos arquivos.

```python
print(Path.home())
```

Seus scripts geralmente possuem permissão para escrever dentro desse diretório.

## 3. Caminhos Absolutos e Caminhos Relativos

Existem duas formas de especificar o caminho de um arquivo:

*   **Caminho Absoluto:** Inicia pelo diretório raiz (ex: `C:\` no Windows). É o caminho completo que mostra todos os passos do filesystem até o arquivo.
*   **Caminho Relativo:** Depende do **diretório de trabalho** (*working directory*) atual do programa.

### Diretório de Trabalho (CWD)

Todo programa roda a partir de um diretório. Podemos verificar e alterar esse diretório:

```python
from pathlib import Path
import os

# Verificar diretório atual (Current Working Directory)
print(Path.cwd())

# Mudar diretório de trabalho
os.chdir(Path.home())
print(Path.cwd())
```

## 4. Manipulando Caminhos de Arquivos

### Verificando e convertendo caminhos

```python
# Verificar se é absoluto
print(Path.cwd().is_absolute()) # True
print(Path('primeira_pasta').is_absolute()) # False

# Transformar relativo em absoluto
print(Path.cwd() / Path('primeira_pasta'))
```

> [!IMPORTANT] Variável `__file__`
> Para garantir que o script encontre arquivos localizados na mesma pasta onde ele está, utilize a variável especial `__file__`.
> ```python
> print(Path(__file__).parent.absolute()) # Caminho da pasta onde o script está
> ```

### Pegando partes de um caminho

Um caminho pode ser dividido em partes:

*   **Anchor:** Diretório raiz.
*   **Drive:** Letra do disco (apenas Windows).
*   **Parent:** Pasta que contém o arquivo.
*   **Name:** Nome do arquivo (formado por *stem* + *suffix*).
*   **Stem:** Nome base do arquivo.
*   **Suffix:** Extensão do arquivo.

```python
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)  # 'C:\'
print(p.parent)  # WindowsPath('C:/Users/Al')
print(p.name)    # 'spam.txt'
print(p.stem)    # 'spam'
print(p.suffix)  # '.txt'
print(p.drive)   # 'C:'

# Acessar hierarquia superior
print(p.parents[0]) # C:/Users/Al
print(p.parents[1]) # C:/Users
```

## 5. Retornando Conteúdos e Validando Caminhos

### Listar arquivos

```python
# Usando pathlib
print(list(Path.home().glob('*'))) # Lista tudo
print(list(Path.home().glob('*.txt'))) # Lista apenas arquivos .txt
```

### Validar existência e tipo

```python
caminho = Path('C:/exemplo/arquivo.txt')

print(caminho.exists()) # Verifica se existe
print(caminho.is_dir()) # Verifica se é uma pasta
print(caminho.is_file()) # Verifica se é um arquivo
```
