---
title: "Criando um Formulário de Entrada de Dados com Tkinter"
date: 2026-09-27
draft: false
tags:
  - python
  - tkinter
  - gui
description: "Guia detalhado sobre como construir formulários de entrada de dados utilizando a biblioteca Tkinter do Python, abordando criação de interface e processamento de dados."
---

Exemplo de como construir formulários de entrada de dados utilizando a biblioteca Tkinter do Python. O processo geralmente envolve a **criação da interface gráfica** com widgets como labels, entries, spinboxes e comboboxes, e a **implementação da funcionalidade** para capturar e processar os dados inseridos pelo usuário.

### Criação da Interface Gráfica

![](Pasted%20image%2020241107114633.png)

> [!INFO] Widgets Essenciais
> - **`tkinter.Label`:** Utilizado para exibir textos informativos no formulário.
> - **`tkinter.Entry`:** Permite a entrada de texto pelo usuário.
> - **`tkinter.Text`:** Permite a entrada de múltiplas linhas de texto, ideal para campos maiores.
> - **`tkinter.Button`:** Cria botões interativos para acionar funcionalidades, como enviar os dados do formulário.
> - **`tkinter.Spinbox`:** Permite ao usuário selecionar um valor numérico dentro de um intervalo predefinido.
> - **`tkinter.Combobox` (ou `ttk.Combobox`):** Cria um menu dropdown para o usuário selecionar uma opção dentre as disponíveis.
> - **`tkinter.Checkbutton` (ou `ttk.Checkbutton`):** Cria caixas de seleção para o usuário marcar ou desmarcar opções.

> [!TIP] Dicas de Organização
> - **Gerenciadores de Layout:** Utilize `pack`, `grid` ou `place` para organizar os widgets dentro do formulário. `pack` é o mais simples, centralizando os widgets, enquanto `grid` permite um posicionamento mais preciso em linhas e colunas.
> - **Frames:** Utilize `tkinter.Frame` (ou `ttk.Frame`) para agrupar widgets relacionados dentro do formulário, melhorando a organização e a aparência visual.
> - **Padding:** Ajuste o espaçamento entre widgets e bordas utilizando o atributo `padding` nos widgets ou nos gerenciadores de layout.

### Capturando e Processando os Dados

**Funções Associadas aos Widgets:**

- **Atributo `command`:** Utilize o atributo `command` em botões para chamar uma função específica quando o botão for clicado.
- **Método `get()`:** Utilize o método `get()` em entries, spinboxes e comboboxes para recuperar os valores inseridos pelo usuário.
- **Eventos:** Utilize `bind` para associar eventos, como clicar em um botão ou selecionar um item em um combobox, a funções específicas.

> [!WARNING] Validação e Processamento
> - **Validação:** Implemente rotinas de validação para verificar se os dados inseridos são válidos, como verificar se campos obrigatórios foram preenchidos e se os dados possuem o formato correto.
> - **Armazenamento:** Utilize bibliotecas como `openpyxl` para salvar os dados em um arquivo Excel ou `sqlite3` para armazená-los em um banco de dados SQLite.
> - **Outras Ações:** Os dados podem ser processados de diversas formas, como enviar para um servidor web, gerar um arquivo PDF, gerar imagens com a API do ChatGPT, etc.

> [!EXAMPLE] Exemplo de Implementação (Simplificado)
> ```python
> import tkinter as tk
>
> def enviar_dados():
>   nome = nome_entry.get()
>   idade = idade_spinbox.get()
>   print(f"Nome: {nome}, Idade: {idade}")
>
> window = tk.Tk()
> window.title("Formulário de Entrada")
>
> nome_label = tk.Label(window, text="Nome:")
> nome_label.grid(row=0, column=0)
>
> nome_entry = tk.Entry(window)
> nome_entry.grid(row=0, column=1)
>
> idade_label = tk.Label(window, text="Idade:")
> idade_label.grid(row=1, column=0)
>
> idade_spinbox = tk.Spinbox(window, from_=18, to=100)
> idade_spinbox.grid(row=1, column=1)
>
> enviar_button = tk.Button(window, text="Enviar", command=enviar_dados)
> enviar_button.grid(row=2, column=0, columnspan=2)
>
> window.mainloop()
> ```

Este exemplo demonstra a criação de um formulário simples com campos de nome e idade. Ao clicar no botão "Enviar", os dados são recuperados dos widgets e exibidos no console. É importante destacar que este é apenas um exemplo básico, e a complexidade do seu formulário dependerá dos seus requisitos específicos.

## Passo a Passo para Criar um Formulário de Entrada de Dados com Tkinter

Este é um guia detalhado para a criação de formulários de entrada de dados com Tkinter. Abaixo, um passo a passo detalhado, com base nas informações das fontes, para te auxiliar nesse processo.

### Algoritmo para Criação de Formulário de Entrada de Dados com Tkinter

Esta lista de tarefas descreve as etapas para a criação de um formulário de entrada de dados com Tkinter.

**1. Configuração Inicial:**

> [!TODO] Configuração Inicial
> - Importar bibliotecas necessárias:
>     - `tkinter` como `tk` para interface gráfica. 
>     - `ttk` para widgets com temas. 
>     - Bibliotecas adicionais, como `filedialog`, `messagebox`, e bibliotecas de processamento de dados (ex.: `openpyxl` para Excel).
> - Criar a janela principal:
>     - Instanciar a janela (`window = tk.Tk()` ou `window = ctk.CTk()` para CustomTkinter). 
>     - Definir o título da janela usando `window.title()`. 
>     - Definir a geometria inicial da janela com `window.geometry()` (opcional).

**2. Design da Interface:**

> [!TODO] Design da Interface
> - Criar widgets para o formulário:
>     - Labels com `tk.Label()`: para exibir texto descritivo.
>     - Entries com `tk.Entry()`: para entrada de texto do usuário.
>     - Botões com `tk.Button()`: para acionar ações.
>         - Definir a função a ser chamada no atributo `command`.
>     - Spinboxes com `tk.Spinbox()`: para selecionar valores numéricos em um intervalo.
>     - Comboboxes com `ttk.Combobox()`: para selecionar uma opção de uma lista.
>     - Checkbuttons com `tk.Checkbutton()`: para marcar ou desmarcar opções.
> - Organizar os widgets com um gerenciador de layout:
>     - `grid()`: para organizar em linhas e colunas.
>         - Usar `row` e `column` para definir a posição.
>         - Usar `columnspan` para widgets ocuparem várias colunas.
>         - Usar `sticky` para controlar o comportamento ao redimensionar.
>     - `pack()`: para organizar sequencialmente e centralizar.
>         - Usar `fill` para preencher o espaço disponível.
>         - Usar `side` para posicionar (esquerda, direita, etc.).
>     - `place()`: para posicionar com coordenadas x e y.
> - Adicionar espaçamento e padding:
>     - Usar `padx` e `pady` nos widgets ou no gerenciador de layout.

**3. Funcionalidades do Formulário:**

> [!TODO] Funcionalidades do Formulário
> - Criar funções para capturar os dados dos widgets:
>     - Usar `widget.get()` para entradas de texto, spinboxes e comboboxes.
>     - Usar `variavel_de_controle.get()` para checkbuttons.
> - Implementar validação de dados:
>     - Verificar se os campos obrigatórios foram preenchidos.
>     - Verificar o formato dos dados (ex.: email, número de telefone).
>     - Usar `messagebox` para exibir mensagens de erro ou sucesso.
> - Definir o processamento dos dados:
>     - Salvar em arquivo (Excel, TXT, etc.).
>     - Armazenar em banco de dados.
>     - Enviar para um servidor web.
>     - Gerar outros outputs (PDF, imagens, etc.).

**4. Finalização:**

> [!TODO] Finalização
> - Iniciar o loop de eventos com `window.mainloop()`.

### 1. Importe as Bibliotecas Necessárias

**Tkinter:**

- A biblioteca padrão para interfaces gráficas em Python.
- Importe-a com `import tkinter as tk`.

**ttk (Themed Tkinter):**

- Submódulo do Tkinter que fornece widgets com aparência mais moderna.
- Importe-o com `from tkinter import ttk`.

**Outras Bibliotecas:**

- **`filedialog`:** Permite abrir e salvar arquivos. Importe com `from tkinter import filedialog`.
- **`messagebox`:** Permite exibir caixas de diálogo para mensagens e avisos. Importe com `from tkinter import messagebox`.
- **Bibliotecas específicas para o processamento dos dados:** Como `openpyxl` para Excel, `sqlite3` para banco de dados SQLite, etc.

### 2. Crie a Janela Principal

A janela principal é o container base da sua aplicação.

- **Crie a janela:**
    - Utilize `window = tk.Tk()` ou `window = ctk.CTk()` se estiver usando CustomTkinter.
- **Defina o título:**
    - Utilize `window.title("Título da Janela")`.
- **Defina a geometria (opcional):**
    - Utilize `window.geometry("LarguraxAltura")` para definir o tamanho inicial da janela.

### 3. Adicione os Widgets

Utilize widgets para criar os elementos do seu formulário, como labels, entries, botões, etc.

**Labels:**

- Crie labels com `tk.Label(janela_pai, text="Texto do Label")`.
- O primeiro argumento é o widget pai, que define onde o label será posicionado.

**Entries:**

- Crie entries com `tk.Entry(janela_pai)`.
- Para campos de senha, utilize `show="*" ` para ocultar os caracteres digitados.

**Botões:**

- Crie botões com `tk.Button(janela_pai, text="Texto do Botão", command=funcao_a_ser_chamada)`.
- Utilize o atributo `command` para definir a função que será executada ao clicar no botão.

**Spinboxes:**

- Crie spinboxes com `tk.Spinbox(janela_pai, from_=valor_inicial, to=valor_final)`.
- Permita que o usuário selecione um valor numérico dentro de um intervalo.

**Comboboxes:**

- Crie comboboxes com `ttk.Combobox(janela_pai, values=lista_de_valores)`.
- Permita que o usuário selecione uma opção de um menu dropdown.

**Checkbuttons:**

- Crie checkbuttons com `tk.Checkbutton(janela_pai, text="Texto do Checkbutton", variable=variavel_de_controle)`.
- Permita que o usuário marque ou desmarque opções.

### 4. Organize os Widgets

Utilize gerenciadores de layout para posicionar os widgets no formulário.

**Grid:**

- Divide a janela em linhas e colunas.
- Posicione os widgets usando `widget.grid(row=numero_da_linha, column=numero_da_coluna)`.
- Utilize `columnspan` para um widget ocupar múltiplas colunas.

**Pack:**

- Organiza os widgets sequencialmente.
- Centraliza os widgets na janela por padrão.

**Place:**

- Permite posicionar os widgets com coordenadas x e y.

**Dicas de Organização:**

- Utilize frames (`tk.Frame`) para agrupar widgets relacionados.
- Ajuste o espaçamento com `padx` e `pady` nos widgets ou gerenciadores de layout.
- Utilize o atributo `sticky` no `grid` para controlar o comportamento dos widgets ao redimensionar a janela.

> [!EXAMPLE] Exemplo de Código para Organização de Widgets em Tkinter
> ```python
> import tkinter as tk
> from tkinter import ttk
>
> # Criar a janela principal
> window = tk.Tk()
> window.title("Cadastro de Usuário")
>
> # Criar um frame para conter os widgets do formulário
> form_frame = ttk.Frame(window, padding="20")
> form_frame.grid(row=0, column=0, sticky="nsew")
>
> # Criar os widgets do formulário
> nome_label = ttk.Label(form_frame, text="Nome:")
> nome_entry = ttk.Entry(form_frame)
>
> email_label = ttk.Label(form_frame, text="Email:")
> email_entry = ttk.Entry(form_frame)
>
> senha_label = ttk.Label(form_frame, text="Senha:")
> senha_entry = ttk.Entry(form_frame, show="*")
>
> # Organizar os widgets usando o gerenciador de layout grid
> nome_label.grid(row=0, column=0, sticky="w")
> nome_entry.grid(row=0, column=1, sticky="ew")
>
> email_label.grid(row=1, column=0, sticky="w")
> email_entry.grid(row=1, column=1, sticky="ew")
>
> senha_label.grid(row=2, column=0, sticky="w")
> senha_entry.grid(row=2, column=1, sticky="ew")
>
> # Criar um botão para enviar o formulário
> enviar_button = ttk.Button(form_frame, text="Enviar")
> enviar_button.grid(row=3, column=0, columnspan=2, pady="10")
>
> # Iniciar o loop de eventos
> window.mainloop()
> ```

**Explicação do Código:**

1. **Importação de Bibliotecas:** Importamos `tkinter` como `tk` e `ttk` para utilizar os widgets com tema.
    
2. **Criação da Janela Principal:** Uma janela com o título "Cadastro de Usuário" é criada.
    
3. **Criação do Frame:** Um frame chamado `form_frame` é criado para organizar os widgets do formulário. O padding de 20 pixels adiciona um espaçamento visual ao redor dos widgets dentro do frame. O frame é posicionado na janela principal usando `grid` na linha 0 e coluna 0, com `sticky="nsew"` para que ele se expanda em todas as direções quando a janela for redimensionada.
    
4. **Criação dos Widgets:** Labels e entries para nome, email e senha são criados dentro do `form_frame`. A entry para senha utiliza `show="*"` para mascarar os caracteres digitados.
    
5. **Organização dos Widgets:** Os widgets são organizados usando o gerenciador de layout `grid`, posicionando-os em linhas e colunas específicas dentro do `form_frame`. O atributo `sticky="w"` nos labels alinha-os à esquerda, enquanto `sticky="ew"` nas entries faz com que elas se expandam horizontalmente para preencher o espaço disponível.
    
6. **Botão de Envio:** Um botão "Enviar" é criado e posicionado na linha 3, ocupando ambas as colunas (`columnspan=2`). Um espaçamento vertical de 10 pixels é adicionado com `pady="10"`.
    
7. **Loop de Eventos:** O `window.mainloop()` inicia o loop de eventos principal do Tkinter, que mantém a janela aberta e responde às interações do usuário.

Este exemplo mostra como organizar widgets em um formulário usando um frame e o gerenciador de layout `grid`. As fontes fornecem diversos outros exemplos com widgets e layouts diferentes. Explore-os para aprimorar suas habilidades na criação de interfaces gráficas com Tkinter!

### 5. Implemente a Funcionalidade

Crie funções para capturar os dados dos widgets, validá-los e processá-los.

**Capturando os Dados:**

- Utilize `widget.get()` para recuperar o valor de entries, spinboxes e comboboxes.
- Utilize `variavel_de_controle.get()` para checkbuttons.

**Validação:**

- Verifique se campos obrigatórios foram preenchidos.
- Verifique se os dados possuem o formato correto (ex.: email, número de telefone).
- Utilize `messagebox` para exibir mensagens de erro ou sucesso.

**Processamento dos Dados:**

- Salve os dados em um arquivo Excel, banco de dados ou envie para um servidor web.
- Utilize os dados para gerar outros outputs, como PDF, imagens, etc.

> [!EXAMPLE] Capturando Dados de Widgets em Tkinter
> Dando continuidade ao nosso passo a passo, vamos agora apresentar um exemplo de código para capturar os dados inseridos pelo usuário nos widgets do nosso formulário de cadastro. Para isso, vamos adicionar uma função ao código anterior que será chamada quando o botão "Enviar" for clicado. Essa função irá recuperar os valores dos campos de nome, email e senha.
>
> ```python
> import tkinter as tk
> from tkinter import ttk
> from tkinter import messagebox
>
> # Função para capturar os dados do formulário
> def enviar_dados():
>     nome = nome_entry.get()
>     email = email_entry.get()
>     senha = senha_entry.get()
>
>     # Exibir os dados capturados em uma caixa de diálogo
>     messagebox.showinfo("Dados Capturados", f"Nome: {nome}\nEmail: {email}\nSenha: {senha}")
>
> # Criar a janela principal
> window = tk.Tk()
> window.title("Cadastro de Usuário")
>
> # Criar um frame para conter os widgets do formulário
> form_frame = ttk.Frame(window, padding="20")
> form_frame.grid(row=0, column=0, sticky="nsew")
>
> # Criar os widgets do formulário
> nome_label = ttk.Label(form_frame, text="Nome:")
> nome_entry = ttk.Entry(form_frame)
>
> email_label = ttk.Label(form_frame, text="Email:")
> email_entry = ttk.Entry(form_frame)
>
> senha_label = ttk.Label(form_frame, text="Senha:")
> senha_entry = ttk.Entry(form_frame, show="*")
>
> # Organizar os widgets usando o gerenciador de layout grid
> nome_label.grid(row=0, column=0, sticky="w")
> nome_entry.grid(row=0, column=1, sticky="ew")
>
> email_label.grid(row=1, column=0, sticky="w")
> email_entry.grid(row=1, column=1, sticky="ew")
>
> senha_label.grid(row=2, column=0, sticky="w")
> senha_entry.grid(row=2, column=1, sticky="ew")
>
> # Criar um botão para enviar o formulário
> enviar_button = ttk.Button(form_frame, text="Enviar", command=enviar_dados)
> enviar_button.grid(row=3, column=0, columnspan=2, pady="10")
>
> # Iniciar o loop de eventos
> window.mainloop()
> ```

**Análise do Código:**

1. **Função `enviar_dados()`:**
    
    - Essa função é chamada quando o botão "Enviar" é clicado.
    - Utiliza o método `get()` para recuperar o texto dos widgets `nome_entry`, `email_entry` e `senha_entry` e armazena esses valores nas variáveis `nome`, `email` e `senha`, respectivamente.
    - Em seguida, utiliza a função `messagebox.showinfo()` para exibir uma caixa de diálogo com o título "Dados Capturados" e uma mensagem formatada contendo os dados obtidos.
2. **Botão "Enviar":**
    
    - O atributo `command` do botão `enviar_button` agora está definido como `enviar_dados`. Isso significa que a função `enviar_dados()` será executada quando o botão for clicado.

Ao executar esse código, você terá um formulário simples. Ao clicar no botão "Enviar", os dados inseridos nos campos serão capturados, formatados em uma mensagem e exibidos em uma caixa de diálogo.

Lembre-se: este é um exemplo básico. As fontes que você forneceu demonstram como capturar dados de diversos outros widgets, como comboboxes, checkbuttons, radiobuttons, etc. Além disso, você pode adaptar o código para realizar diferentes tipos de processamento com os dados capturados, como validação, armazenamento em arquivos ou bancos de dados, envio para APIs, etc.

### 6. Inicie o Loop de Eventos

O loop de eventos mantém a janela aberta e responde às interações do usuário.

- Utilize `window.mainloop()`.

### Referência

![Tkinter Data Entry Form tutorial for beginners - Python GUI project [responsive layout] - YouTube](https://www.youtube.com/watch?v=vusUfPBsggw&list=PLs3IFJPw3G9IiHm9PEP1UaMtuvACmxVMj&index=3)
