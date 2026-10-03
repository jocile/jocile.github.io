---
title: Desafio Cadastro De Alunos Resolvido
description: Nesta atividade, você aprenderá a criar um programa de cadastro de alunos para uma escola. Começaremos sem o uso de funções, depois adicionaremos uma…
date: 2026-09-26
draft: false
publish: false
---

## Atividade de Programação em Python: Cadastro de Alunos

Nesta atividade, você aprenderá a criar um programa de cadastro de alunos para uma escola. Começaremos sem o uso de funções, depois adicionaremos uma interface gráfica utilizando Tkinter, e, finalmente, refatoraremos o código para usar funções.

### Parte 1: Cadastro de Alunos sem Funções

Vamos criar um programa simples que solicita os dados dos alunos e os armazena em uma lista.

```python
alunos = []

while True:
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")
    endereco = input("Endereço do aluno: ")
    turma = input("Turma do aluno: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "turma": turma
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar.lower() != 's':
        break

print("Lista de alunos cadastrados:")
for aluno in alunos:
    print(aluno)
```

### Parte 2: Utilizando Tkinter para a Interface Gráfica

Vamos criar uma interface gráfica simples usando Tkinter para cadastrar alunos.

```python
import tkinter as tk

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()
    turma = entry_turma.get()

    aluno = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "turma": turma
    }

    alunos.append(aluno)
    print("Aluno cadastrado:", aluno)

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_turma.delete(0, tk.END)

alunos = []

janela = tk.Tk()
janela.title("Cadastro de Alunos")

label_nome = tk.Label(janela, text="Nome")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_idade = tk.Label(janela, text="Idade")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

label_endereco = tk.Label(janela, text="Endereço")
label_endereco.pack()
entry_endereco = tk.Entry(janela)
entry_endereco.pack()

label_turma = tk.Label(janela, text="Turma")
label_turma.pack()
entry_turma = tk.Entry(janela)
entry_turma.pack()

botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_aluno)
botao_cadastrar.pack()

janela.mainloop()
```

### Parte 3: Refatorando com Funções

Agora, vamos refatorar o código para utilizar funções, tornando-o mais organizado e modular.

**Código Refatorado:**

```python
import tkinter as tk

def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro de Alunos")

    adicionar_widgets(janela)

    janela.mainloop()

def adicionar_widgets(janela):
    global entry_nome, entry_idade, entry_endereco, entry_turma

    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Idade").pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    tk.Label(janela, text="Endereço").pack()
    entry_endereco = tk.Entry(janela)
    entry_endereco.pack()

    tk.Label(janela, text="Turma").pack()
    entry_turma = tk.Entry(janela)
    entry_turma.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar_aluno).pack()

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    endereco = entry_endereco.get()
    turma = entry_turma.get()

    aluno = {
        "nome": nome,
        "idade": idade,
        "endereco": endereco,
        "turma": turma
    }

    alunos.append(aluno)
    print("Aluno cadastrado:", aluno)

    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_turma.delete(0, tk.END)

alunos = []

if __name__ == "__main__":
    criar_janela()
```

## Conclusão

Nesta atividade, você aprendeu a:

1. Criar um cadastro de alunos sem o uso de funções.
2. Utilizar Tkinter para criar uma interface gráfica.
3. Refatorar o código para utilizar funções, tornando-o mais modular e fácil de manter.

## Desafio Extra

Implemente uma funcionalidade para exibir todos os alunos cadastrados em uma nova janela Tkinter quando um botão "Ver Alunos" for clicado.
