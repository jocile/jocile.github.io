---
title: Função para adicionar aluno à lista
description: /Python/tkinter /Python
date: '2026-09-26'
draft: false
tags:
- programador
publish: false
---

/Python/tkinter /Python 

## Exemplo de Cadastro de Alunos

```python
import tkinter as tk

def add_student():
 name = name_entry.get()
 address = address_entry.get()
 student_class = class_entry.get()

 if name and address and student_class:
 student_data = f"Nome: {name}, Endereço: {address}, Turma: {student_class}"
 students.append(student_data)

 # Limpar os campos de entrada
 name_entry.delete(0, tk.END)
 address_entry.delete(0, tk.END)
 class_entry.delete(0, tk.END)
 else:
 print("Por favor, preencha todos os campos!")

# Função para exibir lista de alunos
def show_students():
 text_area.delete(1.0, tk.END)
 for student in students:
 text_area.insert(tk.END, student + "\n")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("400x400")

# Lista para armazenar os dados dos alunos
students = []

# Campos para entrada de dados
tk.Label(janela, text="Nome:").pack()
name_entry = tk.Entry(janela)
name_entry.pack()

tk.Label(janela, text="Endereço:").pack()
address_entry = tk.Entry(janela)
address_entry.pack()

tk.Label(janela, text="Turma:").pack()
class_entry = tk.Entry(janela)
class_entry.pack()

# Botão para cadastrar aluno
tk.Button(janela, text="Cadastrar", command=add_student).pack(pady=10)

# Botão para exibir lista de alunos
tk.Button(janela, text="Exibir Lista", command=show_students).pack(pady=10)

# Área de texto para exibir a lista de alunos
text_area = tk.Text(janela, width=50, height=10)
text_area.pack(pady=10)

# Iniciando o loop principal
janela.mainloop()
```

### Explicação do Código

1. **Função `add_student`**:
 
 - Obtém os dados dos campos de entrada (nome, endereço, turma).
 - Verifica se todos os campos estão preenchidos.
 - Adiciona os dados à lista `students` e limpa os campos de entrada.
2. **Função `show_students`**:
 
 - Limpa a área de texto.
 - Insere os dados de cada aluno da lista `students` na área de texto.
3. **Configuração da Janela Principal**:
 
 - Criamos a janela principal (`janela`) do aplicativo.
 - Definimos os campos de entrada para nome, endereço e turma.
 - Criamos botões para cadastrar e exibir a lista de alunos.
 - Criamos uma área de texto para exibir os dados cadastrados.
4. **Loop Principal**:
 
 - Iniciamos o loop principal do Tkinter com `janela.mainloop()`.

### Exemplo de Cadastro de Alunos com salvamento em arquivo

Este exemplo vai incluir funcionalidades para adicionar, exibir e salvar os dados dos alunos em um arquivo de texto. Vamos manter a simplicidade, mas garantir que o aplicativo seja funcional e útil.

```python
import tkinter as tk
from tkinter import messagebox
import os

# Função para adicionar aluno à lista
def add_student():
 name = name_entry.get()
 address = address_entry.get()
 student_class = class_entry.get()

 if name and address and student_class:
 student_data = f"Nome: {name}, Endereço: {address}, Turma: {student_class}"
 students.append(student_data)

 # Limpar os campos de entrada
 name_entry.delete(0, tk.END)
 address_entry.delete(0, tk.END)
 class_entry.delete(0, tk.END)

 # Atualizar a área de texto
 show_students()
 else:
 messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos!")

# Função para exibir lista de alunos
def show_students():
 text_area.delete(1.0, tk.END)
 for student in students:
 text_area.insert(tk.END, student + "\n")

# Função para salvar lista de alunos em um arquivo
def save_students():
 if students:
 with open("students.txt", "w") as file:
 for student in students:
 file.write(student + "\n")
 messagebox.showinfo("Sucesso", "Dados dos alunos salvos com sucesso!")
 else:
 messagebox.showwarning("Sem Dados", "Nenhum dado de aluno para salvar!")

# Função para carregar lista de alunos de um arquivo
def load_students():
 if os.path.exists("students.txt"):
 with open("students.txt", "r") as file:
 loaded_students = file.readlines()
 for student in loaded_students:
 students.append(student.strip())
 show_students()
 else:
 messagebox.showwarning("Arquivo Não Encontrado", "Nenhum arquivo de dados encontrado!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("400x400")

# Lista para armazenar os dados dos alunos
students = []

# Campos para entrada de dados
tk.Label(janela, text="Nome:").pack()
name_entry = tk.Entry(janela)
name_entry.pack()

tk.Label(janela, text="Endereço:").pack()
address_entry = tk.Entry(janela)
address_entry.pack()

tk.Label(janela, text="Turma:").pack()
class_entry = tk.Entry(janela)
class_entry.pack()

# Botões para interações
tk.Button(janela, text="Cadastrar", command=add_student).pack(pady=10)
tk.Button(janela, text="Exibir Lista", command=show_students).pack(pady=10)
tk.Button(janela, text="Salvar Lista", command=save_students).pack(pady=10)
tk.Button(janela, text="Carregar Lista", command=load_students).pack(pady=10)

# Área de texto para exibir a lista de alunos
text_area = tk.Text(janela, width=50, height=10)
text_area.pack(pady=10)

# Iniciando o loop principal
janela.mainloop()
```

### Explicação do Código

1. **Função `add_student`**:
 - Obtém os dados dos campos de entrada (nome, endereço, turma).
 - Verifica se todos os campos estão preenchidos.
 - Adiciona os dados à lista `students`.
 - Limpa os campos de entrada.
 - Atualiza a área de texto.

2. **Função `show_students`**:
 - Limpa a área de texto.
 - Insere os dados de cada aluno da lista `students` na área de texto.

3. **Função `save_students`**:
 - Verifica se há dados na lista `students`.
 - Salva os dados em um arquivo `students.txt`.
 - Exibe uma mensagem de sucesso ou de aviso se a lista estiver vazia.

4. **Função `load_students`**:
 - Verifica se o arquivo `students.txt` existe.
 - Carrega os dados do arquivo e atualiza a lista `students`.
 - Exibe os dados carregados na área de texto.

5. **Configuração da Janela Principal**:
 - Criamos a janela principal (`janela`) do aplicativo.
 - Definimos os campos de entrada para nome, endereço e turma.
 - Criamos botões para cadastrar, exibir, salvar e carregar a lista de alunos.
 - Criamos uma área de texto para exibir os dados cadastrados.

6. **Loop Principal**:
 - Iniciamos o loop principal do Tkinter com `janela.mainloop()`.

Com esse exemplo mais completo, você pode cadastrar, exibir e salvar os dados dos alunos em um arquivo, proporcionando uma aplicação prática e funcional. Continuem explorando e aprimorando suas habilidades com Tkinter. Bons estudos e boa programação!